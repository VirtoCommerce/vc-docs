# Product ==~query~==

This query allows you to get a product by its Id and calculate all fields based on the parameters being sent. 

## Arguments

| Argument                  	| Description                     	                    |
|---------------------------	|-----------------------------------------------------	|
| `id`  ==String!==           	| The product Id.                                     	|
| `storeId`  ==String!==      	| The Id of the store to retrieve pages from.         	|
| `userId`  ==String==        	| The current user Id.                	                |
| `currencyCode`  ==String==  	| A standardized code of a specific currency.           |
| `cultureName`  ==String==   	| A language to retrieve data in. 	                |

## Possible return

| Possible return                                          	| Description                           	|
|---------------------------------------------------------	|---------------------------------------	|
| [`ProductType`](../objects/ProductType.md)            	|  The type or category of the product.  	|

## Examples


=== "Example 1"
    <div class="grid" markdown>

    ```json title="Query 1"
    {
      product(
        id: "2dcd49147dc04892892af26bb91e5530"
        storeId: "B2B-Store"
        cultureName: "en-us"
        currencyCode: "USD"
      ) {
        id
        name
      }
    }
    ```

    ```json title="Return 1"
    {
      "data": {
        "product": {
          "id": "2dcd49147dc04892892af26bb91e5530",
          "name": "Eye Bolt,Carbon Steel 4.6,M6x70,PK25"
        }
      }
    }
    ```

    </div>

=== "Example 2"

    <div class="grid" markdown>

    ```json title="Query 2"
    {
      product(
        id: "2dcd49147dc04892892af26bb91e5530"
        storeId: "B2B-store"
        currencyCode: "USD"
      ) {
        images {
          id
          name
          group
        }
        prices {
          minQuantity
          tierPrices {
            quantity
            price {
              amount
            }
          }
        }
      }
    }
    ```

    ```json title="Return 2"
    {
      "data": {
        "product": {
          "images": [
            {
              "id": "3aba9278b27442489c13848cc0d12f7d",
              "name": "5ZA21_AS01.jpg",
              "group": "images"
            }
          ],
          "prices": [
            {
              "minQuantity": 1,
              "tierPrices": [
                {
                  "quantity": 1,
                  "price": {
                    "amount": 57.25
                  }
                }
              ]
            }
          ]
        }
      }
    }
    ```

    </div>