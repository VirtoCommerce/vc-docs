# OrganizationType ==~object~==

The `OrganizationType` contains various fields providing information about the organization.

## Fields

| Field                                                                                               	| Description                                               |
|----------------------------------------------------------------------------------------------------	|-----------------------------------------------------------|
| `id` {==String!==}                                    	                                            | The Id of the organization.                               |
| `outerId` {==String==}                                                                                | The external Id of the organization.                      |
| `memberType` {==String!==}         	                                                                | The type of the organization.                             |
| `name` {==String==}                                	                                                | The name of the organization.                            	|
| `status` {==String==}     	                                                                        | The status of the organization.                       	|
| `phones` {==[String]!==} 	                                                                            | The phone numbers associated with the organization.      	|
| `emails` {==[String]!==}        	                                                                    | The email addresses associated with the organization. 	|
| `groups` {==[String]!==}                                	                                            | The groups to which the organization belongs.             |
| `seeObjectType` {==String!==}            	                                                            | The type of object that the organization is associated with. |
| `seoInfo(...)` [{==SeoInfo==}](../../Catalog/objects/SeoInfo.md)                              	    | Request related SEO info.                               	|
| `defaultBillingAddress` [{==MemberAddressType==}](MemberAddressType.md)                               | The default billing address of the organization.        	|
| `defaultShippingAddress` [{==MemberAddressType==}](MemberAddressType.md)        	                    | The default shipping address of the organization.       	|
| `addresses(...)` [{==MemberAddressConnection==}](MemberAddressConnection.md)     	                    | A connection to a list of addresses associated with the organization. 	|
| `DynamicProperties(...)` [{==DynamicPropertyValueType==}](../../Cart/objects/dynamic-property-value-type.md) |   The dynamic properties of the organization.      |
| `description` {==String==}                                                    	                    | The description of the organization.                  	|
| `BusinessCategory` {==String==}                                                                     	| The business category of the organization.            	|
| `ownerId` {==String==}                                                                            	| The ID of the owner of the organization.               	|
| `parentId` {==String==}                                                                            	| The ID of the parent organization, if applicable.      	|
| `contacts(...)` [{==ContactConnection==}](ContactConnection.md)                                      	| A connection to a list of contacts associated with the organization.	|

