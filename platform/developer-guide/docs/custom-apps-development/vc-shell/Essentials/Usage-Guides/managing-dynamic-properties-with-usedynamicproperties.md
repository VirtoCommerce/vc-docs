# How-To: Managing Dynamic Properties with `useDynamicProperties`

The `useDynamicProperties` composable provides a powerful and flexible system for managing dynamic properties in VC-Shell applications. This guide demonstrates how to effectively handle multi-language, multi-value, and dictionary-based properties with seamless integration to UI components.

## Prerequisites

- Understanding of Vue 3 Composition API, including `ref`, `computed`, and reactive state management.
- Familiarity with the `useDynamicProperties` composable (see [useDynamicProperties API Reference](../composables/useDynamicProperties.md)).
- Basic knowledge of TypeScript generics and API client integration.
- Understanding of VC-Shell's dynamic property system and UI components.

## Core Concept

Dynamic properties are flexible data fields that can vary in type, language, and structure. The `useDynamicProperties` composable manages:

- **Dictionary Properties**: Properties with predefined options loaded from an API
- **Multi-language Support**: Properties that vary by locale
- **Multi-value Properties**: Properties that can hold multiple values
- **Measurement Properties**: Properties with numeric values and unit of measure selection
- **Type Safety**: Full TypeScript support for different property structures
- **Async Loading**: Efficient loading of dictionary options and measurement units with search capabilities

The composable abstracts the complexity of property value management while providing a clean interface for UI components.

```typescript
import { useDynamicProperties } from '@vc-shell/framework';

const {
  loading,
  loadDictionaries,
  loadMeasurements,
  getPropertyValue,
  setPropertyValue,
} = useDynamicProperties(
  searchDictionaryItemsFunction,
  PropertyValueConstructor,
  PropertyDictionaryItemConstructor,
  searchMeasurementFunction // Optional for measurement support
);
```

## Implementation Strategies

### 1. Basic Setup with API Client Integration

Start by setting up the composable with your API client:

```typescript
// useProductDynamicProperties.ts
import { useApiClient, useDynamicProperties } from '@vc-shell/framework';
import {
  VcmpSellerCatalogClient,
  IProperty,
  IPropertyValue,
  IPropertyDictionaryItem,
  IPropertyDictionaryItemSearchCriteria,
  IMeasurement,
  PropertyValue,
  PropertyDictionaryItem,
  PropertyDictionaryItemSearchCriteria,
} from '@your-api-package';

export function useProductDynamicProperties() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

  // Define the search function for dictionary items
  const searchDictionaryItemsFunction = async (
    criteria: IPropertyDictionaryItemSearchCriteria
  ): Promise<IPropertyDictionaryItem[] | undefined> => {
    try {
      const client = await getApiClient();
      const searchCriteria = new PropertyDictionaryItemSearchCriteria(criteria);
      const response = await client.searchDictionaryItems(searchCriteria);
      return response.results;
    } catch (error) {
      console.error('Failed to load dictionary items:', error);
      return undefined;
    }
  };

  // Define the search function for measurement units (optional)
  const searchMeasurementFunction = async (
    measureId: string,
    locale?: string
  ): Promise<IMeasurement[] | undefined> => {
    try {
      const client = await getApiClient();
      const response = await client.getMeasurements(measureId, locale);
      return response.results;
    } catch (error) {
      console.error('Failed to load measurements:', error);
      return undefined;
    }
  };

  // Initialize the composable with proper typing
  const {
    loading,
    loadDictionaries,
    loadMeasurements,
    getPropertyValue,
    setPropertyValue,
  } = useDynamicProperties<
    IProperty,
    IPropertyValue,
    IPropertyDictionaryItem,
    IPropertyDictionaryItemSearchCriteria,
    IMeasurement
  >(
    searchDictionaryItemsFunction,
    PropertyValue,
    PropertyDictionaryItem,
    searchMeasurementFunction
  );

  return {
    loading,
    loadDictionaries,
    loadMeasurements,
    getPropertyValue,
    setPropertyValue,
  };
}
```

### 2. Integration with VcDynamicProperty Component

Use the composable with the `VcDynamicProperty` component for seamless UI integration:

