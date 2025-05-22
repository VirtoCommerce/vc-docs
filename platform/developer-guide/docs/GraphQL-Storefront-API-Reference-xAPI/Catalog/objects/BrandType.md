# BrandType ==~object~==

This type represents a brand in the catalog. It is used to retrieve brand metadata such as the brand name, logo, banner, permalink, and description. Featured brands can be highlighted on the frontend.

## Fields

| Field                                  | Description                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------- |
| `id` ==String!==                       | Brand ID.                                                                   |
| `brandPropertyName` ==String==         | Brand property name used to identify the brand field in product properties. |
| `brandPropertyValue` ==String==        | Unlocalized brand name as stored in product data.                           |
| `name` ==String==                      | Localized brand display name.                                               |
| `featured` ==Boolean==                 | Indicates if the brand is featured.                                         |
| `description` ==String==               | Optional localized brand description.                                       |
| `permalink` ==String!==                | Unique URL slug for linking to the brand's product listing.                 |
| `bannerUrl` ==String==                 | URL to the brand’s banner image.                                            |
| `logoUrl` ==String==                   | URL to the brand’s logo image.                                              |

