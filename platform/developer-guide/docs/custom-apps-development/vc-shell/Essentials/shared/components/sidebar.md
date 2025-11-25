# Sidebar Component

The `Sidebar` component provides a flexible and responsive sidebar container for displaying content that can be toggled on and off. It is designed to work well on both mobile and desktop devices with different rendering options.

Sidebars are a common UI pattern used to display supplementary content, navigation options, or temporary user interfaces that can be revealed and hidden as needed. The `Sidebar` component in VC-Shell provides a standardized implementation of this pattern with responsive behavior and positioning options. It utilizes Vue's `<Teleport>` component to move the sidebar to the `<body>` tag on mobile devices (when `$isMobile.value` is true), ensuring it stacks correctly above other content. On desktop views (`$isDesktop.value` is true), the `<Teleport>` is disabled, and the sidebar renders in its original place in the component tree.

## key features

- Responsive design for both mobile and desktop views.
- Left or right positioning.
- Configurable rendering mode:
    - `mobile`: Renders only when `$isMobile.value` is true.
    - `desktop`: Renders only when `$isDesktop.value` is true.
    - `always` (default): Renders on mobile (via Teleport) or desktop, depending on the current device context.
- Optional title with automatic header rendering.
- Backdrop overlay for mobile views that dismisses the sidebar on click.
- Teleport functionality for proper stacking context on mobile devices.
- Built-in close button with customizable visibility.

## API reference

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `'left' \| 'right'` | `'right'` | The position of the sidebar. |
| `render` | `'always' \| 'mobile' \| 'desktop'` | `'always'` | Determines when the sidebar should be rendered. `'always'` means it will render based on device context ($isMobile or $isDesktop). `'mobile'` restricts rendering to mobile only, and `'desktop'` to desktop only. |
| `isExpanded` | `boolean` | Required | Whether the sidebar is currently expanded and visible. |
| `title` | `string` | `undefined` | The title to display in the sidebar header. If provided, a default header with the title and close button (if `closeCross` is true) will be rendered. |
| `closeCross` | `boolean` | `true` | Whether to show the default close button in the header. Relevant only if `title` is provided or the `header` slot is not used. |

### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `close` | - | Emitted when the user clicks the close button or the backdrop overlay |

### Slots

| Name | Props | Description |
|------|------|-------------|
| `header` | `{ header: VNode }` | Custom header content. If this slot is used, it overrides the default header. The `header` prop provides the default VNode for the header (dynamically created using `h()`), which includes the `title` and `closeCross` if applicable. You can choose to render this default header or provide entirely custom markup. |
| `content` | - | The main content of the sidebar. This slot's content is always rendered within the sidebar's content area when `isExpanded` is true. If `isExpanded` is false, this slot's content is passed through (rendered directly in place of the `Sidebar` component without the sidebar chrome). |

## Usage examples

### Basic usage

```vue
<template>
  <div>
    <VcButton @click="toggleSidebar">Toggle Sidebar</VcButton>
    
    <Sidebar
      :is-expanded="sidebarOpen"
      position="right"
      title="Settings"
      @close="sidebarOpen = false"
    >
      <template #content>
        <div class="tw-p-4">
          <h3>Settings Panel</h3>
          <p>Configure your application settings here.</p>
          <!-- Settings content -->
        </div>
      </template>
    </Sidebar>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Sidebar, VcButton } from '@vc-shell/framework';

const sidebarOpen = ref(false);

function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}
</script>
```

### Mobile-only sidebar with custom header

```vue
<template>
  <div>
    <VcButton @click="toggleSidebar">Open Mobile Menu</VcButton>
    
    <Sidebar
      :is-expanded="sidebarOpen"
      position="left"
      render="mobile"
      :close-cross="false"
      @close="sidebarOpen = false"
    >
      <template #header>
        <div class="tw-flex tw-justify-between tw-items-center tw-p-4 tw-border-b tw-border-solid tw-border-gray-200">
          <h2 class="tw-text-xl tw-font-bold">Menu</h2>
          <VcButton icon="material-close" text @click="sidebarOpen = false" />
        </div>
      </template>
      
      <template #content>
        <nav class="tw-p-4">
          <ul>
            <li v-for="item in menuItems" :key="item.id" class="tw-mb-3">
              <a :href="item.url" class="tw-block tw-p-2 tw-hover:bg-gray-100 tw-rounded">
                {{ item.label }}
              </a>
            </li>
          </ul>
        </nav>
      </template>
    </Sidebar>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Sidebar, VcButton } from '@vc-shell/framework';

const sidebarOpen = ref(false);
const menuItems = [
  { id: 1, label: 'Home', url: '/' },
  { id: 2, label: 'Products', url: '/products' },
  { id: 3, label: 'About', url: '/about' },
  { id: 4, label: 'Contact', url: '/contact' }
];

function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}
</script>
```

### Desktop-only sidebar with form

