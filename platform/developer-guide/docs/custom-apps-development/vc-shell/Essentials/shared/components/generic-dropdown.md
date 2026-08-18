# GenericDropdown Component

The `GenericDropdown` component (`VcDropdown`) is a flexible shared component used to display a list of items in a floating panel, triggered by a custom element. It's designed for scenarios where a temporary list of options or actions needs to be shown, such as in "show more" buttons or custom selection UIs that don't fit the standard `VcSelect` or `VcInputDropdown` patterns.

It leverages the `@floating-ui/vue` library for positioning and `v-on-click-outside` from `@vueuse/components` for closing the dropdown when clicking outside.

`GenericDropdown` provides a trigger area (via the `trigger` slot) and a dropdown panel that appears when the trigger is activated. The content of the dropdown can be a list of items or custom content.

## Key features

-   Customizable trigger element.
-   Flexible item rendering through slots.
-   Control over open/closed state via `v-model:opened` or `opened` prop.
-   Positioning powered by Floating UI (supports various placements, offset, flip, and shift).
-   Optional teleport to `body` for better stacking context (controlled by `floating` prop).
-   Responsive behavior (mobile-specific classes).
-   Support for empty state.
-   Different visual variants (`default`, `secondary`).

## API reference

### Props

The component uses a generic type `T` for the `items` array.

| Prop           | Type                                 | Default                               | Description                                            |
| :------------- | :------------------------------------| :------------------------------------ | :-------------------------------------------------------|
| `opened`       | `boolean`                            | `true`                                | Controls the visibility of the dropdown. Can be used with `v-model:opened`.  |
| `items`        | `T[]`                                | `[]`                                  | An array of items to display in the dropdown.                                               |
| `emptyText`    | `string`                             | `undefined`                           | Text to display when the `items` array is empty and the `empty` slot is not used.                           |
| `itemText`     | `(item: T) => string`                | `undefined`                           | A function to extract the text to display for an item if the `item` slot is not used.                       |
| `isItemActive` | `(item: T) => boolean`               | `undefined`                           | A function to determine if an item should be styled as active.                                                 |
| `floating`     | `boolean`                            | `false`                               | If `true`, teleports the dropdown to `<body>` and uses absolute positioning. If `false`, renders inline.       |
| `placement`    | `'bottom' \| 'bottom-end' \| 'bottom-start' \| 'top' \| 'top-end' \| 'top-start'` | `'bottom'`    | Preferred placement of the dropdown relative to the trigger, powered by Floating UI.      |
| `variant`      | `'default' \| 'secondary'`           | `'default'`                           | Visual variant of the dropdown, affecting background and item border colors.                                |
| `offset`       | `{ mainAxis?: number; crossAxis?: number }` | `{ mainAxis: 0, crossAxis: 0 }`       | Offset of the dropdown from the trigger element along the main and cross axes.         |
| `maxHeight`    | `number \| string`                   | `300`                                 | Maximum height of the items container. Can be a number (pixels) or a string (e.g., `'50vh'`). The actual CSS is `max-height: v-bind(...)`. |

### Events

| Event             | Payload   | Description                                                                   |
| :---------------- | :-------- | :---------------------------------------------------------------------------- |
| `item-click`      | `item: T` | Emitted when an item in the dropdown is clicked.                                |
| `update:opened`   | `opened: boolean` | Emitted when the `opened` state changes (e.g., by clicking outside). Used for `v-model:opened`. |

### Slots

| Name              | Scope Props                       | Description                                             |
| :---------------- | :---------------------------------| :------------------------------------------------------- |
| `trigger`         | `{ isActive: boolean }`           | Content for the trigger element. `isActive` is true when the dropdown is open.                                                   |
| `items-container` | `{ items: T[], close: () => void }` | Allows providing a custom container for the items. If not used, a default container renders items using the `item` slot or `itemText` prop. `close` function can be called to close the dropdown. |
| `item`            | `{ item: T, click: () => void }` | Custom rendering for an individual item. `click` function can be called to trigger the `item-click` event for that item. If not used, `itemText` prop is used. |
| `empty`           | -                                   | Content to display when the `items` array is empty. If not used, `emptyText` prop is displayed.                                              |

## CSS variables

```scss
:root {
  --dropdown-bg-color: var(--neutrals-50);
  --dropdown-text-color: var(--neutrals-950);
  --dropdown-border-color: var(--app-bar-divider-color); // Note: Seems like a variable from another component context
  --dropdown-hover-bg-color: var(--primary-50);
  --dropdown-divider-color: var(--neutrals-200);        // Used for mobile item borders
  --dropdown-divider-item-color: var(--neutrals-100);    // Default variant item border

  --dropdown-bg-color-light: var(--additional-50);        // Secondary variant background
  --dropdown-divider-item-color-light: var(--neutrals-200); // Secondary variant item border
}
```

