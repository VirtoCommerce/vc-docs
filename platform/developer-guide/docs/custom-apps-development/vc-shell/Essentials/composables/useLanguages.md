# useLanguages Composable

The `useLanguages` composable provides functionality for managing internationalization and language settings in VC-Shell applications. It offers methods for changing the application's locale, retrieving language information, and handling language-related UI elements like flag icons.

The `useLanguages` composable is implemented as a shared composable (using Vue's `createSharedComposable`), ensuring that there's only one instance throughout the application. It helps manage the application's current locale, synchronizes it with the Vue I18n plugin and form validation (via Vee-Validate), and provides utilities for language display and formatting.

## API Reference

### Return value

The `useLanguages` composable returns an object with the following properties and methods:

```typescript
interface IUseLanguages {
  setLocale: (locale: string) => void;                  // Change the application's locale
  currentLocale: ComputedRef<string>;                   // Current active locale
  getLocaleByTag: (localeTag: string) => string | undefined;  // Get native language name from tag
  resolveCamelCaseLocale: (locale: string) => string;   // Format locale strings properly
  getFlag: (language: string) => Promise<string>;       // Get flag icon for a language
  getCountryCode: (language: string) => string;         // Get country code for a language
}
```

### Methods

#### setLocale

Changes the application's current locale, affecting i18n translations and form validations.

```typescript
setLocale(locale: string): void
```

- `locale`: The locale code to set as current (e.g., 'en', 'fr', 'es')

#### getLocaleByTag

Returns the native name of a language based on its locale tag.

```typescript
getLocaleByTag(localeTag: string): string | undefined
```

- `localeTag`: The locale tag (e.g., 'en-US', 'fr-FR')
- Returns: The native name of the language (e.g., 'English', 'Français')

#### resolveCamelCaseLocale

Formats a camelCase locale string into a standard hyphenated format and validates it against available locales.

```typescript
resolveCamelCaseLocale(locale: string): string
```

- `locale`: A locale string that might be in camelCase (e.g., 'enUS')
- Returns: Properly formatted locale (e.g., 'en-US'), or 'en' as fallback

#### getFlag

Retrieves the flag icon URL for a given language.

```typescript
getFlag(language: string): Promise<string>
```

- `language`: The language code (e.g., 'en', 'fr')
- Returns: Promise resolving to the URL of the flag icon

#### getCountryCode

Returns the ISO 3166-1 alpha-2 country code corresponding to a language.

```typescript
getCountryCode(language: string): string
```

- `language`: The language code (e.g., 'en', 'fr')
- Returns: Country code (e.g., 'us', 'fr')

### Properties

#### currentLocale

A computed reference to the current active locale.

```typescript
currentLocale: ComputedRef<string>
```

## Usage

### Basic usage

```typescript
import { useLanguages } from '@vc-shell/framework';
import { onMounted, watch } from 'vue';

export default {
  setup() {
    const { currentLocale, setLocale, getLocaleByTag } = useLanguages();
    
    // Change the application language
    function changeLanguage(locale) {
      setLocale(locale);
    }
    
    // Get the native name of the current language
    const currentLanguageName = computed(() => {
      return getLocaleByTag(currentLocale.value);
    });
    
    // Watch for changes in the current locale
    watch(currentLocale, (newLocale) => {
      console.log(`Language changed to: ${newLocale}`);
      document.documentElement.lang = newLocale;
    });
    
    return {
      currentLocale,
      currentLanguageName,
      changeLanguage
    };
  }
}
```

### Creating language selector

```vue
<template>
  <div class="language-selector">
    <div v-for="language in availableLanguages" :key="language.code" 
         class="language-option" 
         :class="{ 'active': language.code === currentLocale }"
         @click="changeLanguage(language.code)">
      <img :src="language.flag" :alt="language.name" class="flag-icon" />
      <span>{{ language.name }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useLanguages } from '@vc-shell/framework';
import { useI18n } from 'vue-i18n';

const { currentLocale, setLocale, getLocaleByTag, getFlag } = useLanguages();
const { availableLocales } = useI18n();

const availableLanguages = ref([]);

// Initialize available languages with flags
onMounted(async () => {
  for (const locale of availableLocales) {
    const name = getLocaleByTag(locale);
    const flag = await getFlag(locale);
    
    if (name) {
      availableLanguages.value.push({
        code: locale,
        name,
        flag
      });
    }
  }
});

function changeLanguage(locale) {
  setLocale(locale);
}
</script>

<style scoped>
.language-selector {
  display: flex;
  gap: 10px;
}

.language-option {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}

.language-option.active {
  background-color: #f0f0f0;
  font-weight: bold;
}

.flag-icon {
  width: 20px;
  height: 15px;
  object-fit: cover;
}
</style>
```

### Working with language tags and names

```typescript
import { useLanguages } from '@vc-shell/framework';

export default {
  setup() {
    const { getLocaleByTag, resolveCamelCaseLocale } = useLanguages();
    
    // Format and normalize locale tags
    function formatLocale(locale) {
      // Convert camelCase to standard format (e.g., 'enUS' to 'en-US')
      const normalizedLocale = resolveCamelCaseLocale(locale);
      
      // Get the native name of the language
      const languageName = getLocaleByTag(normalizedLocale);
      
      return {
        code: normalizedLocale,
        name: languageName
      };
    }
    
    // Example usage
    console.log(formatLocale('enUS')); // { code: 'en-US', name: 'English' }
    console.log(formatLocale('frFR')); // { code: 'fr-FR', name: 'Français' }
    
    return {
      formatLocale
    };
  }
}
```

### Using LanguageSelector component

VC-Shell provides a ready-to-use `LanguageSelector` component that leverages the `useLanguages` composable:

```vue
<template>
  <div class="settings-panel">
    <LanguageSelector />
    <!-- Other settings components -->
  </div>
</template>

<script setup>
import { LanguageSelector } from '@vc-shell/framework';
</script>
```

## Best practices

* **Store user preference**: The composable automatically stores the user's language preference in local storage (`VC_LANGUAGE_SETTINGS`), so it persists across sessions.
* **Consistent locale format**: Always use standard locale formats (e.g., **en-US**, **fr-FR**) in your code, and use the provided utilities to normalize any non-standard formats.
* **Native language names**: Use the `getLocaleByTag` method to display language names in their native form, which provides a better user experience.
* **Flag icons**: Use the `getFlag` method to retrieve appropriate flag icons for languages, following international conventions.
* **Validation integration**: The composable automatically synchronizes the locale with Vee-Validate, ensuring consistent internationalization of form validations.
* **Dynamic translations**: When adding new languages, include all required translation keys, especially `language_name` which is used by language selector components.
* **Fallback handling**: The composable handles fallbacks gracefully, defaulting to 'en' when a requested locale is not available.

