# ProductType
The chart below shows the `ProductType` parameter and all its child parameters and options:

![image](./media/ProductType.jpeg)

<<<<<<< Updated upstream
## Schema Fields

|# |Name             |Type                                 |Description|
|--|-----------------|-------------------------------------|-----------|
| 1|id               |StringGraphType                      |The unique ID of the product|
| 2|code             |StringGraphType                      |The product SKU|
| 3|catalogId        |StringGraphType                      |CatalogId of the product|
| 4|category         |[CategoryType](#categorytype) |Field to resolve category of the requested product|
| 5|name             |StringGraphType                      |Name of the product|
| 6|descriptions     |List of DesciptionType               |Reviews of product|
| 7|productType      |StringGraphType                      |The type of product|
| 8|slug             |StringGraphType                      |Url of the product|
| 9|metaDescription  |StringGraphType                      |Meta description of the product|
|10|metaKeywords     |StringGraphType                      |Meta keywords of the product|
|11|metaTitle        |StringGraphType                      |Meta title of the product|
|12|imgSrc           |StringGraphType                      |Main image of the product|
|13|outerId          |StringGraphType                      |Category outer Id|
|14|brandName        |StringGraphType                      |Brand name of the product|
|15|masterVariation  |VariationType                        |Main variation of the product|
|16|variations       |List of VariationType                |Product variations|
|17|availabilityData |AvailabilityDataType                 |Product availability information|
|18|images           |List of ImageType                    |Product images|
|19|prices           |List of PriceType                    |Product prices|
|20|properties       |List of PropertyType                 |Product properties|
|21|assets           |List of AssetType                    |Product assets|
|22|outlines         |List of OutlineType                  |Category outlines|
|23|seoInfos         |List of SeoInfoType                  |SEO information of the product|
|24|associations     |ProductAssociationType               |Product associations|
|25|breadcrumbs      |BreadcrumbType                       |Product navigation information|
|26|videos           |VideoType                            |Product videos|
|27|keyProperties    |List of PropertyType                 |Configurable list of properties

## Product Key Properties

The `ProductType` query has a special configurable field, `keyProperties`. To make a catalog property appear in the `keyProperties` list, you need to configure it in the Catalog module by adding the `KeyProperty` attribute to `Property Attributes`. `KeyProperties` are auto sorted by the attribute value in the ascending order.

![Key Properties](./media/KeyPropertiesAttr.png)

The `keyProperties` field can be limited by the `take` argument.

## Example
The following query enables showing only first three key properties:

```json
query {
  products(
    storeId: "B2B-store"
    cultureName: "en-US"
  ) {
    items 
=======
## Fields

| Field                                                                   	| Description                                                                                  	|
|-------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------	|
| `id` {==String!==}                                                      	| A unique identifier for the product.                                                         	|
| `code` {==String!==}                                                    	| The SKU of the product.                                                                      	|
| `catalogId` {==String==}                                                 	| The unique ID of the catalog.                                                                	|
| `productType` {==String==}                                              	| The type of product.                                                                         	|
| `minQuantity` {==Int==}                                                  	| The minimum quantity that can be ordered for the product.                                    	|
| `maxQuantity` {==Int==}                                                  	| The maximum quantity that can be ordered for the product.                                    	|
| `outline` {==String==}                                                   	| All parent category IDs relative to the requested catalog, concatenated together.            	|
| `slug` {==String==}                                                      	| The URL slug for the product, related to the request.                                        	|
| `name` {==String!==}                                                     	| The name of the product.                                                                    	|
| `seoInfo` [{==SeoInfo==}](SeoInfo.md)                                     | A list of SEO information associated with the product.                                      	|
| `descriptions(...)` [{==DescriptionType==}](DescriptionType.md)           | A list of descriptions or reviews associated with the product.                               	|
| `description(...)` [{==DescriptionType==}](DescriptionType.md)            | A description or review associated with the product.                                         	|
| `category` [{==Category==}](category/CategoryType.md)                    | The category to which the product is associated.                                             	|
| `imgSrc` {==String==}                                                    	| The URL or path to the main image of the product.                                            	|
| `outerId` {==String==}                                                  	| The outer identifier of the category to which the product belongs.                           	|
| `brandName` {==String==}                                                 	| The brand name associated with the product.                                                  	|
| `masterVariation` [{==VariationType==}](VariationType.md)                	| The main variation of the product.                                                           	|
| `variations` [{==VariationType==}](VariationType.md)                     	| A list of variations available for the product.                                              	|
| `hasVariations` {==Boolean==}                                           	| Indicates whether the product has variations or not.                                         	|
| `availabilityData` [{==AvailabilityData==}](AvailabilityData.md)        	| Information about the availability of the product.                                           	|
| `images` [{==ImageType==}](ImageType.md)                                	| A list of images associated with the product.                                                	|
| `price` [{==PriceType==}](Price/PriceType.md)                            | The price of the product.                                                                    	|
| `prices` [{==PriceType==}](Price/PriceType.md)         	                | A list of prices associated with the product.                                                	|
| `properties(...)` [{==Property==}](Property/Property.md)                	| A list of properties or attributes associated with the product.                              	|
| `keyProperties(...)` [{==Property==}](Property/Property.md)              | A list of key properties associated with the product. The `keyProperties` field can be limited by the `take` argument.        	|
| `assets` [{==Asset==}](Asset.md)                                         	| A list of assets associated with the product.                                               	|
| `outlines` [{==OutlineType==}](OutlineType.md)                           	| A list of category outlines for the product.                                                 	|
| `breadcrumbs` [{==Breadcrumb==}](Breadcrumb.md)                           	| Product navigation information in the form of breadcrumbs.                                  |
| `vendor` [{==CommonVendor==}](CommonVendor/Commonvendor.md)            	| The vendor associated with the product.                                                       |
| `inWishlist` {==Boolean!==}                            	                  | Indicates whether the product is in the user's wishlist or not.                               |
| `associations(...)` [{==ProductAssociationConnection==}](ProductAssociation/ProductAssociationConnection.md) 	| The associations or relationships of the product with other products. This field is resolved using the object.  	|
| `videos(...)` [{==VideoConnection==}](VideoConnection/VideoConnection.md)| The videos associated with the product.                                                      	|

## Examples

<hr />
=== "Query"
    ```json
    query {
      products(
        storeId: "B2B-store"
        cultureName: "en-US"
      ) {
        items 
        {
          keyProperties (take:3) {
            name
            value
            label
            displayOrder
            propertyDictItems
            {
              pageInfo
              {
                endCursor
                hasNextPage
                hasPreviousPage
              }
              totalCount
              items
              {
                sortOrder
                __typename
                value
              }
            }
            id
            type
          }
        }
      }
    }
    ```

=== "Return"
    ```json
>>>>>>> Stashed changes
    {
      keyProperties (take:3) {
        name
        value
      }
    }
<<<<<<< Updated upstream
  }
}
```
=======
    ```



## Configuring `keyProperties`
To make a catalog property appear in the `keyProperties` list:

  1. Open the platform and go to the **Catalog** module.
  1. Click the three dots next the name of the required catalog and select **Manage** from the dropdown menu.
  1. Selects the **Properties** widget.
  1. In the new blade, select the **Product property** from a list.
  1. In the **Manage property** blade select **Attributes**.
  1. Add the **KeyProperty** attribute to **Current attributes**.`KeyProperties` are automatically sorted in ascending order based on the attribute value.
    ![KeyProperties](../objects/media/KeyPropertiesAttr.png)
>>>>>>> Stashed changes
