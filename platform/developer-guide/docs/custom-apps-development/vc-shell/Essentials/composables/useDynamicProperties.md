# `useDynamicProperties` Composable

The `useDynamicProperties` composable is a powerful and generic utility designed to manage the state and logic associated with dynamic properties within Vue applications. It is particularly useful for handling properties that may be multi-language, multi-value, or draw their values from a dictionary (a list of predefined options, often loaded asynchronously).

This composable abstracts the complexities of fetching dictionary items, getting the appropriate property value based on locale or other criteria, and setting new values for properties, including all necessary transformations for multi-language and dictionary-based fields. Its generic nature allows it to be used with various API client types and data structures by providing specific type definitions and data-handling functions at initialization.

## Features

-   **Generic Implementation**: Adaptable to different property and dictionary item structures through TypeScript generics.
-   **Dictionary Management**: Handles asynchronous loading of dictionary items (options for select-like inputs) with keyword search and localization.
-   **Multi-language Support**: Correctly gets and sets values for properties that vary by language.
-   **Multi-value Support**: Manages properties that can hold multiple values.
-   **Loading State**: Provides a reactive `loading` state for dictionary operations.
-   **Decoupled Data Fetching**: Accepts a custom function for fetching dictionary items, allowing integration with any API client.
-   **Decoupled Data Instantiation**: Accepts constructors for property values and dictionary items, allowing use of specific classes from API clients.

## API

### Generics

The composable and its related interfaces use several generic types to ensure flexibility:

-   `TProperty extends IBaseProperty<TPropertyValue>`: Represents the type of the dynamic property object. Must extend `IBaseProperty`.
-   `TPropertyValue extends IBasePropertyValue`: Represents the type of an individual value of a property. Must extend `IBasePropertyValue`.
-   `TPropertyDictionaryItem extends IBasePropertyDictionaryItem`: Represents the type of a dictionary item. Must extend `IBasePropertyDictionaryItem`.
-   `TPropertyDictionaryItemSearchCriteria extends IBasePropertyDictionaryItemSearchCriteria`: Represents the type for search criteria when fetching dictionary items. Must extend `IBasePropertyDictionaryItemSearchCriteria`.

You can find the definitions of `IBaseProperty`, `IBasePropertyValue`, `IBasePropertyDictionaryItem`, and `IBasePropertyDictionaryItemSearchCriteria` within the `useDynamicProperties/index.ts` file. These base interfaces define the minimum expected structure.

### Parameters

The `useDynamicProperties` function is initialized with the following parameters:

| Parameter                             | Type                                                                                                 | Description                                                                                                                               |
| :------------------------------------ | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `searchDictionaryItemsFunction`       | `(criteria: TPropertyDictionaryItemSearchCriteria) => Promise<TPropertyDictionaryItem[] \| undefined>` | An asynchronous function that fetches dictionary items based on the provided criteria. It should return a promise resolving to an array of `TPropertyDictionaryItem` or `undefined`. |
| `PropertyValueConstructor`            | `new (data?: Partial<TPropertyValue>) => TPropertyValue`                                             | A constructor function for creating instances of `TPropertyValue`. Used internally when setting property values.                            |
| `PropertyDictionaryItemConstructor`   | `new (data?: Partial<TPropertyDictionaryItem>) => TPropertyDictionaryItem`                           | A constructor function for creating instances of `TPropertyDictionaryItem`. Used internally when processing dictionary items.           |
| `searchMeasurementFunction` (optional) | `(measureId: string, locale?: string) => Promise<TMeasurement[] \| undefined>`                      | An optional asynchronous function that fetches measurement units for properties with `valueType` of "Measure". Used for unit of measure selection. |

### Return value

The `useDynamicProperties` function returns an object (`IUseDynamicProperties<...>`) containing the following reactive properties and methods:

