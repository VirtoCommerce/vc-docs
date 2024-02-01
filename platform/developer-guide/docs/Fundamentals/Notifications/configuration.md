# Configuration
This section explains the basic configuration for the Notifications module via the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#notifications)

| Node                              | Default or Sample Value         | Description                                                                                                               |
| --------------------------------- | ------------------------------  | ------------------------------------------------------------------------------------------------------------------------- |
| Gateway                           | `"Smtp"`<br>`"SendGrid"`        | The current notification sending gateway.<br>The out-of-the-box implemented and<br>supported values are `Smtp`, `SendGrid`.  |
| DefaultSender                     | `"noreply@gmail.com"`           | This **required** setting provides sender<br>identification used by the current notification sending gateway.           |
| Smtp                              |                                | SMTP gateway configuration.<br>Used if the `Gateway` setting has the `Smtp` value.                                        |
| Smtp:SmtpServer                   | `"smtp.gmail.com"`              | The SMTP server address for sending emails.                                                                               |
| Smtp:Port                         | `587`                          | The port number to use when connecting to the SMTP server.                                                                |
| Smtp:Login                        |                                | The login (username) for authenticating to the SMTP server.                                                               |
| Smtp:Password                     |                                | The password for authenticating to the SMTP server.                                                                       |
| Smtp:ForceSslTls                  | `false`                        | If set to `true`, forces the usage of SSL/TLS when connecting to the SMTP server.                                         |
| SendGrid                          |                                | SendGrid gateway configuration.<br>Used when the `Gateway` setting has the `SendGrid` value.                              |
| SendGrid:ApiKey                   |                                | The API key for authenticating to the SendGrid service.                                                                   |
| Notifications:DiscoveryPath       | `Templates`                    | Relative folder path in the local file system<br>that will be used to discover notification template files<br>during notification rendering. |
| Notifications:FallbackDiscoveryPath|                                | Alternative relative folder path in the local file<br>system that will be used to discover alternative template<br>files during notification rendering.<br>Templates found through this path will be used as a backup,<br>in case the templates defined in the<br>`Notifications:DiscoveryPath` setting are not found. |

**Example**

```json title="appsettings.json"
"Notifications": {
    "Gateway": "Smtp",
    "DefaultSender": "noreply@gmail.com",
    "Smtp": {
      "SmtpServer": "smtp.gmail.com",
      "Port": 587,
      "Login": "",
      "Password": "",
      "ForceSslTls": false
    },
    "SendGrid": {
      "ApiKey": ""
    },
    "Notifications:DiscoveryPath": "Templates",
    "Notifications:FallbackDiscoveryPath": ""
}
```

