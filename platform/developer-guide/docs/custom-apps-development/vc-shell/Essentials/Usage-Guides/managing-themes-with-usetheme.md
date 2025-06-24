# How-To: Managing Application Themes with `useTheme`

The `useTheme` composable in VC-Shell provides a robust way to manage and switch between different visual themes within your application. This guide covers how to define new themes, create variations of existing ones, register them, and how CSS integration works automatically.

## Prerequisites

-   Understanding of Vue 3 Composition API.
-   Familiarity with the `useTheme` composable, its interfaces (`ThemeDefinition`, `DisplayTheme`), and methods (see [useTheme API Reference](../composables/useTheme.md)).
-   Basic knowledge of CSS custom properties (variables).
-   Understanding of how to define theme-specific CSS overrides using attribute selectors like `:root[data-theme="theme-key"]`.

## Core Concept

`useTheme` allows your application to define a list of available themes. Each theme is identified by a unique `key` (e.g., "light", "dark", "blue-contrast") and can have an optional `localizationKey` for its display name. The composable leverages `@vueuse/core::useColorMode` internally to automatically manage a `data-theme` attribute on the `<html>` element.

When a theme is changed (e.g., via the built-in `VcThemeSelector` component or programmatically using `setTheme`), `useTheme` updates `document.documentElement.dataset.theme` to the new theme's `key`. Your CSS then uses this attribute on the `:root` element (e.g., `:root[data-theme="my-theme-key"]`) to apply theme-specific styles, primarily by overriding a base set of CSS custom properties.

## Implementation Strategies

### 1. Defining and Registering a New Custom Theme

To add a completely new theme (e.g., "ocean-wave"), you need to:

**A. Define CSS Variables for the New Theme:**
   In your application's custom SASS/CSS file (e.g., `your-app/src/styles/custom.scss` or a dedicated theme file), create a new block for your theme using the `:root[data-theme="your-theme-key"]` selector. You will need to define all the relevant CSS custom properties that your application uses for styling. Refer to [Default Color Palette (Light Theme)](#default-color-palette-light-theme) for the list of variables used by the default `light` theme.

   ```scss
   /* In your custom.scss or a theme-specific file */
   :root[data-theme="ocean-wave"] {
     --primary-50: #E0F7FA;  // Example: Light cyan
     --primary-500: #0077B6; // Example: Main blue
     --primary-950: #023047; // Example: Dark blue

     --secondary-500: #80CBC4; // Example: Tealish

     /* Define all other necessary variables: 
        --neutrals-..., --accent-..., --warning-..., --danger-..., --success-..., --info-... 
     */
   }
   ```

**B. Register the New Theme in `useTheme`:**
   Typically in your main application setup (e.g., `App.vue` or a dedicated startup script), register your new theme definition.

   ```typescript
   // Example: App.vue or a startup script
   import { useTheme, type ThemeDefinition } from '@vc-shell/framework';

   const { register, setTheme } = useTheme();

   const newTheme: ThemeDefinition = {
     key: 'ocean-wave',
     localizationKey: 'THEMES.OCEAN_WAVE' // Optional: for display in VcThemeSelector
   };

   register(newTheme);

   // You can set this theme programmatically if needed:
   // setTheme('ocean-wave');
   // Or it will be available in the VcThemeSelector component.
   ```

### 2. Creating a Variation of an Existing Theme (e.g., a custom light theme)

If you want to create a variation of an existing theme (like the default `light` theme) by only changing a few colors, without rewriting all CSS variables from scratch, follow these steps:

**A. Define a New Key for Your Variation:**
   Choose a unique key, for example, `light-customized`.

**B. Register This Variation in `useTheme`:**

   ```typescript
   // Example: App.vue or a startup script
   import { useTheme, type ThemeDefinition } from '@vc-shell/framework';

   const { register } = useTheme();

   const lightThemeVariation: ThemeDefinition = {
     key: 'light-customized',
     localizationKey: 'THEMES.LIGHT_CUSTOMIZED' // Optional
   };

   register(lightThemeVariation);
   ```

