# How-To: Implementing Role-Based Access Control with `usePermissions`

The `usePermissions` composable provides a robust system for implementing role-based access control in VC-Shell applications. This guide demonstrates how to effectively control access to features, UI elements, and navigation based on user permissions in your application components.

## Prerequisites

- Understanding of Vue 3 Composition API and template syntax.
- Familiarity with the `usePermissions` composable (see [usePermissions API Reference](../composables/usePermissions.md)).
- Basic knowledge of VC-Shell's application architecture and user management.
- Understanding of role-based access control concepts and security patterns.

## Core Concept

The Permission system provides two main approaches for permission checks:

- **Composable Usage**: Using `usePermissions()` in TypeScript code
- **Template Helper**: Using the global `$hasAccess` function directly in Vue templates
- **Automatic Administrator Access**: Administrators automatically bypass all permission checks
- **Flexible Permission Types**: Supports single permissions, multiple permissions (OR logic), and conditional access

The system integrates seamlessly with VC-Shell's navigation, dashboard, and UI components.

```typescript
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

// Single permission check
if (hasAccess('create-products')) {
  // User can create products
}

// Multiple permissions (OR logic)
if (hasAccess(['edit-products', 'manage-products'])) {
  // User has either permission
}
```

## Implementation Strategies

### 1. Component Template Permission Control

Control visibility of UI elements based on user permissions:

```vue
<!-- ProductManagement.vue -->
<template>
  <div class="product-management">
    <!-- Create button - only for users with create permission -->
    <VcButton 
      v-if="$hasAccess('create-products')"
      @click="createProduct"
    >
      Create Product
    </VcButton>

    <!-- Product list with conditional actions -->
    <VcTable :items="products">
      <template #actions="{ item }">
        <VcButton 
          v-if="$hasAccess('edit-products')"
          size="sm"
          @click="editProduct(item)"
        >
          Edit
        </VcButton>
        <VcButton 
          v-if="$hasAccess('delete-products')"
          size="sm"
          variant="danger"
          @click="deleteProduct(item)"
        >
          Delete
        </VcButton>
        <VcButton 
          v-if="$hasAccess(['publish-products', 'manage-products'])"
          size="sm"
          variant="outline"
          @click="publishProduct(item)"
        >
          Publish
        </VcButton>
      </template>
    </VcTable>

    <!-- Admin-only section -->
    <div v-if="$hasAccess('admin-access')" class="admin-section">
      <h3>Administrative Actions</h3>
      <VcButton @click="bulkOperations">Bulk Operations</VcButton>
      <VcButton @click="systemSettings">System Settings</VcButton>
    </div>

    <!-- Conditional content based on multiple permissions -->
    <div v-if="$hasAccess('view-analytics') && $hasAccess('view-reports')">
      <ProductAnalytics />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

function createProduct() {
  // Additional permission check in logic if needed
  if (!hasAccess('create-products')) {
    notification.error('Permission denied');
    return;
  }
  // Create product logic
}

function deleteProduct(product: Product) {
  // Multiple permission check example
  if (!hasAccess(['delete-products', 'admin-access'])) {
    notification.error('Insufficient permissions');
    return;
  }
  // Delete logic
}
</script>
```

### 2. Computed Properties for Complex Permission Logic

Use computed properties for reactive permission checks:

```vue
<!-- UserManagement.vue -->
<template>
  <div class="user-management">
    <div class="user-actions">
      <VcButton 
        v-if="canCreateUsers"
        @click="createUser"
      >
        Create User
      </VcButton>
      
      <VcButton 
        v-if="canManageRoles"
        @click="manageRoles"
      >
        Manage Roles
      </VcButton>
    </div>

    <VcTable :items="users">
      <template #actions="{ item }">
        <VcButton 
          v-if="canEditUser(item)"
          size="sm"
          @click="editUser(item)"
        >
          Edit
        </VcButton>
        <VcButton 
          v-if="canDeleteUser(item)"
          size="sm"
          variant="danger"
          @click="deleteUser(item)"
        >
          Delete
        </VcButton>
      </template>
    </VcTable>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

// Computed properties for permissions
const canCreateUsers = computed(() => hasAccess('create-users'));
const canManageRoles = computed(() => hasAccess(['manage-roles', 'admin-access']));

// Function-based permission checks for dynamic data
function canEditUser(user: User) {
  if (hasAccess('admin-access')) return true;
  if (hasAccess('edit-users')) return true;
  if (hasAccess('edit-own-profile') && user.id === currentUser.value?.id) return true;
  return false;
}

function canDeleteUser(user: User) {
  return hasAccess(['delete-users', 'admin-access']) && user.id !== currentUser.value?.id;
}
</script>
```

