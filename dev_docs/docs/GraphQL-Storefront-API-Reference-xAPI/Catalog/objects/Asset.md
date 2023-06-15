# Asset ==~object~==

The `assetType` object represents an asset. It can be an image, video, document, or any other type of file associated with products, variations, categories, or other entities. 

## Fields

| Field                    	| Description                                                                                            	|
|--------------------------	|--------------------------------------------------------------------------------------------------------	|
| `id` {==String==}          	| The unique identifier of the asset.                                                                    	|
| `name` {==String==}        	| The name or title of the asset.                                                                        	|
| `mimeType` {==String==}    	|  The MIME type of the asset, indicating its file format.                                               	|
| `size` {==Long==}          	|  The size of the asset file in bytes.                                                                  	|
| `url` {==String==}         	| The URL or web address where the asset can be accessed or downloaded.                                  	|
| `relativeUrl` {==String==} 	| The relative URL path of the asset, typically used in relation to the website or application's domain. 	|
| `typeId` {==String==}      	| The unique identifier of the asset type.                                                               	|
| `group` {==String==}       	| The grouping or category to which the asset belongs.                                                   	|
| `cultureName` {==String==} 	| The language associated with the asset, indicating the intended audience or localization.              	|

