# ContactType ==~object~==

This type represents a contact and includes various fields to describe the contact's information.

## Fields

| Field                                                                       	| Description                                                     	|
|----------------------------------------------------------------------------	|-----------------------------------------------------------------	|
| `id`  ==String==              	                                            | The Id of the contact.                                          	|
| `outerId`  ==String==         	                                            | The external Id of the contact.                                 	|
| `memberType`  ==String==      	                                            | The type of the contact.                                        	|
| `name`  ==String==            	                                            | The name of the contact.                                        	|
| `status`  ==String==          	                                            | The status of the contact.                                      	|
| `phones`  ==[String]==        	                                            | The phone numbers associated with the contact.                   	|
| `emails`  ==[String]==        	                                            | The email addresses associated with the contact.                 	|
| `groups`  ==[String]==        	                                            | The groups to which the contact belongs.                         	|
| `seoObjectType`  ==String==   	                                            | The type of object that the contact is associated with.          	|
| `seoInfo(...)` [ ==SeoInfo== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/SeoInfo)              | Request related SEO info.                                       	|
| `defaultBillingAddress` [ ==MemberAddressType== ](MemberAddressType.md)     	| The default billing address of the contact.                      	|
| `defaultShippingAddress` [ ==MemberAddressType== ](MemberAddressType.md)    	| The default shipping address of the contact.                     	|
| `addresses(...)` [ ==MemberAddressConnection== ](MemberAddressConnection.md)  | A connection to a list of addresses associated with the contact. 	|
| `dynamicProperties(...)` [ ==DynamicPropertyValueType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type)| The dynamic properties of the contact.|
| `firstName`  ==String==       	                                            | The first name of the contact.                                  	|
| `lastName`  ==String==                                                      	| The last name of the contact.                                   	|
| `middleName`  ==String==      	                                            | The middle name of the contact.                                 	|
| `fullName`  ==String==        	                                            | The full name of the contact.                                   	|
| `about`  ==String==           	                                            | Information about the contact.                                  	|
| `defaultLanguage`  ==String==                                                 | The default language of the contact.                              |
| `currencyCode`  ==String==                                                    | The preferred currency code of the contact.                       |
| `birthDate`  ==Date==         	                                            | The birth date of the contact.                                  	|
| `securityAccounts` [ ==UserType== ](UserType.md)                              | The security accounts associated with the contact.               	|
| `organizationId`  ==String==  	                                            | The Id of the organization associated with the contact.          	|
| `organizationsIds`  ==[String]!==                                             | The Ids of the organizations associated with the contact.        	|
| `organizations(...)` [ ==OrganizationConnection== ](OrganizationConnection.md)| A connection to a list of organizations associated with the contact.|