### 3. Blade Component Permission Control

Control blade access and functionality based on permissions:

```vue
<!-- ProductDetailsBlade.vue -->
<script lang="ts" setup>
import { computed } from 'vue';
import { usePermissions } from '@vc-shell/framework';

// Define blade permissions
defineOptions({
  name: 'ProductDetails',
  url: '/product',
  permissions: 'view-products' // Required to open this blade
});

const { hasAccess } = usePermissions();

// Internal permission checks for blade functionality
const canEdit = computed(() => hasAccess('edit-products'));
const canDelete = computed(() => hasAccess('delete-products'));
const canPublish = computed(() => hasAccess(['publish-products', 'admin-access']));

function handleSave() {
  if (!hasAccess('edit-products')) {
    notification.error('You do not have permission to edit products');
    return;
  }
  // Save logic
}

function handleDelete() {
  if (!hasAccess('delete-products')) {
    notification.error('You do not have permission to delete products');
    return;
  }
  // Delete logic
}
</script>

<template>
  <VcBlade title="Product Details">
    <div class="product-form">
      <!-- Form fields -->
      <VcInput v-model="product.name" label="Product Name" :readonly="!canEdit" />
      
      <!-- Action buttons based on permissions -->
      <div class="actions">
        <VcButton 
          v-if="canEdit"
          @click="handleSave"
        >
          Save
        </VcButton>
        
        <VcButton 
          v-if="canPublish"
          variant="outline"
          @click="handlePublish"
        >
          Publish
        </VcButton>
        
        <VcButton 
          v-if="canDelete"
          variant="danger"
          @click="handleDelete"
        >
          Delete
        </VcButton>
      </div>
    </div>
  </VcBlade>
</template>
```

### 4. Menu Registration with Permissions

Register application menu items with permission requirements:

```typescript
// bootstrap.ts
import { addMenuItem } from '@vc-shell/framework';

export function setupApplicationMenu() {
  // Public menu item (no permissions required)
  addMenuItem({
    id: 'dashboard',
    title: 'Dashboard',
    icon: 'fas fa-home',
    priority: 0,
    url: '/'
  });

  // Permission-protected menu items
  addMenuItem({
    id: 'products',
    title: 'Products',
    icon: 'fas fa-box',
    priority: 10,
    url: '/products',
    permissions: 'view-products' // Single permission
  });

  addMenuItem({
    id: 'orders',
    title: 'Orders', 
    icon: 'fas fa-shopping-cart',
    priority: 20,
    url: '/orders',
    permissions: ['view-orders', 'manage-orders'] // Multiple permissions (OR)
  });

  addMenuItem({
    id: 'users',
    title: 'User Management',
    icon: 'fas fa-users',
    priority: 30,
    url: '/users',
    permissions: 'manage-users'
  });

  addMenuItem({
    id: 'admin',
    title: 'Administration',
    icon: 'fas fa-cog',
    priority: 100,
    url: '/admin',
    permissions: 'admin-access' // Admin only
  });
}
```

### 5. Dashboard Widget Permission Control

Control dashboard widget visibility using permissions:

