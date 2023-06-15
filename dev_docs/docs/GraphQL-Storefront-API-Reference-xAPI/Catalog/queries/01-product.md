# Product

This query allows you to get a product by its ID and calculate all fields based on the parameters being sent.

<<<<<<< Updated upstream
## Definition

```
product(id: !string, storeId: !string, userId: !string, currencyCode: string, cultureName: string)
```

## Arguments

|#|Name        |Type           |Description                |
|-|------------|---------------|---------------------------|
|1|id          |Non null StringGraphType|Product of the Id          |
|2|storeId     |Non null StringGraphType|Store Id                   |
|3|userId      |Non null StringGraphType|Current user Id            |
|4|currencyCode|StringGraphType|Currency code (e.g. "USD") |
|5|cultureName |StringGraphType|Culture name (e.g. "en-US")|

## Example

```json
{
    product(
        id: "8b7b07c165924a879392f4f51a6f7ce0"
        storeId: "Electronics"
        userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
        cultureName: "en-us"
        currencyCode: "USD")
=======
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

<hr />
=== "Query 1"
    ```json
>>>>>>> Stashed changes
    {
        id
        name
<<<<<<< Updated upstream
    }
}
```

## Displaying Tier Pricing on Product Page

```json
query
{
  product(
        id:"9cbd8f316e254a679ba34a900fccb076" 
        storeId:"Electronics"
        currencyCode:"USD")
  {
    prices
=======
      }
    }  
    ```

=== "Return 1"
    ```json
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
  }
}
```
=======
    ```

=== "Query 2"
    ```json
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
    ```json
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
>>>>>>> Stashed changes
