# AvailabilityData ==~object~==

The `AvailabilityData` refers to the information related to the availability and inventory status of a product or variation. The `AvailabilityData` object provides details about the current stock availability, purchase eligibility, and inventory tracking status of a specific product or variation.

## Fields

| Field                                	| Description                                                                          	|
|------------------------------------	|--------------------------------------------------------------------------------------	|
| `availableQuantity` {==Long!==}   	| The quantity of product or variation that is currently available for purchase.       	|
| `isBuyable` {==Boolean==}         	| Indicates whether the product or variation is available for purchase or not.         	|
| `isAvailable` {==Boolean==}       	| Indicates whether the product or variation is available for selection or not.        	|
| `isInStock` {==Boolean==}         	| Indicates whether the product or variation is currently in stock or not.             	|
| `isActive` {==Boolean==}          	| Indicates whether the product or variation is active or not.                         	|
| `isTrackInventory` {==Boolean==}  	| Indicates whether the inventory of the product or variation is being tracked or not. 	|
| `inventories` [{==InventoryInfo==}](InventoryInfo.md) 	| The inventory information associated with the product or variation.                  	|


[Read more about managing product availability](https://docs.virtocommerce.org/new/user_docs/catalog/setting-product-availability/){ .md-button }