```typescript
// dashboard-setup.ts
import { registerDashboardWidget } from '@vc-shell/framework';
import SalesWidget from './widgets/SalesWidget.vue';
import UserAnalyticsWidget from './widgets/UserAnalyticsWidget.vue';
import AdminWidget from './widgets/AdminWidget.vue';

export function setupDashboardWidgets() {
  // Widget visible to all users
  registerDashboardWidget({
    id: 'welcome',
    name: 'Welcome',
    component: WelcomeWidget,
    size: { width: 2, height: 1 },
    position: { x: 0, y: 0 }
  });

  // Sales widget - requires view-sales permission
  registerDashboardWidget({
    id: 'sales-overview',
    name: 'Sales Overview',
    component: SalesWidget,
    size: { width: 3, height: 2 },
    position: { x: 2, y: 0 },
    permissions: ['view-sales-data'] // Only users with this permission see the widget
  });

  // Analytics widget - requires multiple permissions
  registerDashboardWidget({
    id: 'user-analytics',
    name: 'User Analytics',
    component: UserAnalyticsWidget,
    size: { width: 2, height: 2 },
    position: { x: 0, y: 1 },
    permissions: ['view-analytics', 'view-user-data'] // OR logic
  });

  // Admin-only widget
  registerDashboardWidget({
    id: 'admin-panel',
    name: 'Admin Panel',
    component: AdminWidget,
    size: { width: 4, height: 1 },
    position: { x: 0, y: 3 },
    permissions: 'admin-access'
  });
}
```

### 6. Composable with Permission Checks

Create composables that integrate permission checking:

```typescript
// useProductOperations.ts
import { usePermissions } from '@vc-shell/framework';

export function useProductOperations() {
  const { hasAccess } = usePermissions();

  function createProduct(productData: ProductData) {
    if (!hasAccess('create-products')) {
      throw new Error('Permission denied: create-products required');
    }
    
    // Create product logic
    return api.createProduct(productData);
  }

  function updateProduct(id: string, productData: ProductData) {
    if (!hasAccess('edit-products')) {
      throw new Error('Permission denied: edit-products required');
    }
    
    // Update product logic
    return api.updateProduct(id, productData);
  }

  function deleteProduct(id: string) {
    if (!hasAccess(['delete-products', 'admin-access'])) {
      throw new Error('Permission denied: delete-products or admin-access required');
    }
    
    // Delete product logic
    return api.deleteProduct(id);
  }

  function publishProduct(id: string) {
    if (!hasAccess(['publish-products', 'admin-access'])) {
      throw new Error('Permission denied: publish-products or admin-access required');
    }
    
    // Publish product logic
    return api.publishProduct(id);
  }

  // Return permission-checked functions
  return {
    createProduct: hasAccess('create-products') ? createProduct : null,
    updateProduct: hasAccess('edit-products') ? updateProduct : null,
    deleteProduct: hasAccess(['delete-products', 'admin-access']) ? deleteProduct : null,
    publishProduct: hasAccess(['publish-products', 'admin-access']) ? publishProduct : null,
    
    // Permission flags for UI
    canCreate: hasAccess('create-products'),
    canEdit: hasAccess('edit-products'),
    canDelete: hasAccess(['delete-products', 'admin-access']),
    canPublish: hasAccess(['publish-products', 'admin-access'])
  };
}
```

### 7. Router Navigation Guards

Implement route-level permission protection for **regular pages** (not blades). When adding routes, it's important to place them correctly in your routing configuration. Pages that should appear within the main application layout (with the shell's header, sidebar, etc.) should be added as `children` of the main `App` component route. Standalone pages like `Login` are defined at the top level.

Blades automatically handle permissions through `defineOptions`, which are processed by the framework and added to `meta.permissions` internally.

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router';
import { usePermissions, App, Login } from '@vc-shell/framework';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // Main application route with shared layout
    {
      path: '/',
      component: App,
      name: 'App',
      meta: {
        root: true,
      },
      // Routes that should render inside the main App layout go here
      children: [
        {
          path: '', // Default child route, often the dashboard
          name: 'Dashboard',
          component: () => import('@/pages/Dashboard.vue'),
          // No permissions required for dashboard
        },
        {
          path: 'reports', // resolves to /reports
          name: 'Reports',
          component: () => import('@/pages/Reports.vue'),
          meta: {
            permissions: ['view-reports', 'view-analytics'] // User needs ANY of these
          }
        },
        {
          path: 'settings', // resolves to /settings
          name: 'Settings',
          component: () => import('@/pages/Settings.vue'),
          meta: {
            permissions: 'admin-access'
          }
        },
      ],
    },
    
    // Standalone pages (like Login) which do not use the main App layout
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    
    // Note: Blade routes are handled automatically by the framework.
    // They use permissions from defineOptions, so no manual route config is needed for them.
  ]
});

