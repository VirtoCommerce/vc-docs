# How-To: Integrating Shared Authentication Pages

VC-Shell provides several pre-built "shared pages" for common authentication flows like login, user invitation, password reset, and changing passwords. This guide explains how to integrate and customize these pages within your application using Vue Router.

## Prerequisites

-   Understanding of Vue 3 and Vue Router.
-   An existing VC-Shell application setup with routing configured.
-   Familiarity with your application's asset paths for logos and background images.

## Core Concept

Shared authentication pages are Vue components exported from `@vc-shell/framework`. You integrate them by defining routes in your application's router configuration file (typically `src/router/routes.ts`). These components accept various props to customize their appearance (logo, background, titles) and sometimes behavior (e.g., a custom composable for login logic).

## Available Shared Pages

The primary shared pages for authentication include:

-   **`Login`**: Handles user login.
-   **`Invite`**: Allows users to accept an invitation and set their password.
-   **`ResetPassword`**: Enables users to reset their password after requesting a password reset link.
-   **`ChangePasswordPage`**: A dedicated page for users to change their current password, often used when a password has expired or needs to be forcibly changed.

## Step 1: Importing Shared Page Components

First, import the necessary page components from `@vc-shell/framework` in your `routes.ts` file. You'll also typically import any assets like logos or background images.

```typescript
// src/router/routes.ts
import { RouteRecordRaw } from "vue-router";
import { Login, Invite, ResetPassword, ChangePasswordPage } from "@vc-shell/framework";

// Example: Import assets for branding
// Ensure these paths are correct for your project structure
// For Vite, assets in /public can be referenced directly with a leading /
import whiteLogoImage from "/assets/logo-white.svg"; // Your app's white logo
import bgImage from "/assets/background.jpg";       // Your app's background image

// Example: Import a custom login composable if you have one
import { useLogin } from "../composables/useLogin"; // Path to your custom useLogin composable

const version = import.meta.env.PACKAGE_VERSION; // Optional: for displaying app version
```

## Step 2: Configuring Routes

Define routes for each shared page, passing necessary props for customization.

### 1. Login Page (`Login`)

The `Login` component handles the user sign-in process.

**Route Configuration Example:**

```typescript
// In your routes array within src/router/routes.ts
{
  name: "Login",
  path: "/login",
  component: Login,
  meta: {
    appVersion: version, // Optional: useful for display on the login page
  },
  props: () => ({
    composable: useLogin,    // Pass your custom login composable
    logo: whiteLogoImage,    // Path to your logo image
    background: bgImage,     // Path to your background image
    title: "My Application Portal", // Custom title for the login form
  }),
}
```

**Key Props for `Login`:**

-   `composable`: A function that returns your login logic (e.g., an instance of `useLogin` from your app's composables, which might wrap the framework's `useUserManagement`). This allows for custom login procedures.
-   `logo`: URL or path to the logo displayed on the form.
-   `background`: URL or path to the background image for the page.
-   `title`: The main title displayed on the login form.

### 2. Invite Page (`Invite`)

The `Invite` component is used when a user accepts an invitation to the application. It typically requires `userId` and `token` from the URL query parameters.

**Route Configuration Example:**

```typescript
{
  name: "Invite",
  path: "/invite", // URL will be like /invite?userId=...&token=...
  component: Invite,
  props: (route) => ({
    userId: route.query.userId,
    token: route.query.token,
    userName: route.query.userName,
    logo: whiteLogoImage,
    background: bgImage,
  }),
}
```

**Key Props for `Invite`:**

-   `userId`, `token`, `userName`: Typically passed via URL query parameters. These are essential for the invitation acceptance process.
-   `logo`, `background`: For branding, similar to the Login page.

### 3. Reset Password Page (`ResetPassword`)

The `ResetPassword` component allows users to set a new password using a token received (usually via email).

**Route Configuration Example:**

```typescript
{
  name: "ResetPassword",
  path: "/resetpassword", // URL will be like /resetpassword?userId=...&token=...
  component: ResetPassword,
  props: (route) => ({
    userId: route.query.userId,
    token: route.query.token,
    userName: route.query.userName,
    logo: whiteLogoImage,
    background: bgImage,
  }),
}
```

**Key Props for `ResetPassword`:**

-   `userId`, `token`, `userName`: Similar to the Invite page, these are usually from URL query parameters and are vital for the password reset flow.
-   `logo`, `background`: For consistent branding.

### 4. Change Password Page (`ChangePasswordPage`)

The `ChangePasswordPage` provides a dedicated interface for users to change their password. This can be accessed through user settings or forced upon login if their password has expired.

**Route Configuration Example:**

```typescript
{
  name: "ChangePassword",
  path: "/changepassword",
  component: ChangePasswordPage,
  meta: {
    // 'forced: true' is often used in scenarios where the user *must*
    // change their password before proceeding, e.g., after a password expiry.
    // The ChangePasswordPage component might behave differently based on this meta field.
    forced: true,
  },
  props: (route) => ({
    // Only background is typically needed; other elements are standard.
    background: bgImage,
  }),
}
```

**Key Props for `ChangePasswordPage`:**

-   `background`: For branding the page.
-   `meta.forced`: An optional meta field. If `true`, the component might adapt its UI or behavior, for instance, by not allowing navigation away until the password is changed.

## Step 3: Add Routes to Your Router Instance

Ensure these route definitions are included in the `routes` array that you use to create your Vue Router instance.

```typescript
// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router';
// ... import your routes array that now includes the shared page routes ...
import { routes } from './routes';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes, // Your combined routes array
});

export { router };
```

## Customization and Best Practices

-   **Branding**: Consistently use your application's `logo`, `background`, and `title` props across these pages for a unified user experience.
-   **Custom Logic (`useLogin`)**: For the `Login` page, providing a custom `useLogin` composable is common to integrate with your specific backend authentication or to add extra logic before or after login.
-   **Asset Paths**: Ensure your image paths for `logo` and `background` are correct relative to your project's public assets directory or build process.
-   **Security**: Always handle tokens (`userId`, `token`) securely. These pages are part of flows that are sensitive.
-   **Error Handling**: The shared page components have built-in error handling for common scenarios. Your custom `useLogin` composable should also implement robust error handling.

By following these steps, you can quickly and effectively integrate standardized, customizable authentication pages into your VC-Shell application.

## Related Resources

-   [Vue Router Documentation](https://router.vuejs.org/)