| Property / Method    | Type                                                                                                                               | Description               |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| `loading`            | `ComputedRef<boolean>`                                                                                                             | A read-only computed ref that is `true` while dictionary items are being loaded, and `false` otherwise.                                                                                                                                |
| `loadDictionaries`   | `(propertyId: string, keyword?: string, locale?: string) => Promise<TPropertyDictionaryItem[] \| undefined>`                       | Asynchronously loads dictionary items for a given `propertyId`. Optionally accepts a `keyword` for searching and a `locale` for localizing the dictionary items (e.g., setting the `value` field on each item based on `localizedValues`). |
| `getPropertyValue`   | `(property: TProperty, locale: string) => string \| TPropertyValue[] \| (TPropertyDictionaryItem & { value: string })[]`               | Retrieves the value of a given `property` for a specific `locale`. Handles multi-language, multi-value, and dictionary properties appropriately. Returns a single value, an array of values, or an array of dictionary items.         |
| `setPropertyValue`   | `(data: { property: TProperty; value: string \| TPropertyValue[] \| (TPropertyDictionaryItem & { value: string })[]; dictionary?: TPropertyDictionaryItem[]; locale?: string; initialProp?: TProperty; unitOfMeasureId?: string; }) => void` | Sets the value of a given `property`. It handles the necessary transformations for multi-language, multi-value, dictionary, and measurement properties. The `dictionary` parameter should contain the current list of dictionary items if applicable. The `locale` is crucial for multi-language properties. `initialProp` can be used to determine if a boolean value change is from undefined/empty or an actual flip. `unitOfMeasureId` is used for measurement properties. |
| `loadMeasurements`   | `(measureId: string, keyword?: string, locale?: string) => Promise<TMeasurement[] \| undefined>`                                   | Asynchronously loads measurement units for a given `measureId`. Optionally accepts a `keyword` for searching and a `locale` for localization. Used for properties with `valueType` of "Measure".                                      |

## Usage

```typescript
import { useDynamicProperties, useApiClient } from '@vc-shell/framework';
import {
  IProperty,
  IPropertyValue,
  IPropertyDictionaryItem,
  IPropertyDictionaryItemSearchCriteria,
  IMeasurement,
  PropertyValue,
  PropertyDictionaryItem,
  PropertyDictionaryItemSearchCriteria,
  VcmpMyApiClient,
} from '@your-api-package';

// Setup API client integration
const { getApiClient } = useApiClient(VcmpMyApiClient);

const searchDictionaryItemsFunction = async (
  criteria: IPropertyDictionaryItemSearchCriteria
): Promise<IPropertyDictionaryItem[] | undefined> => {
  const client = await getApiClient();
  const response = await client.searchDictionaryItems(
    new PropertyDictionaryItemSearchCriteria(criteria)
  );
  return response.results;
};

const searchMeasurementFunction = async (
  measureId: string,
  locale?: string
): Promise<IMeasurement[] | undefined> => {
  const client = await getApiClient();
  const response = await client.getMeasurements(measureId, locale);
  return response.results;
};

// Initialize the composable
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

// Get property value for current locale
const value = getPropertyValue(property, currentLocale);

// Set property value
setPropertyValue({
  property,
  value: newValue,
  dictionary: dictionaryItems,
  locale: currentLocale,
  initialProp: property,
});

// Set measurement property value
setPropertyValue({
  property: measurementProperty,
  value: measurementValue,
  unitOfMeasureId: selectedUnitId,
  locale: currentLocale,
  initialProp: measurementProperty,
});
```

## Key features

- **Generic type support**: Fully typed with TypeScript generics for different property structures
- **Dictionary management**: Asynchronous loading and caching of dictionary items with search capabilities
- **Multi-language support**: Handles properties that vary by locale with proper value resolution
- **Multi-value properties**: Manages properties that can hold multiple values
- **Measurement support**: Handles measurement properties with unit of measure selection
- **Reactive state**: Provides reactive loading states and automatic updates
- **API integration**: Decoupled from specific API clients through configurable functions

## Important notes

- The composable requires proper TypeScript generic types that extend the base interfaces
- Dictionary items are loaded asynchronously and cached for performance
- Property values are stored within the property's `values` array and managed reactively
- The `setPropertyValue` function handles all necessary transformations for different property types
- Multi-language properties require a locale parameter for proper value resolution
- Measurement properties require both a value and `unitOfMeasureId` for proper handling
- The `loading` state indicates when dictionary operations are in progress
- The optional `searchMeasurementFunction` enables support for measurement properties

## Related resources

- [Managing dynamic properties](../Usage-Guides/managing-dynamic-properties-with-usedynamicproperties.md)
- [useApiClient composable](../composables/useApiClient.md) - For API client integration
- [useLanguages composable](../composables/useLanguages.md) - For multi-language support
