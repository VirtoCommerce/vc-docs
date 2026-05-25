# Migration

This page indexes the upgrade paths between major versions of `@vc-shell/framework` and points to the canonical sources for each step. Read the section that matches the version pair you are upgrading between, then run the codemods bundled in the `@vc-shell/migrate` CLI before tackling the manual changes.

The detailed, file-by-file diffs live upstream in the [vc-shell repository](https://github.com/VirtoCommerce/vc-shell). This page summarizes what changes, why, and how to automate the parts that can be automated. It does not duplicate the upstream guide.

## How to use this page

Pick the version pair you are migrating between (for example, v1.2.x to v2.0.0), read the breaking-change summary, then run the listed codemods. Manual changes follow the codemod pass. Each version section links to the upstream guide for the full per-file diff.

Before you start:

- Commit your working tree so you can review the migration diff cleanly.
- Run the codemods in `--dry-run` mode first to preview the changes.
- Plan to migrate one app at a time; many v1 APIs keep working through compatibility shims, so partial migrations are safe.

## v1 to v2

Version 2.0.0 of `@vc-shell/framework` shipped in April 2026. It rewrites the blade lifecycle, replaces the legacy table, splits the framework package into sub-entries, and renames the App Switcher to the App Hub. The upstream [MIGRATION_GUIDE.md](https://github.com/VirtoCommerce/vc-shell/blob/main/MIGRATION_GUIDE.md) catalogs 48 individual migration guides grouped into five phases. Work through them in phase order.

### Breaking changes

The most disruptive changes, by category:

- **Module entry points.** `createAppModule(pages, locales, templates, components)` is replaced by `defineAppModule({ blades, locales, notificationTemplates })`. The lightweight `createModule()` helper is removed.
- **Blade composables.** `useBladeNavigation()` becomes `useBlade()`. The `onBeforeClose` guard inverts: return `true` to prevent close, not `false`.
- **Blade boilerplate.** VcBlade reads `expanded` and `closable` from the descriptor; pages no longer declare these props or wire up `@close`/`@expand`/`@collapse` emits.
- **Notifications.** `useNotifications()` becomes `useBladeNotifications()` and gains automatic blade-scoped cleanup. The new `useBroadcastFilter()` composable replaces the `signalR: { creator }` install option.
- **Extensions.** `useExtensionSlot()` and `<ExtensionSlot>` are replaced by `defineExtensionPoint()`, `useExtensionPoint()`, and `<ExtensionPoint>`.
- **Tables.** The legacy `VcTable` is removed. Use the new `VcDataTable` with slot-based `<VcColumn>` children. A `VcTableAdapter` provides backward compatibility under the `VcTable` name.
- **Dynamic views.** The JSON-schema-driven `createDynamicAppModule` subsystem and `useDynamicModules()` CDN loader are removed. Rewrite dynamic modules as explicit Vue components, or adopt the new `@vc-shell/mf-host`/`@vc-shell/mf-module` Vite Module Federation packages for runtime composition.
- **Package layout.** Wildcard deep imports (`@vc-shell/framework/core/...`) no longer work; import from the documented sub-entries `@vc-shell/framework/ui`, `@vc-shell/framework/ai-agent`, `@vc-shell/framework/extensions`, or `@vc-shell/framework/globals`. The framework also stops calling `app.component()` and `app.directive()` automatically; import every `Vc*` component and directive explicitly.
- **Tooling.** Floor versions move to Vue 3.5, Vue Router 5, and `vue-tsc` 3. The `platformUrl` install option is removed; configure the platform URL via the `APP_PLATFORM_URL` environment variable. `window.Vue`, `window.moment`, and peers are no longer assigned. The `moment` dependency is replaced by `date-fns`.
- **Renames.** "App Switcher" is renamed to "App Hub" across props, slots, and composables (`disableAppSwitcher` to `disableAppHub`, `#app-switcher` to `#app-hub`, `useAppSwitcher()` to `useAppHub()`).
- **Component props.** `VcButton` drops the boolean shorthands `small`, `outline`, `raised` (use `variant`/`size` instead). `VcSwitch` drops `tooltip` (use `hint`). `VcIcon` drops `useContainer`. `VcBanner` drops the legacy variants `light-danger`, `info-dark`, and `primary`. CSS class suffixes migrate from `_modifier` to `--modifier` (strict BEM).

For the complete list, see the [upstream migration index](https://github.com/VirtoCommerce/vc-shell/blob/main/MIGRATION_GUIDE.md) and the per-change notes under [migration/](https://github.com/VirtoCommerce/vc-shell/tree/main/migration).

!!! tip
    Many v1 APIs continue to work via adapter layers in v2. Deprecated APIs emit console warnings in development with a link to the relevant migration note, so you can migrate incrementally, one module at a time.

### Codemods

The `@vc-shell/migrate` CLI applies most renames and structural rewrites automatically. From the root of your app, run:

```bash title="bash"
npx @vc-shell/migrate --dry-run
```

Review the planned changes, then drop `--dry-run` to apply them. To list every transform with its target version and category:

```bash title="bash"
npx @vc-shell/migrate --list
```

The CLI detects your current framework version from **package.json** and selects the transforms required to reach the target. The full transform set for the 2.0 path covers `define-app-module`, `use-blade-migration`, `notification-migration`, `blade-props-simplification`, `rewrite-imports` (ai-agent and extensions splits), `remove-deprecated-aliases` (injection keys), `widgets-migration`, `composable-return-types` (20 type renames), `banner-variants`, `switch-tooltip-prop`, `icon-container-prop`, and `shims-to-globals` (tsconfig and shim files). Three transforms are diagnostic and report findings without writing files: `icon-audit` (Font Awesome to Lucide), `scss-safe-use` (`@import` to `@use`), and `menu-group-config` (legacy `group`/`groupIcon` properties).

### Manual changes

The codemods cover the common cases. The following require hand edits because they involve project-level decisions, not mechanical renames:

| Area | What to do |
| --- | --- |
| Widget registration | Convert imperative `registerWidget()`/`unregisterWidget()` calls into the declarative `useBladeWidgets([...])` configuration array. |
| Dynamic views | Rewrite each `createDynamicAppModule` JSON schema as an explicit Vue blade page registered through `defineAppModule`. |
| CDN module loader | Replace `useDynamicModules()` with static imports (`app.use(...)`) for single deployments, or migrate to `@vc-shell/mf-host`/`@vc-shell/mf-module` for true runtime federation. |
| Icons | Replace Font Awesome class names with Lucide names. The `icon-audit` diagnostic lists every occurrence with a suggested replacement. |
| SCSS | Convert each `@import` to `@use`/`@forward`. The `scss-safe-use` diagnostic lists the files to update. |
| Menu groups | Move `group`, `groupIcon`, and `inGroupPriority` into a `groupConfig: { id, title, icon, priority, permissions }` object on each menu item. |
| Login | Replace `VcLoginForm` with `VcAuthLayout`, moving branding and logos into the new slots. |
| Dashboard | Replace the static dashboard grid with `DraggableDashboard` and register widgets through `registerDashboardWidget()`. |
| Custom CSS targeting framework classes | Update selectors from `vc-component_modifier` to `vc-component--modifier`. |
| `package.json` peer dependencies | Declare `vue >= 3.5` and `vue-router >= 4.2.0` as peers. Run `npx @vc-shell/migrate --update-deps` to align the curated peer set automatically. |

## v2 to v3

Version 3 is not in development at this time. The active 2.x line continues to ship feature and fix releases. Track the upstream [CHANGELOG.md](https://github.com/VirtoCommerce/vc-shell/blob/main/CHANGELOG.md) for the current release notes. When a major bump is announced, the codemods for it will land in `@vc-shell/migrate` and a section will appear on this page.

## Latest version highlights

These are the headline additions in v2.0.0 that you will want to adopt after the migration completes. The full list is in the upstream [WHATS_NEW.md](https://github.com/VirtoCommerce/vc-shell/blob/main/WHATS_NEW.md).

- **Unified `useBlade()` composable** combining navigation, lifecycle, and context APIs, with typed options via `useBlade<MyOptions>()`.
- **`defineBlade()` macro** that moves blade metadata (URL, permissions, menu item) out of `defineOptions()` into a dedicated compile-time macro processed by the Vite plugin.
- **`VcDataTable`** with slot-based columns, virtual scroll, inline editing, column resize and reorder with state persistence, pull-to-refresh on mobile, and the `useDataTableSort()`/`useDataTablePagination()` composables for boilerplate-free list pages.
- **`useBladeForm()`** that consolidates `useForm`, `useModificationTracker`, `useBeforeUnload`, and `onBeforeClose` into one composable, with VcBlade auto-detecting modification state via provide/inject.
- **Transparent skeletons** in VcBlade: when `loading=true`, every child UI component renders a layout-matching skeleton with zero changes to existing pages, plus a `useBladeLoading()` composable for custom components.
- **App Hub** unifying app switching, sidebar search, App Bar widgets (`useAppBarWidget()`), and settings menu entries (`useSettingsMenu()`) into one programmatic surface.
- **Dark theme** plus a z-index token scale, Tailwind colors bound to CSS custom properties, semantic surface/overlay/shadow/glass tokens, and the Lato font bundled by default.
- **Module Federation packages** `@vc-shell/mf-config` and `@vc-shell/mf-host` for first-class Vite-based micro-frontend deployments.

## Migration tooling

The `@vc-shell/migrate` CLI is the recommended way to run the v1 to v2 transforms. It is published to npm as **@vc-shell/migrate** and is normally invoked via `npx` so you always get the latest patch.

Common invocations:

```bash title="bash"
# Preview every applicable transform without writing files.
npx @vc-shell/migrate --dry-run

# Apply all applicable transforms.
npx @vc-shell/migrate

# Apply a single transform (bypasses the version filter).
npx @vc-shell/migrate --transform blade-props-simplification

# List every transform with its introducedIn version and category.
npx @vc-shell/migrate --list

# Migrate one app in a monorepo.
npx @vc-shell/migrate --cwd apps/my-app

# Also bump @vc-shell/* packages and align peer-dep versions.
npx @vc-shell/migrate --update-deps
```

How transform selection works: each transform declares the framework version that introduced its breaking change. The CLI runs every transform whose `introducedIn` falls between your current version (read from **package.json**) and the `--to` target (defaults to the latest 2.x stable). Transforms you have already passed are skipped, so reruns are safe.

Format preservation: the CLI uses [jscodeshift](https://github.com/facebook/jscodeshift) and [recast](https://github.com/benjamn/recast) for AST rewrites, so untouched lines keep their original indentation, quotes, trailing commas, and line breaks. Writes are atomic, so a crash mid-run cannot leave a corrupted file.

After the CLI finishes, a `MIGRATION_REPORT.md` is generated in your app root listing every modified file, every diagnostic warning, and every manual follow-up item flagged by the diagnostic transforms. Read it before committing. Pass `--no-report` to skip generation.

For the full CLI reference, troubleshooting tips, and the rationale behind each transform, see the upstream [@vc-shell/migrate README](https://github.com/VirtoCommerce/vc-shell/blob/main/cli/migrate/README.md).