**C. Add a CSS Block for the Variation, Overriding Only Necessary Variables:**
   In your application's `custom.scss` file (or a dedicated theme CSS file that is imported into your project), create a new CSS block for your theme variation, for example, `:root[data-theme="light-customized"]`.

   To ensure your theme variation is complete, it's best to copy all CSS variables from a base theme (e.g., the `light` theme variables, which you can find in the [Default Color Palette (Light Theme)](#default-color-palette-light-theme) section of this document) into this new block. Then, modify only the variables you wish to change for your `light-customized` variation.

   **Example for `light-customized` in `custom.scss`:**
   ```scss
   /* In your app's custom.scss */
   :root[data-theme="light-customized"] {
     /* Start by copying all variables from the :root[data-theme="light"] block,
        as shown in the [Default Color Palette (Light Theme)](#default-color-palette-light-theme) section. */

     // --- Copied from :root[data-theme="light"] ---
     --primary-50: #EFF7FC;
     --primary-100: #DAEDF7;
     --primary-200: #B0DAEE;
     --primary-300: #85C6E6;
     --primary-400: #5BB2DD;
     --primary-500: #319ED4; /* Original light theme primary */
     --primary-600: #288DBF;
     --primary-700: #237AA5;
     --primary-800: #1D678C;
     --primary-900: #185573;
     --primary-950: #154B66;
     // ... (copy all other variables: secondary, accent, neutrals, states, etc.)

     /* Then, override only the specific variables you want to change: */
     --primary-500: #FF6347; /* Example: Change primary to Tomato Red */
     // Any variable not overridden here will be the one copied from the light theme.
   }
   ```

Now, when `light-customized` is selected via `useTheme` (e.g., through `VcThemeSelector`), the attribute `data-theme="light-customized"` will be applied to the `<html>` element. The browser will use the CSS rules from the `:root[data-theme="light-customized"]` block.

**Important Note on Variations:**

-   From `useTheme`'s perspective, `light-customized` is a completely new, distinct theme identified by its unique `key`.
-   From a CSS management perspective, you are creating a *derived* theme by copying and modifying an existing set of CSS variables, which can save effort compared to defining every variable from scratch if the changes are minimal.

### 3. Directly Overriding an Existing Registered Theme's Styles

If your goal is to modify the appearance of an *already registered theme* (like the default `light` theme) without creating and registering a new `ThemeDefinition` (like `light-customized`), you can do so directly in your application's `custom.scss` file.

Simply add a CSS block for the theme you want to modify (e.g., `:root[data-theme="light"]`) in your `custom.scss` and specify only the CSS variables you wish to override. The build process and CSS cascade will ensure these overrides are applied when that theme is active.

**Example of Overriding `light` theme in `custom.scss`:**

```scss
/* In your app's custom.scss */

/* Override specific variables for the 'light' theme */
:root[data-theme="light"] {
  --primary-500: #D946EF; /* Fuchsia 500 - a new primary for light theme */
}
```

When the `light` theme is active, `--primary-500` will be fuchsia. Other variables from the base themes will remain unchanged.

This approach is straightforward for making targeted changes to existing themes without altering their registration in `useTheme`.

## Default Color Palette (Light Theme)

Below is a representative example of how the default `light` theme color palette is defined using CSS custom properties in `framework/assets/styles/theme/colors.scss`. When creating custom themes, you would typically override these variables.

