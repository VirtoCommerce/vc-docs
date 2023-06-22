# Cart ==~query~==

This query allows you to retrieve information about a shopping cart. 

## Arguments

| Argument                       | Description                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------|
| `storeId` {==String!==}        | A standardized code of a specific currency.                                                     |
| `userId`  {==String==}         | The ID of the store to retrieve pages from.                                                     |
| `currencyCode` {==String!==}   | A standardized code of a specific currency.                                                     |
| `cultureName` {==String==}     | The language to retrieve data in.                                                               |
| `cartName` {==String==}        | The name or the identifier of the cart.                                                         |
| `cartType` {==String==}        | The type of cart being queried.                                                                 |

## Possible returns

| Possible return                                         	| Description                                                              	|
|---------------------------------------------------------	|------------------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                     |  Defines the properties and fields associated with a shopping cart.    	|

## Examples

=== "Query"
    ```json linenums="1"
    {
        cart (storeId: "Electronics"
            cartName: "default"
            userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
            cultureName: "en-Us"
            currencyCode: "USD"
            cartType: "cart")
        {
            id
            name
            hasPhysicalProducts
            status
            storeId
            isAnonymous
            comment
            taxPercentRate
            taxType
            addresses { countryName regionName city addressType }
            dynamicProperties { name value valueType }
            shipments { shipmentMethodCode shipmentMethodOption }
            availableShippingMethods { code optionName optionDescription }
            discounts { amount description }
            currency { code symbol }
            payments { paymentGatewayCode }
            availablePaymentMethods { code paymentMethodType }
            items { id sku }
            coupons { code isAppliedSuccessfully }
            itemsCount
            itemsQuantity
            type
        }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
    "data": {
        "cart": {
        "id": "5abc76d6-02ca-4a5b-af5f-92088a631f4c",
        "name": "default",
        "hasPhysicalProducts": false,
        "status": null,
        "storeId": "Electronics",
        "isAnonymous": true,
        "comment": null,
        "taxPercentRate": 0,
        "taxType": null,
        "addresses": [],
        "dynamicProperties": [],
        "shipments": [],
        "availableShippingMethods": [
            {
            "code": "FixedRate",
            "optionName": "Ground",
            "optionDescription": null
            },
            {
            "code": "FixedRate",
            "optionName": "Air",
            "optionDescription": null
            }
        ],
        "discounts": null,
        "currency": {
            "code": "USD",
            "symbol": "$"
        },
        "payments": [],
        "availablePaymentMethods": [
            {
            "code": "DefaultManualPaymentMethod",
            "paymentMethodType": "Unknown"
            }
        ],
        "items": [],
        "coupons": [],
        "itemsCount": 0,
        "itemsQuantity": 0,
        "type": "cart"
        }
    }
    }
    ```