The component also uses Tailwind CSS utility classes for its structure and applies dynamic classes like `vc-dropdown__dropdown--mobile`, `vc-dropdown__dropdown--floating`, `vc-dropdown__dropdown--[variant]`, and `vc-dropdown__dropdown--[placement]`.

## Basic usage example

```vue
<template>
  <div>
    <GenericDropdown
      :opened="isDropdownOpen"
      :items="languages"
      :item-text="item => item.name"
      floating
      placement="bottom-end"
      @update:opened="isDropdownOpen = $event"
      @item-click="selectLanguage"
    >
      <template #trigger="{ isActive }">
        <VcButton :variant="isActive ? 'primary' : 'outline'">
          Select Language {{ isActive ? '▲' : '▼' }}
        </VcButton>
      </template>
      <template #item="{ item, click }">
        <div 
          class="tw-p-2 hover:tw-bg-gray-100 tw-cursor-pointer"
          @click="click"
        >
          <span>{{ item.name }} ({{ item.code }})</span>
        </div>
      </template>
      <template #empty>
        <div class="tw-p-4 tw-text-gray-500">No languages available.</div>
      </template>
    </GenericDropdown>

    <p v-if="selectedLanguage" class="tw-mt-4">Selected: {{ selectedLanguage.name }}</p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { GenericDropdown } from '@vc-shell/framework/shared'; // Adjust path as per your project
import { VcButton } from '@vc-shell/framework/ui'; // Adjust path

interface Language {
  code: string;
  name: string;
}

const isDropdownOpen = ref(false);
const languages = ref<Language[]>([
  { code: 'en', name: 'English' },
  { code: 'es', name: 'Español' },
  { code: 'fr', name: 'Français' },
]);
const selectedLanguage = ref<Language | null>(null);

function selectLanguage(lang: Language) {
  selectedLanguage.value = lang;
  isDropdownOpen.value = false; // Manually close after selection
  console.log('Language selected:', lang);
}
</script>
```

## Advanced usage: custom item and trigger

The `GenericDropdown` is often used within other components to provide "more options" functionality.

**Conceptual Example:**

```vue
<template>
  <div class="widget-toolbar">
    <!-- Visible widgets -->
    <MyWidgetComponent v-for="widget in visibleWidgets" :key="widget.id" :widget-data="widget" />

    <GenericDropdown
      v-if="overflowWidgets.length > 0"
      v-model:opened="showOverflow"
      :items="overflowWidgets"
      floating
      placement="bottom-end"
      variant="secondary"
    >
      <template #trigger="{ isActive }">
        <div 
          class="more-button"
          :class="{ 'more-button--active': isActive }"
          @click="showOverflow = !showOverflow"
        >
          <VcIcon icon="material-more_vert" />
        </div>
      </template>

      <template #item="{ item, click }">
        <!-- In the actual example, item is a widget config, and a component is rendered -->
        <div @click="click" class="overflow-widget-item">
          <component 
            :is="item.component" 
            v-bind="item.props || {}"
            class="tw-p-3 tw-w-full"
            horizontal 
          />
        </div>
      </template>
    </GenericDropdown>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { GenericDropdown, VcIcon } from '@vc-shell/framework';
import MyWidgetComponent from './MyWidgetComponent.vue';

interface WidgetConfig {
  id: string;
  component: any; // Vue component
  props?: Record<string, any>;
  // ... other widget properties
}

const showOverflow = ref(false);
const allWidgets = ref<WidgetConfig[]>([
  // ... list of all widget configurations ...
]);

const MAX_VISIBLE_WIDGETS = 3;

const visibleWidgets = computed(() => allWidgets.value.slice(0, MAX_VISIBLE_WIDGETS));
const overflowWidgets = computed(() => allWidgets.value.slice(MAX_VISIBLE_WIDGETS));

// Method to handle item click if needed, e.g., if items are actions
// function handleOverflowWidgetClick(widgetConfig: WidgetConfig) {
//   console.log('Overflow widget clicked:', widgetConfig.id);
//   showOverflow.value = false; 
// }
</script>

<style scoped>
.widget-toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
}
.more-button {
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
  background-color: #f0f0f0;
}
.more-button--active {
  background-color: #e0e0e0;
}
.overflow-widget-item {
  /* Styling for items if they are not full components taking over the slot */
}
</style>
```

## Considerations

-   **Styling**: The component provides basic structure and classes. Custom styling for the trigger and items is often necessary to match the application's design.
-   **Teleporting**: When `floating` is `true`, the dropdown content is teleported to `body`. This is generally good for avoiding z-index issues and clipping, but be aware of CSS scoping if styles rely on parent selectors.
-   **State Management**: The `opened` state can be controlled externally via the `opened` prop and `update:opened` event (useful for `v-model:opened`) or managed internally if only the `trigger` slot is used to toggle.

This component provides a good primitive for building various custom dropdown-like UIs when standard select inputs are not suitable. 
