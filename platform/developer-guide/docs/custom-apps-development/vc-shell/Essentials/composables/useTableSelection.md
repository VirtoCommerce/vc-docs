# useTableSelection

The `useTableSelection` composable is a dedicated utility for managing table selection state in blade list pages. It simplifies handling selected items, extracting IDs, managing "select all" state, and responding to user interactions with table checkboxes, working seamlessly with the `VcTable` component.

## Basic Usage

The most common use case is to pair `useTableSelection` with `VcTable`. You handle the `@selection-changed` and `@select:all` events from the table using the handlers provided by the composable.

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    multiselect
    select-all
    @selection-changed="handleSelectionChange"
    @select:all="handleSelectAll"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useTableSelection, VcTable, type ITableColumns } from '@vc-shell/framework';

interface User {
  id: string;
  name: string;
  email: string;
}

// 1. Initialize the composable
const {
  selectedItems,
  selectedIds,
  allSelected,
  hasSelection,
  handleSelectionChange,
  handleSelectAll,
  resetSelection,
} = useTableSelection<User>();

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Name' },
  { id: 'email', title: 'Email' },
]);

const items = ref<User[]>([/* ... your data ... */]);

// 2. Use selection state in toolbar actions
const deleteSelected = async () => {
  if (allSelected.value) {
    await api.deleteAll();
  } else {
    await api.deleteByIds(selectedIds.value);
  }
  resetSelection();
};
</script>
```

## Using with Toolbar Actions

A common pattern is to enable/disable toolbar buttons based on selection state:

```vue
<script lang="ts" setup>
import { computed, ref } from 'vue';
import { useTableSelection, type IBladeToolbar } from '@vc-shell/framework';

const {
  selectedIds,
  hasSelection,
  allSelected,
  resetSelection,
  handleSelectionChange,
  handleSelectAll,
} = useTableSelection<Offer>();

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: 'refresh',
    title: 'Refresh',
    icon: 'material-refresh',
    async clickHandler() {
      resetSelection();
      await reload();
    },
  },
  {
    id: 'deleteSelected',
    title: 'Delete Selected',
    icon: 'material-delete',
    disabled: computed(() => !hasSelection.value),
    async clickHandler() {
      await deleteOffers({
        ids: selectedIds.value,
        allSelected: allSelected.value,
      });
      resetSelection();
      await reload();
    },
  },
]);
</script>
```

## Custom ID Field

By default, the composable extracts IDs from the `id` property of each item. You can customize this behavior:

### Using a Different Property Name

```typescript
interface Product {
  productId: string;
  name: string;
}

const { selectedIds } = useTableSelection<Product>({
  idField: 'productId',
});
```

### Using a Function

```typescript
interface LineItem {
  offerId?: string;
  productId?: string;
  sku: string;
}

const { selectedIds } = useTableSelection<LineItem>({
  idField: (item) => item.offerId ?? item.productId ?? item.sku,
});
```

## API Reference

### Initialization

`useTableSelection<T>(options?: UseTableSelectionOptions<T>)`

#### `UseTableSelectionOptions<T>`

An optional object to configure ID extraction.

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `idField` | `keyof T \| ((item: T) => string \| undefined)` | `'id'` | The field or function to use for extracting IDs from items. |

### Return Value

The composable returns an object with the following properties and methods:

#### State Properties

##### `selectedItems`

`Ref<T[]>` - Array of currently selected item objects. This is the primary source of truth for selection state.

##### `selectedIds`

`ComputedRef<string[]>` - Computed array of IDs extracted from selected items using the configured `idField`.

##### `allSelected`

`Ref<boolean>` - Whether "select all" across pagination is active. Used for bulk operations that should affect all items, not just the current page.

##### `selectionCount`

`ComputedRef<number>` - Number of currently selected items.

##### `hasSelection`

`ComputedRef<boolean>` - Whether any items are currently selected. Useful for enabling/disabling toolbar actions.

#### Event Handlers

##### `handleSelectionChange(items: T[])`

Handler for `VcTable`'s `@selection-changed` event. Updates `selectedItems` with the new selection array.

```vue
<VcTable @selection-changed="handleSelectionChange" />
```

##### `handleSelectAll(selected: boolean)`

Handler for `VcTable`'s `@select:all` event. Updates `allSelected` state and clears `selectedItems` when deselecting all.

```vue
<VcTable @select:all="handleSelectAll" />
```

#### Utility Methods

##### `resetSelection()`

Clears all selection state: sets `selectedItems` to empty array and `allSelected` to `false`. Call this after bulk operations or when reloading data.

```typescript
const reload = async () => {
  resetSelection();
  await loadItems();
};
```

##### `selectItems(items: T[])`

Programmatically set the selected items. Useful for action builders or programmatic selection.

```typescript
// Select a single item
selectItems([item]);

// Add item to existing selection
selectItems([...selectedItems.value, newItem]);
```

##### `isSelected(item: T)`

Check if a specific item is currently selected. Returns `boolean`.

```typescript
if (isSelected(item)) {
  console.log('Item is selected');
}
```

##### `deselectByIds(ids: string[])`

Remove items from selection by their IDs.

```typescript
// Deselect specific items
deselectByIds(['id1', 'id2']);
```

## Migration from Manual Implementation

If you have existing code with manual selection handling, here's how to migrate:

### Before

```typescript
const selectedOfferIds = ref<string[]>([]);
const selectedOffers = ref<Offer[]>([]);
const allSelected = ref(false);

const onSelectionChanged = (items: Offer[]) => {
  selectedOffers.value = items;
  selectedOfferIds.value = items.flatMap((item) => (item.id ? [item.id] : []));
};

async function selectAllOffers(all: boolean) {
  allSelected.value = all;
}

const reload = async () => {
  selectedOfferIds.value = [];
  await loadOffers();
};
```

### After

```typescript
const {
  selectedItems: selectedOffers,
  selectedIds: selectedOfferIds,
  allSelected,
  handleSelectionChange: onSelectionChanged,
  handleSelectAll: selectAllOffers,
  resetSelection,
} = useTableSelection<Offer>();

const reload = async () => {
  resetSelection();
  await loadOffers();
};
```

## Integration Notes

### With AI Agent Context

The `useTableSelection` composable does not automatically integrate with AI Agent context. If you need AI Agent integration, call `useAiAgentContext` separately:

```typescript
const { selectedItems } = useTableSelection<Offer>();
useAiAgentContext({ dataRef: selectedItems });
```

### With useTableSort

These composables work independently and can be used together:

```typescript
const { sortExpression, handleSortChange } = useTableSort({
  initialProperty: 'createdDate',
  initialDirection: 'DESC',
});

const {
  selectedIds,
  handleSelectionChange,
  resetSelection,
} = useTableSelection<Offer>();
```

## TypeScript Support

The composable is fully typed with generics:

```typescript
// Type is inferred from the generic parameter
const { selectedItems } = useTableSelection<Offer>();
// selectedItems is Ref<Offer[]>
// selectedIds is ComputedRef<string[]>
```
