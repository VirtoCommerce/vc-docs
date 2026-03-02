# whiteLabelingSettings ==~query~==

This query allows you to retrieve white labeling settings.

## Arguments

| Argument                      | Description                                         |
|-------------------------------|-----------------------------------------------------|
| `organizationId` ==String==   | The Id of the organization.                        |
| `userId` ==String==           | The Id of the user.                                |
| `storeId` ==String==          | The Id of the store.                               |
| `cultureName` ==String==      | A language to retrieve data in.                    |

## Possible returns

| Possible return                                      | Description                                    |
|------------------------------------------------------|------------------------------------------------|
| [`WhiteLabelingSettingsType`](../objects/WhiteLabelingSettingsType.md) | The white labeling settings for the given parameters. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  whiteLabelingSettings(organizationId: "f081c52234754c9c8229aa42d6a19220", storeId: "Electronics", cultureName:"en-US") {
    userId
    organizationId
    logoUrl
    secondaryLogoUrl
    faviconUrl
    favicons {
      rel
      type
      sizes
      href
    }
    themePresetName
    footerLinks {
      title
      url
      childItems {
        title
        url
      }
    }
  }
}
```

```json title="Return"
{
  "data": {
    "whiteLabelingSettings": {
      "userId": null,
      "organizationId": "f081c52234754c9c8229aa42d6a19220",
      "logoUrl": "https://example.com/logo.png",
      "secondaryLogoUrl": "https://example.com/logo-footer.png",
      "faviconUrl": "https://example.com/favicon.ico",
      "themePresetName": "default",
      "favicons": [],
      "footerLinks": []
    }
  }
}
```

</div>