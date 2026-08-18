# VcApp

VcApp is the root container component for VC-Shell applications. It provides the overall application layout including the app bar, navigation menu, workspace for blades, and popup container. This component serves as the foundation for the entire application interface and manages core services and providers.

## Basic usage

```vue
<template>
  <VcApp
    :is-ready="isAppReady"
    :logo="appLogo"
    :version="appVersion"
    :title="appTitle"
    :avatar="userAvatar"
    :name="userName"
    :role="userRole"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcApp } from '@vc-shell/framework';

const isAppReady = ref(true);
const appLogo = '/assets/logo.svg';
const appVersion = 'v1.0.0';
const appTitle = 'My Application';
const userAvatar = '/assets/avatar.jpg';
const userName = 'John Doe';
const userRole = 'Administrator';
</script>
```

## Props

| Prop                 | Type      | Default | Description                                           |
|----------------------|-----------|---------|-------------------------------------------------------|
| `isReady`            | `boolean` | -       | Indicates if the application is ready to be displayed |
| `logo`               | `string`  | -       | URL to the application logo image                     |
| `version`            | `string`  | -       | Application version string                            |
| `title`              | `string`  | -       | Application title                                     |
| `avatar`             | `string`  | -       | URL to the user avatar image                          |
| `name`               | `string`  | -       | User name displayed in the user dropdown              |
| `role`               | `string`  | -       | User role displayed in the user dropdown              |
| `disableMenu`        | `boolean` | `false` | Whether to disable the navigation menu                |
| `disableAppSwitcher` | `boolean` | `false` | Whether to disable the app switcher functionality     |

## Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `logo-click` | `goToRoot: () => void` | Emitted when the logo is clicked |

## Slots

| Slot Name | Description |
|-----------|-------------|
| `app-switcher` | Custom app switcher component |

## CSS variables

The app component uses CSS variables for theming, which can be customized:

```css
:root {
  --app-background: var(--secondary-200);  /* Background color for the entire application */
}
```

## Automatic service providers

VcApp automatically provides several core services and utilities to the application:

- **Menu service**: Manages the navigation menu items.
- **Settings menu**: Manages settings menu items.
- **AppBar widget service**: Manages widgets in the app bar.
- **Global search**: Provides global search functionality.
- **Dashboard service**: Manages dashboard components.
- **Mobile buttons service**: Manages mobile buttons in the app bar.

## Default UI components

VcApp comes with several pre-registered UI components:

* **Settings menu items**:
   - Language selector.
   - Theme selector.
   - Change password button.
   - Logout button.

* **App bar widgets**:
   - Notification dropdown

## Mobile support

VcApp provides responsive design with different layouts for mobile and desktop:
- On desktop, the app bar and navigation menu appear side by side
- On mobile, the app bar and navigation menu stack vertically

## Examples

### Basic application setup

```vue
<template>
  <VcApp
    :is-ready="isAppReady"
    :logo="appLogo"
    :title="appTitle"
    @logo-click="handleLogoClick"
  />
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { VcApp, useUser } from '@vc-shell/framework';

const isAppReady = ref(false);
const appLogo = '/assets/logo.svg';
const appTitle = 'My Application';

const { isAuthenticated } = useUser();

onMounted(async () => {
  // Initialize your application here
  // For example, load configuration, check authentication, etc.
  await checkAuthentication();
  isAppReady.value = true;
});

function handleLogoClick(goToRoot) {
  // Custom logic before navigating to root
  console.log('Logo clicked');
  goToRoot();
}

async function checkAuthentication() {
  // Your authentication logic here
  await new Promise(resolve => setTimeout(resolve, 1000));
}
</script>
```

### Custom app switcher

```vue
<template>
  <VcApp
    :is-ready="isAppReady"
    :title="appTitle"
  >
    <template #app-switcher>
      <div class="custom-app-switcher">
        <button 
          v-for="app in apps" 
          :key="app.id"
          class="app-button"
          @click="switchToApp(app)"
        >
          <img :src="app.icon" :alt="app.title" class="app-icon">
          <span>{{ app.title }}</span>
        </button>
      </div>
    </template>
  </VcApp>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcApp } from '@vc-shell/framework';

const isAppReady = ref(true);
const appTitle = 'My Application';

const apps = [
  { id: 'app1', title: 'Marketing', icon: '/assets/marketing.svg', url: '/marketing' },
  { id: 'app2', title: 'Orders', icon: '/assets/orders.svg', url: '/orders' },
  { id: 'app3', title: 'Products', icon: '/assets/products.svg', url: '/products' },
];

function switchToApp(app) {
  window.location.href = app.url;
}
</script>

<style scoped>
.custom-app-switcher {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px;
}

.app-button {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px;
  border-radius: 4px;
  background: transparent;
  border: none;
  cursor: pointer;
}

.app-button:hover {
  background: rgba(0, 0, 0, 0.05);
}

.app-icon {
  width: 24px;
  height: 24px;
}
</style>
```

## Workspace and blade navigation

VcApp automatically provides a workspace area for blade navigation. The blades are managed by the BladeNavigation service, which is used to navigate between different views within the application.

```vue
<script lang="ts" setup>
import { onMounted } from 'vue';
import { useBladeNavigation } from '@vc-shell/framework';

const { openBlade } = useBladeNavigation();

onMounted(() => {
  // Open a blade programmatically
  openBlade({
    blade: YourBladeName,
    param: 'optional-id',
    options: { /* Additional options */ },
    onOpen: () => { /* Handle open event */ },
    onClose: () => { /* Handle close event */ }
  });
});
</script>
```
