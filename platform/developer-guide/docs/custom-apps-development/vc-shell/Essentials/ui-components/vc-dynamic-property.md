# VcDynamicProperty

VcDynamicProperty is a versatile component designed for rendering different types of form inputs based on property metadata. It automatically determines the appropriate input type (text, number, boolean, date, etc.) and handles different scenarios like multivalue, multilanguage, and dictionary values.

## Basic Usage

```vue
<template>
  <VcDynamicProperty
    v-model="propertyValue"
    :property="propertyDefinition"
    :options-getter="fetchOptionsForProperty"
    :required="isRequired"
    :value-type="propertyType"
    :name="propertyName"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const propertyValue = ref(null);
const propertyDefinition = {
  id: 'property1',
  name: 'Property One',
  valueType: 'ShortText'
};

const isRequired = true;
const propertyType = 'ShortText';
const propertyName = 'propertyOne';

async function fetchOptionsForProperty(propertyId, keyword, locale) {
  // Function to fetch property options if it's a dictionary property
  if (propertyId === 'property1') {
    return [
      { id: 'option1', value: 'Option 1' },
      { id: 'option2', value: 'Option 2' }
    ];
  }
  return [];
}
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `Object` | - | Property definition object, must include an `id` |
| `modelValue` | `any` | - | Current value of the property |
| `optionsGetter` | `Function` | - | Function to get options for dictionary properties |
| `measurementsGetter` | `Function` | - | Function to get measurement units for measurement properties |
| `required` | `boolean` | - | Whether the property is required |
| `multivalue` | `boolean` | `false` | Whether the property supports multiple values |
| `multilanguage` | `boolean` | `false` | Whether the property supports multiple languages |
| `currentLanguage` | `string` | - | Current language code for multilanguage properties |
| `valueType` | `string` | - | Type of property (ShortText, LongText, Number, Integer, DateTime, Boolean, Measure) |
| `dictionary` | `boolean` | `false` | Whether the property is a dictionary property (with predefined options) |
| `name` | `string` | - | Property name |
| `optionsValue` | `string` | `'id'` | Field name to use for option values in dictionaries |
| `optionsLabel` | `string` | `'value'` | Field name to use for option labels in dictionaries |
| `displayNames` | `Array` | - | Array of localized display names for the property |
| `rules` | `Object` | - | Validation rules (e.g., `{ min?: number; max?: number; regex?: string; }`) |
| `disabled` | `boolean` | `false` | Whether the property is disabled |
| `placeholder` | `string` | - | Placeholder text for the input |

## Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `update:model-value` | `{value, dictionary, locale, unitOfMeasureId}` | Emitted when the property value changes. For measurement properties, includes `unitOfMeasureId` |

## CSS Variables

`VcDynamicProperty` itself does not define specific CSS variables for its own styling. Instead, it renders various underlying input components (like `VcInput`, `VcSelect`, `VcTextarea`, `VcSwitch`, `VcMultivalue`) based on the property type. Each of these child components may have its own set of CSS variables that can be used for theming. 

Here are links to the CSS variables documentation for the commonly used underlying components:

- Text inputs: See `VcInput` component CSS variables
- Dropdown selects: See `VcSelect` component CSS variables 
- Multiline text: See `VcTextarea` component CSS variables
- Boolean switches: See `VcSwitch` component CSS variables
- Multiple values: See `VcMultivalue` component CSS variables

When styling a form that uses `VcDynamicProperty`, you should reference the CSS variables of the specific components that will be rendered based on your property types.


## Automatic Input Type Selection

VcDynamicProperty automatically renders the appropriate input component based on the property's `valueType` and other attributes:

| Value Type | Multivalue | Dictionary | Component |
|------------|------------|------------|-----------|
| `ShortText` | No | No | `VcInput` |
| `ShortText` | Yes | No | `VcMultivalue` |
| `ShortText` | No | Yes | `VcSelect` |
| `ShortText` | Yes | Yes | `VcMultivalue` with options |
| `Number` or `Integer` | No | No | `VcInput` (type="number") |
| `Number` or `Integer` | Yes | No | `VcMultivalue` (type="number") |
| `DateTime` | No | No | `VcInput` (type="datetime-local") |
| `LongText` | No | No | `VcTextarea` |
| `Boolean` | No | No | `VcSwitch` |
| `Measure` | No | No | `VcInputDropdown` with unit selection |

## Localization Support

VcDynamicProperty supports localization in two ways:

1. **Multilanguage Properties**: When `multilanguage` is `true`, the component adds a language suffix to the property name and key.

2. **Localized Display Names**: The component can display localized property names using `vue-i18n`.

## Dictionary Properties

For dictionary properties (those with predefined options):

- The `optionsGetter` function is used to fetch options
- Options can be filtered using a search keyword
- The component supports both single and multi-select scenarios

## Integrating with `useDynamicProperties` Composable

The `VcDynamicProperty` component is often used in conjunction with the `useDynamicProperties` composable, which helps manage the state and logic for dynamic properties, especially when dealing with API interactions, dictionary loading, and multi-language values.

The `useDynamicProperties` composable provides:

- `getPropertyValue`: A function to get the current value for a property, correctly handling multi-language and dictionary types. This can be directly bound to `VcDynamicProperty`'s `:model-value`.
- `setPropertyValue`: A function to update a property's value. This is typically called in the `@update:model-value` event handler of `VcDynamicProperty`.
- `loadDictionaries`: A function to asynchronously load dictionary options. This can be passed to `VcDynamicProperty`'s `:options-getter` prop.

Refer to the [`useDynamicProperties` documentation](../composables/useDynamicProperties.md) for a detailed guide on its setup and API.

### Example: Using `VcDynamicProperty` with `useDynamicProperties`

This example demonstrates how to integrate `VcDynamicProperty` with `useDynamicProperties` to manage a list of dynamic properties.

```vue
<template>
  <div>
    <VcDynamicProperty
      v-for="property in allProperties"
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
      @update:model-value="(eventData) => setPropertyValue({ property, ...eventData, locale: currentLocale })"
    />
    <div v-if="loading" class="tw-mt-4">Loading dictionary options...</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import VcDynamicProperty from '@vc-shell/framework'; // Assuming VcDynamicProperty is correctly exported
