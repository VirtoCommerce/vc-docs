# AvailabilityData ==~object~==

This type refers to the information related to the availability and inventory status of a product or variation. 

## Fields

| Field                                	| Description                                                                          	|
|------------------------------------	|--------------------------------------------------------------------------------------	|
| `availableQuantity`  ==Long!==    	| The quantity of product or variation that is currently available for purchase.       	|
| `isBuyable`  ==Boolean==          	| Indicates whether the product or variation is available for purchase.               	|
| `isAvailable`  ==Boolean==        	| Indicates whether the product or variation is available for selection.            	|
| `isInStock`  ==Boolean==          	| Indicates whether the product or variation is currently in stock.                  	|
| `isActive`  ==Boolean==           	| Indicates whether the product or variation is active.                              	|
| `isTrackInventory`  ==Boolean==   	| Indicates whether the inventory of the product or variation is being tracked.      	|
| `inventories` [ ==InventoryInfo== ](InventoryInfo.md)    | The inventory information associated with the product or variation.|

![Readmore](media/readmore.png){: width="25"} [Managing Product Availability](../../../../../user-guide/catalog/setting-product-availability)

