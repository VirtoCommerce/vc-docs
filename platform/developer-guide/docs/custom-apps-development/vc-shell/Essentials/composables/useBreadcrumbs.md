# useBreadcrumbs Composable

The `useBreadcrumbs` composable provides functionality for managing navigation breadcrumbs in VC-Shell applications. It helps track user navigation paths and create a hierarchical trail showing the user's location within the application.

The `useBreadcrumbs` composable manages a history of breadcrumb items, allowing you to push new items as the user navigates deeper into the application and remove items when the user navigates back. This creates a dynamic breadcrumb trail that accurately reflects the user's current location in the navigation hierarchy.

## API reference

### Return value

The `useBreadcrumbs` composable returns an object with the following properties and methods:

```typescript
interface IUseBreadcrumbs {
  breadcrumbs: ComputedRef<Breadcrumbs[]>;  // Array of breadcrumb items
  push: (breadcrumb: Breadcrumbs) => void;  // Add a breadcrumb to the trail
  remove: (ids: string[]) => void;          // Remove breadcrumbs by their IDs
}
```

### Methods

#### push

Adds a new breadcrumb to the trail. If the breadcrumb has the same ID or title as the current one, it won't create duplicates.

```typescript
push(breadcrumb: Breadcrumbs): void
```

- `breadcrumb`: The breadcrumb object to add to the trail

#### remove

Removes one or more breadcrumbs from the trail by their IDs.

```typescript
remove(ids: string[]): void
```

- `ids`: Array of breadcrumb IDs to remove

### Properties

#### breadcrumbs

A computed reference to the array of breadcrumb items currently in the trail.

```typescript
breadcrumbs: ComputedRef<Breadcrumbs[]>
```

### Breadcrumbs interface

The breadcrumb objects used with this composable should follow this interface:

```typescript
interface Breadcrumbs {
  id: string;                            // Unique identifier for the breadcrumb
  title: string | ComputedRef<string>;   // Display text for the breadcrumb
  icon?: string | Component;             // Optional icon for the breadcrumb
  clickHandler?: (id: string) => Promise<boolean | void> | boolean | void;  // Click handler
}
```

## Usage

```typescript
import { useBreadcrumbs } from '@vc-shell/framework';

const { breadcrumbs, push, remove } = useBreadcrumbs();

// Add a breadcrumb
push({
  id: 'home',
  title: 'Home',
  icon: 'material-home',
  clickHandler: () => {
    // Navigation logic
    return true; // Return true to remove subsequent breadcrumbs
  }
});

// Remove breadcrumbs by IDs
remove(['breadcrumb-id-1', 'breadcrumb-id-2']);
```

## Related resources

- [VcBreadcrumbs Component](../ui-components/vc-breadcrumbs.md) - UI component for displaying breadcrumbs
- [Navigation](../navigation.md) - General information about navigation in VC-Shell 
- [Implementing Navigational Breadrumbs](../Usage-Guides/implementing-navigational-breadcrumbs-with-usebreadcrumbs.md) - Guide for implementing navigation with useBreadcrumbs
