# How-To: Managing Blade Toolbars with `useToolbar`

This guide provides practical examples and best practices for using the `useToolbar` composable to manage toolbar items within your VC-Shell application's blades.

## Introduction

The `useToolbar` composable simplifies the process of adding, removing, and updating toolbar buttons and other UI elements associated with a specific blade (a distinct section or page within the application). It integrates with the `VcBlade` component, which is typically responsible for rendering the toolbar.

There are two primary ways to define toolbar items for a `VcBlade`:

1.  **Declaratively via the `toolbar-items` prop of `VcBlade`**: This is the most common and recommended method for static or moderately dynamic toolbars. You define an array of `IBladeToolbar` (which is compatible with `IToolbarItem`) objects and pass it directly to the `VcBlade` component.
2.  **Programmatically via `useToolbar` composable**: This method is useful for more complex scenarios where toolbar items need to be managed dynamically from within a component's setup logic, or when multiple child components within a blade need to contribute to the same toolbar.

This guide focuses on the **declarative approach using the `toolbar-items` prop**. While `useToolbar` provides methods like `registerToolbarItem`, `unregisterToolbarItem`, etc., these are often used internally by `VcBlade` or for advanced use cases. For most common scenarios, directly providing the `toolbar-items` array to `VcBlade` is sufficient and leverages the underlying capabilities of `useToolbar` indirectly.

Refer to the [`useToolbar` API Reference](../composables/useToolbar.md) for a detailed description of all its methods and the `IToolbarItem` interface.

## 1. Defining Toolbar Items Declaratively for `VcBlade`

The `VcBlade` component accepts a `toolbar-items` prop, which takes an array of objects conforming to the `IBladeToolbar` interface (which is compatible with `IToolbarItem` from `useToolbar.md`).

**Key `IToolbarItem` (and `IBladeToolbar`) Properties:**

*   `id` (string, required): Unique identifier.
*   `title` (string | ComputedRef<string>, required): Display text. Can be reactive.
*   `icon` (string | Component, optional): Material Design icon name, SVG path, or a Vue component.
*   `priority` (number, optional): Order in the toolbar (higher values usually mean further left).
*   `isVisible` (boolean | Ref<boolean> | ComputedRef<boolean>, optional): Controls visibility. Defaults to `true`. Can be reactive.
*   `isDisabled` (boolean | Ref<boolean> | ComputedRef<boolean>, optional): Controls enabled/disabled state. Defaults to `false` (enabled). Can be reactive.
*   `clickHandler` (Function, optional): Function to execute on click.
*   `component` (Component, optional): A custom Vue component to render instead of a standard button.
*   `props` (Record<string, any>, optional): Props for the custom `component`.

### Example 1: Basic Toolbar Items

In this example, a `ref` `bladeToolbar` is defined, holding an array of toolbar item configurations. This `ref` is then passed to the `:toolbar-items` prop of the `VcBlade` component.

```vue
// In your <script setup lang="ts">
import { computed, ref } from 'vue';
import { useI18n } from 'vue-i18n'; // For internationalization
import { type IBladeToolbar } from '@vc-shell/framework'; // Or IToolbarItem if preferred

const { t } = useI18n(); // For translating titles

// Define the toolbar items as a reactive ref
const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: 'refresh',
    title: computed(() => t('OFFERS.PAGES.LIST.TOOLBAR.REFRESH')), // Reactive title
    icon: 'material-refresh',
    async clickHandler() {
      // Logic for refreshing data
      console.log('Refresh clicked');
      // await reload(); // Example action
    },
    isVisible: true, // Static visibility
  },
  {
    id: 'add',
    title: computed(() => t('OFFERS.PAGES.LIST.TOOLBAR.ADD')),
    icon: 'material-add',
    clickHandler() {
      // Logic for adding a new item
      console.log('Add clicked');
      // addOffer(); // Example action
    },
  },
  {
    id: 'deleteSelected',
    title: computed(() => t('OFFERS.PAGES.LIST.TOOLBAR.DELETE')),
    icon: 'material-delete',
    async clickHandler() {
      // Logic for deleting selected items
      console.log('Delete selected clicked');
      // removeOffers(); // Example action
    },
    // Reactive disabled state
    disabled: computed(() => selectedOfferIds.value?.length === 0), 
    // Reactive visibility (e.g., only show on desktop)
    isVisible: computed(() => isDesktop.value), 
  },
]);

// Reactive state that might be used in `disabled` or `isVisible` computed properties
const selectedOfferIds = ref<string[]>([]); 
const isDesktop = ref(true); // Example, replace with actual $isDesktop or similar

// ... rest of your setup ...
</script>

<template>
  <VcBlade
    title="My Blade Title"
    :toolbar-items="bladeToolbar" 
    <!-- other VcBlade props -->
  >
    <!-- Blade content -->
  </VcBlade>
</template>
```

