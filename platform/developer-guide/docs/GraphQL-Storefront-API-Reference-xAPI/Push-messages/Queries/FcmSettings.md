# FcmSettings ==~query~==

This query retrieves the Firebase Cloud Messaging (FCM) settings required for configuring and using FCM in the application.

## Possible returns

| Possible return                                         | Description                                             |
|---------------------------------------------------------|---------------------------------------------------------|
| [`FcmSettingsType`](../Objects/FcmSettingsType.md)      | The structured data containing FCM settings.            |

## Examples

=== "Query"

    ```graphql linenums="1"
    query {
      fcmSettings {
        apiKey
        authDomain
        projectId
        storageBucket
        messagingSenderId
        appId
        vapidKey
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "fcmSettings": {
          "apiKey": "your-api-key",
          "authDomain": "your-auth-domain",
          "projectId": "your-project-id",
          "storageBucket": "your-storage-bucket",
          "messagingSenderId": "your-messaging-sender-id",
          "appId": "your-app-id",
          "vapidKey": "your-vapid-key"
        }
      }
    }
    ```