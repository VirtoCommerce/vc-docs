# Configuration

To make configurations:

1. Update platform. 

    [Platform latest version](https://github.com/VirtoCommerce/vc-platform/releases/tag/3.304.0){ .md-button }

1. Install App Insights module.

    [Module latest version](https://github.com/VirtoCommerce/vc-module-app-insights){ .md-button }

1. Make necessary configurations:
    <hr />

    === "Logging (from configuration)"

        The module comes with a [sink](https://github.com/serilog-contrib/serilog-sinks-applicationinsights) for Serilog that writes events to Microsoft Application Insights. 

        To enable AI logging, update the following `Serilog` configuration sections:

        ```JSON
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

        !!! Note
            The `telemetryConverter` has to be specified with the full type name and the assembly name. 
        
            A `connectionString` can be omitted if it's supplied in the APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.

    === "Logging (from code)"

        To configure Serilog's Application Insights sink from your code:

        1. Use special `ILoggerConfigurationService` interface:

            ```cs
            public class ApplicationInsightsLoggerConfiguration : ILoggerConfigurationService
            {
                private readonly TelemetryConfiguration _configuration;

                public ApplicationInsightsLoggerConfiguration(TelemetryConfiguration configuration)
                {
                    _configuration = configuration;
                }

                public void Configure(LoggerConfiguration loggerConfiguration)
                {
                    loggerConfiguration.WriteTo.ApplicationInsights(telemetryConfiguration: _configuration,
                    telemetryConverter: TelemetryConverter.Traces,
                    restrictedToMinimumLevel: Serilog.Events.LogEventLevel.Error);
                }
            }
            ```

        1. Register `Initialize` method in `Module.cs`:

            ```cs
            public void Initialize(IServiceCollection serviceCollection)
            {
                serviceCollection.AddTransient<ILoggerConfigurationService, ApplicationInsightsLoggerConfiguration>();
            }
            ```


        !!! Note
            The `telemetryConverter` has to be specified with the full type name and the assembly name. 
        
            A `connectionString` can be omitted if it's supplied in the APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.

    === "Telemetry"

        To send data to an Application Insights dashboard via instrumentation key:

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

        The following keys are used:

        | Key name                              	| Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
        |---------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
        | `SamplingOptions.Processor`           	| Lets you chose between two sampling methods: <ul> <li>**Adaptive sampling**: automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions.<br>[Read more](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling?tabs=net-core-new#configuring-adaptive-sampling-for-aspnet-applications){ .md-button }</li> <li>**Fixed-rate sampling**: reduces the volume of telemetry sent from both applications. Unlike adaptive sampling, it reduces telemetry at a fixed rate controlled by `SamplingPercentage` setting. </li> </ul> 	|
        | `IncludedTypes`                       	| A semi-colon delimited list of types to be sampled. Recognized types are: <ul> <li>`Dependency`</li> <li>`Event`</li> <li>`Exception`</li> <li>`PageView`</li> <li>`Request`</li> <li>`Trace`</li></ul> The specified types will be sampled. All telemetry of other types will always be transmitted. All types are included by default.                                                                                                                                                                                                                                                            	|
        | `ExcludedTypes`                       	| A semi-colon delimited list of types not to be sampled. Recognized types are:  <ul> <li>`Dependency`</li> <li>`Event`</li> <li>`Exception`</li> <li>`PageView`</li> <li>`Request`</li> <li>`Trace`</li> </ul> All telemetry of the specified types is transmitted. The types that aren't specified will be sampled. Empty by default.                                                                                                                                                                                                                                                                 	|
        | `EnableSqlCommandTextInstrumentation` 	| For SQL calls, the name of the server and database is always collected and stored as the name of the collected Dependency Telemetry. Another field, called data, can contain the full SQL query text. To opt in to SQL Text collection, set this setting to `true`.                                                                                                                                                                                                                                                                                                                                   	|
        | `IgnoreSqlTelemetryOptions`           	| Controls the Application Insights telemetry processor that excludes SQL queries related to dependencies. Any SQL command name or statement that contains a string from the `QueryIgnoreSubstrings` options will be ignored.                                                                                                                                                                                                                                                                                                                                                                           	|


        This module supports configuration by config and code. You can read more about configuration [here](https://github.com/serilog-contrib/serilog-sinks-applicationinsights).



1. Update XApi module.

    [Module latest version](www.github.com/VirtoCommerce/vc-module-experience-api/releases/tag/3.313.0){ .md-button }



    
