# Deployment

Build, configure, and deploy a VC-Shell app to production, whether as a standalone bundle or a Module Federation host that loads dynamic remotes from the Platform.

## Prerequisites

Before deploying, make sure you have:

- A production-ready build pipeline that runs Node.js 20 and Yarn 4.
- A Virto Commerce Platform instance with the OAuth client configured for the production origin.
- Static hosting (CDN, S3 bucket, NGINX, container) for the bundled assets.

## Production build

The scaffold ships a `build` script that runs Vite in production mode and emits the application bundle plus TypeScript declaration files:

```bash
yarn build
```

Internally, this expands to `yarn build:app && yarn build:types`. The first step runs `cross-env APP_ENV=production vite build` and writes hashed, minified assets to **dist/**. The second step runs `vue-tsc --declaration --emitDeclarationOnly --outDir dist/types` and emits **.d.ts** files for downstream consumers.

The output of **dist/** is everything you need to deploy. Serve it from any static host that can return **index.html** for unknown paths so the client-side router handles deep links.

To smoke-test the production bundle locally before shipping, run:

```bash
yarn preview
```

This starts a static server that mirrors the eventual deployment and helps catch base-path or asset issues that only surface in production builds.

## Environments and configuration

Vite loads environment variables from **.env** files at build time. The scaffold ships **.env** with the public defaults and **.env.local** with a placeholder for the Platform URL, which stays out of version control. For per-mode overrides, add **.env.production**, **.env.staging**, or **.env.&lt;mode&gt;** alongside them.

```bash title=".env.production"
APP_PLATFORM_URL=https://platform.example.com
APP_BASE_PATH=/apps/my-app/
APP_I18N_LOCALE=en
APP_I18N_FALLBACK_LOCALE=en
```

Variables must be prefixed with `APP_` to be exposed to the client bundle. The framework configures Vite with `envPrefix: "APP_"`, so anything else is dropped at build time. `APP_BASE_PATH` and `APP_PLATFORM_URL` are read by the framework's Vite preset and inlined into the bundle as `import.meta.env.APP_BASE_PATH` and `import.meta.env.APP_PLATFORM_URL`.

Because the values are baked into the bundle at build time, do not store secrets in **.env** files. Anything in the client bundle is visible to every user. Use the Platform's OAuth flow for credentialed access and inject runtime URLs through the build pipeline.

## Standalone deployment

The default deployment is a standalone SPA. After `yarn build`, copy **dist/** to your static host and configure a fallback rewrite so unknown paths return **index.html**.

Common targets:

- NGINX or Apache with a `try_files` rewrite to **index.html**.
- Amazon S3 with CloudFront, using the SPA error-document trick to return **index.html** with a 200 status.
- Azure Static Web Apps with the `navigationFallback` rule.
- GitHub Pages, with `APP_BASE_PATH` set to the repo subpath.
- A container image based on `nginx:alpine` that copies **dist/** into **/usr/share/nginx/html/**.

When deploying under a subpath, set `APP_BASE_PATH` to that subpath, including the trailing slash (`/apps/my-app/`). Vite uses this value as the `base` option, and the router prefixes every navigation path with it.

## Module Federation deployment

When the app composes remote modules at runtime, two extra concerns appear: the host must reach the Platform registry, and remote bundles must be served with permissive CORS.

### Host app

The host calls `registerRemoteModules()` during bootstrap, which issues a `POST` request to **/api/frontend-modules** on the Platform. The endpoint returns the registry of compatible remote bundles for the current app. Because the request uses `credentials: "same-origin"`, deploy the host on the same origin as the Platform whenever possible. If you cannot, set up a reverse proxy that forwards **/api/** to the Platform, preserving cookies. Direct cross-origin calls require the Platform's CORS policy and OAuth client to list the host origin explicitly.

### Remote module

A remote module is built with `dynamicModuleConfiguration()` from `@vc-shell/mf-module`. The build emits a Module Federation bundle to **dist/mf/** with `remoteEntry.js` as the entry file:

```text
my-remote-module/dist/mf/
├─ remoteEntry.js     entry the host loads
├─ assets/
│  ├─ index.css
│  └─ ... (chunks)
```

Upload **dist/mf/** to a static host and register the resulting `remoteEntry.js` URL in the Platform's frontend-modules table. The host filters the registry by `compatibleWith.dependencies["@vc-shell/framework"]`, so the remote's manifest must declare the framework version range it was built against. Mismatched ranges cause the host to skip the remote with a console warning rather than break the app.

## Embedded mode

When the app ships as a Platform module, it also runs inside the AngularJS back office through embedded mode. The build, env, and hosting story is identical; only the manifest changes.

![Readmore](platform/embedded-mode.md){: width="25"} Embedded mode setup.

## CI/CD

A typical pipeline installs dependencies, runs the static checks, builds the bundle, and deploys the artifact. The scaffold ships `lint` and `type-check` as the verification commands; replace them with `check` if your project extends the umbrella script from the monorepo template.

```yaml title=".github/workflows/deploy.yml"
- run: yarn install --immutable
- run: yarn lint
- run: yarn type-check
- run: yarn build
- run: <deploy step>
```

For deploys, copy **dist/** to the static host, invalidate the CDN cache for **index.html**, and keep the hashed assets cached for a long time. The hashed filenames make cache busting automatic on the next deploy.

## Common deployment mistakes

!!! warning "Wrong APP_BASE_PATH"
    The `APP_BASE_PATH` value used by the build must match the URL path where the app is served. A mismatch breaks asset URLs and HTML5 history routing. Verify the value in **.env.production** before running `yarn build`, and confirm the bundled **index.html** uses the expected paths.

!!! warning "OAuth client missing the production origin"
    The Platform's OAuth client lists allowed origins. A new production deploy on a fresh origin requires the OAuth client to be updated, or the sign-in handshake fails with a CORS or redirect error.

!!! warning "Module Federation host on a different origin from remotes"
    Remote bundles served from another origin need a CORS policy that allows the host. Configure the static host serving **remoteEntry.js** to send `Access-Control-Allow-Origin` for the host origin, otherwise the host fails to fetch the remote and skips the module.

!!! warning "Forgot to set NODE_ENV"
    `yarn build` sets `APP_ENV=production` through the scaffold script, but custom CI scripts may bypass it. Without production mode, Vite skips tree shaking and minification, and the bundle ships unoptimized.

!!! warning "Missing SPA rewrite"
    A static host that returns 404 for unknown paths breaks deep links and page reloads. Configure the host to return **index.html** for any path that does not match a built asset.

![Readmore](../introduction/architecture-overview.md){: width="25"} Module Federation in the architecture overview.
![Readmore](modules-and-extensions/index.md){: width="25"} Distributing modules.
![Readmore](platform/embedded-mode.md){: width="25"} Embedded mode.
