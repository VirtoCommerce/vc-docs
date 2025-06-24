# VcTable

VcTable is a highly customizable data table component that provides comprehensive functionality for displaying, sorting, filtering, and interacting with tabular data. It supports various features like multi-select, sorting, pagination, responsive design for both desktop and mobile views, column reordering, and custom action buttons.

## Basic Usage

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    state-key="my-table"
    :sort="sort"
    @header-click="onHeaderClick"
    @item-click="onItemClick"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTable, ITableColumns } from '@vc-shell/framework';

const columns = ref<ITableColumns[]>([
  {
    id: 'name',
    title: 'Name',
    sortable: true,
    alwaysVisible: true
  },
  {
    id: 'sku',
    title: 'SKU',
    sortable: true,
    width: 120
  },
  {
    id: 'createdDate',
    title: 'Created Date',
    sortable: true,
    type: 'date-ago'
  }
]);

const items = ref([
  { id: '1', name: 'Product 1', sku: 'SKU001', createdDate: new Date('2023-01-15') },
  { id: '2', name: 'Product 2', sku: 'SKU002', createdDate: new Date('2023-02-20') },
  { id: '3', name: 'Product 3', sku: 'SKU003', createdDate: new Date('2023-03-25') }
]);

const sort = ref('name:ASC');

function onHeaderClick(column: ITableColumns) {
  // Handle header click for sorting
  if (column.sortable) {
    const field = column.id;
    const currentSort = sort.value.split(':');
    
    if (currentSort[0] === field) {
      sort.value = currentSort[1] === 'ASC' ? `${field}:DESC` : `${field}:ASC`;
    } else {
      sort.value = `${field}:ASC`;
    }
  }
}

function onItemClick(item) {
  // Handle item click
  console.log('Item clicked:', item);
}
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `columns` | `ITableColumns[]` | `[]` | Array of column definitions for the table |
| `items` | `T[]` | `[]` | Array of data items to display in the table |
| `sort` | `string` | - | Sort expression in format 'fieldName:direction' (e.g., 'name:ASC') |
| `multiselect` | `boolean` | `false` | Enables row selection with checkboxes |
| `disableItemCheckbox` | `(item: T) => boolean` | - | Function to determine if a specific row's checkbox should be disabled |
| `expanded` | `boolean` | `true` | Controls whether the table is in expanded view |
| `totalLabel` | `string` | - | Label to display for total count in footer |
| `totalCount` | `number` | `0` | Total count of items (used for pagination) |
| `pages` | `number` | `0` | Total number of pages |
| `currentPage` | `number` | `0` | Current active page |
| `searchPlaceholder` | `string` | - | Placeholder text for the search input |
| `searchValue` | `string` | - | Current search value |
| `loading` | `MaybeRef<boolean>` | - | Controls loading state of the table |
| `empty` | `StatusImage` | - | Configuration for empty state view |
| `notfound` | `StatusImage` | - | Configuration for not found state view |
| `header` | `boolean` | `true` | Controls visibility of the table header |
| `footer` | `boolean` | `true` | Controls visibility of the table footer |
| `activeFilterCount` | `number` | `0` | Number of active filters |
| `selectedItemId` | `MaybeRef<string>` | - | ID of the currently selected item |
| `pullToReload` | `boolean` | - | Enables pull-to-reload functionality on mobile |
| `resizableColumns` | `boolean` | `true` | Enables column resizing |
| `reorderableColumns` | `boolean` | `true` | Enables column reordering |
| `reorderableRows` | `boolean` | `false` | Enables row reordering |
| `stateKey` | `string` | - | Key for persisting table state (column order, visibility, width) |
| `selectAll` | `boolean` | - | Enables select all functionality |
| `enableItemActions` | `boolean` | - | Enables row action buttons |
| `editing` | `boolean` | - | Enables in-line editing mode |
| `addNewRowButton` | `{ show: boolean; title: string }` | - | Configuration for add new row button |
| `paginationVariant` | `ComponentProps<typeof VcPagination>["variant"]` | `'default'` | Variant of pagination to use |
| `selectionItems` | `T[]` | - | Pre-selected items |
| `disableFilter` | `boolean` | - | Disables filtering functionality |
| `columnSelector` | `"auto" \| "defined" \| MaybeRef<ITableColumns[]> \| (() => ITableColumns[])` | `'auto'` | Controls column selection behavior |
| `noHeaderCheckbox` | `boolean` | - | Hides header checkbox in multiselect mode |
| `itemActionBuilder` | `(item: T) => IActionBuilderResult<T>[] \| undefined` | - | Function to build action buttons for each row |

## Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `paginationClick` | `page: number` | Emitted when a pagination link is clicked |
| `selectionChanged` | `values: T[]` | Emitted when selected items change |
| `search:change` | `value: string \| undefined` | Emitted when search input changes |
| `headerClick` | `item: ITableColumns` | Emitted when a column header is clicked |
| `itemClick` | `item: T` | Emitted when a row is clicked |
| `scroll:ptr` | - | Emitted on pull-to-refresh action |
| `row:reorder` | `{ dragIndex: number; dropIndex: number; value: T[] }` | Emitted when a row is reordered |
| `select:all` | `values: boolean` | Emitted when select all is toggled |
| `onEditComplete` | `{ event: { field: string; value: string \| number }; index: number }` | Emitted when in-line edit is completed |
| `onAddNewRow` | - | Emitted when add new row button is clicked |
| `onCellBlur` | `{ row: number \| undefined; field: string }` | Emitted when a cell loses focus in edit mode |

## Slots

| Slot Name | Props | Description |
|-----------|-------|-------------|
| `header` | `{ header: VNode }` | Custom header content |
| `filters` | `{ closePanel: () => void }` | Custom filters panel content |
| `mobile-item` | `{ item: T }` | Custom template for mobile item view |
| `item_{fieldName}` | `{ item: T; cell: ITableColumns \| TableColPartial; index: number }` | Custom cell content for specific column |
| `notfound` | - | Custom content for not found state |
| `empty` | - | Custom content for empty state |
| `footer` | - | Custom footer content |

## Column Configuration

The `columns` prop accepts an array of `ITableColumns` objects with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | `string` | Unique identifier for the column, typically matches a property name in your data items |
| `title` | `string \| Ref<string>` | Display title for the column |
| `field` | `string` | Optional field path if different from id |
| `width` | `number` | Width of the column in pixels |
| `sortable` | `boolean` | Whether the column is sortable |
| `alwaysVisible` | `boolean` | Whether the column is always visible even in collapsed mode |
| `visible` | `boolean` | Controls initial visibility of the column |
| `required` | `boolean` | Indicates if the column is required (shows an indicator) |
| `type` | `string` | Predefined cell type ('date', 'date-ago', 'money', 'number', 'status-icon', 'image', etc.) |

## Status Images

The `empty` and `notfound` props accept a `StatusImage` object with the following properties:

```ts
interface StatusImage {
  image?: string;       // URL to image
  text: string | Ref<string>; // Display text
  action?: string;      // Action button text
  clickHandler?: () => void; // Click handler for action button
}
```

## CSS Variables

The table component uses CSS variables for theming, which can be customized:

