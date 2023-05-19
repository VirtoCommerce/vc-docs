

The Platform reads Serilog configuration from the appsettings.json and can also be configured from the code. To achieve this, Platform provides `ILoggerConfigurationService` interface that allows users writing and adding their own sinks or making customizations. 

```json title="appsettings.json"
UseSerilog((context, services, loggerConfiguration) =>
{
    // read from configuration
    _ = loggerConfiguration.ReadFrom.Configuration(context.Configuration);
    // enrich configuration from external sources
    var configurationServices = services.GetService<IEnumerable<ILoggerConfigurationService>>();
    foreach (var service in configurationServices)
    {
        service.Configure(loggerConfiguration);
    }
})
```

This code shows how Serilog is being initialized in the Platform:

1. First the `loggerConfiguration` objects are initialized from the configuration sections and then passed to a list of external services. To implement your own config services, first create a class that inherits `ILoggerConfig` and implement it. For example, this is the implementation for the Azure Application Insights sink:

    ```json title="appsettings.json"
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

1. Register the implementation in module.cs Initialize method of your external module:

    ```json title="appsettings.json"
    public void Initialize(IServiceCollection serviceCollection)
    {
        serviceCollection.AddTransient<ILoggerConfigurationService, ApplicationInsightsLoggerConfiguration>();
    }
    ```

## References

* [Serilog Library](http://serilog.net/)

* [Serilog ASP .NET Core](https://github.com/serilog/serilog-aspnetcore)

* [Settings Configuration](https://github.com/serilog/serilog-settings-configuration)

* [Provided Sinks](https://github.com/serilog/serilog/wiki/Provided-Sinks)