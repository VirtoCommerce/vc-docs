# How-To: Building Navigation Menus with `useMenuService`

The `useMenuService` composable provides a centralized system for managing application navigation menus in VC-Shell. This guide demonstrates how to effectively register menu items, organize them into groups, and implement permission-based navigation for comprehensive menu systems.

## Prerequisites

- Understanding of Vue 3 Composition API and application lifecycle.
- Familiarity with the `useMenuService` composable (see [useMenuService API Reference](../composables/useMenuService.md)).
- Basic knowledge of VC-Shell's permission system and routing.
- Understanding of application bootstrap and module registration patterns.

## Core Concept

The Menu Service manages the application's navigation structure through:

- **Menu Item Registration**: Adding individual navigation items with metadata
- **Group Organization**: Organizing items into logical sections with priorities
- **Permission Control**: Showing/hiding menu items based on user permissions
- **Dynamic Updates**: Runtime menu modification based on application state
- **Automatic Module Registration**: Modules can automatically add themselves to the menu

Menu items can be registered manually or automatically through module registration. When using `createAppModule`, any blade with a `menuItem` property in its `defineOptions` will be automatically added to the navigation menu.

```typescript
import { useMenuService } from '@vc-shell/framework';

const { addMenuItem } = useMenuService();

// Manual registration
addMenuItem({
  id: 'dashboard',
  title: 'Dashboard',
  url: '/dashboard',
  icon: 'material-dashboard',
  priority: 10
});
```

## Implementation Strategies

### 1. Application Bootstrap Setup

Register core application menu items during bootstrap:

This pattern is ideal for adding core pages like a main Dashboard. For a complete walkthrough of creating a custom page and adding it to the menu, see the [Adding Custom Pages and Menu Items](./adding-custom-pages-and-menu-items.md) guide.

```typescript
// src/bootstrap.ts
import { useMenuService } from '@vc-shell/framework';

export function bootstrap() {
  const { addMenuItem } = useMenuService();

  // Core navigation items
  addMenuItem({
    id: "dashboard",
    title: "SHELL.MENU.DASHBOARD",
    icon: "material-home",
    priority: 0,
    url: "/",
  });
}
```

### 2. Automatic Module Registration

The most common pattern is to let modules automatically register themselves by adding `menuItem` to blade components:

```vue
<!-- ProductListBlade.vue -->
<script lang="ts" setup>
import { defineOptions } from 'vue';

// Automatic menu registration through defineOptions
defineOptions({
  name: 'ProductList',
  url: '/products',
  menuItem: {
    title: 'Products',
    icon: 'material-inventory',
    priority: 10,
    groupConfig: {
      id: 'catalog-group',
      title: 'Catalog',
      icon: 'material-category',
      priority: 20
    },
    permissions: 'products:view'
  }
});
</script>
```

When this blade is registered through `createAppModule`, it will automatically appear in the navigation menu:

```typescript
// src/modules/products/index.ts
import { createAppModule } from '@vc-shell/framework';
import ProductListBlade from './pages/ProductListBlade.vue';
import ProductDetailsBlade from './pages/ProductDetailsBlade.vue';

export default createAppModule({
  ProductList: ProductListBlade,    // Will be added to menu automatically
  ProductDetails: ProductDetailsBlade // No menuItem = won't appear in menu
});
```

### 3. Manual Module-Based Registration

For more control, you can manually register menu items within module setup:

```typescript
// src/modules/products/index.ts
import { createAppModule, useMenuService } from '@vc-shell/framework';

export function registerProductsMenu() {
  const { addMenuItem } = useMenuService();

  addMenuItem({
    id: "products-catalog",
    title: "Products Catalog",
    url: "/products/catalog",
    icon: "material-category",
    priority: 10,
    groupConfig: {
      id: 'products-group',
      title: 'Products',
      icon: 'material-inventory',
      priority: 10
    }
  });

  addMenuItem({
    id: "products-import",
    title: "Import Products", 
    url: "/products/import",
    icon: "material-upload",
    priority: 20,
    groupConfig: {
      id: 'products-group'
    },
    permissions: 'products:import'
  });
}

// Call during module initialization
registerProductsMenu();
```

### 4. Permission-Based Menu Items

