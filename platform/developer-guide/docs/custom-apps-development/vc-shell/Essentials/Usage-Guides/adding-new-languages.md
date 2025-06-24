# How-To: Adding New Languages to Applications and Modules

This guide explains how to add support for new languages in your VC-Shell based applications and custom modules. Proper internationalization (i18n) is crucial for reaching a global audience.

## Overview

VC-Shell utilizes the `vue-i18n` library for internationalization. Language management, including setting the current locale and loading translation messages, is facilitated by the `useLanguages` composable.

## Adding Languages to an Application

To add a new language to your main application, you need to create JSON translation files and ensure they are correctly registered.

### 1. Locale File Naming Convention

Language files should be placed in your application's `locales` directory (e.g., `my-app/src/locales/`).

-   **Two-letter codes**: For languages like English, French, German, use their two-letter ISO 639-1 code as the filename (e.g., `en.json`, `fr.json`, `de.json`).
-   **Extended codes**: For regional variations or languages with more specific codes (e.g., British English `en-GB`, Canadian French `fr-CA`), the filename should match this extended code (e.g., `enGb.json` or `en-gb.json` - the `useLanguages` composable can resolve camelCase, but hyphenated is standard).

**Example:**
If your application is `my-app`, the path would be `apps/my-app/src/locales/es.json` for Spanish.

### 2. Core `language_name` Key

Each main application language file (e.g., `en.json`, `es.json`) **must** contain a `language_name` key. This key's value is the native display name of the language and is used by components like the `LanguageSelector`.

**Example (`es.json`):**
```json
{
  "language_name": "Español",
  "SHELL": {
    "MENU": {
      "DASHBOARD": "Tablero"
    }
    // ... other translations
  }
}
```

### 3. Registering Application Locales

Application locales are typically imported and registered in your `main.ts` file. The `VirtoShellFramework` plugin and `useLanguages` composable handle the setup.


## Adding Languages to Modules

Custom modules within VC-Shell should also have their own `locales` directory to store translations specific to that module.

### 1. Module Locale File Structure

Each module that requires translations should have a `locales` subdirectory. Inside this directory, create JSON files for each supported language, following the same naming conventions as application-level locale files (e.g., `en.json`, `es.json`).

**Example for a module named `my-custom-module`:**
```
vendor-portal/src/modules/my-custom-module/
├── components/
├── composables/
├── locales/
│   ├── en.json
│   └── es.json
├── pages/
└── index.ts  // Module definition
```

### 2. Merging Module Locales

When a module is loaded, its locales are typically merged with the global i18n instance. This is often handled within the module's entry point (e.g., `index.ts` of the module) or during the dynamic module loading process if applicable. VC-Shell's module system usually facilitates this.

## Initializing Locales in `main.ts`

The `main.ts` file of your application is where the initial language setup occurs. This involves `vue-i18n` and the `useLanguages` composable.

### Configuring Default Locales via Environment Variables

For flexibility across different environments (development, production), it is best practice to define your default and fallback locales in `.env` files.

```
# .env file
APP_I18N_LOCALE=en
APP_I18N_FALLBACK_LOCALE=en
```

These variables are read by Vite and made available in your application code via `import.meta.env`. You then pass them to the framework during initialization, as shown in the example below.

### Key Steps:

1.  **Import `useLanguages`**: From `@vc-shell/framework`.
2.  **Import Locale Messages**: Import all your application-specific locale files.
3.  **Plugin Setup**: When installing `VirtoShellFramework`, you can pass i18n configuration, including the default and fallback locales.
4.  **Merge Locales**: After the app is created, iterate through your imported locale messages and use `app.config.globalProperties.$mergeLocaleMessage(key, message)` to add them to `vue-i18n`.
5.  **Set Initial Locale**: Use the `setLocale` function from `useLanguages` to set the active language. `currentLocale` (also from `useLanguages`) provides the resolved locale, often considering user's previously saved preference from local storage.

### Why this approach?

-   **Persistence**: `useLanguages` handles saving the selected language to local storage, so the user's preference persists across sessions.
-   **Synchronization**: It synchronizes the chosen locale with `vue-i18n`, VeeValidate (for localized validation messages), and updates the `lang` attribute of the `<html>` tag.
-   **Centralized Management**: Provides a consistent way to manage language settings throughout the application.

### Example Snippet:

