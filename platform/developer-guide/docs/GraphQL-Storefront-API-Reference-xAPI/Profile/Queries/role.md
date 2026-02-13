# Role ==~query~==

This connection allows you to get role by its name.

## Arguments

| Argument                           	| Description                                                                                              	|
|------------------------------------	|----------------------------------------------------------------------------------------------------------	|
| `roleName` ==String!==           	  | The name of the role                                                                                     	|

## Possible returns

| Possible return                                                       	| Description                           	|
|-----------------------------------------------------------------------	|---------------------------------------	|
| [`RoleType`](../Objects/RoleType.md)     	                              | The role's information and attributes.	|

## Example

<div class="grid" markdown>

```json title="Query"
{
  role(roleName: "Store administrator") {
    id
    name
    permissions
  }
}
```

```json title="Return"
{
  "data": {
    "role": {
      "id": "store-admin",
      "name": "Store administrator",
      "permissions": [
        "storefront:user:view",
        "storefront:user:create",
        "storefront:organization:view",
        "storefront:user:delete",
        "storefront:organization:edit",
        "storefront:user:edit",
        "storefront:user:invite",
        "storefront:order:view",
        "storefront:order:changestatus"
      ]
    }
  }
}
```

</div>