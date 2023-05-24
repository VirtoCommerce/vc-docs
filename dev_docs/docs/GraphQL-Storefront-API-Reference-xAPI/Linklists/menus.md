# Menus

| Endpoint 	| Arguments                                                           	| Return                                       	|
|----------	|---------------------------------------------------------------------	|----------------------------------------------	|
| `menus`  	| `storeId`<br>`cultureName`<br>`keyword` 	| Several menu pages according to the keyword. 	|

## Example

<hr />
=== "Query"

    The query is requesting information about menus in the specified Virto Commerce store, including their names, unique identifiers, and associated menu items with their respective URLs, titles, priorities, and associations with other objects.

    ```
    query {
      menus(
        storeId:"B2B-store"
        cultureName:"en-US"
      )
      {
        name
        outerId
        items{
          url
          title
          outerId
          priority
          associatedObjectId
          associatedObjectName
          associatedObjectType
        }
      }
    }
    ```

=== "Return"

    The return represents the retrieved menus and their associated menu items. Each menu item is described by properties such as URL, title, priority, and associated object information. The example return includes information about multiple menus, their names, menu items, and associated objects (if any)

    ```
    {
      "data": {
        "menus": [
          {
            "name": "catalog-menu",
            "outerId": null,
            "items": [
              {
                "url": "/bolts",
                "title": "Bolts",
                "outerId": null,
                "priority": 20,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/printers",
                "title": "Printers",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
          {
            "name": "main-menu-section1",
            "outerId": null,
            "items": [
              {
                "url": "~/test",
                "title": "Test",
                "outerId": null,
                "priority": 0,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
          {
            "name": "Printers",
            "outerId": null,
            "items": [
              {
                "url": "/printers/all-in-one",
                "title": "Inject printers",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/printers/multifunction-printers",
                "title": "Laser printers",
                "outerId": null,
                "priority": 0,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
          {
            "name": "Bolts",
            "outerId": null,
            "items": [
              {
                "url": "/bolts/freight-car-bolts",
                "title": "Freight car bolts",
                "outerId": null,
                "priority": 30,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/carriage-bolts",
                "title": "Carriage bolts",
                "outerId": null,
                "priority": 20,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/eyebolts",
                "title": "Eyebolts",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "/bolts/flange-bolts",
                "title": "Flange Bolts",
                "outerId": null,
                "priority": 0,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          },
          {
            "name": "main-menu",
            "outerId": null,
            "items": [
              {
                "url": "~/bolts",
                "title": "General Catalogue",
                "outerId": null,
                "priority": 30,
                "associatedObjectId": "02fe37dcaeb2458a831011abe43fd335",
                "associatedObjectName": "Bolts",
                "associatedObjectType": "category"
              },
              {
                "url": "~/printers",
                "title": "Find a Branch",
                "outerId": null,
                "priority": 20,
                "associatedObjectId": "d6019d4d27e44854a58ebbd5428b873b",
                "associatedObjectName": "Printers",
                "associatedObjectType": "category"
              },
              {
                "url": "~/",
                "title": "Contact Us",
                "outerId": null,
                "priority": 10,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              },
              {
                "url": "~/",
                "title": "main-menu-section1",
                "outerId": null,
                "priority": 0,
                "associatedObjectId": null,
                "associatedObjectName": null,
                "associatedObjectType": null
              }
            ]
          }
        ]
      }
    }    
    ```
