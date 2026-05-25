# Permissions Model

VC-Shell consumes a user's Platform permissions as a flat string list and uses it to gate blade navigation, menu visibility, toolbar buttons, and arbitrary UI fragments.

Permissions are string identifiers like `order:read`, `catalog:manage`, or `orders:order:view`, granted by Platform roles. The framework loads the current user's permission set at sign-in and keeps it available for the session through `usePermissions()` and the `$hasAccess` template helper.

Blade-level gating is declarative. A blade declares `permissions` through `defineBlade`, and the framework checks them during navigation and menu rendering. You do not write the guard yourself: when a user without the required permission tries to open a workspace by URL, the framework cancels the navigation, shows a toast, and redirects to the main route.

Server-side enforcement is the source of truth. Every check described on this page runs in the browser, on data the user can read with DevTools. UI gating exists to hide controls the user cannot exercise, not to keep secrets. The Platform's API rejects unauthorized calls regardless of what the UI shows.

## Permission strings

A permission is an opaque string. The Platform decides the naming; VC-Shell only does set membership against the user's list. The convention across Virto Commerce is `<domain>:<entity>:<verb>` or the shorter `<module>:<action>` form. Common shapes:

- `order:read`, `order:create`, `order:update`, `order:delete`, `order:manage`.
- `catalog:product:edit`, `catalog:category:read`, `catalog:manage`.
- `orders:order:view`, `catalog:product:edit`.

The exact strings come from the Platform role assigned to the user. Module authors agree with the backend team on which permission gates which blade, then hardcode the strings in `defineBlade` and on individual toolbar items. Treat them as identifiers that match a contract, not as a typed enum the framework exposes.

Two short-circuits apply to every check, regardless of the string:

- `hasAccess(undefined)` and `hasAccess([])` return `true`. No restriction means visible.
- `user.isAdministrator === true` returns `true` for every input. Administrators bypass all UI gates.

## Blade-level gating

A blade declares its required permissions through `defineBlade`. The framework checks them every time a workspace is about to open.

```vue title="src/modules/orders/pages/OrdersList.vue"
<script setup lang="ts">
import { useBlade, VcBlade } from "@vc-shell/framework";

defineBlade({
  name: "OrdersList",
  url: "/orders",
  isWorkspace: true,
  permissions: ["orders:order:view"],
  menuItem: {
    title: "ORDERS.MENU.TITLE",
    icon: "lucide-shopping-cart",
    priority: 10,
    permissions: ["orders:order:view"],
  },
});
</script>
```

What the framework does with `permissions`:

- The sidebar filters out workspaces the user cannot reach. A blade whose permission the user lacks does not appear as a menu entry.
- A direct URL visit to a forbidden workspace redirects to the main route and shows an "access restricted" toast.
- Programmatic `openBlade` calls to a forbidden workspace are blocked by the same check.

`menuItem.permissions` is independent of the blade's own gate. It defaults to the blade-level `permissions` only when you let it; if you set `menuItem.permissions` explicitly, that value wins for menu visibility, even when it disagrees with the blade's own gate. Keep the two in sync unless you have a reason to diverge.

Child blades, the details panels opened from a list, are opened programmatically. They inherit no gate from their parent. If a details blade should be permission-gated, declare `permissions` on it too.

- [Permissions plugin reference.](../plugins/permissions.md)

## Component-level gating

Inside a blade, `usePermissions()` and `$hasAccess` cover the cases the declarative gate cannot reach: individual buttons, conditional sections, business logic that branches on access.

```vue title="In a blade template"
<template>
  <VcButton v-if="$hasAccess('order:create')">Create order</VcButton>

  <VcButton v-if="$hasAccess(['order:update', 'order:manage'])">Edit order</VcButton>
</template>
```

```ts title="In a composable"
import { usePermissions } from "@vc-shell/framework";

const { hasAccess } = usePermissions();

if (!hasAccess("catalog:manage")) {
  notification.warning("You do not have access to manage the catalog.");
  return;
}
```

