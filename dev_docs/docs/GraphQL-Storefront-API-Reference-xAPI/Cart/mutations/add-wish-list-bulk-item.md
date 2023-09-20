# addWishListBulkItem ==~mutation~==

This mutation adds products to various wish lists.

## Arguments

The `InputAddWishlistBulkItemType` is an input object type used for adding multiple items to one or more wishlists. 

| Field                       | Description                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| `listIds` {==[String]==}    | An array of wishlist Ids to which the items will be added.                                        |
| `productId` {==String==}    | The Id of the product to be added to the wishlists.                                               |
| `quantity` {==Int==}        | The quantity of the product to be added. This field is optional and can be omitted if not needed. |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`BulWishListType`]()                                    	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation addWishlistBulkItem ($command: InputAddWishlistBulkItemType!) {
      addWishlistBulkItem (command: $command) {    
        wishlists {          
          name
          id
          items {
            id
            quantity
            product {
              name
            }
          }
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
      "listIds": ["ce682f58-3bbd-42e5-a576-08c82a86ca11", "1b249c7a-5b7b-434d-a9b5-56a67ff993fe"],
      "productId" : "92e671024a8648de97dedcd488f58455"
    }
    ```