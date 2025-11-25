# Understanding Blade Anatomy in VC-Shell

Blades are fundamental UI panels in VC-Shell applications, used to display content, forms, lists, and details related to specific tasks or entities. Understanding their structure is key to building consistent and user-friendly interfaces.

The primary UI component responsible for the common structure of a blade (like its header, toolbar area, and content slot) is the **`VcBlade` UI component**. Your custom Vue components, which represent the specific content and logic of a blade (e.g., `ProductDetailsPage.vue`), are typically placed *inside* this `VcBlade` wrapper. This guide focuses on the anatomy provided by the `VcBlade` component and how it structures your custom content.

## Core Structural Elements Provided by `VcBlade`

A `VcBlade` component typically provides the following sections to frame your custom blade content:

### 1. Blade Header

*   **Description:** The top section of the blade, usually containing the title and an optional icon. It clearly identifies the purpose of the blade. This header is part of the `VcBlade` component.
*   **Key `VcBlade` Props:** `title`, `subtitle`, `icon`.

![Blade Layout](/platform/developer-guide/latest/custom-apps-development/media/blade-layout.png)

### 2. Blade Toolbar

*   **Description:** Located typically below the header, the toolbar contains action buttons and controls relevant to the blade's content. This toolbar is also managed by the `VcBlade` component.
*   **Key `VcBlade` Prop:** `toolbarItems`. Toolbars can also be dynamically managed using `useToolbar` in conjunction with `VcBlade`.

![Blade Layout](/platform/developer-guide/latest/custom-apps-development/media/blade-layout1.png)

*   **Further Reading:** [Managing Blade Toolbars with useToolbar](./managing-blade-toolbars-with-usetoolbar.md)

### 3. Blade Content Area

*   **Description:** The main body of the blade where your custom Vue component (e.g., your `ProductDetailsPage.vue`) is rendered. `VcBlade` provides a default slot for this purpose.

![Blade Layout](/platform/developer-guide/latest/custom-apps-development/media/blade-layout2.png)

### 4. Blade Widgets Area

*   **Description:** Blades can display contextual widgets, which are typically small, self-contained Vue components offering supplementary information or actions. These widgets are not directly defined via a prop on `VcBlade`. Instead, they are programmatically registered for a specific blade instance using the `useWidgets` composable. The `VcBlade` component includes a designated area where these registered widgets are displayed.
*   **Key Management Composable:** `useWidgets`.

![Blade Layout](/platform/developer-guide/latest/custom-apps-development/media/blade-layout3.png)

*   **Further Reading:** [Creating and Registering Blade Widgets with `useWidgets`](./creating-and-registering-widgets-with-usewidgets.md)

## Properties of the `VcBlade` UI Component

The `VcBlade` UI component accepts several important props to control its appearance and behavior as a container for your custom blade content:

*   `title?: string`: The text displayed in the `VcBlade`'s header.
*   `subtitle?: string`: An optional subtitle displayed in the `VcBlade`'s header.
*   `icon?: string`: An icon to display in the `VcBlade`'s header.
*   `width?: number | string`: Defines the width of the `VcBlade` panel (e.g., "50%", "300px"). Defaults to "30%".
*   `expanded?: boolean`: Controls if the `VcBlade` panel itself should occupy the full available width within its blade navigation container (relevant in multi-blade layouts).
*   `closable?: boolean`: Determines if the `VcBlade` shows a close button in its header (defaults to `true`).
*   `toolbarItems?: BladeToolbarItem[]`: An array of objects defining the items for the `VcBlade`'s toolbar.
*   `modified?: boolean`: If set to `true`, indicates that the blade has unsaved changes, potentially showing a visual cue.

**Note on Custom Blade Component Props:**
The Vue components you create to be displayed *inside* `VcBlade` (e.g., `MyCustomBladePage.vue`) are expected to accept their own set of standard props, such as `param`, `options`, and also `expanded` and `closable` (which are passed by the blade navigation system to control the custom blade's behavior). For details on these standard props for your custom blade components, please refer to the [Developing Custom Modules guide](/platform/developer-guide/latest/custom-apps-development/vc-shell/Guides/developing-custom-modules.md#props-and-emits).

## Events Emitted by the `VcBlade` UI Component

The `VcBlade` UI component emits events in response to interactions with its own controls (primarily within its header):

*   `close`: Emitted when the close button in the `VcBlade`'s header is clicked.
*   `expand`: Emitted when the expand control in the `VcBlade`'s header is clicked.
*   `collapse`: Emitted when the collapse control in the `VcBlade`'s header is clicked.

**Note on Custom Blade Component Emits:**
Your custom blade components (e.g., `MyCustomBladePage.vue`) will typically listen to these events from `VcBlade` (e.g., `<VcBlade @close="$emit('close:blade')">`). They then emit their own standardized events like `close:blade`, `parent:call`, etc., for the blade navigation system or parent blades to handle. These standard emits for custom blade components are detailed in the [Developing Custom Modules guide](/platform/developer-guide/latest/custom-apps-development/vc-shell/Guides/developing-custom-modules.md#props-and-emits).

## The Blade Page Component Contract

While `VcBlade` provides the visual frame, the custom Vue component you create for a blade's content (e.g., `ProductDetailsPage.vue`) must adhere to an implicit contract to integrate properly with the navigation system (`useBladeNavigation`).

This contract involves three key parts: standard props, standard emits, and exposing the title.

### Standard Props & Emits

Your blade page component should accept a standard set of props (`expanded`, `closable`, `param`, etc.) and emit standard events (`close:blade`, `parent:call`, etc.) to communicate with the navigation system.

*   For a detailed list of these props and emits, please refer to the [Developing Custom Modules guide](/platform/developer-guide/latest/custom-apps-development/vc-shell/Guides/developing-custom-modules).

### Exposing the Blade Title (`defineExpose`)

For the navigation system (specifically `useBreadcrumbs`) to correctly display the blade's title in breadcrumbs or other UI elements, your blade component **must** expose its title via the `defineExpose` compiler macro.

The title is often a `computed` property, allowing it to be dynamic (e.g., changing from "Create Product" to the actual product name once it's loaded).

**Example (`ProductDetailsPage.vue`):**
```vue
<script setup lang="ts">
import { computed, ref } from 'vue';

// --- Props, State, etc. ---
const props = defineProps<{ param?: string }>();
const productName = ref(''); // Assume this gets populated from an API call

// --- Computed Title ---
const bladeTitle = computed(() => {
  // If editing an existing product with a loaded name
  if (props.param && productName.value) {
    return productName.value;
  }
  // If creating a new product
  return 'Create Product';
});

// --- Expose the Title ---
// This is crucial for breadcrumbs and navigation!
defineExpose({
  title: bladeTitle,
});
</script>
```
By exposing the `title`, you allow the parent navigation components to reactively access and display it, ensuring the UI is always in sync with the state of your blade.

## Interaction with Blade Navigation

Blades are managed by the `useBladeNavigation` composable, which handles their opening, closing, and stacking. The `VcBladeNavigation` component is responsible for rendering the visible stack of blades.

## Related Documentation

*   **UI Component:** [`VcBlade`](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/ui-components/vc-blade)
*   **Developing Custom Modules (Blade Creation):** [`developing-custom-modules.md`](/platform/developer-guide/latest/custom-apps-development/vc-shell/Guides/developing-custom-modules)
*   **Working with Blade Navigation:** [`working-with-blade-navigation.md`](./working-with-blade-navigation.md) 
