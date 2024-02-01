# Overview

VC Platform supports two logging libraries out of the box:

* Serilog (built-in in the platform). 

    ![Readmore](media/readmore.png){: width="25"} [Serilog overview](https://serilog.net/)

* MS Azure Application Insights (as separated module). 

    ![Readmore](media/readmore.png){: width="25"} [App Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

!!! NOTE

    Starting from version 3.304.0 we are transitioning to Serliog library for leverage more advanced logging capabilities like structured data, storing log events in various formats, data enrichment option, etc. As part of this transition, Azure Application Insights has been moved to a dedicated Virto Commerce module, offering even more flexibility and control over your logging and telemetry. 

## Basic scenarios

Here are basic usage scenarios how to use platform logging.

### Configuring logging

Logging configuration is provided by the `Serilog` section of **appsettings.{ENVIRONMENT}.json files**, where the `{ENVIRONMENT}` placeholder is the [environment](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-7.0). 

Here is an example of Serilog configuration. In this file we use two sinks (Console and Debug) for writing logs, and also define default severity level for lg.

```json title="appsettings.Development.json"
{
  "Serilog": {
    "Using": [
      "Serilog.Sinks.Console",
      "Serilog.Sinks.Debug"
    ],
    "MinimumLevel": {
      "Default": "Error",
      "Override": {
        "Microsoft.AspNetCore": "Information"        
      }
    },
    "WriteTo": [
      "Console",
      "Debug"
    ]
  }
}
```

In this example:

* The two sinks (Console and Debug) are used to writing logs.
* The log level `Error` is set as default. That means, all logs messages with log level `Error` or higher will be logged, all other logs with log level lower than `Error` like `Information`, `Trace`, `Debug` will be skipped.
* The `Microsoft.AspNetCore` category applies to all categories that start with `Microsoft.AspNetCore`. For example, this setting applies to the `Microsoft.AspNetCore.Routing.EndpointMiddleware` category. 
* The `Microsoft.AspNetCore` category logs at log level `Information` and higher.

[See more configuration examples](https://github.com/serilog/serilog-settings-configuration)

### Writing Log Events

Log events are written to sinks using the `Log` static class, or the methods on an `ILogger`:

```
Log.Warning("Disk quota {Quota} MB exceeded by {User}", quota, user);
```

The same example using `ILogging` interface:

```
ILogger logger;
logger.LogWarning("Disk quota {Quota} MB exceeded by {User}", quota, user);
```


**References**:

* [Logging in .NET Core and ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-7.0)

* [Serilog ASP .NET Core](https://github.com/serilog/serilog-aspnetcore)

* [Settings Configuration](https://github.com/serilog/serilog-settings-configuration)

* [Provided Sinks](https://github.com/serilog/serilog/wiki/Provided-Sinks)


**Next steps**:

* [How to update your custom logging configuration to platform 3.304 and above](how-to-update.md)

* [Application insight module](application-insights.md)

* [Extending logging](extended-logging.md)