```vue
<!-- ProductPropertiesForm.vue -->
<template>
  <div class="product-properties">
    <h3 class="tw-text-lg tw-font-semibold tw-mb-4">Product Properties</h3>
    
    <div class="properties-grid tw-space-y-4">
      <VcDynamicProperty
        v-for="property in properties"
        :key="property.id || property.name"
        :property="property"
        :name="property.name || ''"
        :value-type="property.valueType || ''"
        :dictionary="property.dictionary"
        :multilanguage="property.multilanguage"
        :multivalue="property.multivalue"
        :required="property.required || false"
        :current-language="currentLocale"
        :options-getter="loadDictionaries"
        :display-names="property.displayNames"
        :rules="{
          min: property.validationRules?.min,
          max: property.validationRules?.max,
          regex: property.validationRules?.regex,
        }"
        :model-value="getPropertyValue(property, currentLocale)"
        @update:model-value="(eventData) => handlePropertyUpdate(property, eventData)"
      />
    </div>
    
    <div v-if="loading" class="tw-mt-4 tw-flex tw-items-center tw-gap-2">
      <VcLoading size="sm" />
      <span class="tw-text-sm tw-text-gray-600">Loading options...</span>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcDynamicProperty, VcLoading, useLanguages } from '@vc-shell/framework';
import { useProductDynamicProperties } from './useProductDynamicProperties';
import type { IProperty } from '@your-api-package';

interface Props {
  properties: IProperty[];
}

const props = defineProps<Props>();

const { currentLocale } = useLanguages();
const {
  loading,
  loadDictionaries,
  loadMeasurements,
  getPropertyValue,
  setPropertyValue,
} = useProductDynamicProperties();

function handlePropertyUpdate(property: IProperty, eventData: any) {
  setPropertyValue({
    property,
    value: eventData.value,
    dictionary: eventData.dictionary,
    locale: currentLocale.value,
    initialProp: property,
  });
}
</script>
```

### 3. Working with Measurement Properties

Measurement properties require special handling for unit of measure selection:

```vue
<!-- MeasurementPropertyForm.vue -->
<template>
  <div class="measurement-properties">
    <h3 class="tw-text-lg tw-font-semibold tw-mb-4">Product Measurements</h3>
    
    <VcDynamicProperty
      v-for="property in measurementProperties"
      :key="property.id || property.name"
      :property="property"
      :name="property.name || ''"
      :value-type="property.valueType || ''"
      :required="property.required || false"
      :current-language="currentLocale"
      :options-getter="loadDictionaries"
      :measurements-getter="loadMeasurements"
      :display-names="property.displayNames"
      :model-value="getPropertyValue(property, currentLocale)"
      @update:model-value="(eventData) => handleMeasurementUpdate(property, eventData)"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcDynamicProperty, useLanguages } from '@vc-shell/framework';
import { useProductDynamicProperties } from './useProductDynamicProperties';
import type { IProperty } from '@your-api-package';

interface Props {
  measurementProperties: IProperty[];
}

const props = defineProps<Props>();

const { currentLocale } = useLanguages();
const {
  loading,
  loadDictionaries,
  loadMeasurements,
  getPropertyValue,
  setPropertyValue,
} = useProductDynamicProperties();

function handleMeasurementUpdate(property: IProperty, eventData: any) {
  setPropertyValue({
    property,
    value: eventData.value,
    unitOfMeasureId: eventData.unitOfMeasureId,
    locale: currentLocale.value,
    initialProp: property,
  });
}
</script>
```

### 4. Working with Different Property Types

The composable handles different property types automatically. Here's how to work with the most common scenarios:

```typescript
// Working with different property types
const { getPropertyValue, setPropertyValue } = useProductDynamicProperties();

// Text properties (ShortText, LongText)
const textValue = getPropertyValue(textProperty, currentLocale);
// textValue will be a string

// Dictionary properties (single value)
const dictionaryValue = getPropertyValue(dictionaryProperty, currentLocale);
// dictionaryValue will be a dictionary item with { value: string }

// Multi-value dictionary properties
const multiDictionaryValue = getPropertyValue(multiDictionaryProperty, currentLocale);
// multiDictionaryValue will be an array of dictionary items

// Boolean properties
const booleanValue = getPropertyValue(booleanProperty, currentLocale);
// booleanValue will be a string "true" or "false"

// Setting values follows the same pattern
setPropertyValue({
  property: textProperty,
  value: "New text value",
  locale: currentLocale.value,
  initialProp: textProperty,
});

// Measurement properties
const measurementValue = getPropertyValue(measurementProperty, currentLocale);
// measurementValue will be a string representing the numeric value

// Setting measurement values requires both value and unit
setPropertyValue({
  property: measurementProperty,
  value: "10.5",
  unitOfMeasureId: "kg",
  locale: currentLocale.value,
  initialProp: measurementProperty,
});
```
```

## Best Practices

* **Type Safety**: Always use proper TypeScript generics to ensure type safety across your property management system.

* **API Integration**: Create dedicated composables for different API clients to maintain separation of concerns.

* **Error Handling**: Provide comprehensive error handling for API failures in your search function.

* **Reactivity**: Ensure that property objects are reactive (using `ref` or `reactive`) so that changes are properly detected.

* **Locale Management**: Always pass the current locale when getting or setting property values for multi-language properties.

* **Dictionary Loading**: Use the `loadDictionaries` function directly as the `options-getter` prop for `VcDynamicProperty` components.

* **Property Updates**: When handling property updates, always include the `initialProp` parameter to help with boolean value change detection.

* **Measurement Properties**: For measurement properties, always provide both `value` and `unitOfMeasureId` when setting values, and use the `loadMeasurements` function for unit selection.