```scss
// Light Theme Default Variables (from colors.scss)
:root[data-theme="light"] {
  // Primary
  --primary-50: #EFF7FC;
  --primary-100: #DAEDF7;
  --primary-200: #B0DAEE;
  --primary-300: #85C6E6;
  --primary-400: #5BB2DD;
  --primary-500: #319ED4; /* default */
  --primary-600: #288DBF;
  --primary-700: #237AA5;
  --primary-800: #1D678C;
  --primary-900: #185573;
  --primary-950: #154B66;

  // Secondary
  --secondary-50: #F4F7F9;
  --secondary-100: #ECF1F5;
  --secondary-200: #DBE4EC;
  --secondary-300: #CAD8E4;
  --secondary-400: #BACBDB;
  --secondary-500: #A9BFD2; /* default */
  --secondary-600: #81A1BD;
  --secondary-700: #5983A8;
  --secondary-800: #436480;
  --secondary-900: #2E4558;
  --secondary-950: #243544;

  // Accent
  --accent-50: #EFF7FC;
  --accent-100: #DAEDF7;
  --accent-200: #B0DAEE;
  --accent-300: #85C6E6;
  --accent-400: #5BB2DD;
  --accent-500: #319ED4; /* default */
  --accent-600: #288DBF;
  --accent-700: #237AA5;
  --accent-800: #1D678C;
  --accent-900: #185573;
  --accent-950: #154B66;

  // Neutrals
  --neutrals-50: #FAFAFA;
  --neutrals-100: #F5F5F5;
  --neutrals-200: #EBEBEB;
  --neutrals-300: #D4D4D4;
  --neutrals-400: #A3A3A3;
  --neutrals-500: #737373; /* default */
  --neutrals-600: #525252;
  --neutrals-700: #404040;
  --neutrals-800: #262626;
  --neutrals-900: #171717;
  --neutrals-950: #0A0A0A;

  // Additional
  --additional-50: #FFFFFF;
  --additional-950: #000000;

  // States

  // Warning
  --warning-50: #FFF6D6;
  --warning-100: #FFF2C4;
  --warning-200: #FFE7A0;
  --warning-300: #FFDA7C;
  --warning-400: #FFCB59;
  --warning-500: #FFBA35; /* default */
  --warning-600: #FC9E00;
  --warning-700: #B46B0F;
  --warning-800: #8C4F00;
  --warning-900: #542D00;
  --warning-950: #381D00;


  // Danger
  --danger-50: #FFE9E8;
  --danger-100:#FFD9D9;
  --danger-200: #FFB5B5;
  --danger-300: #FF9191;
  --danger-400: #FF6E6E;
  --danger-500: #FF4A4A; /* default */
  --danger-600: #FF0808;
  --danger-700: #C40000;
  --danger-800: #820000;
  --danger-900: #400000;
  --danger-950: #1F0000;

  // Success
  --success-50: #E4F4E2;
  --success-100: #C8E9CB;
  --success-200: #A9D4BA;
  --success-300: #8DC6A4;
  --success-400: #72B98F;
  --success-500: #57AB79; /* default */
  --success-600: #43875F;
  --success-700: #316144;
  --success-800: #1E3C2A;
  --success-900: #0B1610;
  --success-950: #020403;

  // Info
  --info-50: #EDF8FD;
  --info-100: #E3EFF5;
  --info-200: #C4DEEB;
  --info-300: #A6CDE1;
  --info-400: #87BCD6;
  --info-500: #69ABCC; /* default */
  --info-600: #4093BD;
  --info-700: #327393;
  --info-800: #245269;
  --info-900: #15313F;
  --info-950: #0E212A;
}

```
This example shows a subset of variables for the `light` theme. If you need to implement a dark theme or other custom themes, you would define a new block like `:root[data-theme="dark"] { ... }` with your overridden CSS variables.

## Best Practices

1.  **Define in CSS First**: Always define your theme's colors and styles in CSS using the `:root[data-theme="your-theme-key"]` selector before registering the theme key with `useTheme`.
2.  **Complete Variable Set**: When defining a new theme or a variation, ensure all necessary CSS custom properties used by your application and framework components are defined within that theme's CSS block to avoid visual inconsistencies. It's often safest to copy the full set from a base theme (like `light`) and then modify.
3.  **Centralized Registration**: Register all `ThemeDefinition` objects early in your application's lifecycle (e.g., in `main.ts`).
4.  **CSS Custom Properties**: Rely heavily on CSS custom properties for theming. Define a base set for your default theme and override them for other themes.
5.  **System Preference**: If you register a theme with `key: 'system'`, `useColorMode` (used internally) can be configured to automatically respect OS preferences. Consult `@vueuse/core::useColorMode` documentation for options if you need fine-grained control over this.
6.  **Clear Keys**: Use clear, descriptive, and kebab-case `key` values for your themes (e.g., `light-high-contrast`, `brand-blue`).
7.  **Localization**: Provide `localizationKey` in `ThemeDefinition` for user-friendly theme names in the `VcThemeSelector` or any custom UI.
8.  **Refer to Default Palette**: Use the [Default Color Palette (Light Theme)](#default-color-palette-light-theme) section in this document as a reference for the full list of default CSS variables provided by the `light` theme.

## Related Resources

-   [useTheme API Reference](../composables/useTheme.md) - Detailed API documentation.
-   [@vueuse/core `useColorMode`](https://vueuse.org/core/useColorMode/) - The underlying composable used by `useTheme` for `data-theme` attribute management.
