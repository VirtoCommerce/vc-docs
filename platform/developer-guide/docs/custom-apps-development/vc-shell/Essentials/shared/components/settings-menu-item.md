# SettingsMenuItem Component

The `SettingsMenuItem` component is designed to be the standard building block for items within a settings menu, such as the one managed by `useSettingsMenu`. It provides a consistent look and feel, including an icon/image, title, and interactive states. It also offers slots for customization, allowing it to serve as a base for more complex settings entries that might include dropdowns or other interactive elements.

## Basic usage

```vue
<template>
  <SettingsMenuItem
    title="My Setting"
    icon="material-settings"
    @trigger:click="handleSettingClick"
  />
</template>

<script lang="ts" setup>
import { SettingsMenuItem } from '@vc-shell/framework'; // Adjust path as needed

function handleSettingClick() {
  console.log('My Setting clicked');
  // Handle setting interaction
}
</script>
```

## API reference

### Props

| Prop            | Type                        | Default     | Description                                                                                                |
|-----------------|-----------------------------|-------------|------------------------------------------------------------------------------------------------------------|
| `title`         | `string`                    | `undefined` | The main text displayed for the menu item.                                                                 |
| `icon`          | `string \| Component`       | `undefined` | An icon to display next to the title. Can be a string (e.g., Material Icon name) or a Vue component.         |
| `image`         | `string`                    | `undefined` | URL of an image to display. If both `icon` and `image` are provided, `icon` takes precedence.              |
| `emptyIcon`     | `string`                    | `undefined` | Placeholder icon for `VcImage` if `image` is provided but fails to load (passed to underlying `VcImage`). |
| `isActive`      | `boolean`                   | `false`     | Whether the menu item is currently active, applying active styling.                                        |
| `disabled`      | `boolean`                   | `false`     | If true, the item is visually styled as disabled and `trigger:click` events are not emitted.               |
| `isVisible`     | `boolean`                   | `true`      | Controls the visibility of the menu item. If false, it's hidden using `display: none`.                     |
| `triggerAction` | `"click" \| "hover" \| "none"` | `"click"`   | Defines the action that triggers events. Currently, only `"click"` effectively emits an event (`trigger:click`). `"none"` disables click-triggered events. `"hover"` is defined but not implemented to emit `trigger:hover` by default. |

### Events

| Event           | Payload | Description                                                                 |
|-----------------|---------|-----------------------------------------------------------------------------|
| `trigger:click` | -       | Emitted when the trigger area of the item is clicked, unless `disabled` is true or `triggerAction` is `'none'`. |
| `trigger:hover` | -       | Defined, but not emitted by default internal handlers. Intended for future use or custom hover handling.      |

### Slots

| Name         | Props | Description                                                                                                                                                              |
|--------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `trigger`    | -     | Allows providing entirely custom content for the trigger area of the menu item. If used, it replaces the default structure containing `icon`, `title`, and `additional` slots. |
| `icon`       | -     | Custom content for the icon part of the default trigger. Overrides the default `VcIcon` or `VcImage` rendering based on `icon` and `image` props.                         |
| `title`      | -     | Custom content for the title part of the default trigger. Overrides the default `<p class="vc-menu-item__title">{{ title }}</p>`.                                          |
| `additional` | -     | Slot for additional content to be placed next to the title within the default trigger's content area (e.g., a badge or secondary text).                                   |
| `content`    | -     | Slot for content to be displayed below the trigger area. Typically used for dropdowns, expandable sections, or forms related to the settings item.                       |

## CSS Variables

The `SettingsMenuItem` component uses the following CSS variables for styling:

```css
:root {
  --menu-item-text-color: var(--additional-950);       /* Text color for the title and other text content */
  --menu-item-border-color: var(--neutrals-200);     /* Border color for the bottom border of the item */
  --menu-item-bg: transparent;                         /* Default background color of the item */
  --menu-item-bg-hover: var(--primary-50);           /* Background color when a clickable item is hovered */
  --menu-item-icon-color-hover: var(--primary-700);  /* Intended for icon color on hover, but not directly applied by default CSS. May require custom styling. */
  --menu-item-bg-active: var(--primary-50);          /* Background color when the item is active (`isActive` prop is true) */
  /* Note: .vc-menu-item__icon uses --menu-item-icon-color which is not defined in the root. It likely defaults to text color or needs to be defined. */
}
```

