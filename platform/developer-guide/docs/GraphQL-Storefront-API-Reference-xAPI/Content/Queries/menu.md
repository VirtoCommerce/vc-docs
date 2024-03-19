# Menu ==~query~==

This query is used to retrieve a specific menu based on the provided criteria.

## Arguments

| Argument                | Description                                                 |
|-------------------------|-------------------------------------------------------------|
| `storeId` ==String!==   | The Id of the store for which to retrieve the menu.         |
| `cultureName` ==String==| A language to retrieve data in.                             |
| `name` ==String!==      | The name of the menu to retrieve.                           |


## Possible returns

| Possible return                                          	| Description             	|
|---------------------------------------------------------	|--------------------------	|
| [`MenuLinkListType`](../Objects/MenuLinkListType.md)      |  A list of menu links.   	|

## Examples

=== "Query"

    ```json linenums="1"
    {
      menu(
        storeId: "B2B-store"
        cultureName: "en-US"
        name: "Bolts"
      ) {
        items {
          url
          title
        }
      }
    }
    ```


=== "Return"

    ```json linenums="1"
    "data": {
        "menu": { 
            "items": [ 
                { 
                  "url": "/bolts/freight-car-bolts", 
                  "title": "Freight car bolts" 
                }, 
                { 
                  "url": "/bolts/carriage-bolts", 
                  "title": "Carriage bolts" 
                }, 
                { 
                  "url": "/bolts/eyebolts", 
                  "title": "Eyebolts" 
                }, 
                { 
                  "url": "/bolts/flange-bolts", 
                  "title": "Flange Bolts" 
                } 
            ] 
        } 
    } 
    ```