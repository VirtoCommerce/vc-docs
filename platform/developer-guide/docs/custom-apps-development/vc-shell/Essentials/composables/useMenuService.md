# useMenuService Composable

The `useMenuService` composable provides access to the Menu Service, which handles the registration and organization of menu items in the VC-Shell framework. This composable allows components to add, remove, and manage menu items throughout the application.

The `useMenuService` composable is a key utility for managing the application's navigation menu structure. It works with the Menu Service to provide a centralized way of registering menu items, organizing them into groups, and setting up the overall navigation hierarchy.

## API reference

### Return value

The `useMenuService` composable returns the Menu Service object with the following properties and methods:

```typescript
interface MenuService {
  addMenuItem: (item: MenuItem) => void;    // Adds a menu item to the menu
  menuItems: Ref<MenuItem[]>;               // Reactive reference to the menu items
  removeMenuItem: (item: MenuItem) => void; // Removes a menu item from the menu
}
```

### Methods

#### addMenuItem

Adds a menu item to the navigation menu.

```typescript
addMenuItem(item: MenuItem): void
```

- `item`: The menu item to add. See the MenuItem interface for details.

#### removeMenuItem

Removes a menu item from the navigation menu.

```typescript
removeMenuItem(item: MenuItem): void
```

- `item`: The menu item to remove.

### Properties

#### menuItems

A reactive reference to the array of menu items, organized into their final structure with groups and priorities applied.

```typescript
menuItems: Ref<MenuItem[]>
```

### MenuItem interface

```typescript
interface MenuItem {
  id?: string;                           // Unique identifier (generated if not provided)
  title: string | ComputedRef<string>;   // Menu item title (will be localized)
  url?: string;                          // Route URL or path
  routeId?: string;                      // Optional route identifier (e.g., for named routes)
  icon?: string | Component;             // Icon identifier or component
  priority?: number;                     // Sorting priority (lower = higher in the menu)
  permissions?: string | string[];       // Required permissions
  
  // Modern group configuration
  groupConfig?: {                       
    id: string;                          // Group ID (required)
    title?: string;                      // Group title (optional)
    icon?: string | Component;           // Group icon (optional)
    priority?: number;                   // Group priority (optional)
    permissions?: string | string[];     // Group permissions (optional)
  };
}
```

## Usage

### Basic usage

```typescript
import { useMenuService } from '@vc-shell/framework';

export default {
  setup() {
    const { addMenuItem } = useMenuService();
    
    // Add a menu item
    addMenuItem({
      id: 'dashboard',
      title: 'Dashboard',
      url: '/dashboard',
      icon: 'material-dashboard',
      priority: 10
    });
    
    // Add another menu item
    addMenuItem({
      id: 'products',
      title: 'Products',
      url: '/products',
      icon: 'material-inventory',
      priority: 20
    });
  
  }
}
```

### Using in application bootstrap

```typescript
// src/bootstrap.ts
import { useMenuService } from '@vc-shell/framework';
import { App } from 'vue';

export function bootstrap(app: App) {
  const { addMenuItem } = useMenuService();

  // Add Dashboard to main menu
  addMenuItem({
    id: "dashboard",
    title: "SHELL.MENU.DASHBOARD",  // Translation key
    icon: "material-home",
    priority: 0,
    url: "/",
  });
  
  // Add Contacts section
  addMenuItem({
    id: "contacts",
    title: "CONTACTS.MENU.TITLE",
    icon: "material-contacts",
    priority: 10,
    url: "/contacts"
  });
}
```

### Creating grouped menu items

```typescript
import { useMenuService } from '@vc-shell/framework';

export default {
  setup() {
    const { addMenuItem } = useMenuService();
    
    // Modern approach with groupConfig
    addMenuItem({
      id: "settings",
      title: 'Settings',
      url: '/settings',
      icon: 'settings',
      priority: 100,
      groupConfig: {
        id: 'settings-group',
        title: 'Settings',
        icon: 'material-settings',
        priority: 100
      }
    });
    
    // Add more items to the same group (minimal config)
    addMenuItem({
      id: "users",
      title: 'Users',
      url: '/users',
      icon: 'people',
      priority: 110,
      groupConfig: {
        id: 'settings-group'  // Just the group ID
      }
    });
    
    addMenuItem({
      id: "security",
      title: 'Security',
      url: '/security',
      icon: 'shield',
      priority: 120,
      groupConfig: {
        id: 'settings-group'  // Same group ID
      }
    });
  }
}
```

### Menu with permissions

```typescript
import { useMenuService } from '@vc-shell/framework';

export default {
  setup() {
    const { addMenuItem } = useMenuService();
    
    // Add a menu item that requires specific permissions
    addMenuItem({
      id: "admin-dashboard",
      title: 'Admin Dashboard',
      url: '/admin',
      icon: 'admin_panel_settings',
      priority: 5,
      permissions: 'admin-access'  // Can be a string
    });
    
    // Add a menu item that requires multiple permissions
    addMenuItem({
      id: "security-settings",
      title: 'Security Settings',
      url: '/admin/security',
      icon: 'security',
      priority: 15,
      permissions: ['admin-access', 'security-manage']  // Can be an array
    });
    
    // Add a group with permissions
    addMenuItem({
      id: "user-management",
      title: 'User Management',
      url: '/admin/users',
      icon: 'manage_accounts',
      priority: 25,
      groupConfig: {
        id: 'admin-group',
        title: 'Administration',
        icon: 'admin_panel_settings',
        permissions: 'admin-access'  // Group-level permission
      }
    });
  }
}
```

## Best practices

* **Registration timing**: Register menu items as early as possible in the application lifecycle, typically during the bootstrap process.
* **Localization**: Use translation keys for menu item titles to support multilingual applications.
* **Permissions**: Use the permissions property to control menu item visibility based on user roles.
* **Group organization**: Use the groupConfig approach for more complex grouping scenarios.
* **Priorities**: Use priorities to control the order of menu items and groups.

## Related resources

- [Permissions system](../composables/usePermissions.md) - Information about the permissions system
- [Navigation](../navigation.md) - General navigation documentation 