```typescript
import VirtoShellFramework, { useLanguages } from "@vc-shell/framework";
import { createApp } from "vue";
import { router } from "./router"; // Your app's router
import * as locales from "./locales"; // Import all files from your app's locales/ dir
// ... other imports

async function startApp() {
  // ... (user loading, etc.)

  const { currentLocale, setLocale } = useLanguages(); // Get language functions

  const app = createApp(/* Root Component */);

  // Initialize VirtoShellFramework with i18n options from environment variables
  app.use(VirtoShellFramework, {
    router,
    i18n: {
      locale: import.meta.env.APP_I18N_LOCALE,
      fallbackLocale: import.meta.env.APP_I18N_FALLBACK_LOCALE,
    },
  });

  // ... (other plugins and module registrations)

  // Merge application-specific locales
  Object.entries(locales).forEach(([key, message]) => {
    // 'key' here would be 'en', 'es', etc. based on filenames
    app.config.globalProperties.$mergeLocaleMessage(key, message);
  });

  // Set the initial locale for the application
  // currentLocale.value already considers stored preferences or defaults
  setLocale(currentLocale.value);

  // ... (error handling, mount app)

  app.mount("#app");
}

startApp();
```

By calling `setLocale(currentLocale.value)`, you ensure that the application starts with either the user's saved language preference or the default language if no preference is stored. The `useLanguages` composable abstracts the complexities of interacting with `vue-i18n` and local storage.

## Graceful Fallback for Missing Translations

When you add a new language, you may not have all the translations ready at once. VC-Shell's internationalization is configured to handle this gracefully using a fallback mechanism.

If a translation key is not found in the current language's file (e.g., `de.json`), the system will automatically look for that same key in the `fallbackLocale` (which is typically configured as 'en' in `main.ts`).

**What this means for you:**

-   You can roll out a new feature with English-only text initially.
-   When you add a new language file (e.g., `de.json`), you only need to translate the keys you are ready for.
-   Any untranslated keys will automatically and safely display the English text, preventing broken UI elements or raw keys from appearing to the user.
-   This allows for an iterative approach to localization.

## Advanced Usage and `vue-i18n` Features

While the `useLanguages` composable and the process described above cover the primary mechanism for adding and managing languages in VC-Shell, `vue-i18n` itself offers a rich set of features for localization.

### Displaying Translations

The most common way to display translated strings in your Vue templates is by using the `$t` function:

```html
<template>
  <h1>{{ $t('SHELL.MENU.DASHBOARD') }}</h1>
  <p>{{ $t('welcomeMessage', { userName: 'Alex' }) }}</p> <!-- Example with parameters -->
  <p>{{ $tc('notifications', notificationCount) }}</p> <!-- Example with pluralization -->
</template>
```

### Using `useI18n` in `<script setup>`

For more programmatic control or access within your `<script setup>` block, you can use the `useI18n` composable directly from `vue-i18n`:

```typescript
import { useI18n } from 'vue-i18n';

const { t, locale } = useI18n();

const pageTitle = computed(() => t('myPage.title'));

function switchToGerman() {
  locale.value = 'de'; // Note: For global language switching, prefer useLanguages().setLocale()
}
```
However, for changing the application's language, it's recommended to use `useLanguages().setLocale()` as it handles additional synchronizations (like VeeValidate and `<html>` tag).

### Formatting Dates and Numbers

`vue-i18n` also supports locale-sensitive date and number formatting:

```html
<template>
  <p>Date: {{ $d(new Date(), 'short') }}</p>
  <p>Currency: {{ $n(12345.67, 'currency', { currency: 'USD' }) }}</p>
</template>
```

### Best Practices and Further Information

For a comprehensive understanding of all `vue-i18n` features (like component interpolation, detailed pluralization rules, datetime and number formats per locale) and best practices for structuring your translation keys, please refer to:

-   The [i18n Plugin documentation](../plugins/i18n.md) for an overview of VC-Shell's i18n plugin.
-   The official [Vue I18n Documentation](https://vue-i18n.intlify.dev/).

The [Best Practices section in the i18n Plugin documentation](../plugins/i18n.md#best-practices) also contains valuable guidelines for organizing translations, naming keys, and ensuring complete localization.

## Related Resources

-   [useLanguages Composable](./../composables/useLanguages.md) - Detailed documentation for the `useLanguages` composable.
-   [VeeValidate Localization](https://vee-validate.logaretm.com/v4/guide/i18n/) - For localizing validation messages. 
-   [Guides: Internationalization](./../../Guides/internationalization.md)
-   [Plugins: i18n](./../plugins/i18n.md)