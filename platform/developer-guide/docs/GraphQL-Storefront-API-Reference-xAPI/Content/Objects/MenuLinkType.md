# MenuLinkType ==~object~==

The `MenuLinkType` represents a menu link within a menu. It defines the properties and characteristics of a single menu link.

## Fields

| Field                                 | Description                                                            |
|---------------------------------------|------------------------------------------------------------------------|
| `title` {==String==}                  | The title of the menu link.                                            |
| `url` {==String==}                    | The URL associated with the menu link.                                 |
| `priority` {==Int==}                  | The priority or order of the menu link within the menu.                |
| `associatedObjectId` {==String==}     | The Id of the object associated with the menu link.                    |
| `associatedObjectName` {==String==}   | The name of the associated object.                                     |
| `associatedObjectType` {==String==}   | The type of the associated object.                                     |
| `outerId` {==String==}                | The external Id of the menu link.                                      |
| `childItems` [{==MenuLinkType==}]     | An array of child `MenuLinkType` objects.<br>Each object represents a nested menu link, allowing for the creation of hierarchical menus.                     |

