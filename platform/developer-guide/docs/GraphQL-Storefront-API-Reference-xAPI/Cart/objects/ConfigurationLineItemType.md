# ConfigurationLineItemType ==~object~==  

This type represents a line item in a product configuration, detailing the associated product and pricing information.  

## Fields  

| Field                                                                     | Description                                                           |  
|---------------------------------------------------------------------------|-----------------------------------------------------------------------|  
| `id` ==String==                                                           | The Id of the configuration line item.                                |  
| `quantity` ==Int==                                                        | The quantity of the item in the configuration.                        |  
| `product` [ ==Product== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/queries/product)               | The product associated with this configuration line item.             |  
| `currency` [ ==CurrencyType!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/currency-type)    | The currency associated with the configuration item.                  |  
| `listPrice` [ ==MoneyType!== ](../objects/money-type.md)                  | The standard list price of the configuration item.                    |  
| `extendedPrice` [ ==MoneyType!== ](../objects/money-type.md)              | The extended price based on the quantity of the configuration item.   |  
| `salePrice` [ ==MoneyType!== ](../objects/money-type.md)                  | The sale price of the configuration item.                             |  
| `discountAmount` [ ==MoneyType!== ](../objects/money-type.md)             | The amount of any discount applied to the configuration item.         |  
