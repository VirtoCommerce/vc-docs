# Overview

VC Platform supports two logging options:

* via MS Azure Application Insights (separate module). 

* via Serilog (integrated with the Platform). 

## MS Azure Application Insights

Azure Application Insights module collects metric, application telemetry data and application trace logging data in Microsoft Azure Application Insights. It enables:

* Collecting standard metric.
* Collecting application telemetry data.
* Collecting application trace logging data.
* Flexible configuration by config and code.

To use this feature, install the [Application Insights Module](https://github.com/VirtoCommerce/vc-module-app-insights).

[Read more about Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview){ .md-button }

## Serilog

Serilog is a popular logging library for .NET and .NET Core applications. It provides a flexible logging framework. It enables developers to:

* Easily capture log messages from various sources.
* Persist them to a variety of targets, such as files, databases, and cloud services.

One of the key features of Serilog is its support for structured logging. This means that log messages are not just plain text, but also contain structured data in the form of key-value pairs. It enables:

* More advanced filtering, searching, and analysis of log data.
* Easier integration with other tools and systems.

Serilog also supports a wide range of logging sinks, which are plugins that define where log messages should be sent. These sinks include file-based sinks, database sinks, and cloud-based sinks for services such as Azure, AWS, and Seq.

To enable out-of-the-box logging, install the latest version of the [Platform integrated with Serilog](https://github.com/VirtoCommerce/vc-platform/releases/tag/3.304.0).

To configure logging, read the [Configuration](configuration.md) article.

[Read more about Serilog](https://serilog.net/){ .md-button }