```vue
<template>
  <div>
    <VcButton @click="toggleSidebar">Edit Item</VcButton>
    
    <Sidebar
      :is-expanded="sidebarOpen"
      position="right"
      render="desktop"
      title="Edit Item"
      @close="sidebarOpen = false"
    >
      <template #content>
        <div class="tw-p-4">
          <VcForm @submit.prevent="saveItem">
            <VcInput v-model="item.name" label="Name" class="tw-mb-4" />
            <VcTextarea v-model="item.description" label="Description" class="tw-mb-4" />
            
            <div class="tw-flex tw-justify-end tw-gap-2">
              <VcButton variant="outline" @click="sidebarOpen = false">Cancel</VcButton>
              <VcButton type="submit">Save</VcButton>
            </div>
          </VcForm>
        </div>
      </template>
    </Sidebar>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Sidebar, VcButton, VcForm, VcInput, VcTextarea } from '@vc-shell/framework';

const sidebarOpen = ref(false);
const item = ref({
  name: 'Sample Item',
  description: 'This is a sample item description.'
});

function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}

function saveItem() {
  // Save item logic here
  console.log('Saving item:', item.value);
  sidebarOpen.value = false;
}
</script>
```

### Sidebar with nested content

```vue
<template>
  <div>
    <VcButton @click="toggleSidebar">Open Details</VcButton>
    
    <Sidebar
      :is-expanded="sidebarOpen"
      position="right"
      title="Product Details"
      @close="sidebarOpen = false"
    >
      <template #content>
        <div class="tw-p-4">
          <div class="tw-mb-6">
            <h3 class="tw-text-lg tw-font-medium tw-mb-2">{{ product.name }}</h3>
            <p class="tw-text-gray-600">{{ product.description }}</p>
          </div>
          
          <div class="tw-mb-6">
            <h4 class="tw-font-medium tw-mb-2">Product Information</h4>
            <dl class="tw-grid tw-grid-cols-2 tw-gap-2">
              <dt>SKU</dt>
              <dd>{{ product.sku }}</dd>
              <dt>Price</dt>
              <dd>${{ product.price.toFixed(2) }}</dd>
              <dt>Inventory</dt>
              <dd>{{ product.inventory }} in stock</dd>
            </dl>
          </div>
          
          <div>
            <h4 class="tw-font-medium tw-mb-2">Related Products</h4>
            <ul class="tw-space-y-2">
              <li v-for="item in relatedProducts" :key="item.id" class="tw-p-2 tw-border tw-border-gray-200 tw-rounded">
                {{ item.name }} - ${{ item.price.toFixed(2) }}
              </li>
            </ul>
          </div>
        </div>
      </template>
    </Sidebar>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Sidebar, VcButton } from '@vc-shell/framework';

const sidebarOpen = ref(false);
const product = {
  name: 'Premium Widget',
  sku: 'WDG-1234',
  description: 'A high-quality widget for all your widget needs.',
  price: 29.99,
  inventory: 42
};

const relatedProducts = [
  { id: 1, name: 'Widget Accessory', price: 9.99 },
  { id: 2, name: 'Widget Pro', price: 49.99 },
  { id: 3, name: 'Widget Lite', price: 19.99 }
];

function toggleSidebar() {
  sidebarOpen.value = !sidebarOpen.value;
}
</script>
```

## CSS customization

The `Sidebar` component uses CSS variables for styling, which can be overridden in your application's CSS:

```css
:root {
  --sidebar-bg-color: var(--neutrals-100);
  --sidebar-header-height: 82px; /* Height of the default header */
  --sidebar-header-icon-color: var(--primary-500); /* Color of the close icon in the default header */
  --sidebar-title-color: var(--additional-950); /* Color of the title in the default header */
  --sidebar-header-padding: 18px; /* Padding within the default header */
  --sidebar-dropdown-icon-color: var(--neutrals-500); /* Color for custom icons if placed directly, default close icon uses --sidebar-header-icon-color */
  --sidebar-overlay-color: var(--additional-950); /* Base color for the backdrop overlay (opacity is applied via `tw-bg-black/50`) */
}
```

## Best practices

* **Responsive design**: Use the `render` option to control visibility. `render="mobile"` is ideal for mobile-specific navigation menus. `render="desktop"` can be used for side panels that only make sense on larger screens. `render="always"` (default) provides flexibility, rendering the sidebar appropriately for the current device context.
* **Positioning**: Choose `position="left"` or `position="right"` based on the content's purpose. Left is common for primary navigation, while right is often used for secondary information, filters, or actions.
* **Clear title**: If using the default header (by providing a `title` prop and not using the `header` slot), ensure the title is descriptive.
* **Content overflow**: The `sidebar__content` area is scrollable. Be mindful of the amount of content to ensure a good user experience, especially on smaller screens.
* **State management**: The `isExpanded` prop is crucial. Control this from the parent component, typically with a button that toggles its state. This state should accurately reflect whether the sidebar is intended to be visible.
* **Closing mechanism**: Ensure users can easily close the sidebar. The default close button (`closeCross` prop) and overlay click (on mobile) handle this. If providing a custom header via the `header` slot, make sure to implement a close mechanism and emit the `close` event.
* **Teleport consideration**: Understand that on mobile, the sidebar content is teleported to `<body>`. This can affect scoped CSS if not handled carefully (though generally, global styles or component-specific styles with sufficient specificity should work).

## Related resources

- [VcAppBar Component](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/ui-components/vc-app) - The `VcApp` often contains the `VcAppBar` which might house a button to toggle a `Sidebar`.
- [VcBladeNavigation Component](./blade-navigation.md) - For more complex, stacked panel navigation, `VcBladeNavigation` is preferred over nested sidebars.
- [VcPopup Component](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/ui-components/vc-popup) - For modal dialogs, which are distinct from sidebars. 
