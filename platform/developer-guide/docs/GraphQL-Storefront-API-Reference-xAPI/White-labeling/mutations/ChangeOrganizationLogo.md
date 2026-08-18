# changeOrganizationLogo ==~mutation~==  

This mutation updates the logo for a specific organization.  

## Arguments  

The `InputChangeOrganizationLogoCommandType` represents the input data required to change an organization's logo.  

| Field                        | Description                                             |
|------------------------------|---------------------------------------------------------|
| `organizationId` ==String!== | The Id of the organization whose logo is being updated. |
| `logoUrl` ==String==         | The URL of the new logo image.                          |

## Possible returns  

| Possible return                    | Description                                              |
|------------------------------------|----------------------------------------------------------|
| [ChangeOrganizationLogoResultType](../objects/ChangeOrganizationLogoResultType.md) | The result of the logo update, including status details. |

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: InputChangeOrganizationLogoCommandType!) {  
  changeOrganizationLogo(command: $command) {  
    isSuccess
    errorMessage
  }  
}  
```

```json title="Variables"
{  
  "command": {  
    "organizationId": "d690f3df-8782-4dcc-99be-a1f644220e50",  
    "logoUrl": "/api/files/a42162a18d1c4a309516dc9777221c0d"  
  }  
}  
```

</div>