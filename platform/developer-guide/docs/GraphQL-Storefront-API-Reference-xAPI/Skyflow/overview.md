# Skyflow

The **Skyflow** module provides secure management of payment card data and related operations:

* Retrieves stored Skyflow cards for users and stores.
* Deletes Skyflow cards safely while maintaining PCI compliance.

| Queries                                         | Objects                      	| Mutations                                                               	|
|-------------------------------------------------|------------------------------	|--------------------------------------------------------------------------	|
| [skyflowCards](queries/skyflowCards.md)      | [SkyflowCardResponseType](objects/SkyflowCardResponseType.md) <br> [SkyflowCardType](objects/SkyflowCardType.md) <br> [DeleteSkyflowCardCommandType](objects/DeleteSkyflowCardCommandType.md)| <br> [deleteSkyflowCard](mutations/deleteSkyflowCard.md) |

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-skyflow/releases)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-skyflow/releases/latest)