**Explanation:**

*   Each object in the `bladeToolbar` array defines a button.
*   `title` can be a `computed` property, allowing for dynamic, translated, or reactive labels.
*   `clickHandler` defines the action to perform when the button is clicked.
*   `disabled` and `isVisible` can also be `computed` properties, allowing buttons to enable/disable or show/hide based on application state (e.g., `selectedOfferIds.value?.length === 0` or `isDesktop.value`).

### Example 2: More Complex Toolbar with Conditional Visibility

This example demonstrates more complex visibility conditions for toolbar items.

```vue
// In your <script setup lang="ts">
import { computed, ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { type IBladeToolbar } from '@vc-shell/framework';

const { t } = useI18n();

// Example reactive state used in toolbar item definitions
const offerDetails = ref({
  id: 'offer123', // Example property
  prices: [{ listPrice: 10 }], // Example property
  isActive: true, // Example property
});
const isFormValid = ref(true); // Example property
const modified = ref(true); // Example property
const offerLoading = ref(false); // Example property
const param = ref('offer123'); // Example property, simulating if an existing item is being edited

const isDisabledSave = computed(
  () => !(offerDetails.value.prices && offerDetails.value.prices.length && isFormValid.value && modified.value),
);

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: 'save',
    title: computed(() => t('OFFERSCLASSIC.PAGES.DETAILS.TOOLBAR.SAVE')),
    icon: 'material-save',
    async clickHandler() {
      if (isFormValid.value) {
        // Save logic
        console.log('Save clicked');
      } else {
        // Show error
        console.error('Form is not valid');
      }
    },
    isVisible: true,
    disabled: isDisabledSave, // Using a computed ref for disabled state
  },
  {
    id: 'enable',
    title: t('OFFERSCLASSIC.PAGES.DETAILS.TOOLBAR.ENABLE'), // Can be a static string if not translated
    icon: 'material-visibility',
    async clickHandler() {
      if (offerDetails.value.id) {
        offerDetails.value.isActive = true;
        console.log('Enable clicked');
      }
    },
    // Visibility depends on multiple conditions
    isVisible: computed(() => !!param.value && !offerLoading.value && !offerDetails.value.isActive),
  },
  {
    id: 'disable',
    title: t('OFFERSCLASSIC.PAGES.DETAILS.TOOLBAR.DISABLE'),
    icon: 'material-visibility_off',
    async clickHandler() {
      if (offerDetails.value.id) {
        offerDetails.value.isActive = false;
        console.log('Disable clicked');
      }
    },
    isVisible: computed(() => !!param.value && !offerLoading.value && offerDetails.value.isActive),
  },
  {
    id: 'delete',
    title: t('OFFERSCLASSIC.PAGES.DETAILS.TOOLBAR.DELETE'),
    icon: 'material-delete',
    async clickHandler() {
      // Confirmation logic
      // if (await showConfirmation('Are you sure?')) {
      //   // Delete logic
      //   console.log('Delete confirmed');
      // }
    },
    isVisible: computed(() => !!param.value && !offerLoading.value),
  },
]);

// ... rest of your setup ...
</script>

<template>
  <VcBlade
    :title="bladeTitle"
    :toolbar-items="bladeToolbar"
    <!-- other VcBlade props -->
  >
    <!-- Blade content -->
  </VcBlade>
</template>
```

**Explanation:**

*   The `isVisible` property for "enable", "disable", and "delete" buttons uses `computed` properties that depend on various reactive states (`param.value`, `offerLoading.value`, `offerDetails.value.isActive`). This ensures the toolbar adapts to the current context.
*   The "save" button's `disabled` state is also a `computed` property, making it interactive only when certain conditions are met.

## 2. Programmatic Management with `useToolbar()` (Advanced)

While the declarative `toolbar-items` prop is often sufficient, you can use the methods returned by `useToolbar()` directly if you need finer-grained control from your `setup` function or if different child components need to contribute to the same blade's toolbar.

