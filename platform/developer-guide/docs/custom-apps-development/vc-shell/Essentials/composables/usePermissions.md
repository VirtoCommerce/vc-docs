# usePermissions Composable

The `usePermissions` composable provides functionality for checking user permissions in a VC-Shell application. It allows components and services to determine if the current user has specific permissions, which is essential for implementing role-based access control.

The `usePermissions` composable integrates with VC-Shell's user management system to provide permission checking capabilities. It automatically handles administrator privileges and supports both single and multiple permission checks.

## API reference

### Return value

The `usePermissions` composable returns an object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `hasAccess` | `(permissions: string \| string[] \| undefined) => boolean` | Function to check if user has the specified permission(s) |

### hasAccess function

The `hasAccess` function can be used in several ways:

```typescript
// Check a single permission
hasAccess('create-products');

// Check multiple permissions (returns true if user has ANY of the permissions)
hasAccess(['create-products', 'edit-products']);

// Pass undefined (always returns true)
hasAccess(undefined);
```

**Parameters:**
- `permissions` (string | string[] | undefined): The permission(s) to check
  - `string`: Single permission name
  - `string[]`: Array of permissions (OR logic - user needs ANY permission)
  - `undefined`: Always returns true (no permission required)

**Returns:**
- `boolean`: `true` if user has access, `false` otherwise

**Logic:**
- Always returns `true` if user is an administrator
- Always returns `true` if permissions parameter is `undefined`
- For arrays: returns `true` if user has ANY of the permissions
- For strings: returns `true` if user has the specific permission

## Global template helper: `$hasAccess`

In addition to the composable, VC-Shell provides a global helper function `$hasAccess` that can be used directly in Vue component templates without needing to import `usePermissions`.

```vue
<template>
  <!-- Single permission check -->
  <VcButton v-if="$hasAccess('create-users')" @click="createUser">
    Create User
  </VcButton>
  
  <!-- Multiple permissions (OR logic) -->
  <div v-if="$hasAccess(['edit-content', 'publish-content'])">
    Content Management
  </div>
  
  <!-- Complex permission logic -->
  <div v-if="$hasAccess('admin-access') && $hasAccess('user-management')">
    Admin Panel
  </div>
</template>
```

## Basic usage

### In Script/Setup
```typescript
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

// Single permission
const canCreateUsers = hasAccess('create-users');

// Multiple permissions
const canModifyContent = hasAccess(['edit-content', 'publish-content']);

// In functions
function performAction() {
  if (hasAccess('required-permission')) {
    // Execute action
  }
}
```

### In templates
```vue
<template>
  <!-- Using global helper -->
  <VcButton v-if="$hasAccess('permission-name')">Action</VcButton>
    
  <!-- Using computed from script -->
  <VcButton v-if="canPerformAction">Action</VcButton>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

const canPerformAction = computed(() => hasAccess('permission-name'));
</script>
```

## Integration with useUser

The `usePermissions` composable internally uses the `useUser` composable to get the current user's permissions. It automatically updates when the user's permissions change.

```typescript
// Internal implementation reference
export function usePermissions(): IUsePermissions {
  const { user } = useUser();
  
  function hasAccess(permissions: string | string[] | undefined) {
    // Administrator always has access
    if (!permissions || user.value?.isAdministrator) {
      return true;
    }
    
    // Permission checking logic...
  }
  
  return { hasAccess };
}
```

## Best practices

* **Computed properties**: When using permissions to control UI elements, wrap `hasAccess` calls in computed properties to ensure reactive updates.
* **Template helper**: Use `$hasAccess` in templates for simple visibility checks and `hasAccess` in script for complex logic.
* **Permission naming**: Use consistent, descriptive permission names following a clear pattern.
* **Multiple permissions**: Remember that permission arrays use OR logic - user needs ANY of the permissions.
* **Error handling**: Always handle the case where a user doesn't have permission gracefully.
* **Administrator handling**: Administrators automatically bypass all permission checks - no need for special handling.

## Related resources

- [Implementing role-based access control with usePermissions](../Usage-Guides/implementing-role-based-access-control-with-usepermissions.md) - Comprehensive guide with practical examples
- [useUser composable](./useUser.md) - User authentication and management
- [Permissions plugin](../plugins/permissions.md) - Framework permission system setup