// Navigation guard for permission checking (applies to regular pages only)
router.beforeEach((to, from, next) => {
  const { hasAccess } = usePermissions();
  
  // Check if route requires permissions
  if (to.meta.permissions) {
    if (hasAccess(to.meta.permissions as string | string[])) {
      next();
    } else {
      // Redirect to unauthorized page or show error
      next({ name: 'Unauthorized' });
    }
  } else {
    next();
  }
});

export default router;
```

**Important Notes:**

- **Nested vs. Top-level Routes**: As shown above, place pages intended to be inside your main application UI as `children` of the `App` route. Standalone pages (e.g., authentication) are placed at the top level.
- **Blades**: Use `permissions` in `defineOptions` - framework handles route protection automatically.
- **Regular Pages**: Require manual `meta.permissions` configuration and navigation guards as shown in the example.
- **Framework Integration**: Blade permissions from `defineOptions` are automatically converted to `meta.permissions` by the framework.

### 8. Form Field Conditional Rendering

Control form field visibility based on permissions:

```vue
<!-- ProductForm.vue -->
<template>
  <VcForm @submit="handleSubmit">
    <!-- Basic fields visible to all users with view permission -->
    <VcInput 
      v-model="product.name" 
      label="Product Name" 
      :readonly="!canEdit"
    />
    
    <VcTextarea 
      v-model="product.description" 
      label="Description"
      :readonly="!canEdit"
    />

    <!-- Price field - only for users with price management permission -->
    <VcInput 
      v-if="$hasAccess('manage-prices')"
      v-model="product.price" 
      label="Price" 
      type="number"
      :readonly="!canEdit"
    />

    <!-- Internal notes - admin only -->
    <VcTextarea 
      v-if="$hasAccess('admin-access')"
      v-model="product.internalNotes" 
      label="Internal Notes"
    />

    <!-- Inventory section - requires inventory permission -->
    <div v-if="$hasAccess('manage-inventory')" class="inventory-section">
      <h3>Inventory Management</h3>
      <VcInput 
        v-model="product.stockQuantity" 
        label="Stock Quantity" 
        type="number"
      />
      <VcInput 
        v-model="product.reorderLevel" 
        label="Reorder Level" 
        type="number"
      />
    </div>

    <!-- Action buttons -->
    <div class="form-actions">
      <VcButton 
        v-if="canEdit"
        type="submit"
      >
        Save
      </VcButton>
      
      <VcButton 
        v-if="$hasAccess('publish-products')"
        variant="outline"
        @click="handlePublish"
      >
        Save & Publish
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
import { usePermissions } from '@vc-shell/framework';

const { hasAccess } = usePermissions();

const canEdit = computed(() => hasAccess(['edit-products', 'admin-access']));

function handleSubmit() {
  if (!canEdit.value) {
    notification.error('You do not have permission to edit products');
    return;
  }
  // Submit logic
}

function handlePublish() {
  if (!hasAccess('publish-products')) {
    notification.error('You do not have permission to publish products');
    return;
  }
  // Publish logic
}
</script>
```

## Best Practices

* **Template vs Script Usage**: Use `$hasAccess` in templates for simple visibility control and `hasAccess` in script for complex logic.

* **Permission Naming**: Use clear, descriptive permission names following a consistent pattern (e.g., `action-resource` format like `edit-products`, `view-orders`).

* **Multiple Permissions**: When using arrays, remember it implements OR logic - user needs ANY of the permissions.

* **Administrator Handling**: The system automatically grants administrators access to everything - no need to check for admin role explicitly.

* **Early Returns**: Check permissions early in functions to avoid unnecessary processing.

* **User Feedback**: Always provide clear feedback when users lack permissions using notifications or disabled states.

* **Computed Properties**: Use computed properties for permissions that affect reactive UI elements.

* **Defensive Programming**: Always validate permissions in business logic, not just in the UI.

