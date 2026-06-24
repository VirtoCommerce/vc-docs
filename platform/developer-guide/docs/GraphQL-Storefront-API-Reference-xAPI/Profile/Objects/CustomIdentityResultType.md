# CustomIdentityResultType ==~object~==

This type provides feedback on the outcome of identity-related operations. 

## Fields

| Field                                                             | Description                                                                                                                |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `succeeded`  ==Boolean!==                                         | Indicates whether the identity operation succeeded.                                                                        |
| `errors` [ ==IdentityErrorInfoType== ](IdentityErrorInfoType.md)  | An array of `IdentityErrorInfoType` objects that provide details<br>about any errors encountered during the identity operation. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../InputApplicationUserLoginType">← InputApplicationUserLoginType</a>
    <a href="../IdentityResultType">IdentityResultType →</a>
</div>
