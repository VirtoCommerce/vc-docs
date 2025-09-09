# MS Azure Application Insights 

Azure Application Insights is a monitoring and diagnostics service provided by Microsoft Azure that allows you to collect and analyze telemetry data. In Virto Commerce, it collects metrics, application telemetry data, and application trace logging data within the Application Insights module.

## Virto Commerce Application Insights module

Application Insights was integrated to the VC Platform till the release of 3.314.0 version, where it was replaced with Serilog library. 

You can still use MS Azure Application Insights by installing it separately as a module:

* Without extra settings.
* Setting the required configurations if you prefer a customized version.

[![Install Latest Release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-app-insights/releases)

## Application Insights module сonfiguration

Configuring the Application Insights module includes:

* [Configuring telemetry from the appsettings.json file.](application-insights.md#configure-telemetry-from-appsettingsjson-file)
* [Configuring logging from the appsettings.json file.](application-insights.md#configure-logging-from-appsettingsjson-file)
* [Configuring logging from code.](application-insights.md#configure-logging-from-code)

### Configure telemetry from appsettings.json file

To send data to the Application Insights dashboard via the instrumentation key:

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--AppInsights2-start-->"
   end="<!--AppInsights2-end-->"
%}

Values used are described below:

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--AppInsights1-start-->"
   end="<!--AppInsights1-end-->"
%}


### Configure logging from appsettings.json file

The module includes a Serilog [sink](https://github.com/serilog-contrib/serilog-sinks-applicationinsights) for writing events to Microsoft Application Insights. Enable Application Insights logging by updating the following Serilog configuration sections:

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--AppInsights3-start-->"
   end="<!--AppInsights3-end-->"
%}

Make sure to specify the **telemetryConverter** with the full type and assembly name. A connection string is optional if provided via the **APPLICATIONINSIGHTS_CONNECTION_STRING** environment variable.

### Configure logging from code

To configure Serilog's Application Insights sink in code:

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

1. Register the `Initialize` method in **module.cs**:

      ```cs
      public void Initialize(IServiceCollection serviceCollection)
      {
         serviceCollection.AddTransient<ILoggerConfigurationService, ApplicationInsightsLoggerConfiguration>();
      }
      ```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../how-to-update">← Updating to Serilog integrated version </a>
    <a href="../extended-logging">Extended logging →</a>
</div>