## Usage examples

### Basic clickable item

```vue
<template>
  <SettingsMenuItem
    title="Profile Settings"
    icon="material-person"
    @trigger:click="goToProfile"
  />
</template>

<script lang="ts" setup>
import { SettingsMenuItem } from '@vc-shell/framework';

function goToProfile() {
  console.log('Navigating to profile settings...');
  // router.push('/profile-settings');
}
</script>
```

### Item with an image

```vue
<template>
  <SettingsMenuItem
    title="Company Logo"
    image="/path/to/your/logo.png"
    emptyIcon="material-broken-image"
    @trigger:click="openLogoUploadModal"
  />
</template>

<script lang="ts" setup>
import { SettingsMenuItem } from '@vc-shell/framework';

function openLogoUploadModal() {
  console.log('Opening logo upload modal...');
}
</script>
```

### Disabled item

```vue
<template>
  <SettingsMenuItem
    title="Advanced Feature (Coming Soon)"
    icon="material-star"
    disabled
    isVisible
  />
</template>

<script lang="ts" setup>
import { SettingsMenuItem } from '@vc-shell/framework';
</script>
```

### Item with custom content (dropdown example)

This example shows how you might structure an item that reveals more content on click.

```vue
<template>
  <SettingsMenuItem
    title="Notification Settings"
    icon="material-notifications"
    :isActive="isDropdownOpen"
    @trigger:click="toggleDropdown"
  >
    <template #content v-if="isDropdownOpen">
      <div class="custom-dropdown-content">
        <label>
          <input type="checkbox" v-model="emailNotifications" />
          Enable Email Notifications
        </label>
        <br/>
        <label>
          <input type="checkbox" v-model="pushNotifications" />
          Enable Push Notifications
        </label>
      </div>
    </template>
  </SettingsMenuItem>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { SettingsMenuItem } from '@vc-shell/framework';

const isDropdownOpen = ref(false);
const emailNotifications = ref(true);
const pushNotifications = ref(false);

function toggleDropdown() {
  isDropdownOpen.value = !isDropdownOpen.value;
}
</script>

<style scoped>
.custom-dropdown-content {
  padding: 10px 10px 10px 46px; /* Align with title, considering icon width and margin */
  background-color: var(--menu-item-bg-hover); /* Example style for dropdown area */
  border-bottom: 1px solid var(--menu-item-border-color);
}
.custom-dropdown-content label {
  display: block;
  margin-bottom: 5px;
}
</style>
```

### Item with additional slot content

```vue
<template>
  <SettingsMenuItem
    title="Language"
    icon="material-language"
    @trigger:click="openLanguageSelector"
  >
    <template #additional>
      <VcBadge variant="info" content="EN" class="tw-ml-auto" />
    </template>
  </SettingsMenuItem>
</template>

<script lang="ts" setup>
import { SettingsMenuItem, VcBadge } from '@vc-shell/framework'; // Assuming VcBadge is available

function openLanguageSelector() {
  console.log('Opening language selector...');
}
</script>
```

### Fully custom trigger

```vue
<template>
  <SettingsMenuItem @trigger:click="handleCustomClick">
    <template #trigger>
      <div class="my-custom-trigger">
        <VcIcon icon="material-logout" class="custom-icon" />
        <span class="custom-title">Log Out</span>
        <VcIcon icon="material-arrow_forward_ios" size="xs" class="tw-ml-auto" />
      </div>
    </template>
  </SettingsMenuItem>
</template>

<script lang="ts" setup>
import { SettingsMenuItem, VcIcon } from '@vc-shell/framework';

function handleCustomClick() {
  console.log('Logout initiated...');
}
</script>

<style scoped>
.my-custom-trigger {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 12px; /* Corresponds to p-3 */
  font-size: 0.875rem; /* Corresponds to text-sm */
  color: var(--menu-item-text-color);
}
.custom-icon {
  width: 24px; /* Corresponds to w-6 */
  margin-right: 12px; /* Corresponds to mr-3 */
  font-size: 16px;
}
.custom-title {
  flex-grow: 1;
}
</style>
```

This structure provides a solid foundation for various types of settings menu entries, from simple links to more complex interactive elements. 