Control menu visibility based on user permissions:

```typescript
// Permission-controlled menu setup
export function setupSecureMenuItems() {
  const { addMenuItem } = useMenuService();
  const { hasPermission } = usePermissions();

  // Admin-only section
  if (hasPermission('admin')) {
    addMenuItem({
      id: "admin-dashboard",
      title: "Admin Dashboard",
      url: "/admin",
      icon: "material-admin_panel_settings",
      priority: 5,
      permissions: 'admin-access'
    });

    addMenuItem({
      id: "user-management",
      title: "Users",
      url: "/admin/users",
      icon: "material-people",
      priority: 10,
      groupConfig: {
        id: 'admin-group',
        title: 'Administration',
        icon: 'material-settings',
        permissions: 'admin-access'
      }
    });
  }

  // Role-based items
  if (hasPermission('reports:view')) {
    addMenuItem({
      id: "analytics",
      title: "Analytics",
      url: "/analytics", 
      icon: "material-analytics",
      priority: 30,
      permissions: ['reports:view', 'analytics:access']
    });
  }
}
```

### 5. Dynamic Menu Registration

Register menu items based on application state or user data:

```typescript
// Dynamic menu based on user context
export function setupDynamicMenus() {
  const { addMenuItem } = useMenuService();
  const { user } = useUser();

  // Tenant-specific menus
  if (user.value?.tenantType === 'marketplace') {
    addMenuItem({
      id: "marketplace-tools",
      title: "Marketplace Tools",
      url: "/marketplace",
      icon: "material-store",
      priority: 15
    });
  }

  // Feature-flag based menus
  if (isFeatureEnabled('advanced-analytics')) {
    addMenuItem({
      id: "advanced-reports",
      title: "Advanced Reports",
      url: "/reports",
      icon: "material-assessment",
      priority: 20,
      groupConfig: {
        id: 'reports-group',
        title: 'Reports',
        priority: 40
      }
    });
  }
}
```

### 6. Grouped Menu Organization

Create well-organized menu groups with proper hierarchy:

```typescript
// Organized menu structure with groups
export function setupGroupedMenus() {
  const { addMenuItem } = useMenuService();

  // E-commerce group
  const ecommerceGroup = {
    id: 'ecommerce-group',
    title: 'E-commerce',
    icon: 'material-shopping_bag',
    priority: 20
  };

  addMenuItem({
    id: "catalog",
    title: "Catalog Management",
    url: "/catalog",
    icon: "material-category",
    priority: 10,
    groupConfig: ecommerceGroup
  });

  addMenuItem({
    id: "inventory",
    title: "Inventory",
    url: "/inventory", 
    icon: "material-warehouse",
    priority: 20,
    groupConfig: ecommerceGroup
  });

  // Operations group
  const operationsGroup = {
    id: 'operations-group',
    title: 'Operations',
    icon: 'material-business',
    priority: 30
  };

  addMenuItem({
    id: "fulfillment",
    title: "Fulfillment",
    url: "/fulfillment",
    icon: "material-local_shipping",
    priority: 10,
    groupConfig: operationsGroup
  });

  addMenuItem({
    id: "returns",
    title: "Returns",
    url: "/returns",
    icon: "material-keyboard_return", 
    priority: 20,
    groupConfig: operationsGroup
  });
}
```

## MenuItem Configuration

When defining menu items, whether through the `addMenuItem` function of `useMenuService` or via the `menuItem` property in a blade's `defineOptions`, you should use an object that conforms to the `MenuItem` interface defined in the [`useMenuService` API documentation](../composables/useMenuService.md#menuitem-interface). This interface typically includes fields like:

```typescript
import { type ComputedRef, type Component } from 'vue';

interface MenuItem {
  id?: string;                           // Unique identifier (generated if not provided when using useMenuService)
  title: string | ComputedRef<string>;   // Menu item title (use translation keys for localization)
  url?: string;                          // Route URL or path for navigation
  routeId?: string;                      // Optional route identifier (e.g., for named Vue Router routes)
  icon?: string | Component;             // Icon identifier (e.g., 'material-home') or an imported Vue component
  priority?: number;                     // Sorting priority (lower numbers appear higher in the menu)
  permissions?: string | string[];       // Optional: Permissions required to display this item
  
  // Modern group configuration
  groupConfig?: {                       
    id: string;                          // Group ID (required to associate item with a group)
    title?: string | ComputedRef<string>; // Group title (required only when this item is the first to define the group)
    icon?: string | Component;           // Optional icon for the group
    priority?: number;                   // Optional priority for the group itself (affects group order)
    permissions?: string | string[];     // Optional: Permissions required to display the entire group
  };
}
```

