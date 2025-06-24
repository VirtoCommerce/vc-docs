# VcPagination Component

The `VcPagination` component is a navigation component that enables users to browse through multiple pages of content. It provides a simple and intuitive way to navigate between pages with first, previous, next, and last page controls.

## Storybook

[VcPagination Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcpagination--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcpagination--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcPagination
    :pages="totalPages"
    :currentPage="currentPage"
    @itemClick="handlePageChange"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination } from '@vc-shell/framework';

const totalPages = 10;
const currentPage = ref(1);

const handlePageChange = (page: number) => {
  currentPage.value = page;
  // Fetch data for the new page
};
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `pages` | `number` | `1` | Total number of pages |
| `currentPage` | `number` | `1` | Current active page |
| `variant` | `'default' \| 'minimal'` | `'default'` | Visual style variant |
| `expanded` | `boolean` | `false` | Whether to show more page numbers (not used in current implementation) |

## Events

| Event | Payload | Description |
|-------|---------|-------------|
| `itemClick` | `number` | Emitted when a page is selected with the page number as payload |

## CSS Variables

```css
:root {
  --pagination-item-width: 29px;                         /* Width of each pagination button */
  --pagination-item-height: 29px;                        /* Height of each pagination button */
  --pagination-item-color: var(--neutrals-500);          /* Text color for pagination buttons */
  --pagination-item-color-hover: var(--primary-500);     /* Text color for buttons on hover */
  --pagination-item-color-current: var(--additional-50); /* Text color for current page button */
  --pagination-item-color-disabled: var(--neutrals-400); /* Text color for disabled buttons */
  
  --pagination-item-background-color: var(--additional-50);       /* Background color for buttons */
  --pagination-item-background-color-hover: var(--primary-100);   /* Background color for buttons on hover */
  --pagination-item-background-color-current: var(--primary-500); /* Background color for current page button */
  --pagination-item-background-color-disabled: var(--neutrals-100); /* Background color for disabled buttons */
  
  --pagination-item-border-radius: 3px;                  /* Border radius of pagination buttons (Note: actually using rounded-full in component) */
  --pagination-item-border-color: var(--secondary-100);  /* Border color for pagination buttons */
  --pagination-item-border-color-hover: var(--neutrals-200);     /* Border color for buttons on hover */
  --pagination-item-border-color-current: var(--neutrals-200);   /* Border color for current page button */
  --pagination-item-border-color-disabled: var(--neutrals-200);  /* Border color for disabled buttons */
}
```

## Examples

### Basic Pagination

```vue
<template>
  <VcPagination
    :pages="5"
    :currentPage="currentPage"
    @itemClick="handlePageChange"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination } from '@vc-shell/framework';

const currentPage = ref(1);

const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
```

### Pagination with Many Pages

```vue
<template>
  <VcPagination
    :pages="20"
    :currentPage="currentPage"
    @itemClick="handlePageChange"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination } from '@vc-shell/framework';

const currentPage = ref(7);

const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
```

### Pagination with Page Indicator

```vue
<template>
  <div>
    <div class="tw-mb-2">
      Current Page: {{ currentPage }} of {{ totalPages }}
    </div>
    <VcPagination
      :pages="totalPages"
      :currentPage="currentPage"
      @itemClick="handlePageChange"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination } from '@vc-shell/framework';

const totalPages = 15;
const currentPage = ref(5);

const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
```

### Integration with Table

```vue
<template>
  <div>
    <VcTable :items="currentItems" :columns="columns" />
    
    <div class="tw-mt-4 tw-flex tw-justify-between tw-items-center">
      <div class="tw-text-sm tw-text-[var(--neutrals-500)]">
        Showing {{ (currentPage - 1) * itemsPerPage + 1 }} to 
        {{ Math.min(currentPage * itemsPerPage, items.length) }} of 
        {{ items.length }} items
      </div>
      
      <VcPagination
        :pages="totalPages"
        :currentPage="currentPage"
        @itemClick="handlePageChange"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcPagination, VcTable } from '@vc-shell/framework';

const items = [
  // Imagine a list of 100 items here
  // ...
];

const columns = [
  { key: 'id', title: 'ID' },
  { key: 'name', title: 'Name' },
  { key: 'description', title: 'Description' }
];

const currentPage = ref(1);
const itemsPerPage = 10;

const totalPages = computed(() => Math.ceil(items.length / itemsPerPage));

const currentItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return items.slice(start, end);
});

const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
```

### Mobile-Responsive Pagination

The `VcPagination` component is automatically responsive and will adjust the number of visible page buttons based on the device:

- On desktop: Shows 5 page buttons
- On mobile: Shows 3 page buttons

This behavior is handled automatically by the component using the `isMobile` injection.

```vue
<template>
  <div>
    <h3>Try resizing your browser window to see responsive behavior</h3>
    <VcPagination
      :pages="12"
      :currentPage="currentPage"
      @itemClick="handlePageChange"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination } from '@vc-shell/framework';

const currentPage = ref(5);

const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
```

### With Loading State

```vue
<template>
  <div>
    <div v-if="loading" class="tw-text-center tw-py-4">
      <VcLoading />
    </div>
    <div v-else>
      <VcTable :items="items" :columns="columns" />
      
      <div class="tw-mt-4 tw-flex tw-justify-end">
        <VcPagination
          :pages="totalPages"
          :currentPage="currentPage"
          @itemClick="fetchPage"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPagination, VcTable, VcLoading } from '@vc-shell/framework';

const items = ref([]);
const loading = ref(false);
const currentPage = ref(1);
const totalPages = ref(10);
const columns = [
  { key: 'id', title: 'ID' },
  { key: 'name', title: 'Name' }
];

// Simulated API call
const fetchPage = async (page: number) => {
  loading.value = true;
  currentPage.value = page;
  
  try {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // Simulate data
    items.value = Array.from({ length: 10 }, (_, i) => ({
      id: (page - 1) * 10 + i + 1,
      name: `Item ${(page - 1) * 10 + i + 1}`
    }));
  } finally {
    loading.value = false;
  }
};

// Initial data fetch
fetchPage(1);
</script>
```
