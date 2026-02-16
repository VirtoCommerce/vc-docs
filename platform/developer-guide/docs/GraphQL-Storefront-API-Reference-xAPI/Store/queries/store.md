# Store ==~query~==

This query allows you to retrieve information about a store.

## Arguments

| Argument                          | Description                                                   |
|-----------------------------------|---------------------------------------------------------------|
| `storeId` ==String!==             | The Id of the store to retrieve information from.             |
| `cultureName` ==String==          | The language to retrieve data in.                             |
| `domain` ==String==               | The domain or region to retrieve store information from.      |

## Possible Returns

| Possible Return                                        | Description                                                                                                     |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [`StoreResponseType`](../objects/StoreResponseType.md) | Defines the properties and fields associated with the store, including its basic information and configuration. |


## Example

<div class="grid" markdown>

```json title="Query"
query{
  store(storeId: "B2B-store", cultureName: "en-US") {
    userId
    userName
    storeId
    storeName
    catalogId
    storeUrl
    defaultLanguage {
      isInvariant
      cultureName
      nativeName
      threeLetterLanguageName
      threeLetterRegionName
      twoLetterLanguageName
      twoLetterRegionName
    }
    availableLanguages {
    }
    defaultCurrency {
      code
      symbol
    }
    availableCurrencies {
      code
      symbol
    }
    settings {
      quotesEnabled
      subscriptionEnabled
      taxCalculationEnabled
    }
  }
}
```

```json title="Return"
{
  "data": {
    "store": {
      "storeId": "testStore",
      "storeName": "000",
      "catalogId": "fc596540864a41bf8ab78734ee7353a3",
      "storeUrl": "https://vcptcore-qa-storefront.paas.govirto.com/",
....

      "settings": {
        "quotesEnabled": true,
        "subscriptionEnabled": true,
        "taxCalculationEnabled": true,
        "anonymousUsersAllowed": true,
        "isSpa": true,
        "emailVerificationEnabled": true,
        "emailVerificationRequired": true,
        "createAnonymousOrderEnabled": true,
        "seoLinkType": "None"
      }
    }
  }
}
```

</div>