Key points for `MenuItem` configuration:

-   **`id`**: While optional in `useMenuService.addMenuItem` (where it's auto-generated if missing), providing a unique `id` is good practice, especially for items defined in `defineOptions` or if you need to reference them later (e.g., for removal, though `removeMenuItem` is less commonly used manually).
-   **`title`**: Use translation keys for `title` to support multiple languages (e.g., `SHELL.MENU.DASHBOARD`).
-   **`priority`**: This determines the order of items within their group or at the top level. Lower numbers appear first.
-   **`groupConfig.id`**: Essential for grouping. All items belonging to the same group must share the same `groupConfig.id`.
-   **`groupConfig.title`**: Only needs to be specified by the *first* item that defines a new group. Subsequent items added to that group only need the `groupConfig.id`. If multiple items provide a `title` for the same `groupConfig.id`, the service typically uses the first one it encounters or based on priority.
-   **`groupConfig.priority`**: This priority is for the group itself, determining its order relative to other groups or top-level items. Item `priority` determines order *within* a group.

### Minimal Group Configuration

When adding items to an existing group, or when the first item in a module defines a group, you often only need minimal `groupConfig` details.

**Example 1: First item in a blade defines a new group (via `defineOptions`)**

```vue
<!-- ProductsBlade.vue -->
<script lang="ts" setup>
import { defineOptions } from 'vue';

defineOptions({
  name: 'Products',
  url: '/products',
  menuItem: {
    title: 'PRODUCTS.MENU.TITLE',       // Translation key for product list
    icon: 'material-inventory',
    priority: 10,
    groupConfig: {
      id: 'catalog-group',            // Defines or joins 'catalog-group'
      title: 'CATALOG.MENU.GROUP_TITLE' // Title for the group (translation key)
      // icon and priority for the group itself can also be set here
    }
  }
});
</script>
```

**Example 2: Subsequent item added to the *same* group (via `defineOptions` in another blade)**

```vue
<!-- CategoriesBlade.vue -->
<script lang="ts" setup>
import { defineOptions } from 'vue';

defineOptions({
  name: 'Categories',
  url: '/categories',
  menuItem: {
    title: 'CATEGORIES.MENU.TITLE',   // Translation key for category list
    icon: 'material-category',
    priority: 20,                     // Will appear after 'Products' in the same group
    groupConfig: {
      id: 'catalog-group'           // Only ID needed, as group 'catalog-group' is already defined (with title)
    }
  }
});
</script>
```

**Example 3: Manual registration with `useMenuService` for an existing group**

```typescript
// Assuming 'catalog-group' was already defined with a title by a blade
import { useMenuService } from '@vc-shell/framework';
const { addMenuItem } = useMenuService();

addMenuItem({
  id: 'brands-link',
  title: 'BRANDS.MENU.TITLE',
  url: '/brands',
  icon: 'material-star',
  priority: 30,
  groupConfig: {
    id: 'catalog-group' // Title for groupConfig not needed here
  }
});
```

## Best Practices

* **Automatic Registration**: Prefer automatic menu registration through `defineOptions` and `menuItem` for blade components to keep menu configuration close to the component.

* **Group Organization**: Use the modern `groupConfig` approach instead of deprecated `group` and `groupIcon` properties for better maintainability.

* **Permission Integration**: Always use the `permissions` property for sensitive menu items rather than conditional registration based on roles.

* **Translation Keys**: Use translation keys for menu titles and group titles to support multiple languages.

* **Priority Planning**: Plan your priority numbering system (e.g., increments of 10) to allow for future menu items without reorganization.

* **Consistent Iconography**: Use Material Design icons consistently across your menu items for a cohesive visual experience.

* **URL Consistency**: Ensure menu URLs align with your blade URLs and routing structure.
