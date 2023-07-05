# InventoryInfo ==~object~==

The `InventoryInfo` provides essential data for tracking and managing inventory levels and ensuring accurate stock availability for customers.

## Fields

| Field                                     	| Description                                                                           	|
|-------------------------------------------	|---------------------------------------------------------------------------------------	|
| `inStockQuantity` {==Long==}               	| The quantity of the item that is currently in stock and available for sale.           	|
| `reservedQuantity` {==Long==}              	| The quantity of the item that has been reserved or allocated for pending orders.      	|
| `fullfillmentCenterId` {==String!==}       	| The unique identifier of the fulfillment center where the item is stored or managed. 	    |
| `fullfillmentCenterName` {==String!==}     	| The name of the fulfillment center where the item is stored or managed.                  	|
| `allowPreorder` {==Boolean==}              	| Indicates whether preordering of the item is allowed.                                 	|
| `allowBackorder` {==Boolean==}             	| Indicates whether backordering of the item is allowed.                                	|
| `preorderAvailabilityDate` {==DateTime==}  	| The date and time when the item will be available for preorder, if applicable.        	|
| `backorderAvailabilityDate` {==DateTime==} 	| The date and time when the item will be available for backorder, if applicable.       	|