```css
:root {
  /* Main table variables */
  --table-border-color: var(--neutrals-200);            /* Table border color */
  --table-select-all-border-color: var(--neutrals-200); /* Border color for select all bar */
  --table-header-bg: var(--primary-50);                 /* Header background color */
  --table-header-border-color: var(--neutrals-200);     /* Header border color */
  --table-header-border:
    inset 0px 1px 0px var(--table-header-border-color),
    inset 0px -1px 0px var(--table-header-border-color); /* Header border style */
  --table-header-text-color: var(--secondary-950);      /* Header text color */
  --table-resizer-color: var(--neutrals-200);           /* Color for column resizer */
  --table-reorder-color: var(--primary-400);            /* Color for reorder indicator */
  --table-select-all-bg: var(--primary-100);            /* Background for select all section */
  
  /* Row styling */
  --table-row-bg-hover: var(--primary-100);             /* Background color for row hover */
  --table-row-bg-odd: var(--additional-50);             /* Background color for odd rows */
  --table-row-bg-even: var(--neutrals-50);              /* Background color for even rows */
  --table-row-hover: var(--primary-100);                /* Background color for row hover */
  --table-row-bg-selected: var(--primary-100);          /* Background color for selected rows */
  
  /* Actions styling */
  --table-actions-bg: var(--primary-100);               /* Background color for action buttons */
  --table-actions-bg-hover: var(--primary-100);         /* Background color for action buttons on hover */
  --table-actions-bg-hover-selected-item: var(--primary-100); /* Background for action buttons on selected row hover */
  --table-actions-text-color: var(--neutrals-600);      /* Text color for actions */
  --table-actions-tooltip-text: var(--neutrals-600);    /* Tooltip text color */
  --table-actions-icon-color: var(--primary-500);       /* Icon color for actions */
  --table-actions-icon-color-hover: var(--primary-600); /* Icon color for actions on hover */
  --table-actions-color-danger: var(--danger-500);      /* Color for danger actions */
  --table-actions-color-success: var(--success-500);    /* Color for success actions */
  
  /* Footer and other components */
  --table-footer-bg: var(--neutrals-50);                /* Footer background color */
  --table-footer-border-color: var(--neutrals-200);     /* Footer border color */
  --table-row-drag-color: var(--primary-400);           /* Color for row drag indicator */
  --table-row-drag-shadow: inset 0 -2px 0 0 var(--table-row-drag-color); /* Shadow for dragged row */
  --table-mobile-border-color: var(--secondary-200);    /* Border color for mobile items */
  --table-text-color: var(--neutrals-950);              /* Text color for table cells */
  --table-sort-icon-color: var(--neutrals-400);         /* Color for sort icons */
  
  /* Cell specific variables */
  --table-cell-error-color: var(--danger-500);          /* Color for cell error state */
  --table-cell-text-color: var(--neutrals-400);         /* Secondary text color in cells */
  --table-cell-text-base-color: var(--additional-950);  /* Primary text color in cells */
  
  /* Filter component variables */
  --table-filter-counter-bg: var(--additional-50);      /* Background for filter counter */
  --table-filter-counter-text-color: var(--info-500);   /* Text color for filter counter */
  --table-filter-mobile-panel-overlay: var(--neutral-500); /* Overlay color for mobile filter panel */
  --table-filter-desktop-shadow-color: var(--additional-950); /* Shadow color for desktop filter panel */
  --table-filter-desktop-shadow: 1px 1px 11px rgb(from var(--table-filter-desktop-shadow-color) r g b / 7%); /* Shadow for filter panel */
  --table-filter-panel-bg: var(--additional-50);        /* Background color for filter panel */
  --table-filter-close-icon-color: var(--neutrals-500); /* Color for filter close icon */
  --table-filter-panel-border-color: var(--neutrals-200); /* Border color for filter panel */
  --table-filter-panel-header-title-color: var(--neutrals-600); /* Title color for filter panel */
  
  /* Counter component variables */
  --table-counter-label-color: var(--secondary-950);    /* Label color for counter in footer */
  --table-counter-value-color: var(--primary-500);      /* Value color for counter in footer */
  --table-counter-value-border-color: var(--neutrals-500); /* Border color for counter in footer */
  
  /* Base header variables */
  --table-base-header-border-color: var(--neutrals-200); /* Border color for base header */
  --table-base-header-input-icon-color: var(--neutrals-400); /* Icon color for search input */
  
  /* Mobile view variables */
  --table-mobile-background-color: var(--additional-50); /* Background color for mobile items */
  --table-mobile-action-bg: var(--secondary-400);       /* Background color for mobile actions */
  --table-mobile-action-text-color: var(--additional-50); /* Text color for mobile actions */
  --table-mobile-action-popup-overlay: var(--neutrals-100); /* Overlay color for mobile actions popup */
  --table-mobile-action-popup-bg: var(--additional-50); /* Background color for mobile actions popup */
  --table-mobile-action-popup-shadow-color: var(--secondary-200); /* Shadow color for mobile popup */
  --table-mobile-action-popup-shadow: 1px 1px 22px var(--table-mobile-action-popup-shadow-color); /* Shadow for mobile popup */
  --table-mobile-action-popup-border-color: var(--neutrals-200); /* Border color for mobile popup */
  --table-mobile-action-popup-title-color: var(--neutrals-700); /* Title color for mobile popup */
  --table-mobile-action-popup-icon-color: var(--secondary-600); /* Icon color for mobile popup */
  --table-mobile-action-popup-action-text-color: var(--primary-500); /* Action text color for mobile popup */
  --table-mobile-action-success: var(--success-400);    /* Success action color for mobile */
  --table-mobile-action-danger: var(--danger-500);      /* Danger action color for mobile */
  --table-mobile-action-selected: var(--primary-100);   /* Selected item color for mobile */
  --table-mobile-action-more: var(--neutrals-400);      /* More actions color for mobile */
  
  /* Column switcher variables */
  --table-column-switcher-dropdown-bg: var(--additional-50); /* Background for column switcher dropdown */
  --table-column-switcher-dropdown-border: var(--neutrals-200); /* Border for column switcher dropdown */
  --table-column-switcher-dropdown-item-hover: var(--primary-50); /* Hover color for dropdown items */
  --table-column-switcher-text-color: var(--neutrals-950); /* Text color for column switcher */
  
  /* Add new row button variables */
  --table-add-new-icon-color: var(--primary-400);       /* Icon color for add new row button */
}
```

