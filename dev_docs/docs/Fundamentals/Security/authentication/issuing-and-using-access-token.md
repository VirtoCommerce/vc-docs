
The Virto Commerce OAuth 2.0 service provides the following authentication flows:

-   [**Client credentials**](https://oauth.net/2/grant-types/client-credentials/): Creates a token for an API client
    
-   [**Password flow**](https://oauth.net/2/grant-types/password): Creates a token through the user login credentials; used by operations scoped to a specific user session
    
-   [**Refresh token flow**](https://oauth.net/2/grant-types/refresh-token/): Refreshes an access token
    

## Resource Owner Password Credential Flow

To obtain an access token through the password flow, you need to provide the username and unencrypted password of the existing user. The returned access token can be used for consuming API resources on behalf of the user with all applied permissions to this user account.

```json
POST http://{platform_host}/connect/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=password&username=johndoe&password=A3ddj3w&scope=offline_access
```

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ0NjQ2...",
  "token_type": "Bearer",
  "expires_in": 1799,
  "refresh_token": "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6..."
}
```

The issued access token life time is controlled by the `Authorization:AccessTokenLifeTime` setting, the default value being one hour.<!---Add link to settings - WHAT SETTINGS!?-->

## Client Credentials Flow (Recommended for Machine-to-Machine Communication)

Virto Commerce platform authenticates and authorizes the app rather than a user. For this scenario, typical authentication schemes, such as username/password or social media credentials do not make sense.

Instead, Virto Commerce apps use the Client Credentials Flow (defined in [OAuth 2.0 RFC 6749, section 4.4](https://tools.ietf.org/html/rfc6749#section-4.4)), which enables passing along their Client ID and Client Secret for authentication to get a token.

To create a new OAuth app, you can use Platform Manager. Navigate to ***More > Security > OAuth Application*** and click ***Add*** in the screen toolbar.

!!! warning
	In the current version, all OAuth clients will have admin permissions, with no permissions or scope assignments supported. To create API apps that have limited permissions or scopes to resources, use Password Flow instead (see below). Moving forward, we intend to use roles and permissions as custom scopes to limit access to resources according to the permissions (scopes) granted to an application.

To obtain an access token through the client credentials flow, issue the following request to the authentication service, providing your `client_id` and `client_secret` via post request body:

```
POST http://{platform_host}/connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=s6BhdRkqt3&client_secret=gX1fBat3bV
```

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "access_token":"2YotnFZFEjr1zCsicMWpAA",
  "token_type":"bearer",
  "expires_in":3600
}
```

### Refresh Token Flow

To obtain an access token through the refresh token flow, you need to provide the OAuth client credentials, as well as the refresh token:

```
POST http://{platform_host}/connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token&refresh_token={token}&scope=offline_access
```

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ0NjQ2Qj...",
  "token_type": "Bearer",
  "expires_in": 1800,
  "scope": "offline_access",
  "refresh_token": "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNT..."
}
```

The issued access refresh token life time is controlled by the `Authorization:RefreshTokenLifeTime` setting with the default value of 14 days.<!---Add link to settings - WHAT SETTINGS!?-->

### Using an access token

Upon successful completion of an authorization flow, the OAuth 2.0 service will return an access token.

Use the access token in the Authorization header of all requests to Virto API as follows:

```
POST http://{platform_host}/api/{some_resource}
Authorization: Bearer {accesstoken}
```