```typescript
import { useToolbar, type IToolbarItem, BladeInstance } from '@vc-shell/framework';
import { ref, computed, onMounted, onUnmounted, inject } from 'vue';

export default {
  setup() {
    const { 
      registerToolbarItem, 
      unregisterToolbarItem, 
      updateToolbarItem 
    } = useToolbar();
    
    // It's crucial to know the current blade's ID. 
    // This might be injected or come from a prop.
    const currentBlade = inject(BladeInstance, { id: 'default-blade-id' }); 
    // Fallback 'default-blade-id' should be replaced with actual logic to get the current blade ID.
    // If VcBlade handles registration via its prop, you might not need to call these directly.

    const buttonTitle = ref('My Dynamic Button');
    const isButtonEnabled = ref(true);

    const dynamicToolbarItem: IToolbarItem = {
      id: 'my-dynamic-item',
      title: computed(() => buttonTitle.value), // Reactive title
      icon: 'material-settings',
      priority: 50,
      isDisabled: computed(() => !isButtonEnabled.value), // Reactive disabled state
      clickHandler: () => {
        console.log('Dynamic item clicked!');
        buttonTitle.value = 'Clicked!';
        isButtonEnabled.value = false;
      }
    };

    onMounted(() => {
      // This assumes VcBlade is not already managing items via :toolbar-items for this specific item.
      // If VcBlade manages items, direct registration might conflict or be redundant.
      // This is more for cases where a child component needs to add to a toolbar
      // that is NOT managed by its direct parent's :toolbar-items prop, or for global toolbars.
      
      // Make sure currentBlade.id is correctly populated
      // registerToolbarItem(dynamicToolbarItem, currentBlade.id); 
      // The useToolbar() composable usually operates on the *currently active blade context* 
      // implicitly if not passed bladeId, or VcBlade itself uses useToolbar internally.
      // For direct usage for a specific blade, ensure the service knows which blade to target.
      // The direct methods on useToolbar() often affect the "current" blade.
      // The `registerToolbarItem` in `useToolbar.md` does not take `bladeId`.
      // It registers to the current blade context.

      registerToolbarItem(dynamicToolbarItem); 
    });

    // Example of updating an item
    function updateButton() {
      updateToolbarItem('my-dynamic-item', { title: 'Updated Title' });
    }

    onUnmounted(() => {
      // Always clean up registered items
      // unregisterToolbarItem('my-dynamic-item', currentBlade.id); 
      // Similar to register, unregister typically works on the current blade context.
      unregisterToolbarItem('my-dynamic-item');
    });

    return { updateButton };
  }
}
</script>
```
**Note on Programmatic Usage:**

The `useToolbar().registerToolbarItem` and related functions typically operate on the "current" or "active" blade context. The `VcBlade` component itself often uses `useToolbar` internally to manage the items passed to its `toolbar-items` prop. Direct programmatic registration is more common for:

*   Widgets or child components deep within a blade that need to add items without passing them all the way up to the `VcBlade`'s `toolbar-items` prop.
*   Scenarios where items are highly dynamic and their lifecycle is tied closely to a specific child component rather than the blade itself.
*   Extending a toolbar managed by `VcBlade` with additional items from a child component.

Ensure you understand the current blade context when using these methods directly to avoid items appearing on the wrong toolbar. In many cases, passing a reactive array to `VcBlade`'s `:toolbar-items` prop is the simpler and more common pattern.

## 3. Pre-registration (Global Toolbar Items)

As mentioned in the `useToolbar` API reference, VC-Shell provides a global `addToolbarItem` function. This is used for registering toolbar items that should be available very early in the application lifecycle, even before the main toolbar service is fully initialized. This is typically for framework-level or core module toolbar items.

```typescript
// In a main plugin or bootstrap file (e.g., main.ts or a specific module's setup)
import { addToolbarItem, type IToolbarItem } from '@vc-shell/framework'; 
import MyCustomToolbarComponent from './MyCustomToolbarComponent.vue';
import { markRaw } from 'vue';

const coreToolbarItem: IToolbarItem = {
  id: 'core-action-xyz',
  title: 'Core Action',
  icon: 'material-star',
  priority: 10,
  clickHandler: () => console.log('Core Action executed')
};

// Example: Pre-registering a toolbar item for a specific blade ID.
// The signature might be addToolbarItem(bladeId: string, item: IToolbarItem)
// or it might register to a global/default context if bladeId is not applicable.
// This depends on the specific implementation of `addToolbarItem` in your VC-Shell version.
// Assuming it can target a blade:
addToolbarItem('my-target-blade-id', coreToolbarItem); 

// Example for a custom component toolbar item
const customCompItem: IToolbarItem = {
  id: 'custom-toolbar-comp',
  component: markRaw(MyCustomToolbarComponent), // markRaw is important for components
  priority: 20,
  props: { initialMode: 'view' }
};
addToolbarItem('my-target-blade-id', customCompItem);
```
Items pre-registered this way are queued and then processed when the toolbar system initializes.

## Conclusion

For most common use cases with `VcBlade`, defining your toolbar items as a reactive array and passing it to the `:toolbar-items` prop is the recommended and most straightforward approach. This leverages the power of `useToolbar` implicitly. Direct use of `useToolbar()` methods like `registerToolbarItem` is available for more advanced or dynamic scenarios. Always refer to the `IToolbarItem` interface for all available configuration options.

