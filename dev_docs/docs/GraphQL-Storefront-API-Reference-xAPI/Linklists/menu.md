# Menu

| Endpoint 	| Arguments                                                           	| Return                                       	|
|----------	|---------------------------------------------------------------------	|----------------------------------------------	|
| `menu`   	| `storeId`<br>`cultureName`<br>`name`    	| Specific menu page.                          	|

## Example

<hr />
=== "Query"

    In this query, you're requesting information from the `Bolts` menu in the B2B-store. You're interested in retrieving the URLs and titles of the menu items within that menu.

    ```
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

    The example return shows four menu items with their respective URLs and titles: `Freight car bolts`, `Carriage bolts`, `Eyebolts`, and `Flange Bolts`.

    ```
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