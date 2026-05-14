# Custom Authentication

Customize how users sign in to a VC-Shell app: enterprise SSO through Platform-managed external providers, custom UI on top of the framework's auth flow, and mock credentials for tests.

VC-Shell version 1 shipped a pluggable `IAuthProvider` interface that let an app swap the entire authentication mechanism in client code. That interface was removed in version 2. The framework now hard-wires the OAuth password-grant flow against the Virto Commerce Platform's `/connect/token` endpoint, and routes every external sign-in through Platform's `/externalsignin` redirect. This is a deliberate narrowing: every request the framework issues, including the silent token refresh and the SignalR push-notification connection, depends on a Platform-shaped session, so a fully pluggable client-side provider could never have produced a session those subsystems would accept.

What you can still customize is everything around that flow: which external identity providers appear on the login page, what the auth pages look like, and what your app does immediately before and after `signIn` and `signOut`. The shared `Login`, `Invite`, `ResetPassword`, and `ChangePasswordPage` components consume `useUserManagement`, the framework's single auth surface; your code wraps that composable to add side effects, and you configure SSO providers on the Platform server, not in the app.

## When to use

- Replace password sign-in with enterprise SSO (Azure AD, Okta, Auth0, Google Workspace).
- Run both password and SSO sign-in side by side, with SSO as the default.
- Add app-specific side effects to sign-in or sign-out, for example, telemetry, locale prep, or profile load.
- Substitute a fixture user during end-to-end tests so the test suite never hits a real Platform.
- Build a standalone, unauthenticated kiosk or marketing app that renders VC-Shell components without an auth flow at all.

## The auth surface in v2

Two composables expose every auth operation the framework knows about. `useUser` is the read-side singleton consumed by widgets and page guards; `useUserManagement` adds the write-side methods that the shared auth pages call.

```ts title="src/composables/auth-surface.ts"
import { useUser, useUserManagement } from "@vc-shell/framework";

const { user, isAuthenticated, isAdministrator, getAccessToken } = useUser();

const {
  signIn,
  signOut,
  validatePassword,
  resetPasswordByToken,
  requestPasswordReset,
  changeUserPassword,
  validateToken,
  getLoginType,
} = useUserManagement();
```

`signIn(username, password)` posts to `/connect/token` with `grant_type=password` and stores the resulting tokens in `localStorage` under `vc_auth_data`. The fetch interceptor reads from that key on every API call and silently refreshes when the access token expires. Replacing the storage manually breaks the interceptor, so any customization wraps these methods rather than reimplementing them.

## Enterprise SSO through Platform external providers

The framework auto-discovers external sign-in providers on mount. When the `Login` page loads, it calls `useExternalProvider().getProviders()`, which reads from `/api/platform/security/externalSignInProviders`, and renders one button per provider returned. No client-side wiring is required; the providers come from Platform configuration.

Configure the provider on the Platform side. For example, to add Azure AD, set the following keys in **appsettings.json** or environment variables on the Platform host:

```json title="appsettings.json"
{
  "ExternalAuthentication": {
    "AzureAd": {
      "Authority": "https://login.microsoftonline.com/<tenant-id>",
      "ClientId": "<client-id>",
      "ClientSecret": "<client-secret>",
      "DefaultUserType": "Manager"
    }
  }
}
```

Restart Platform and reload the app. The `Login` page now shows an "Azure AD" button alongside the credentials form; clicking it redirects the browser to Platform's `/externalsignin?authenticationType=AzureAd`, Platform handles the OIDC dance with Azure, and the user lands back on the app with a Platform-shaped session in `localStorage`. Sign-out goes through `/externalsignin/signout` so the IdP session is terminated too.

To present SSO as the only option, hide the credentials form by passing `ssoOnly` to the `Login` route props.

```ts title="src/router/routes.ts"
{
  name: "Login",
  path: "/login",
  component: Login,
  props: () => ({ ssoOnly: true, logo, background }),
},
```

When `ssoOnly` is true and `getProviders()` returns nothing, the page renders an empty-state placeholder instead of the username and password fields.

## Recipe: app-specific hooks around sign-in

