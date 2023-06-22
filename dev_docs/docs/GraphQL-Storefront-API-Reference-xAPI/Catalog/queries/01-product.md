# Product ==~query~==

This query allows you to get a product by its Id and calculate all fields based on the parameters being sent. 

## Arguments

| Argument                  	| Description                     	|
|---------------------------	|---------------------------------	|
| `id` {==String!==}          	| Product Id.                     	|
| `storeId` {==String!==}     	| Store Id.                       	|
| `userId` {==String==}       	| Current user Id.                	|
| `currencyCode` {==String==} 	| A code of a specific currency.  	|
| `cultureName` {==String==}  	| A language to retrieve data in. 	|

## Possible returns

| Possible return                                          	| Description                           	|
|---------------------------------------------------------	|---------------------------------------	|
| [`ProductType`](../objects/01-ProductType.md)            	|  The type or category of the product.  	|

## Examples

=== "Query 1"
    ```json linenums="1"
    {
      product(
          id: "8b7b07c165924a879392f4f51a6f7ce0"
          storeId: "Electronics"
          userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
          cultureName: "en-us"
          currencyCode: "USD")
      {
        id
        name
      }
    }  
    ```

=== "Return 1"
    ```json linenums="1"
    {
      "data": {
        "product": {
          "id": "8b7b07c165924a879392f4f51a6f7ce0",
          "name": "ASUS ZenFone 2 ZE551ML 16GB Smartphone"
        }
      }
    }
    ```

=== "Query 2"
    ```json linenums="1"
    {
        product(
                id:"9cbd8f316e254a679ba34a900fccb076" 
                storeId:"Electronics"
                currencyCode:"USD")
        {
            prices
            {
            minQuantity
            tierPrices
            {
                quantity
                price
            {
                amount
            }
            }
            }
        }
        }
    ```

=== "Return 2"
    ```json linenums="1"
        {
        "data": {
            "product": {
            "prices": [
                {
                "minQuantity": 1,
                "tierPrices": [
                    {
                    "quantity": 1,
                    "price": {
                        "amount": 995.99
                    }
                    }
                ]
                }
            ]
            }
        }
        }
    ```