## Mobile Support

VcTable provides a responsive design that adapts to mobile screens. You can customize the mobile view using the `mobile-item` slot to provide a card-like experience instead of the tabular view.

```vue
<template>
  <VcTable :items="items" :columns="columns">
    <template #mobile-item="{ item }">
      <div class="tw-p-4">
        <div class="tw-font-bold">{{ item.name }}</div>
        <div class="tw-text-sm tw-text-gray-600">SKU: {{ item.sku }}</div>
        <div class="tw-mt-2">Created: {{ new Date(item.createdDate).toLocaleDateString() }}</div>
      </div>
    </template>
  </VcTable>
</template>
```

## Customizing Cell Content

You can customize the content of specific columns using the `item_{columnId}` slot.

```vue
<template>
  <VcTable :items="items" :columns="columns">
    <!-- Custom render for the "status" column -->
    <template #item_status="{ item }">
      <VcBadge :variant="item.isActive ? 'success' : 'danger'">
        {{ item.isActive ? 'Active' : 'Inactive' }}
      </VcBadge>
    </template>
    
    <!-- Custom render for the "actions" column -->
    <template #item_actions="{ item }">
      <div class="tw-flex tw-gap-2">
        <VcButton
          variant="icon"
          icon="material-edit"
          @click.stop="editItem(item)"
        />
        <VcButton
          variant="icon"
          icon="material-delete"
          @click.stop="deleteItem(item)"
        />
      </div>
    </template>
  </VcTable>
</template>
```

## Column Selection and State Persistence

VcTable provides built-in column selection and state persistence functionality. The `columnSelector` prop controls how columns are defined and the `stateKey` prop enables state persistence.

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    column-selector="defined"
    state-key="products_table"
  />
