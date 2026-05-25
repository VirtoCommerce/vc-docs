# Brand ==~query~==

This query allows you to retrieve a specific brand by its ID and optionally localize the result based on the language (culture).

## Arguments

| Argument                 | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| `id` ==String!==         | The ID of the brand to retrieve.                          |
| `storeId` ==String!==    | The ID of the store to retrieve the brand from.           |
| `cultureName` ==String== | A language to retrieve localized brand data in.           |

## Possible return

| Possible return                        | Description                      |
| -------------------------------------- | -------------------------------- |
| [`BrandType`](../objects/BrandType.md) | The brand object and its fields. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  brand(
    id: "Efes"
    storeId: "B2B-store"
    cultureName: "en-US"
  ) {
      id
      name
      description
      logoUrl
    }
}
```

```json title="Return"
{
  "data": {
    "brand": {
      "id": "Efes",
      "name": "Efes",
      "description": null,
      "logoUrl": null
    }
  }
}
```

</div>