# useSettings Composable

The `useSettings` composable provides functionality for retrieving and managing UI customization settings in VC-Shell applications. It allows components to access application-wide settings such as logo, title, and user details, enabling consistent UI customization across the application.

The `useSettings` composable communicates with the platform's Settings API to fetch UI customization settings. These settings can include the application logo, title, and other UI-related configurations. The composable also provides a method to override these settings programmatically.

## API reference

### Return value

The `useSettings` composable returns an object with the following properties and methods:

```typescript
interface IUseSettings {
  readonly uiSettings: Ref<IUISetting>;  // UI settings object
  readonly loading: ComputedRef<boolean>; // Loading state
  applySettings: (args: { logo?: string; title?: string; avatar?: string; role?: string }) => void; // Override settings
}
```

### Methods

#### applySettings

Overrides the current UI settings with custom values. This does not update the server settings but applies the changes locally in the application.

```typescript
applySettings(args: { logo?: string; title?: string; avatar?: string; role?: string }): void
```

**Parameters:**
- `args`: An object containing the settings to override:
  - `logo` (string, optional): URL to the application logo
  - `title` (string, optional): Application title
  - `avatar` (string, optional): URL to the user avatar
  - `role` (string, optional): User role description

**Example:**
```typescript
applySettings({
  title: 'My Custom App',
  logo: '/assets/custom-logo.svg'
});
```

### Properties

#### uiSettings

A reactive reference to the UI settings object.

```typescript
uiSettings: Ref<IUISetting>
```

The `IUISetting` interface includes:

```typescript
interface IUISetting {
  contrast_logo?: string;  // Logo used on contrasting backgrounds
  logo?: string;           // Main application logo
  title?: string;          // Application title
  avatar?: string;         // User avatar
  role?: string;           // User role
}
```

#### loading

A computed boolean indicating whether settings are currently being loaded.

```typescript
loading: ComputedRef<boolean>
```

## Basic usage

### In script/setup
```typescript
import { useSettings } from '@vc-shell/framework';
import { computed } from 'vue';

    const { uiSettings, loading, applySettings } = useSettings();
    
// Access current settings
    const appTitle = computed(() => uiSettings.value.title || 'Default Title');
    const appLogo = computed(() => uiSettings.value.logo || '/default-logo.svg');
    
// Override settings
function customizeApp() {
      applySettings({
    title: 'Custom Application',
        logo: '/custom-logo.svg'
      });
    }
```

### In templates
```vue
<template>
  <div v-if="!loading" class="app-header">
    <img :src="uiSettings.logo || defaultLogo" :alt="uiSettings.title" />
    <h1>{{ uiSettings.title || 'Default Title' }}</h1>
  </div>
  <div v-else class="loading">Loading...</div>
</template>

<script lang="ts" setup>
import { useSettings } from '@vc-shell/framework';

const { uiSettings, loading } = useSettings();
const defaultLogo = '/assets/default-logo.svg';
</script>
```

## Best practices

* **Default values**: Always provide default values when accessing settings properties, as they might be undefined initially or if they failed to load.
* **Loading state**: Use the `loading` property to show appropriate loading indicators while settings are being fetched.
* **Reactive usage**: Take advantage of Vue's reactivity system by using computed properties or watchers when working with settings.
* **Settings scope**: Remember that changes made with `applySettings` are only applied locally for the current session and don't affect server-side settings.
* **Initialization**: The composable automatically attempts to load settings when it's first initialized, so there's no need to explicitly trigger loading.
* **Error handling**: The composable handles API errors internally, but you might want to add your own error handling for UI feedback.
* **Caching**: Settings are cached after the first load, so repeated calls to the composable won't trigger redundant API requests.