</template>
```

The `columnSelector` prop can have the following values:
- `"auto"`: Automatically determine columns from data items
- `"defined"`: Use only the columns defined in the `columns` prop
- A custom function or ref: Use a custom function or ref to get columns

## Row Actions (Contextual)

You can add contextual action buttons to each row by using two props:
- `enable-item-actions`: A boolean prop that must be set to `true` to show the actions column.
- `item-action-builder`: A function that receives the data for a single row (`item`) and must return an array of action objects.

This allows you to dynamically generate actions based on the state of each item. For instance, you can show an "Activate" button for a disabled item and a "Deactivate" button for an enabled one.

### Example with Contextual Actions

This example shows how to build a different set of actions for items based on their `isActive` status.

```vue
<template>
  <VcTable
    :columns="columns"
    :items="products"
    :item-action-builder="itemActionBuilder"
    enable-item-actions
    state-key="products-table-with-actions"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTable, IActionBuilderResult, type ITableColumns } from '@vc-shell/framework';

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Product Name' },
  { id: 'status', title: 'Status' }
]);

const products = ref([
  { id: '1', name: 'Product A', isActive: true },
  { id: '2', name: 'Product B', isActive: false },
  { id: '3', name: 'Product C', isActive: true },
]);

/**
 * This function is called for each row to generate its actions.
 * @param item - The data item for the current row.
 * @returns An array of action definitions for the row.
 */
function itemActionBuilder(item: { id: string, name: string, isActive: boolean }): IActionBuilderResult[] {
  const actions: IActionBuilderResult[] = [];

  // Always show the edit action
  actions.push({
    title: 'Edit',
    icon: 'material-edit',
    clickHandler: () => editProduct(item),
  });

  // Conditionally show an "Activate" or "Deactivate" action
  if (item.isActive) {
    actions.push({
      title: 'Deactivate',
      icon: 'material-pause_circle_outline',
      clickHandler: () => toggleProductStatus(item.id),
    });
  } else {
    actions.push({
      title: 'Activate',
      icon: 'material-play_circle_outline',
      type: 'success', // Optional: use 'success' or 'danger' for color
      clickHandler: () => toggleProductStatus(item.id),
    });
  }

  // Always show the delete action at the end
  actions.push({
    title: 'Delete',
    icon: 'material-delete',
    type: 'danger',
    clickHandler: () => deleteProduct(item.id),
  });
  
  return actions;
}

function editProduct(product) {
  // Logic to open an edit blade or navigate to an edit page
  console.log('Editing product:', product);
}

function deleteProduct(productId) {
  // Logic for API call and confirmation dialog
  console.log('Deleting product with ID:', productId);
  products.value = products.value.filter(p => p.id !== productId);
}

function toggleProductStatus(productId) {
  // Logic to call API and update status
  const product = products.value.find(p => p.id === productId);
  if(product) {
    product.isActive = !product.isActive;
    console.log(`Product ${productId} status changed to: ${product.isActive}`);
  }
}
</script>
```

## Examples

### Basic Table with Sorting

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    :sort="sort"
    state-key="basic-table"
    @header-click="onHeaderClick"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTable, ITableColumns } from '@vc-shell/framework';

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Name', sortable: true },
  { id: 'email', title: 'Email', sortable: true },
  { id: 'role', title: 'Role', sortable: true },
  { id: 'status', title: 'Status', sortable: true }
]);

const items = ref([
  { id: '1', name: 'John Doe', email: 'john@example.com', role: 'Admin', status: 'Active' },
  { id: '2', name: 'Jane Smith', email: 'jane@example.com', role: 'Editor', status: 'Active' },
  { id: '3', name: 'Bob Johnson', email: 'bob@example.com', role: 'Viewer', status: 'Inactive' }
]);

const sort = ref('name:ASC');

function onHeaderClick(column: ITableColumns) {
  if (column.sortable) {
    const field = column.id;
    const currentSort = sort.value.split(':');
    
    if (currentSort[0] === field) {
      sort.value = currentSort[1] === 'ASC' ? `${field}:DESC` : `${field}:ASC`;
    } else {
      sort.value = `${field}:ASC`;
    }
  }
}
</script>
```

### Table with Multi-Select and Actions

