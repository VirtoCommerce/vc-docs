# CategoryType ==~object~==

The `CategoryType` is used to differentiate or group different types of categories.

## Fields

| Field                                                                          	| Description                                                                     	|
|--------------------------------------------------------------------------------	|---------------------------------------------------------------------------------	|
| `id` {==String!==}                                                               	| The Id of the category.                                                         	|
| `imgSrc` {==String==}                                                         	| The category image.                                                             	|
| `code` {==String!==}                                                          	| The SKU of the category.                                                        	|
| `name` {==String!==}                                                       	    | The name of the category.                                                       	|
| `level` {==Int==}                                                                	| Level in the hierarchy.                                                         	|
| `priority` {==Int!==}                                                            	| The priority of the category in relation to other categories.                   	|
| `outline` {==String==}                                                           	| The hierarchical outline of the category.                                       	|
| `slug` {==String==}                                                              	| The URL slug of the category.                                                   	|
| `path` {==String==}                                                            	| The full path of the category within the category hierarchy.                    	|
| `seoInfo` [{==SeoInfo==}](../SeoInfo.md)                                      	| Request related SEO info.                                                       	|
| `descriptions`(...) [{==CategoryDescriptionType==}](CategoryDescriptionType.md)	|  Additional descriptions for the category in different languages.               	|
| `description`(...) [{==CategoryDescriptionType==}](CategoryDescriptionType.md)	| The description of the category in a specific language.                         	|
| `parent` [{==Category==}](/CategoryType.md)                                    	| The parent category of the current category.                                    	|
| `hasParent` {==Boolean==}                                                     	| Indicates whether the category has a parent category.                           	|
| `outlines` [{==OutlineType==}](../OutlineType.md)                              	| The hierarchical outlines of the category and its ancestors.                    	|
| `images` [{==ImageType==}](../ImageType.md)                                    	| The images associated with the category.                                        	|
| `breadcrumbs` [{==Breadcrumb==}](../Breadcrumb.md)                    	        | The breadcrumbs representing the category's position in the category hierarchy. 	|
| `properties(...)` [{==Property==}](../Property/Property.md)                      	| The properties associated with the category.                                    	|
| `childCategories` [{==Category==}](CategoryType.md)                              	| The child categories of the current category.                                   	|


[Read more about managing categories](https://docs.virtocommerce.org/new/user_docs/catalog/managing-categories/){ .md-button }
