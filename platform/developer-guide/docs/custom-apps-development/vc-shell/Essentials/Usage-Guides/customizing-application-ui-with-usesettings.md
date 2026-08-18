# How-To: Customizing Application UI with `useSettings`

The `useSettings` composable provides a powerful system for customizing the application's visual identity and UI elements in VC-Shell applications. This guide demonstrates how to effectively manage and apply UI customization settings such as logos, titles, and user-specific elements.

## Prerequisites

- Understanding of Vue 3 Composition API and reactive properties.
- Familiarity with the `useSettings` composable (see [useSettings API Reference](../composables/useSettings.md)).
- Basic knowledge of VC-Shell's application structure and component hierarchy.
- Understanding of Vue's lifecycle hooks and computed properties.

## Core Concept

The `useSettings` composable provides two main approaches for UI customization:

- **Server-Side Settings**: Automatically loads UI customization from the backend
- **Runtime Customization**: Override settings programmatically using `applySettings`
- **Reactive Updates**: All changes are reactive and immediately reflected in the UI
- **Default Fallbacks**: Graceful handling of missing or undefined settings

The system integrates with VC-Shell's UI components to provide consistent branding across the application.

```typescript
import { useSettings } from '@vc-shell/framework';

const { uiSettings, loading, applySettings } = useSettings();

// Access current settings
console.log(uiSettings.value.title); // Application title
console.log(uiSettings.value.logo);  // Application logo URL

// Override settings
applySettings({
  title: 'My Custom App',
  logo: '/my-logo.svg'
});
```

## Implementation Strategies

### 1. Main Application Setup

Configure the root application component with dynamic UI settings:

```vue
<!-- App.vue -->
<template>
  <VcApp
    :is-ready="isReady"
    :logo="uiSettings.logo"
    :title="uiSettings.title"
    :version="version"
  />
</template>

<script lang="ts" setup>
import { useSettings, useUser } from '@vc-shell/framework';
import { onMounted, ref } from 'vue';
import logoImage from '/assets/logo.svg';

const { isAuthenticated } = useUser();
const { uiSettings, applySettings } = useSettings();
const isReady = ref(false);
const version = import.meta.env.PACKAGE_VERSION;

onMounted(async () => {
  try {
    if (isAuthenticated.value) {
      await customizationHandler();
      isReady.value = true;
    }
  } catch (error) {
    console.error('Failed to initialize app:', error);
    // Set ready anyway to prevent blocking
    isReady.value = true;
  }
});

async function customizationHandler() {
  // Apply settings with fallbacks
  applySettings({
    title: uiSettings.value?.title || 'Default App Title',
    logo: uiSettings.value?.logo || logoImage,
  });
}
</script>
```

### 2. Authentication Pages with Branding

Apply consistent branding to login and authentication pages through router configuration:

```typescript
// router/routes.ts
import { RouteRecordRaw } from 'vue-router';
import { Login, Invite, ResetPassword, ChangePasswordPage } from '@vc-shell/framework';
import whiteLogoImage from '/assets/logo-white.svg';
import bgImage from '/assets/background.jpg';
import { useLogin } from '../composables';

const version = import.meta.env.PACKAGE_VERSION;

export const routes: RouteRecordRaw[] = [
  // ... other routes

  {
    name: 'Login',
    path: '/login',
    component: Login,
    meta: {
      appVersion: version,
    },
    props: () => ({
      logo: whiteLogoImage,
      background: bgImage,
      title: 'Vendor Portal',
    }),
  },
  {
    name: 'Invite',
    path: '/invite',
    component: Invite,
    props: (route) => ({
      userId: route.query.userId,
      token: route.query.token,
      userName: route.query.userName,
      logo: whiteLogoImage,
      background: bgImage,
    }),
  },
  {
    name: 'ResetPassword',
    path: '/resetpassword',
    component: ResetPassword,
    props: (route) => ({
      userId: route.query.userId,
      token: route.query.token,
      userName: route.query.userName,
      logo: whiteLogoImage,
      background: bgImage,
    }),
  },
  {
    name: 'ChangePassword',
    path: '/changepassword',
    component: ChangePasswordPage,
    meta: {
      forced: true,
    },
    props: () => ({
      background: bgImage,
    }),
  },
];
```

**Key Points:**

- Authentication pages receive branding through **router props**, not `useSettings`
- Use `props` function in route configuration to pass logo, background, and title
- Framework authentication components (Login, Invite, ResetPassword) accept these props directly
- This approach ensures branding is available immediately without waiting for settings to load

### 3. Dynamic Settings Based on User Context

Customize application settings based on user authentication and context:

```vue
<!-- App.vue -->
<script lang="ts" setup>
import { useSettings, useUser } from '@vc-shell/framework';
import { onMounted, ref, watch } from 'vue';
import defaultLogo from '/assets/logo.svg';

const { user, isAuthenticated } = useUser();
const { uiSettings, applySettings } = useSettings();
const isReady = ref(false);

// Watch for authentication changes
watch(isAuthenticated, async (authenticated) => {
  if (authenticated) {
    await applyUserSpecificSettings();
  }
}, { immediate: true });

onMounted(async () => {
  if (isAuthenticated.value) {
    await applyUserSpecificSettings();
  }
  isReady.value = true;
});

async function applyUserSpecificSettings() {
  try {
    // Apply settings based on user context
    const customSettings = {
      title: determineApplicationTitle(),
      logo: determineApplicationLogo(),
      avatar: user.value?.avatarUrl,
      role: user.value?.roles?.[0] || 'User'
    };

    applySettings(customSettings);
  } catch (error) {
    console.error('Failed to apply user settings:', error);
    // Apply fallback settings
    applySettings({
      title: 'Portal',
      logo: defaultLogo
    });
  }
}

function determineApplicationTitle(): string {
  // Customize title based on user role or organization
  if (user.value?.isAdministrator) {
    return 'Admin Portal';
  }
  if (user.value?.organizationName) {
    return `${user.value.organizationName} Portal`;
  }
  return uiSettings.value?.title || 'Portal';
}

function determineApplicationLogo(): string {
  // Customize logo based on user organization or preferences
  if (user.value?.organizationLogo) {
    return user.value.organizationLogo;
  }
  return uiSettings.value?.logo || defaultLogo;
}
</script>
```

## Best Practices

* **Loading states**: Always handle loading states when working with settings to prevent UI flicker.

* **Fallback values**: Provide meaningful default values for all UI elements that depend on settings.

* **Error handling**: Implement proper error handling for settings loading and application failures.

* **Performance**: Use computed properties for reactive settings access to optimize re-rendering.

* **Persistence**: Consider implementing local fallbacks for critical UI settings.

 