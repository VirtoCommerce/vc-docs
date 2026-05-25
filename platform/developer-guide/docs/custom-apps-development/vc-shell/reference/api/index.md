# API Reference

The complete reference for VC-Shell's public API. Use this index to locate the page for a specific component, composable, plugin, directive, or utility.

The pages in this section are generated from doc-comments in the `@vc-shell/framework` source and synced into this guide by the `docs-sync` CLI. Edits to the synced content do not survive the next sync; the source of truth is **@vc-shell/framework**.

## Components

UI components shipped under `@vc-shell/framework/ui`. Grouped by role:

| Section | Use it for |
| --- | --- |
| [Layout](../../components/layout/vc-app.md). | App shell, blade containers, cards, containers, rows, columns, sidebar, scrollable containers. |
| [Data display](../../components/data-display/vc-data-table.md). | Tables, accordion, galleries, image tiles. |
| [Form](../../components/form/vc-form.md). | Inputs, selects, switches, date pickers, multivalue, dynamic property, file upload. |
| [Feedback](../../components/feedback/vc-banner.md). | Banners, toasts, popups, tooltips, hints, skeletons, status, progress, loading. |
| [Media](../../components/media/vc-image.md). | Images, video, image upload. |
| [Navigation](../../components/navigation/vc-menu.md). | Menu, pagination, dropdowns, breadcrumbs, links. |
| [Misc](../../components/misc/vc-button.md). | Buttons, badges, icons, labels, widgets. |

## Composables

Composition API functions shipped under `@vc-shell/framework`. Grouped by domain:

| Section | Use it for |
| --- | --- |
| [Blade navigation](../../composables/blade-navigation/useBlade.md). | `useBlade`, `useBladeContext`, `useBladeRegistry`, `useBladeWidgets`. |
| [Data](../../composables/data/useApiClient.md). | `useApiClient`, `useAssets`, `useAssetsManager`, `useDataTablePagination`, `useDataTableSort`, `useTableSelection`, `useTableSort`. |
| [Forms](../../composables/forms/useBladeForm.md). | `useBladeForm`, `useDynamicProperties`, `useModificationTracker`. |
| [Notifications](../../composables/notifications/useNotifications.md). | `useNotifications`, `usePopup`. |
| [Services](../../composables/services/useToolbar.md). | `useToolbar`, `useMenuService`, `useDashboard`, `useSettings`, `useSettingsMenu`, `useAppBarWidget`, `useAppBarMobileButtons`, `useWidgets`. |
| [UI state](../../composables/ui-state/useResponsive.md). | `useResponsive`, `useTheme`, `useLoading`, `useBreadcrumbs`, `useConnectionStatus`, `useKeyboardNavigation`, `useMenuExpanded`, `useSidebarState`, `useSlowNetworkDetection`. |
| [User](../../composables/user/useUser.md). | `useUser`, `useLanguages`, `usePermissions`, `usePlatformLocaleSync`. |
| [Utilities](../../composables/utilities/useAsync.md). | `useAsync`, `useFunctions`, `useBeforeUnload`, `useErrorHandler`, `useAppInsights`, `useWebVitals`. |

## Plugins

Vue plugins installed during `app.use(VirtoShellFramework, ...)`. Each plugin owns a feature surface and exposes a set of composables and component contracts:

- [Modularity.](../../plugins/modularity.md) — `defineAppModule`, `BladeRegistry`, module lifecycle.
- [Extension points.](../../plugins/extension-points.md) — `defineExtensionPoint`, `useExtensionPoint`, `<ExtensionPoint>`.
- [Permissions.](../../plugins/permissions.md) — `usePermissions`, `$hasAccess`.
- [Notifications.](../../plugins/notifications.md) — toast, panel, and custom notification templates.
- [Localization (i18n).](../../plugins/i18n.md) — `vue-i18n` integration, `useLanguages`.
- [SignalR.](../../plugins/signalr.md) — Platform push notifications and real-time updates.
- [Validation.](../../plugins/validation.md) — vee-validate integration.
- [AI Agent.](../../plugins/ai-agent.md) — Conversational agent panel and tools.
- [Global error handler.](../../plugins/global-error-handler.md) — Centralized error capture.

## Directives

Custom Vue directives shipped with the framework:

- [`v-loading`.](directives/v-loading.md) — Show a loader overlay on the host element while a ref is `true`.
- [`v-autofocus`.](directives/v-autofocus.md) — Focus the host element on mount.

## Types

TypeScript interfaces and types consumed by application code:

- [Core types.](types-core.md) — `IBladeToolbar`, `IMenuItem`, `MenuItem`, `Breadcrumbs`, `IValidationRules`, `ITableColumns`, and others.
- [UI types.](types-ui.md) — Component prop and event shapes that escape into application code.
- [Injection keys.](injection-keys.md) — Reactive provide/inject keys exposed by the framework.

## Utilities

Pure helper functions:

- [Date utilities.](date-utilities.md) — Formatting and parsing helpers built on **date-fns**.
- [Thumbnail.](thumbnail.md) — Asset URL transformations for thumbnails.
- [Platform client.](platform-client.md) — Low-level Platform API base.
- [Shared utilities.](shared-utilities.md) — Cross-cutting helpers used by composables.
- [Utilities overview.](utilities-overview.md) — Full index of exported helpers.

## CLI

Command-line tools shipped alongside the framework:

- [create-vc-app.](../cli/create-vc-app.md) — Scaffold apps and dynamic modules.
- [API Client Generator.](../cli/api-client-generator.md) — Generate typed Platform clients.

## Built-in modules

The framework ships two domain modules out of the box. See the [Modules reference index](../modules/index.md) for details.

- [Assets.](../modules/assets.md) — Asset details blade and `useAssets` composable.
- [Assets Manager.](../modules/assets-manager.md) — Multi-asset management blade and `useAssetsManager` composable.
