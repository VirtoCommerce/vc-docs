# SlugInfo ==~query~==

This connection allows you to retrieve information about a slug or permalink.

## Arguments

| Argument                 | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `slug` ==String==        | The SEO-friendly identifier (slug) to look up.                          |
| `permalink` ==String==   | A permalink URL to resolve and retrieve the related entity information. |
| `storeId` ==String==     | The ID of the store context for the lookup.                             |
| `userId` ==String==      | The ID of the current user (if applicable).                             |
| `cultureName` ==String== | The culture or language code to retrieve localized slug information.    |

## Possible returns

| Possible return                                                                   | Description                                       |
| --------------------------------------------------------------------------------- | ------------------------------------------------- |
| [`SlugInfoResponseType`](../objects/SlugInfoResponseType.md)                      | Information about the resolved slug or permalink. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  slugInfo(
    slug: "brands"
    storeId: "B2B-store"
    userId: "30ce3994-2cbc-4c5e-93b8-e56a9792be49"
    cultureName: "en-US"
  )
  {
    entityInfo {
      id
      isActive
      languageCode
      objectId
      objectType
      semanticUrl
      metaDescription
      metaKeywords
      pageTitle
      __typename
    }
    __typename
  }
}
```

```json title="Return"
{
  "data": {
      "slugInfo": {
      "entityInfo": {
        "id": "Brands",
        "isActive": true,
        "languageCode": "en-US",
        "objectId": "Brands",
        "objectType": "Brands",
        "semanticUrl": "brands",
        "metaDescription": null,
        "metaKeywords": null,
        "pageTitle": null,
        "__typename": "SeoInfo"
    },
    "__typename": "SlugInfoResponseType"
    }
  }
}
```

</div>