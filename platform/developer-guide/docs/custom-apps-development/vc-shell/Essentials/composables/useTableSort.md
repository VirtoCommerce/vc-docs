# useTableSort

The `useTableSort` composable is a dedicated utility for managing table sorting logic. It simplifies handling sort state, generating sort expressions, and responding to user interactions with table headers, working seamlessly with components like `VcTable`.

## Basic Usage

The most common use case is to pair `useTableSort` with `VcTable`. You handle the `@header-click` event from the table and bind the `sort` prop to the `sortExpression` provided by the composable.

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    :sort="sortExpression"
    @header-click="handleSortChange"
  />
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue';
import { useTableSort, VcTable, type ITableColumns } from '@vc-shell/framework';

// 1. Initialize the composable
const { sortExpression, handleSortChange } = useTableSort({
  initialProperty: 'name',
  initialDirection: 'ASC',
});

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Name', sortable: true },
  { id: 'email', title: 'Email', sortable: true },
  { id: 'role', title: 'Role' }, // Not sortable
]);

const items = ref([/* ... your data ... */]);

// 2. Watch for changes in the sort expression to refetch data
watch(sortExpression, (newSort) => {
  console.log('New sort expression:', newSort);
  // Call your API to fetch sorted data, e.g., api.fetchUsers({ sort: newSort })
});
</script>
```

## API Reference

### Initialization

`useTableSort(options?: UseTableSortOptions)`

#### `UseTableSortOptions`

An optional object to set the initial sorting state.

| Property | Type | Description |
|---|---|---|
| `initialProperty` | `string` | The ID of the column to sort by initially. |
| `initialDirection` | `'ASC' \| 'DESC'` | The initial sort direction. |

### Return Value

The composable returns an object with the following properties:

#### `currentSort`

A writable computed property (`WritableComputedRef<TableSortState>`) representing the current sort state as an object. Primarily for advanced use cases or two-way binding.

```ts
interface TableSortState {
  property: string | null;
  direction: 'ASC' | 'DESC' | null;
}
```

#### `sortExpression`

A `Ref<string | undefined>` that represents the sort state as a string (e.g., `"name:ASC"`). This is what you typically pass to your API and to `VcTable`'s `:sort` prop.

#### `handleSortChange(sortParam: string)`

A function designed to be the event handler for `VcTable`'s `@header-click` event. It takes the column ID (or a full sort expression) and updates the internal sort state. It automatically handles:
- Sorting by a new column (defaults to 'ASC').
- Toggling the direction ('ASC' <=> 'DESC') when clicking the same column.

#### `resetSort()`

A function to reset the sorting state back to the initial options provided during setup, or to `null` if no initial options were given.