```vue
<template>
  <VcTable
    :columns="columns"
    :items="products"
    multiselect
    select-all
    :item-action-builder="actionBuilder"
    enable-item-actions
    state-key="products-table"
    @selection-changed="onSelectionChanged"
  >
    <template #item_status="{ item }">
      <VcBadge :variant="item.isActive ? 'success' : 'danger'">
        {{ item.isActive ? 'Active' : 'Inactive' }}
      </VcBadge>
    </template>
  </VcTable>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTable, VcBadge, ITableColumns, IActionBuilderResult } from '@vc-shell/framework';

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Product Name', sortable: true, alwaysVisible: true },
  { id: 'sku', title: 'SKU', sortable: true, width: 120 },
  { id: 'price', title: 'Price', sortable: true, width: 100, type: 'money' },
  { id: 'status', title: 'Status', sortable: true, width: 120 }
]);

const products = ref([
  { id: '1', name: 'Product A', sku: 'SKU001', price: 29.99, isActive: true },
  { id: '2', name: 'Product B', sku: 'SKU002', price: 49.99, isActive: true },
  { id: '3', name: 'Product C', sku: 'SKU003', price: 19.99, isActive: false }
]);

const selectedProducts = ref([]);

function actionBuilder(item) {
  return [
    {
      title: 'Edit',
      icon: 'material-edit',
      clickHandler: () => editProduct(item)
    },
    {
      title: 'Delete',
      icon: 'material-delete',
      type: 'danger',
      clickHandler: () => deleteProduct(item)
    }
  ];
}

function onSelectionChanged(items) {
  selectedProducts.value = items;
}

function editProduct(product) {
  // Edit logic
}

function deleteProduct(product) {
  // Delete logic
}
</script>
```

### Table with Pagination and Search

```vue
<template>
  <VcTable
    :columns="columns"
    :items="displayItems"
    :search-value="searchValue"
    :search-placeholder="'Search users...'"
    :pages="pages"
    :current-page="currentPage"
    :total-count="totalCount"
    state-key="users-table"
    @search:change="onSearchChange"
    @pagination-click="onPaginationClick"
  />
</template>

<script lang="ts" setup>
import { ref, computed, watch } from 'vue';
import { VcTable, ITableColumns } from '@vc-shell/framework';

const columns = ref<ITableColumns[]>([
  { id: 'name', title: 'Name', sortable: true },
  { id: 'email', title: 'Email', sortable: true },
  { id: 'role', title: 'Role', sortable: true }
]);

const allUsers = ref([
  /* large array of users */
]);

const searchValue = ref('');
const currentPage = ref(1);
const itemsPerPage = 10;

// Filtered items based on search
const filteredItems = computed(() => {
  if (!searchValue.value) return allUsers.value;
  
  return allUsers.value.filter(user => 
    user.name.toLowerCase().includes(searchValue.value.toLowerCase()) ||
    user.email.toLowerCase().includes(searchValue.value.toLowerCase())
  );
});

// Total count and pages
const totalCount = computed(() => filteredItems.value.length);
const pages = computed(() => Math.ceil(totalCount.value / itemsPerPage));

// Current page items
const displayItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return filteredItems.value.slice(start, end);
});

function onSearchChange(value) {
  searchValue.value = value;
  currentPage.value = 1; // Reset to first page on search
}

function onPaginationClick(page) {
  currentPage.value = page;
}

// Reset pagination when filtered items change
watch(filteredItems, () => {
  if (currentPage.value > pages.value) {
    currentPage.value = Math.max(1, pages.value);
  }
});
</script>
```

## Table with Filtering

VcTable provides a dedicated `#filters` slot to build custom filtering UI. The filter button and panel are automatically managed by the table. You only need to provide the content for the filter panel.

The slot gives you access to a `closePanel` function, which you should call after applying or resetting filters to hide the panel. Use the `active-filter-count` prop to show an indicator on the filter button when filters are active.

