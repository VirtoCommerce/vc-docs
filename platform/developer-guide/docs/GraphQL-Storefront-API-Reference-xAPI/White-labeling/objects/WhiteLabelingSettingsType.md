# WhiteLabelingSettingsType ==~object~==

This type defines the structure of white labeling settings.

## Fields

| Field                                       | Description                                                               |
|---------------------------------------------|---------------------------------------------------------------------------|
| `userId` ==String==                         | The Id of the user associated with the white labeling settings.           |
| `organizationId` ==String==                 | The Id of the organization to which the settings apply.                   |
| `storeId` ==String==                        | The Id of the store for which the white labeling settings are configured. |
| `logoUrl` ==String==                        | The URL of the primary logo used for branding.                            |
| `secondaryLogoUrl` ==String==               | The URL of an alternative logo, typically used in the footer.             |
| `faviconUrl` ==String==                     | The URL of the master favicon displayed in the browser tab.               |
| `themePresetName` ==String==                | The name of the predefined theme applied to the store's interface.        |
| [`footerLinks`](../objects/MenuLinkType.md) | A list of footer links, each represented by a **MenuLinkType** object.    |
| [`favicons`](../objects/FaviconType.md)     | A list of favicons, each represented by a **FaviconType** object.         |

