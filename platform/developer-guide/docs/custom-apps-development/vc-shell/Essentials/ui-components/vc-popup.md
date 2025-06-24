# VcPopup Component

The `VcPopup` component is a versatile modal dialog organism used throughout the VC-Shell framework for displaying various types of modals including alerts, confirmations, and forms. It provides a consistent UI for modal interactions with customizable content, headers, and footers.

## Storybook

[VcPopup Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/organisms-vcpopup--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=organisms-vcpopup--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcButton @click="showPopup = true">Open Popup</VcButton>
  
  <VcPopup 
    v-if="showPopup" 
    title="Example Popup" 
    @close="showPopup = false"
  >
    <template #content>
      <p>This is the content of the popup.</p>
    </template>
    
    <template #footer="{ close }">
      <VcButton @click="close">Close</VcButton>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showPopup = ref(false);
</script>
```

## Props

| Prop                 | Type                                                | Default     | Description                                                 |
| -------------------- | --------------------------------------------------- | ----------- | ----------------------------------------------------------- |
| `title`              | `string`                                            | -           | The title displayed in the popup header                      |
| `closable`           | `boolean`                                           | `true`      | Whether to show a close button in the header                 |
| `variant`            | `'default' \| 'error' \| 'warning' \| 'success' \| 'info'` | `'default'` | Style variant of the popup, affects the icon and colors    |
| `isMobileFullscreen` | `boolean`                                           | `false`     | Whether the popup should be fullscreen on mobile devices    |
| `isFullscreen`       | `boolean`                                           | `false`     | Whether the popup should be fullscreen on all devices       |
| `modalWidth`         | `string`                                            | `'tw-max-w-md'` | CSS class to control the width of the modal                 |

## Events

| Event           | Parameters           | Description                                      |
| --------------- | -------------------- | ------------------------------------------------ |
| `close`         | -                    | Emitted when the popup is closed                  |

## Slots

| Slot             | Props                     | Description                                      |
| ---------------- | ------------------------- | ------------------------------------------------ |
| `header`         | -                         | Custom header content (replaces title)           |
| `content`        | -                         | Main content of the popup                        |
| `footer`         | `{ close: () => void }`   | Footer content with a close function as prop     |

## CSS Variables

The popup component uses CSS variables for theming, which can be customized:

```css
:root {
  --popup-close-btn-bg: var(--neutrals-100);            /* Background color of the close button */
  --popup-close-btn-bg-hover: color-mix(in srgb, var(--popup-close-btn-bg), #000 5%); /* Background color of close button on hover */
  --popup-header-color: var(--primary-700);             /* Text color for the popup header/title */
  --popup-content-text-color: var(--primary-700);       /* Text color for the popup content */
  
  /* Variant icon colors */
  --popup-warning-icon-color: var(--warning-500);       /* Color of the icon when variant is "warning" */
  --popup-error-icon-color: var(--danger-500);          /* Color of the icon when variant is "error" */
  --popup-success-icon-color: var(--success-500);       /* Color of the icon when variant is "success" */
  --popup-info-icon-color: var(--info-500);             /* Color of the icon when variant is "info" */
  
  /* Structure colors */
  --popup-footer-separator: var(--neutrals-200);        /* Color of separator line above footer */
  --popup-overlay-color: var(--additional-50);          /* Base color for the popup overlay */
  --popup-overlay: rgb(from var(--popup-overlay-color) r g b / 75%); /* Semi-transparent overlay color */
  --popup-bg: var(--additional-50);                     /* Background color of the popup */
}
```

## Examples

### Basic Informational Popup

```vue
<template>
  <VcButton @click="showInfoPopup = true">Show Info</VcButton>
  
  <VcPopup 
    v-if="showInfoPopup" 
    title="Information" 
    variant="info"
    @close="showInfoPopup = false"
  >
    <template #content>
      <p>This action will save the current version of your document.</p>
    </template>
    
    <template #footer="{ close }">
      <VcButton @click="close">Got it</VcButton>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showInfoPopup = ref(false);
</script>
```

### Confirmation Popup

```vue
<template>
  <VcButton @click="showConfirmPopup = true">Delete Item</VcButton>
  
  <VcPopup 
    v-if="showConfirmPopup" 
    title="Confirm Deletion" 
    variant="warning"
    @close="showConfirmPopup = false"
  >
    <template #content>
      <p>Are you sure you want to delete this item? This action cannot be undone.</p>
    </template>
    
    <template #footer>
      <div class="tw-flex tw-gap-4 tw-w-full">
        <VcButton 
          variant="outline" 
          @click="showConfirmPopup = false"
        >
          Cancel
        </VcButton>
        <VcButton 
          variant="primary" 
          @click="confirmDelete"
        >
          Delete
        </VcButton>
      </div>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showConfirmPopup = ref(false);

function confirmDelete() {
  // Handle delete logic
  showConfirmPopup.value = false;
}
</script>
```

### Error Popup

```vue
<template>
  <VcButton @click="showErrorPopup = true">Show Error</VcButton>
  
  <VcPopup 
    v-if="showErrorPopup" 
    title="Error Occurred" 
    variant="error"
    @close="showErrorPopup = false"
  >
    <template #content>
      <p>Unable to save changes. Please check your connection and try again.</p>
      <p class="tw-mt-2 tw-text-sm tw-text-[var(--neutrals-500)]">Error code: 503</p>
    </template>
    
    <template #footer="{ close }">
      <VcButton @click="close">Close</VcButton>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showErrorPopup = ref(false);
</script>
```

### Form in Popup

```vue
<template>
  <VcButton @click="showFormPopup = true">Edit Profile</VcButton>
  
  <VcPopup 
    v-if="showFormPopup" 
    title="Edit Profile" 
    modalWidth="tw-max-w-lg"
    @close="showFormPopup = false"
  >
    <template #content>
      <form @submit.prevent="saveProfile" class="tw-space-y-4">
        <div>
          <label class="tw-block tw-mb-1">Name</label>
          <input v-model="profile.name" class="tw-w-full tw-p-2 tw-border tw-rounded" />
        </div>
        
        <div>
          <label class="tw-block tw-mb-1">Email</label>
          <input v-model="profile.email" type="email" class="tw-w-full tw-p-2 tw-border tw-rounded" />
        </div>
        
        <div>
          <label class="tw-block tw-mb-1">Bio</label>
          <textarea v-model="profile.bio" class="tw-w-full tw-p-2 tw-border tw-rounded" rows="3"></textarea>
        </div>
      </form>
    </template>
    
    <template #footer>
      <div class="tw-flex tw-justify-end tw-gap-4 tw-w-full">
        <VcButton 
          variant="outline" 
          @click="showFormPopup = false"
        >
          Cancel
        </VcButton>
        <VcButton 
          variant="primary" 
          @click="saveProfile"
        >
          Save Changes
        </VcButton>
      </div>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showFormPopup = ref(false);
const profile = reactive({
  name: 'John Doe',
  email: 'john@example.com',
  bio: 'Developer and designer'
});

function saveProfile() {
  // Save profile logic
  showFormPopup.value = false;
}
</script>
```

### Fullscreen Popup

```vue
<template>
  <VcButton @click="showFullscreenPopup = true">View Image Gallery</VcButton>
  
  <VcPopup 
    v-if="showFullscreenPopup" 
    title="Image Gallery" 
    isFullscreen
    @close="showFullscreenPopup = false"
  >
    <template #content>
      <div class="tw-grid tw-grid-cols-3 tw-gap-4">
        <img 
          v-for="(image, index) in images" 
          :key="index" 
          :src="image.url" 
          :alt="image.alt"
          class="tw-w-full tw-h-48 tw-object-cover tw-rounded"
        />
      </div>
    </template>
    
    <template #footer="{ close }">
      <VcButton @click="close">Close Gallery</VcButton>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework';

const showFullscreenPopup = ref(false);
const images = [
  { url: 'https://example.com/image1.jpg', alt: 'Image 1' },
  { url: 'https://example.com/image2.jpg', alt: 'Image 2' },
  { url: 'https://example.com/image3.jpg', alt: 'Image 3' },
  { url: 'https://example.com/image4.jpg', alt: 'Image 4' },
  { url: 'https://example.com/image5.jpg', alt: 'Image 5' },
  { url: 'https://example.com/image6.jpg', alt: 'Image 6' },
];
</script>
```

### Custom Header

```vue
<template>
  <VcButton @click="showCustomHeaderPopup = true">Custom Header</VcButton>
  
  <VcPopup 
    v-if="showCustomHeaderPopup" 
    @close="showCustomHeaderPopup = false"
  >
    <template #header>
      <div class="tw-flex tw-items-center">
        <VcIcon icon="star" class="tw-mr-2 tw-text-[var(--warning-500)]" />
        <span class="tw-font-bold">Premium Feature</span>
      </div>
    </template>
    
    <template #content>
      <p>This feature is only available to premium subscribers.</p>
    </template>
    
    <template #footer>
      <div class="tw-flex tw-justify-between tw-w-full">
        <VcButton variant="outline" @click="showCustomHeaderPopup = false">
          Not Now
        </VcButton>
        <VcButton variant="primary" @click="upgradeToPremium">
          Upgrade
        </VcButton>
      </div>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton, VcIcon } from '@vc-shell/framework';

const showCustomHeaderPopup = ref(false);

function upgradeToPremium() {
  // Upgrade logic
  showCustomHeaderPopup.value = false;
}
</script>
```

