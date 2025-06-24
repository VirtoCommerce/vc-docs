# Internationalization (i18n)

VC-Shell provides robust support for internationalization, allowing you to create multi-language applications with ease. The framework's i18n capabilities are built on top of the popular `vue-i18n` library, providing a familiar and powerful API for managing translations and localization.

This guide provides an overview of the key concepts and best practices for implementing i18n in your custom applications.

## Core Concepts

### Translation Files

Translations are stored in JSON files located in the `src/locales` directory of your application or module. Each file corresponds to a specific language and contains a set of key-value pairs.

-   **Application Locales**: Placed in `src/locales` of your main application.
-   **Module Locales**: Bundled within a module's own `locales` directory to ensure portability and encapsulation.

### Locale Registration

For translations to be available in the application, they must be registered with the `vue-i18n` instance. VC-Shell provides streamlined mechanisms for this:

-   **For Applications**: Application-level locales are typically imported and merged into the global i18n instance in the `main.ts` file using `app.config.globalProperties.$mergeLocaleMessage`.
-   **For Modules**: When a VC-Shell module is registered, the framework automatically finds and merges any locale files provided by that module.

### The `useLanguages` Composable

The primary tool for interacting with language settings is the `useLanguages` composable. It provides reactive properties and methods for:

-   Getting and setting the current locale.
-   Accessing the list of available languages.
-   Retrieving localized resources like flag icons.

This composable ensures that language changes are propagated throughout the application, including to integrated libraries like `vee-validate` for localized validation messages.

## Key Principles and Best Practices

1.  **Use Translation Keys**: Always use translation keys (e.g., `t('messages.welcome')`) in your templates and code instead of hardcoding strings. This is the foundation of a localizable application.

2.  **Organize Keys by Namespace**: Structure your translation keys logically using namespaces (e.g., `products.details.title`, `shell.menu.dashboard`). This improves maintainability and reduces the chance of key collisions between different parts of your application.

3.  **Encapsulate Module Translations**: Whenever you create a module, it should contain its own `locales` directory with all the necessary translations for the feature it provides. This makes the module self-contained and easy to reuse or share.

4.  **Use Pluralization and Interpolation**: Leverage `vue-i18n`'s features for handling pluralization (`$tc`) and dynamic values (`$t('greeting', { name: 'User' })`). This is more efficient and maintainable than using conditional logic or string concatenation.

5.  **Provide a Fallback Language**: Always configure a `fallbackLocale` (usually 'en'). This ensures that if a translation key is missing for the current language, the application will display the text from the fallback language instead of showing an empty space or a raw key.

6.  **Centralize Language Switching**: Use the `useLanguages` composable and the `LanguageSelector` component provided by the framework for a consistent language switching experience. The composable handles persisting the user's choice and updating all relevant parts of the application.

## Practical Implementation

For detailed, step-by-step instructions on how to add new languages to both your main application and to individual modules, refer to our practical guides:

-   **[How-To: Adding New Languages](./../Essentials/Usage-Guides/adding-new-languages.md)**: A comprehensive guide on adding and managing locale files.
-   **[`useLanguages` Composable Documentation](./../Essentials/composables/useLanguages.md)**: The full API reference for the language management composable.
-   **[i18n Plugin Documentation](./../Essentials/plugins/i18n.md)**: Technical details about the underlying i18n plugin. 