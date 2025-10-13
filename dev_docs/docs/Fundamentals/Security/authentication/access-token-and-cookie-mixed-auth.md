
Along with JWT access token, Virto manager also uses cookie-based authentication. This additional check is necessary because it is impossible to intercept and inject Authorization header with the token bearer for all API calls requested other than through the [$http](https://docs.angularjs.org/api/ng/service/%24http) service. These calls can be produced by other third-party JS components; direct http links and cookie-based authorization are used to solve this problem.

When the user is authorized in the platform, the system intersects all user permissions with the permissions in the `Authorization:LimitedCookiePermissions` configuration section <!---Add link to this section in Configuration reference--> and adds them into cookies along with issuing the JWT token. When the user makes a request to the platform, they are challenged against the helper cookie and the authentication token in accordance with the following rules:

| Received with Request | JWT Token | Cookies | JWT Token + Cookies |
|--|--|--|--|
| Used for authentication | Token | Cookie | Cookies |

You can configure which permissions can be stored in `limited_permissions` cookies by changing the `Authorization: LimitedCookiePermissions` setting:

```json title="VirtoCommerce.Platform.Web/appsetings.json"
 "Authorization": {
        ...
        "LimitedCookiePermissions": "platform:asset:read;platform:export;content:read;platform:asset:create;licensing:issue;export:download"
        ...
    },
```
