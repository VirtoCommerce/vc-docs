# useTheme Composable

The `useTheme` composable provides functionality for managing and switching between different themes in the VC-Shell framework. It allows defining themes with keys and localization keys, and integrates with `@vueuse/core` for underlying color mode management.

The `useTheme` composable allows applications to register multiple themes, switch between them, and access information about the currently active theme, including its localized name. It is primarily used for implementing theme selection mechanisms.

## API Reference

### Interfaces

```typescript
interface ThemeDefinition {
  key: string; // Unique identifier for the theme, used in CSS and for setting the theme
  localizationKey?: string; // Optional i18n key for the theme's display name
}

interface DisplayTheme {
  key: string; // Unique identifier
  name: string; // Localized display name for the theme
}
```

### Return value

The `useTheme` composable returns an object with the following reactive properties and methods:

```typescript
import type { Ref } from 'vue';
// Import interfaces ThemeDefinition and DisplayTheme as shown above

interface IUseTheme {
  themes: Ref<DisplayTheme[]>;          // Reactive array of registered themes with their display names.
  currentThemeKey: Ref<string>;         // Reactive string representing the key of the current active theme.
  currentLocalizedName: Ref<string>;  // Reactive string for the localized name of the current theme.
  next: () => void;                     // Switches to the next theme in the registered list.
  register: (themesToAdd: ThemeDefinition | ThemeDefinition[]) => void; // Registers one or more new themes.
  unregister: (themeKeysToRemove: string | string[]) => void;      // Removes themes by their keys.
  setTheme: (themeKey: string) => void; // Sets a specific theme as active by its key.
}

// Declaration (actual import path might vary based on your project structure)
declare function useTheme(): IUseTheme;
```

### Methods

#### `register(themesToAdd: ThemeDefinition | ThemeDefinition[]): void`

Registers one or more themes. Each theme is defined by a `ThemeDefinition` object.

-   `themesToAdd`: A single `ThemeDefinition` object or an array of `ThemeDefinition` objects.
    -   `key`: A unique string identifier for the theme (e.g., "light", "dark", "ocean-blue"). This key is used when calling `setTheme` and should match the class/attribute used in your CSS (e.g., `html.ocean-blue`).
    -   `localizationKey` (optional): An i18n key (e.g., "THEMES.OCEAN_BLUE") for fetching the theme's localized display name. If not provided, the display name will be a capitalized version of the `key`.

#### `unregister(themeKeysToRemove: string | string[]): void`

Removes one or more themes from the list of available themes, based on their keys.

-   `themeKeysToRemove`: A single theme key (string) or an array of theme keys (string[]) to remove.

#### `setTheme(themeKey: string): void`

Sets the specified theme as the currently active theme using its unique `key`.

-   `themeKey`: The `key` (string) of the theme to activate. This should correspond to a registered theme key.

#### `next(): void`

Cycles to the next theme in the internal list of registered themes. The order is based on the registration sequence.

### Properties

#### `themes: Ref<DisplayTheme[]>`

A reactive reference to an array of `DisplayTheme` objects. Each object contains the `key` and the localized `name` of a registered theme. Suitable for populating UI selectors.

#### `currentThemeKey: Ref<string>`

A reactive reference to a string that holds the `key` of the currently active theme.

#### `currentLocalizedName: Ref<string>`

A reactive reference to a string that holds the localized display `name` of the currently active theme. This is derived using the `localizationKey` if provided during registration, or by capitalizing the `key`.

## Related resources

-   [How-to: Managing application themes with `useTheme`](../Usage-Guides/managing-themes-with-usetheme.md) - Practical guide and examples for using this composable.
-   VC-Shell's main theming documentation or UI components like `VcThemeSelector` for ready-to-use theme switching UI.
