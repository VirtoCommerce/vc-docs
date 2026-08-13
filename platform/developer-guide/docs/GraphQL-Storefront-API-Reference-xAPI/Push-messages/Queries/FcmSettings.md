# FcmSettings ==~query~==

This query retrieves the Firebase Cloud Messaging (FCM) settings required for configuring and using FCM in the application.

## Possible returns

| Possible return                                         | Description                                             |
|---------------------------------------------------------|---------------------------------------------------------|
| [`FcmSettingsType`](../Objects/FcmSettingsType.md)      | The structured data containing FCM settings.            |


## Example

<div class="grid" markdown>

```graphql title="Query"
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

```json title="Return"
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

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../pushMessages">← Push messages query</a>
    <a href="../../Objects/PushMessageType">PushMessageType →</a>
</div>