Wrap `useUserManagement` in your own composable to inject pre or post-sign-in logic without forking the shared `Login` page.

```ts title="src/composables/useAppLogin.ts"
import { useUserManagement } from "@vc-shell/framework";

export function useAppLogin() {
  const { signIn, signOut, ...rest } = useUserManagement();

  async function signInWithSideEffects(username: string, password: string) {
    const result = await signIn(username, password);
    if (result.succeeded) {
      // Telemetry, locale prep, feature-flag fetch, ...
    }
    return result;
  }

  async function signOutWithCleanup() {
    // Cancel app-specific timers, flush queues, ...
    await signOut();
  }

  return { signIn: signInWithSideEffects, signOut: signOutWithCleanup, ...rest };
}
```

Use `useAppLogin` from your own custom auth pages, or from any callback that needs `signIn` or `signOut`. The shared `Login` component still calls the framework's `useUserManagement().signIn` directly, so for hooks that must run on every login, register an `auth:after-form` extension point or replace the route with a custom wrapper component that calls `useAppLogin`.

## Recipe: mock authentication for end-to-end tests

For Playwright or Cypress runs that must not hit a real Platform, intercept the network at the boundary instead of swapping a client-side provider. The framework speaks two URLs during sign-in: `POST /connect/token` and `GET /api/platform/security/currentuser` (issued by `loadUser`). Stubbing both produces a fully authenticated session.

```ts title="tests/e2e/fixtures/auth.ts"
import { Page } from "@playwright/test";

export async function mockSignedInUser(page: Page, user = { userName: "test", isAdministrator: true }) {
  await page.route("**/connect/token", (route) =>
    route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        access_token: "mock-token",
        refresh_token: "mock-refresh",
        expires_in: 3600,
        token_type: "Bearer",
      }),
    }),
  );

  await page.route("**/api/platform/security/currentuser", (route) =>
    route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify(user) }),
  );
}
```

Call `mockSignedInUser(page)` before `page.goto("/")` in the test setup, then drive the UI normally. Because the access token is whatever your stub returns, downstream API calls hit the stubbed routes too, and the framework never knows it is talking to a fixture.

## Recipe: standalone app without authentication

If you embed VC-Shell components in a marketing site or a public kiosk that has no sign-in, skip the auth router routes entirely and never call `loadUser`. The `useUser` composable returns `isAuthenticated.value === false` and the page guards redirect to a `Login` route only if you wire one. Drop the route, drop the redirect, and the app renders without an auth flow. UI components like `VcDataTable`, `VcButton`, and `VcForm` work without a session; only the components that internally call `useApiClient` against Platform require one.

## Common mistakes

!!! warning "Reaching for IAuthProvider"
    The `IAuthProvider` interface, the `AuthProviderManager` singleton, and the `VirtoShellFramework.configure({ authProvider })` static method shipped in version 1 do not exist in version 2. Searching the framework source for any of these names returns nothing. Wrap `useUserManagement` instead, or configure an external provider on the Platform.

!!! warning "Replacing the token storage"
    The fetch interceptor reads from `localStorage` under `vc_auth_data` on every API call. Writing your own tokens to a different key or returning a custom object from a wrapper composable breaks the interceptor; the API call goes out without an `Authorization` header and Platform answers with a 401. Always let `signIn` write the storage.

!!! warning "Configuring SSO providers in the app"
    External providers are discovered, not declared. The `Login` page calls `getExternalLoginProviders` on Platform; an app cannot inject a provider that Platform has not registered. If a button does not appear, fix the Platform configuration first, then reload the app.

!!! warning "Mocking only `/connect/token` in tests"
    A fulfilled token response with no matching `currentuser` stub leaves `useUser` in the loading state forever. Stub both endpoints in test setup, and stub `/api/platform/security/logout` if your test path exercises sign-out.

![Readmore](auth-pages.md){: width="25"} Wiring the auth UI pages and branding props.

![Readmore](../../getting-started/connecting-to-platform.md){: width="25"} The default Platform OAuth flow.

![Readmore](../../composables/user/useUser.md){: width="25"} useUser composable reference.
