# MS Azure Application Insights 

Azure Application Insights is a monitoring and diagnostics service provided by Microsoft Azure that allows you to collect and analyze telemetry data. In Virto Commerce, it collects metrics, application telemetry data, and application trace logging data within the Application Insights module.

## Virto Commerce Application Insights module

Application Insights was integrated to the VC platform till the release of 3.314.0 version, where it was replaced with Serilog library. 

You can still use MS Azure Application Insights by installing it separately as a module:

* Without extra settings.
* Setting the required configurations if you prefer a customized version.

![Readmore](media/readmore.png){: width="25"} [Install Application Insights module](https://github.com/VirtoCommerce/vc-module-app-insights/releases)

## Configuring Application Insights module

This node in the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#application-insights) adds and customizes the Application Insight section.

| Node                              	    | Default or sample value   	| Description                                                                                                	|
|---------------------------------------	|---------------------------	|--------------------------------------------------------------------------------------------------------------	|
| `SamplingOptions.Processor`           	| `Adaptive`<br>`Fixed`      	| Lets you choose between two sampling methods: <ul> <li>**Adaptive sampling**: automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions.<br>![Readmore](media/readmore.png){: width="25"} [Sampling in Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling?tabs=net-core-new#configuring-adaptive-sampling-for-aspnet-applications) </li> <li>**Fixed-rate sampling**: reduces the volume of telemetry sent from both applications. Unlike adaptive sampling, it reduces telemetry at a fixed rate controlled by `SamplingPercentage` setting. </li> </ul> 	|
| `IncludedTypes`                       	| `Dependency`<br>`Event`<br>`Exception`<br>`PageView`<br>`Request`<br>`Trace`  	| A semi-colon delimited list of types to be sampled. The specified types will be sampled. All telemetry of other types will always be transmitted. All types are included by default.                                                                                        |
| `ExcludedTypes`                       	| `Dependency`<br>`Event`<br>`Exception`<br>`PageView`<br>`Request`<br>`Trace` | A semi-colon delimited list of types not to be sampled. All telemetry of the specified types is transmitted. The types that aren't specified will be sampled. Empty by default.                                                                                                    |
| `EnableSqlCommandTextInstrumentation` 	| `true`<br>`false`          	| For SQL calls, the name of the server and database is always collected and stored as the name of the collected Dependency Telemetry. Another field, called data, can contain the full SQL query text. To opt in to SQL Text collection, set this setting to `true`.                                                              |
| `IgnoreSqlTelemetryOptions`           	|                            	| Controls the Application Insights telemetry processor that excludes SQL queries related to dependencies. Any SQL command name or statement that contains a string from the `QueryIgnoreSubstrings` options will be ignored.                           	|

**Example**

To configure `ApplicationInsights`: 

1. Use current active telemetry configuration which is already initialized in most application types like ASP.NET Core:
    ```json title="appsettings.json"
    {
      "ApplicationInsights": {
        "ConnectionString": "<Copy connection string from Application Insights Resource Overview>"
      }
    }
    ```

1. Configure Platform AP telemetry behavior inside the `VirtoCommerce:ApplicationInsights` section: 
    ```json title="appsettings.json"
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

