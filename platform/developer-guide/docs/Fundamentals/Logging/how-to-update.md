# Update Platform to Serilog Integrated Version

!!! note
    Along with updating platform to 3.304.0 version you have to update xAPI module to [version 3.314.0](https://github.com/VirtoCommerce/vc-module-experience-api/releases/tag/3.314.0) or higher.

To update your platform version to [3.304.0 and higher](https://github.com/VirtoCommerce/vc-platform/releases), use one of the following options:

## Option 1. Migrate existing configuration to Serilog format

If you committed changes to logging configuration:

1. Map existing configuration into Serilog format in the appsettings.{ENVIRONMENT}.json Logging section.
1. Replace the original configuration with the Serilog configuration. 

Below are examples of the **appsettings.{ENVIRONMENT}.json** file before and after migration:

Before:

```json title="appsettings.{ENVIRONMENT}.json"
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  }
}
```

After:
```json title="appsettings.{ENVIRONMENT}.json"
{
  "Serilog": {
  "Using": [
      "Serilog.Sinks.Console"
    ],
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft": "Warning",
        "System": "Warning"
      }
    },
    "WriteTo": [
      {
        "Name": "Console"        
      }
    ]
  }
}
```

![Readmore](media/readmore.png){: width="25"} [Serilog Settings Configuration](https://github.com/serilog/serilog-settings-configuration)

## Option 2. Use Application Insights 

Since Application Insights integration was moved to a separate module:

1. [Download it manually](https://github.com/VirtoCommerce/vc-module-app-insights/releases)  or  [install it via vc-build CLI](../../CLI-tools/more-targets.md#installmodules).

1. Add the following changes to the appsettings.{ENVIRONMENT}.json file.  

  ```json title="appsettings.{ENVIRONMENT}.json"
  {
    "Serilog": {
      "Using": [
        "Serilog.Sinks.ApplicationInsights"
      ],
      "WriteTo": [
        {
          "Name": "ApplicationInsights",
          "Args": {
            "connectionString": "<Copy connection string from Application Insights Resource Overview>",
            "telemetryConverter": "Serilog.Sinks.ApplicationInsights.TelemetryConverters.TraceTelemetryConverter, Serilog.Sinks.ApplicationInsights",
            "restrictedToMinimumLevel": "Error"
          }
        }
      ]
    }
  }
  ```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Logging overview </a>
    <a href="../application-insights">Application Insights →</a>
</div>