`$hasAccess` in templates and `hasAccess` from `usePermissions()` are the same check exposed two ways. Both consult the user's permission set; templates use the global helper, composition API code uses the composable.

Toolbar buttons gate visibility through `isVisible`, a computed boolean that consults `hasAccess`. A blade declares its toolbar as a plain `IBladeToolbar[]` array and passes it to `VcBlade`:

```vue title="Toolbar item gating"
<script setup lang="ts">
import { computed, ref } from "vue";
import { usePermissions, VcBlade, type IBladeToolbar } from "@vc-shell/framework";

const { hasAccess } = usePermissions();

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "save",
    title: "Save",
    icon: "lucide-save",
    isVisible: computed(() => hasAccess("order:update")),
    clickHandler: () => saveOrder(),
  },
  {
    id: "delete",
    title: "Delete",
    icon: "lucide-trash",
    isVisible: computed(() => hasAccess(["order:delete", "order:manage"])),
    clickHandler: () => deleteOrder(),
  },
]);
</script>

<template>
  <VcBlade :toolbar-items="bladeToolbar" />
</template>
```

`isVisible` runs on every reactivity pass, so the toolbar reacts immediately to user-permission changes. Use `disabled: computed(() => !hasAccess(...))` instead when the action should stay visible but be disabled.

- [usePermissions composable reference.](../composables/user/usePermissions.md)

## Working with multiple permissions

`hasAccess` accepts a single string or a string array. Array input applies OR logic: the user passes the check if they hold at least one of the listed permissions. There is no built-in AND form.

```ts title="OR vs AND"
// OR: user needs at least one of these.
if (hasAccess(["order:read", "order:manage"])) { /* ... */ }

// AND: chain calls explicitly.
if (hasAccess("order:read") && hasAccess("order:create")) { /* ... */ }
```

Default-deny is the right reflex. When a check decides whether to expose a destructive action, prefer the narrowest permission that authorizes it and let `hasAccess` return `false` when in doubt. The administrator short-circuit means a power user still sees the control; everyone else needs the explicit grant.

## Server-side is the source of truth

!!! warning "UI gating is not security"
    `$hasAccess` and `usePermissions` run in the browser. The user can edit the cached permission list in the JavaScript console, flip booleans in Vue DevTools, or call the API directly with `curl`. The Platform's authorization filter is the only enforcement that matters. Use UI gating to keep the interface honest, not to keep data safe.

If a permission gate is the only thing standing between a user and a forbidden operation, you have a security bug. Every endpoint the blade calls must enforce the same permission server-side, returning HTTP 403 when the caller is not authorized. The framework surfaces a 403 from any Platform API call as an inline error; the call itself never succeeds.

## Common mistakes

!!! warning "Treating UI gating as a security boundary"
    A `v-if="$hasAccess(...)"` hides a button. It does not stop a determined user from invoking the underlying API. Pair every UI gate with the matching server-side permission requirement.

!!! warning "Mismatched permission strings"
    `order:read` and `orders:read` look identical at a glance and behave like silent bugs: every check returns `false`, every menu item hides, no error fires. Copy the exact strings from the Platform role definition, not from memory.

!!! warning "Assuming `hasAccess` arrays use AND"
    `hasAccess(["order:read", "order:manage"])` passes when the user has either permission. Reviewers and authors both misread this regularly. Use `hasAccess(a) && hasAccess(b)` when you need both.

!!! warning "Forgetting `menuItem.permissions`"
    A blade with `permissions: ["orders:order:view"]` and a `menuItem` without its own `permissions` falls back to the blade gate, which is usually what you want. The moment you set `menuItem.permissions` explicitly, that value wins. Set it deliberately or leave it off; do not copy-paste a stale value that drifts from the blade gate.

!!! warning "Gating child blades by relying on the parent"
    Child blades opened by `openBlade(...)` do not inherit `permissions` from the workspace that opened them. If the details blade should be gated, declare `permissions` on it too.
