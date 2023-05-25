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

### Configure Application Insights

To configure the module to send data to an Application Insights dashboard via instrumentation key: 

1. Use current active telemetry configuration which is already initialized in most application types like ASP.NET Core:
    ```JSON
    {
    "ApplicationInsights": {
        "ConnectionString": "<Copy connection string from Application Insights Resource Overview>"
    }
    }
    ```

1. Configure Platform AP telemetry behavior inside `VirtoCommerce:ApplicationInsights` section: 
    ```JSON
    {
        "VirtoCommerce": {
            "ApplicationInsights": {
                "SamplingOptions": {
                    "Processor": "Adaptive",
                    "Adaptive": {
                        "MaxTelemetryItemsPerSecond": "5",
                        "InitialSamplingPercentage": "100",
                        "MinSamplingPercentage": "0.1",
                        "MaxSamplingPercentage": "100",
                        "EvaluationInterval": "00:00:15",
                        "SamplingPercentageDecreaseTimeout": "00:02:00",
                        "SamplingPercentageIncreaseTimeout": "00:15:00",
                        "MovingAverageRatio": "0.25"
                    },
                    "Fixed": {
                        "SamplingPercentage": 90
                    },
                    "IncludedTypes": "Dependency;Event;Exception;PageView;Request;Trace",
                    "ExcludedTypes": ""
                },
                "EnableSqlCommandTextInstrumentation": true,
                "IgnoreSqlTelemetryOptions": {
                    "QueryIgnoreSubstrings": [
                        "[HangFire].",
                        "sp_getapplock",
                        "sp_releaseapplock"
                    ]
                }
            }
        }
    }
    ```


??? Example "See the keys used in the example"

    The following keys are used:

      | Key name                              	| Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
      |---------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
      | `SamplingOptions.Processor`           	| Lets you chose between two sampling methods: <ul> <li>**Adaptive sampling**: automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions.<br>[Read more](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling?tabs=net-core-new#configuring-adaptive-sampling-for-aspnet-applications){ .md-button }</li> <li>**Fixed-rate sampling**: reduces the volume of telemetry sent from both applications. Unlike adaptive sampling, it reduces telemetry at a fixed rate controlled by `SamplingPercentage` setting. </li> </ul> 	|
      | `IncludedTypes`                       	| A semi-colon delimited list of types to be sampled. Recognized types are: <ul> <li>`Dependency`</li> <li>`Event`</li> <li>`Exception`</li> <li>`PageView`</li> <li>`Request`</li> <li>`Trace`</li></ul> The specified types will be sampled. All telemetry of other types will always be transmitted. All types are included by default.                                                                                                                                                                                                                                                            	|
      | `ExcludedTypes`                       	| A semi-colon delimited list of types not to be sampled. Recognized types are:  <ul> <li>`Dependency`</li> <li>`Event`</li> <li>`Exception`</li> <li>`PageView`</li> <li>`Request`</li> <li>`Trace`</li> </ul> All telemetry of the specified types is transmitted. The types that aren't specified will be sampled. Empty by default.                                                                                                                                                                                                                                                                 	|
      | `EnableSqlCommandTextInstrumentation` 	| For SQL calls, the name of the server and database is always collected and stored as the name of the collected Dependency Telemetry. Another field, called data, can contain the full SQL query text. To opt in to SQL Text collection, set this setting to `true`.                                                                                                                                                                                                                                                                                                                                   	|
      | `IgnoreSqlTelemetryOptions`           	| Controls the Application Insights telemetry processor that excludes SQL queries related to dependencies. Any SQL command name or statement that contains a string from the `QueryIgnoreSubstrings` options will be ignored.                                                                                                                                                                                                                                                                                                                                                                           	|
 </details>