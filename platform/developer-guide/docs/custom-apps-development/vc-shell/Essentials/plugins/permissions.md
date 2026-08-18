# Permissions Plugin & `usePermissions` Composable

The Permissions Plugin, primarily accessed through the `usePermissions` composable, provides role-based access control (RBAC) capabilities within VC-Shell applications. It allows you to restrict access to different parts of your application and conditionally render UI elements based on user permissions.

The `usePermissions` composable integrates with Virto Commerce Platform's permission system. It enables your components and services to check if the currently authenticated user possesses specific permissions required to perform an action or view certain content.

Route protection itself (i.e., defining which permissions are needed for a route) is typically handled declaratively when registering pages/blades through the Modularity system (e.g., via the `permissions` property of a page component passed to `createAppModule`). The VC-Shell framework's navigation guards then enforce these rules, often using `usePermissions` internally.

## Features

- **Permission checking**: Easily check if a user has specific permissions using the `hasAccess` function.
- **Conditional UI Rr**: Show or hide UI elements based on user permissions directly in templates using `$hasAccess` or in script logic.
- **Administrator override**: Users with an Administrator role are typically granted all permissions implicitly.

## Setup

The `usePermissions` composable is available out-of-the-box when using the VC-Shell framework. No special plugin registration is usually required beyond the standard `VcShellFramework` setup, as it relies on the `useUser` composable which is initialized by the framework.

```typescript
// Example: main.ts
import { createApp } from 'vue';
import VcShellFramework from '@vc-shell/framework';
import App from './App.vue';

const app = createApp(App);

app.use(VcShellFramework, {
  router // router instance is needed for navigation guards
  // Other options...
});
```

## Usage

### Check permissions in `<script setup>`

The `usePermissions` composable provides the `hasAccess` function.

```typescript
import { usePermissions } from '@vc-shell/framework';
import { computed } from 'vue';

export default {
  setup() {
    const { hasAccess } = usePermissions();

    function handleCreateProduct() {
      if (hasAccess('catalog:create')) {
        // Proceed with product creation logic
        console.log('User has permission to create a product.');
      } else {
        // Handle unauthorized access attempt (e.g., show a notification)
        console.warn('User does NOT have permission to create a product.');
      }
    }

    // Example for a computed property based on permission
    const canManageOrders = computed(() => hasAccess('order:manage'));

    return {
      handleCreateProduct,
      canManageOrders,
    };
  },
};
```

### Conditional rendering in templates

VC-Shell globally registers `$hasAccess`, which is a convenience wrapper around `usePermissions().hasAccess` for use directly in templates.

```html
<template>
  <div>
    <!-- Show button only if user has 'catalog:create' permission -->
    <button v-if="$hasAccess('catalog:create')">
      Create Product
    </button>

    <!-- Show button if user has EITHER 'catalog:update' OR 'catalog:manage' permission -->
    <button v-if="$hasAccess(['catalog:update', 'catalog:manage'])">
      Edit Product
    </button>

    <div v-if="canManageOrders"> <!-- Assuming canManageOrders is a computed from setup -->
      Order Management Section
    </div>
  </div>
</template>
```

### Checking for multiple permissions

The `hasAccess` function accepts a single permission string or an array of permission strings. If an array is provided, `hasAccess` returns `true` if the user possesses **at least one** of the specified permissions.

```typescript
// Checks if user has EITHER 'catalog:create' OR 'catalog:manage'
const canConfigureCatalog = hasAccess(['catalog:create', 'catalog:manage']);

// This is useful for scenarios where different roles might have overlapping responsibilities.
```

### Route protection and permission definition

As mentioned, defining the permissions required to access a route is typically done when the route (or the blade component associated with it) is registered, often through the `createAppModule` mechanism.

**Example (Conceptual - during module definition):**
```typescript
// my-module/pages/product-create-page.vue
<script setup lang="ts">

defineOptions({
  name: 'ProductCreatePage',
  permissions: ['catalog:create'], // Permission required for this page/route
  url: '/products-create'
});
</script>

// my-module/index.ts
import ProductCreatePage from './pages/product-create-page.vue';
// ...
const pages = { ProductCreatePage };
export default createAppModule(pages, /* locales, etc. */);
```
VC-Shell's navigation guards will then use the permission system (likely `usePermissions` internally) to check against these definitions before navigating to a route. If the user lacks the required permissions, they are typically redirected, and a notification might be displayed.

## Administrator access

Users identified as Administrators (e.g., via `user.value.isAdministrator` from `useUser`) are usually granted access to all functionalities, bypassing explicit permission checks within the `hasAccess` logic.

```typescript
// Simplified internal logic of hasAccess
function hasAccess(requiredPermissions: string | string[]): boolean {
  const { user } = useUser(); // Get current user state
  if (user.value?.isAdministrator) {
    return true; // Administrators have all permissions
  }
  // ... actual permission checking logic against user.value.permissions ...
}
```

## Integration with `useUser`

The `usePermissions` composable relies heavily on the `useUser` composable. `useUser` provides the current user's state, including their assigned `permissions` array and their `isAdministrator` status, which `usePermissions` uses to perform its checks.

## Best practices

1.  **Granular Permissions**: Define and check for specific permissions rather than overly broad ones to maintain fine-grained control.
1.  **Use Permission Constants**: Store permission strings as constants to avoid typos and improve code maintainability and refactorability.
    ```typescript
    // Example: src/core/constants/permissions.ts
    export const PERMISSIONS = {
      CATALOG: {
        READ: 'catalog:read',
        CREATE: 'catalog:create',
        // ...
      },
      ORDERS: {
        READ: 'order:read',
        // ...
      }
    };

    // Usage in component:
    // import { PERMISSIONS } from '@/core/constants/permissions';
    // if (hasAccess(PERMISSIONS.CATALOG.CREATE)) { /* ... */ }
    ```
1.  **Consistent UI/UX**: If a user lacks permission for an action, prefer to hide or disable the corresponding UI element. Avoid showing an active element that leads to an error message upon interaction.

## Related resources

-   [useUser Composable](../composables/useUser.md): Provides user information, including their permissions.
-   [Modularity (createAppModule)](./modularity.md): For how modules and their pages (with permission requirements) are registered.
