# ProductAssociation ==~object~==

The `ProductAssociation` represents the association between products in queries.

## Fields

| Field                                                        	| Description                                                    	|
|-------------------------------------------------------------	|----------------------------------------------------------------	|
| `type`  ==String==                                          	| The type of the association between products.                  	|
| `priority`  ==Int==                                          	| The priority of the product association.                       	|
| `quantity`  ==Int==                                         	| The quantity or count associated with the product association. 	|
| `associatedObjectId`  ==String==                          	| The ID of the associated object.                               	|
| `associatedObjectType`  ==String==                        	| The type of the associated object.                             	|
| `tags`  ==String==                                          	| Tags or labels associated with the product association.        	|
| `product` [ ==Product== ](../ProductType.md)               	| The product object associated with the association.            	|
