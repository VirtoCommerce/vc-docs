# AddWishListBulkItem

This mutation adds products to various wish lists.

## Query

```json
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

## Variables

```json
"command": {
   "listIds": ["ce682f58-3bbd-42e5-a576-08c82a86ca11", "1b249c7a-5b7b-434d-a9b5-56a67ff993fe"],
   "productId" : "92e671024a8648de97dedcd488f58455"
}
```