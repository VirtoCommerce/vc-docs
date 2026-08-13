# Restrict Admin UI Access

By default, any signed-in account that holds at least one permission can enter the admin UI. The `PlatformUI.Access` configuration controls admin UI entry independently of the permissions an account holds. This lets you grant an account the permissions it needs to call protected API endpoints without letting it sign in to the admin panel.

A denied account is redirected to the **Contact admin for support** screen on sign in. It can still authenticate and call the API endpoints its permissions grant.

Configure access under the `PlatformUI.Access` node in **appsettings.json**, described in [PlatformUI](../../../Configuration-Reference/appsettingsjson.md#platformui):

{% include-markdown "../../../Configuration-Reference/appsettingsjson.md" start="<!--platformui-access-start-->" end="<!--platformui-access-end-->" %}

## Evaluation order

Access is evaluated in the following order, and the first matching rule decides the outcome:

1. If `AllowAdministrators` is `true` and the account is an administrator, allow.
1. If `AllowedAccountTypes` is not empty and the account's type is not listed, deny.
1. If any of the account's permissions match `DeniedPermissions`, deny.
1. If `AllowedPermissions` is not empty and none of the account's permissions match, deny.
1. If `RequireAnyPermission` is `true` and the account has no permissions, deny.
1. Otherwise, allow.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../scope-based-permissions">← Scope-based permissions </a>
    <a href="../../encryption-and-signing-credentials">Encryption and signing credentials →</a>
</div>
