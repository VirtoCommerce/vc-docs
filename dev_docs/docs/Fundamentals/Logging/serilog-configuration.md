# Serilog Configuration

!!! Note "Important"
    
    After configuring the logging settings, updating XApi module is required.

    [Update XApi module](www.github.com/VirtoCommerce/vc-module-experience-api/releases/){ .md-button }

To customize logging with Serilog, there are two configuration options:

* Basic.
* Extended. 

## Basic Configuration

Basic Serilog configuration is performed via the [standard settings of the appsettings.json file](https://github.com/serilog/serilog-settings-configuration). 


The example below shows how to enable AI logging:

```JSON title="appsettings.json"
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

## Extended Configuration

[Serilog extended configuration](https://github.com/serilog/serilog/wiki/Provided-Sinks) is applicable when the basic configurations available through the appsettings.json file are not sufficient.

1. To get access to extended configurations, use special `ILoggerConfigurationService` interface. 
    
    In the example below, `telemetryConverter` and `restrictedToMinimumLevel` are configured:

    ```cs title="appsettings.json"
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

    ```cs title="module.cs"
    public void Initialize(IServiceCollection serviceCollection)
    {
        serviceCollection.AddTransient<ILoggerConfigurationService, ApplicationInsightsLoggerConfiguration>();
    }
    ```


!!! Note
    The `telemetryConverter` has to be specified with the full type name and the assembly name. 
        
    A `connectionString` can be omitted if it's supplied in the APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.



