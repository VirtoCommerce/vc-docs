# PageContextResponseType ==~object~==

This type represents a combined response containing all contextual data required to initialize and render a Frontend page.

## Fields

| Field                                                                                    | Description                                                                 |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `slugInfo` [==SlugInfoResponseType==](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/SlugInfoResponseType) | Information about the resolved slug, including the associated entity.|
| `store` [==StoreResponseType==](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/Store/objects/StoreResponseType)   | Store-related data such as store ID, settings, and metadata.       |
| `whiteLabelingSettings` [==WhiteLabelingSettingsType==](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/White-labeling/queries/whiteLabelingSettings) | Branding and theme configuration applied to the Frontend.|
| `user` [==UserType==](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/Profile/Objects/UserType)  | Information about the current user, including identity and profile details. |