import { useDynamicProperties } from "@vc-shell/framework"; // Adjust path as needed
// Define your API client and specific types if not using IBase* directly
import { VcmpMyApiClient, IProperty, IPropertyValue, IPropertyDictionaryItem, MyPropertyDictionaryItemSearchCriteria } from "@api-client";
import { useApiClient } from "@vc-shell/framework";


// Example: A list of properties for the entity being edited
const allProperties = ref<IMyProperty[]>([
  {
    id: 'color',
    name: 'Color',
    valueType: 'ShortText',
    dictionary: true,
    multilanguage: true,
    multivalue: false,
    required: true,
    displayNames: [{ name: "Color", languageCode: "en" }, { name: "Couleur", languageCode: "fr" }],
    values: [],
    validationRules: { max: 50 },
  },
  {
    id: 'description',
    name: 'Description',
    valueType: 'LongText',
    dictionary: false,
    multilanguage: true,
    multivalue: false,
    required: false,
    displayNames: [{ name: "Description", languageCode: "en" }, { name: "Description", languageCode: "fr" }],
    values: [],
  },
  // Add other properties as needed
]);

const currentLocale = ref('en');

// --- Setup for useDynamicProperties ---
// This part would typically involve your actual API client
const { getApiClient } = useApiClient(VcmpMyApiClient); 
const searchDictionaryItemsFunction = async (
  criteria: IMyPropertyDictionaryItemSearchCriteria
): Promise<IMyPropertyDictionaryItem[] | undefined> => {
  console.log('Searching dictionary items with criteria:', criteria);

  // Replace with actual API call:
  const client = await getApiClient();
  const response = await client.searchDictionaryItems(new MyPropertyDictionaryItemSearchCriteria(criteria));
  return response?.results?.map(item => new MyPropertyDictionaryItem(item));
  return [];
};

const {
  loading,
  loadDictionaries,
  getPropertyValue,
  setPropertyValue,
} = useDynamicProperties<
  IProperty,
  IPropertyValue,
  IPropertyDictionaryItem,
  IPropertyDictionaryItemSearchCriteria,
