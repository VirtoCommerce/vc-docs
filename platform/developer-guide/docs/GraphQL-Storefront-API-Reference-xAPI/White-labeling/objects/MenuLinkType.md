# MenuLinkType ==~object~==

This type defines the structure of a menu link item.

## Fields

| Field                             | Description                                                                  |
|-----------------------------------|------------------------------------------------------------------------------|
| `title` ==String!==               | The title of the menu item displayed to users.                               |
| `url` ==String!==                 | The URL associated with the menu item.                                       |
| `priority` ==Int!==               | The priority of the menu item, which determines its order in the menu.       |
| `associatedObjectId` ==String==   | The Id of the object linked to this menu item.                |
| `associatedObjectName` ==String== | The name of the object linked to this menu item.                             |
| `associatedObjectType` ==String== | The type of object linked to this menu item (e.g., category, page, product). |
| `outerId` ==String==              | An external identifier for the menu item, used for integrations.             |
| `childItems` ==[MenuLinkType!]!== | A list of submenu items, each represented by a **MenuLinkType** object.      |

