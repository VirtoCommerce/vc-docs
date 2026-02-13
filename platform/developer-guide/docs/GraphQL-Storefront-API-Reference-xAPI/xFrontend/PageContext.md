# PageContext ==~query~==

This query retrieves all contextual information required to initialize and render a page in the Frontend. It aggregates several backend calls into a single response optimized for frontend use.

## Arguments

| Argument                    | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| `domain` ==String!==        | The current domain used to resolve the store and URL context.        |
| `storeId` ==String!==       | The Id of the store to load configuration and settings from.         |
| `cultureName` ==String==    | The culture/language used to retrieve localized data.                |
| `permalink` ==String==      | The URL path used to resolve slug information.                       |
| `organizationId` ==String== | The Id of the organization associated with the current user context. |
| `userId` ==String==         | The Id of the user for whom contextual data should be retrieved.     |

## Possible returns

| Possible return             | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| [`PageContextResponseType`](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/xFrontend/objects/PageContextResponseType) | A combined object containing all contextual data required to initialize and render a storefront page. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  pageContext(
    domain: "localhost"
    storeId: "B2B-store"
    cultureName: "en-US"
    permalink: "/"
    organizationId: "OrganizationId"
    userId: "UserId"
  ) {
      slugInfo {
        entityInfo {
          id
        }
      }
    store {
      storeId
    }
    whiteLabelingSettings {
      logoUrl
    }
      user {
        id
        userName
      }
    }
}
```

```json title="Return"
{
  "data": {
    "pageContext": {
    "slugInfo": {
        "entityInfo": {
        "id": "92ab56ae-4199-47dc-"
        }
    },
    "store": {
        "storeId": "B2B-store"
    },
    "whiteLabelingSettings": {
        "logoUrl": "https://virtostart-main.govirto.com/cms-content/assets/customization/logo_B2B-store_1750915110008.png"
    },
    "user": {
        "id": "UserId",
        "userName": "Anonymous"
    }
    }
  }
}
```

</div>