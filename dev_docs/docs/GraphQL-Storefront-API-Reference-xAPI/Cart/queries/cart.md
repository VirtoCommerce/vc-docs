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
    cart(
        storeId: "B2B-Store"
        cartName: "default"
        userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
        cultureName: "en-Us"
        currencyCode: "USD"
        cartType: "cart"
    ) {
        id
        name
        hasPhysicalProducts
        status
        storeId
        isAnonymous
        comment
        taxPercentRate
        taxType
        addresses {
        countryName
        regionName
        city
        addressType
        }
        dynamicProperties {
        name
        value
        valueType
        }
        shipments {
        shipmentMethodCode
        shipmentMethodOption
        }
        availableShippingMethods {
        code
        optionName
        optionDescription
        }
        discounts {
        amount
        description
        }
        currency {
        code
        symbol
        }
        payments {
        paymentGatewayCode
        }
        availablePaymentMethods {
        code
        paymentMethodType
        }
        items {
        id
        sku
        }
        coupons {
        code
        isAppliedSuccessfully
        }
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
        "id": "6255f029-d3d9-41ea-9643-a1f99c29c534",
        "name": "default",
        "hasPhysicalProducts": false,
        "status": null,
        "storeId": "B2B-Store",
        "isAnonymous": true,
        "comment": null,
        "taxPercentRate": 0,
        "taxType": null,
        "addresses": [],
        "dynamicProperties": [
            {
            "name": "CartModule_ShoppingCart_Boolean_0_0_0",
            "value": null,
            "valueType": "Boolean"
            },
            {
            "name": "CartModule_ShoppingCart_DateTime_0_0_0",
            "value": null,
            "valueType": "DateTime"
            },
            {
            "name": "CartModule_ShoppingCart_Decimal_0_0_0",
            "value": null,
            "valueType": "Decimal"
            },
            {
            "name": "CartModule_ShoppingCart_Decimal_1_0_0",
            "value": null,
            "valueType": "Decimal"
            },
            {
            "name": "CartModule_ShoppingCart_Html_0_0_0",
            "value": null,
            "valueType": "Html"
            },
            {
            "name": "CartModule_ShoppingCart_Html_0_1_0",
            "value": null,
            "valueType": "Html"
            },
            {
            "name": "CartModule_ShoppingCart_Image_0_0_0",
            "value": null,
            "valueType": "Image"
            },
        ],
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
            "code": "AuthorizeNetPaymentMethod",
            "paymentMethodType": "PreparedForm"
            },
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
