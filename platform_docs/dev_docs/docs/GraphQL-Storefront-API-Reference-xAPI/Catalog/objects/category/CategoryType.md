# CategoryType ==~object~==

The `CategoryType` is used to differentiate or group different types of categories.

## Fields

| Field                                                                          	| Description                                                                     	|
|--------------------------------------------------------------------------------	|---------------------------------------------------------------------------------	|
| `id` {==String!==}                                                               	| The Id of the category.                                                         	|
| `imgSrc` {==String==}                                                         	| The URL or path to the main image of the category.                               	|
| `code` {==String!==}                                                          	| The SKU of the category.                                                        	|
| `name` {==String!==}                                                       	    | The name of the category.                                                       	|
| `level` {==Int==}                                                                	| The level in the hierarchy.                                                      	|
| `priority` {==Int!==}                                                            	| The priority of the category.                                                   	|
| `outline` {==String==}                                                           	| The hierarchical outline.                                       	|
| `slug` {==String==}                                                              	| The URL slug of the category.                                                   	|
| `path` {==String==}                                                            	| The full path of the category within the category hierarchy.                    	|
| `seoInfo` [{==SeoInfo==}](../SeoInfo.md)                                      	| Request related SEO info.                                                       	|
| `descriptions`(...) [{==CategoryDescriptionType==}](CategoryDescriptionType.md)	| Additional descriptions for the category.               	                        |
| `description`(...) [{==CategoryDescriptionType==}](CategoryDescriptionType.md)	| The description of the category.                         	                        |
| `parent` [{==Category==}](/CategoryType.md)                                    	| The parent category of the current category.                                    	|
| `hasParent` {==Boolean==}                                                     	| Indicates whether the category has a parent category.                           	|
| `outlines` [{==OutlineType==}](../OutlineType.md)                              	| A list of category outlines.                    	                                |
| `images` [{==ImageType==}](../ImageType.md)                                    	| The images associated with the category.                                        	|
| `breadcrumbs` [{==Breadcrumb==}](../Breadcrumb.md)                    	        | The breadcrumbs representing the category's position. 	|
| `properties(...)` [{==Property==}](../Property/Property.md)                      	| The properties associated with the category.                                    	|
| `childCategories` [{==Category==}](CategoryType.md)                              	| The child categories of the current category.                                   	|


[Read more about managing categories](https://docs.virtocommerce.org/new/user_docs/catalog/managing-categories/){ .md-button }