>(
  searchDictionaryItemsFunction,
  PropertyValue, // Use your actual PropertyValue constructor
  PropertyDictionaryItem  // Use your actual PropertyDictionaryItem constructor
);
// --- End setup for useDynamicProperties ---

</script>
```

## Examples

### Basic Text Property

```vue
<template>
  <VcDynamicProperty
    v-model="productName"
    :property="{ id: 'name', name: 'Product Name' }"
    :options-getter="getOptions"
    :required="true"
    value-type="ShortText"
    name="productName"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productName = ref('');

async function getOptions() {
  return []; // Not a dictionary property, so no options
}
</script>
```

### Number Property with Validation Rules

```vue
<template>
  <VcDynamicProperty
    v-model="productPrice"
    :property="{ id: 'price', name: 'Price' }"
    :options-getter="getOptions"
    :required="true"
    value-type="Number"
    name="productPrice"
    :rules="{ min: 0, max: 1000 }"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productPrice = ref(0);

async function getOptions() {
  return []; // Not a dictionary property, so no options
}
</script>
```

### Dictionary Property (Dropdown)

```vue
<template>
  <VcDynamicProperty
    v-model="productCategory"
    :property="{ id: 'category', name: 'Category' }"
    :options-getter="getCategoryOptions"
    :required="true"
    value-type="ShortText"
    :dictionary="true"
    name="productCategory"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productCategory = ref(null);

async function getCategoryOptions(propertyId, keyword) {
  // In a real app, you might fetch categories from an API
  const categories = [
    { id: 'electronics', value: 'Electronics' },
    { id: 'clothing', value: 'Clothing' },
    { id: 'books', value: 'Books' },
    { id: 'home', value: 'Home & Garden' }
  ];
  
  if (keyword) {
    return categories.filter(c => c.value.toLowerCase().includes(keyword.toLowerCase()));
  }
  return categories;
}
</script>
```

### Multilanguage Property

```vue
<template>
  <VcDynamicProperty
    v-model="productDescription"
    :property="{ id: 'description', name: 'Description' }"
    :options-getter="getOptions"
    :required="true"
    value-type="LongText"
    name="productDescription"
    :multilanguage="true"
    current-language="en"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productDescription = ref('');

async function getOptions() {
  return []; // Not a dictionary property, so no options
}
</script>
```

### Multivalue Property

```vue
<template>
  <VcDynamicProperty
    v-model="productTags"
    :property="{ id: 'tags', name: 'Tags' }"
    :options-getter="getTagOptions"
    :required="false"
    value-type="ShortText"
    name="productTags"
    :multivalue="true"
    :dictionary="true"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productTags = ref([]);

async function getTagOptions(propertyId, keyword) {
  const tags = [
    { id: 'new', value: 'New' },
    { id: 'sale', value: 'Sale' },
    { id: 'featured', value: 'Featured' },
    { id: 'popular', value: 'Popular' }
  ];
  
  if (keyword) {
    return tags.filter(t => t.value.toLowerCase().includes(keyword.toLowerCase()));
  }
  return tags;
}
</script>
```

### Measurement Property

```vue
<template>
  <VcDynamicProperty
    v-model="productWeight"
    :property="{ id: 'weight', name: 'Weight', valueType: 'Measure', measureId: 'weight' }"
    :options-getter="getOptions"
    :measurements-getter="getMeasurementUnits"
    :required="true"
    value-type="Measure"
    name="productWeight"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcDynamicProperty } from '@vc-shell/framework';

const productWeight = ref({ value: 0, unitOfMeasureId: 'kg' });

async function getOptions() {
  return []; // Not a dictionary property, so no options
}

async function getMeasurementUnits(measureId, locale) {
  // In a real app, you might fetch measurement units from an API
  const units = [
    { id: 'kg', displayName: 'Kilogram', displaySymbol: 'kg', isDefault: true },
    { id: 'g', displayName: 'Gram', displaySymbol: 'g', isDefault: false },
    { id: 'lb', displayName: 'Pound', displaySymbol: 'lb', isDefault: false }
  ];
  
  return units;
}
</script>
```

## Related Resources

- [useDynamicProperties Composable](../composables/useDynamicProperties.md) - For managing dynamic property data and logic.
- [Managing Dynamic Properties How-To Guide](../Usage-Guides/managing-dynamic-properties-with-usedynamicproperties.md)
