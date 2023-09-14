# createQuoteFromCart ==~mutation~==

This mutation creates a quote request from a particular cart.

## Arguments

The `CreateQuoteFromCartCommandType!` represents the arguments for `CreateQuoteFromCart`. 

| Field                     | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| `cartId` {==String!==}    | The Id of the cart from which the quote will be created. |
| `comment` {==String!==}   | A comment for the newly created quote.                   |


## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command: CreateQuoteFromCartCommandType!){
      createQuoteFromCart(command: $command)
          {
        id
        number
        status
        comment
            items{
              productId
              name
              sku
              listPrice{
                amount
              }
              salePrice{
                amount
              }
              selectedTierPrice{
                quantity
                price{
                  amount
                }
              }
          }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {"command": 
      {"cartId": "d34cae74-e863-4a93-a20d-845472b85037",
        "comment": "Sample comment"
      }
    }
    ```

