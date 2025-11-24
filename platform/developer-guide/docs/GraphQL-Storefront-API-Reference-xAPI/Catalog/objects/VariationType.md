# VariationType ==~object~==

This type is used to differentiate or group different types of product variations.

## Fields

| Field                                                                    	| Description                                                   	|
|------------------------------------------------------------------------	|---------------------------------------------------------------	|
| `id`  ==String==                                                      	| The Id of the variation.                                      	|
| `name`  ==String==                                                       	| The name of the variation.                                    	|
| `code`  ==String==                                                    	| The SKU of the variation.                                     	|
| `productType`  ==String==                                             	| The type of the product associated with the variation.        	|
| `minQuantity`  ==Int==                                                  	| The minimum quantity allowed for the variation.               	|
| `maxQuantity`  ==Int==                                                 	| The maximum quantity allowed for the variation.               	|
| `availabilityData` [ ==availabilityData== ](AvailabilityData.md) 	        | The availability data for the variation.                      	|
| `images` [ ==ImageType== ](ImageType.md)                              	| The images associated with the variation.                     	|
| `price` [ ==PriceType== ](Price/PriceType.md)                            	| The price information for the variation.                      	|
| `prices` [ ==PriceType== ](Price/PriceType.md)                        	| The prices associated with the variation.                     	|
| `properties` [ ==Property== ](Property/Property.md)                     	| The properties associated with the variation.                 	|
| `assets` [ ==Asset== ](Asset.md)                                         	| The assets associated with the variation.                     	|
| `outlines` [ ==OutlineType== ](OutlineType.md)                        	| The hierarchical outlines of the variation.                   	|
| `slug`  ==String==                        	                            | The URL slug of the variation.                                	|
| `vendor` [ ==CommonVendor== ](CommonVendor/Commonvendor.md)              	| The vendor associated with the variation.                     	|


![Readmore](media/readmore.png){: width="25"} [Managing Product Variations](/platform/user-guide/latest/catalog/managing-product-variations)