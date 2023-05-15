# How to update platform to Serilog integrated version

!!! note
    Along with updating platform to 3.304.0 version you have to update XApi module to [version 3.314.0](https://github.com/VirtoCommerce/vc-module-experience-api/releases/tag/3.314.0) or higher.

To update your platform version to [3.304.0 and higher](https://github.com/VirtoCommerce/vc-platform/releases), use one of the following options:

## Option 1. Migrate existing configuration to Serilog format

If you commited changes to logging configuration:

1. Map existing configuration into Serilog format in the appsettings.{ENIROMENT}.json Logging section.
1. Replace the original configuration with the Serilog configuration. 

Below are examples of the appsettings.{ENIROMENT}.json file before and after migration:

Before:

```json title="appsettings.{ENIROMENT}.json"
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
```json title="appsettings.{ENIROMENT}.json"
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

[Read more  about Serilog settings configuration](https://github.com/serilog/serilog-settings-configuration){ .md-button }

## Option 2. Use Application Insights 

Since Application Insights integration was moved to a separate module:

1. [Download it manually](https://github.com/VirtoCommerce/vc-module-app-insights/releases)  or  install it via vc-build CLI <!--- TODO: Add link how to install module via vc-build CLI -->.

1. Add the following changes to the appsettings.{ENIROMENT}.json file.  

  ```json title="appsettings.{ENIROMENT}.json"
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