A common pattern is to use a `stagedFilters` object to track changes in the filter UI, and a `query` object to hold the filters that are actually sent to the server. Applying filters copies the staged values to the query and triggers a data refetch.

### Example with Server-Side Filtering

This example demonstrates how to implement filtering that triggers a new data request to a server.

```vue
<template>
  <VcTable
    :columns="columns"
    :items="items"
    :loading="isLoading"
    :active-filter-count="activeFilterCount"
    state-key="users-table-with-filters"
  >
    <template #filters="{ closePanel }">
      <div class="tw-p-4">
        <h3 class="tw-font-semibold tw-mb-4">Filter by Role</h3>
        <div class="tw-flex tw-flex-col tw-gap-2">
          <VcCheckbox v-for="role in allRoles" :key="role" v-model="stagedFilters.roles" :value="role">
            {{ role }}
          </VcCheckbox>
        </div>

        <div class="tw-flex tw-gap-2 tw-mt-6">
          <VcButton @click="applyFilters(closePanel)">Apply</VcButton>
          <VcButton variant="secondary" @click="resetFilters(closePanel)">
            Reset
          </VcButton>
        </div>
      </div>
    </template>
  </VcTable>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted } from "vue";
import { VcTable, VcCheckbox, VcButton, type ITableColumns } from "@vc-shell/framework";

// --- Mock API ---
// This would typically be a call to an API client (e.g., using useApiClient).
// For demonstration, we simulate it with a local function.
const FAKE_DB = [
  { id: "1", name: "John Doe", email: "john@example.com", role: "Admin" },
  { id: "2", name: "Jane Smith", email: "jane@example.com", role: "Editor" },
  { id: "3", name: "Bob Johnson", email: "bob@example.com", role: "Viewer" },
  { id: "4", name: "Alice Williams", email: "alice@example.com", role: "Editor" },
  { id: "5", name: "Charlie Brown", email: "charlie@example.com", role: "Admin" },
];

async function fetchUsers(query: { roles?: string[] }) {
  console.log("Fetching users with query:", query);
  if (!query.roles || query.roles.length === 0) {
    return { results: FAKE_DB, totalCount: FAKE_DB.length };
  }
  const filtered = FAKE_DB.filter((user) => query.roles?.includes(user.role));
  return { results: filtered, totalCount: filtered.length };
}
// --- End Mock API ---

const columns = ref<ITableColumns[]>([
  { id: "name", title: "Name", sortable: true },
  { id: "email", title: "Email", sortable: true },
  { id: "role", title: "Role", sortable: true },
]);

const items = ref<any[]>([]);
const isLoading = ref(true);
const allRoles = ["Admin", "Editor", "Viewer"];

// Staged filters are bound to the UI controls in the filter panel.
const stagedFilters = ref({
  roles: [] as string[],
});

// The query object contains the currently applied filters for the API request.
const query = ref({
  roles: [] as string[],
});

const activeFilterCount = computed(() => {
  return query.value.roles.length > 0 ? 1 : 0;
});

async function loadItems() {
  isLoading.value = true;
  try {
    const response = await fetchUsers(query.value);
    items.value = response.results;
    // In a real app, you would also update pagination state here.
  } catch (e) {
    console.error("Failed to load items", e);
    items.value = []; // Clear items on error
  } finally {
    isLoading.value = false;
  }
}

function applyFilters(closePanel: () => void) {
  // 1. Copy staged filters to the main query object.
  query.value.roles = [...stagedFilters.value.roles];
  // 2. Trigger a data reload with the new query.
  loadItems();
  // 3. Close the filter panel.
  closePanel();
}

function resetFilters(closePanel: () => void) {
  // 1. Clear both staged and active query filters.
  stagedFilters.value.roles = [];
  query.value.roles = [];
  // 2. Trigger a data reload.
  loadItems();
  // 3. Close the filter panel.
  closePanel();
}

// Load initial data when the component mounts.
onMounted(() => {
  loadItems();
});
</script>
``` 
