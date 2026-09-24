# StoreResponseType ==~object~==

This type represents the response data for a store, including its basic information and configuration.

## Fields

| Field                                                                                 | Description                                                 |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `storeId` ==String!==                                                                 | The Id for the store.                                       |
| `storeName` ==String!==                                                               | The name of the store.                                      |
| `catalogId` ==String!==                                                               | The Id for the store's catalog.                             |
| `storeUrl` ==String==                                                                 | The URL of the store.                                       |
| `assetPublicUrl` ==String==                                                           | The store's custom base URL for public asset links. When set, image and asset URLs in the store's queries are rebased onto it. |
| `defaultLanguage` [==LanguageType!==](LanguageType.md)                                | The default language used in the store.                     |
| `availableLanguages` [==[LanguageType!]!==](LanguageType.md)                          | An array of available languages for the store.              |
| `defaultCurrency` [==CurrencyType!==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/currency-type)           | The default currency used in the store.                     |
| `availableCurrencies` [==[CurrencyType!]!==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/currency-type)    | An array of available currencies for the store.             |
| `settings` [==StoreSettingsType!==](StoreSettingsType.md)                             | The settings configuration for the store.                   |
| `graphQLSettings` [==GraphQLSettingsType!==](GraphQLSettingsType.md)                  | The GraphQL settings configuration for the store.           |
| `dynamicProperties` [==DynamicPropertyValueType==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type)| A collection of dynamic property values assigned to the store. |
| `plugins(...)` [==[StorePluginType!]!==](StorePluginType.md)                          | The Module Federation plugins registered for the store, so a frontend host app can discover and load remotes at startup. Can be filtered by the `appId` argument to return only the plugins for a specific frontend host app. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../queries/store">← Store query</a>
    <a href="../StorePluginType">StorePluginType →</a>
</div>
