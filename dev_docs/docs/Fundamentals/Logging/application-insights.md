# MS Azure Application Insights 

Azure Application Insights is a monitoring and diagnostics service provided by Microsoft Azure that allows you to collect and analyze telemetry data. In Virto Commerce, it collects metrics, application telemetry data, and application trace logging data within the Application Insights module.

## Virto Commerce Application Insights module

Application Insights was integrated to the VC platform till the release of 3.314.0 version, where it was replaced with Serilog library. 

You can still use MS Azure Application Insights by installing it separately as a module:

* Without extra settings.
* Setting the required configurations if you prefer a customized version.

[Install Application Insights module](https://github.com/VirtoCommerce/vc-module-app-insights/releases){ .md-button }

## Configuring Application Insights module

{%
include-markdown "../../Configuration-Reference/appsettingsjson.md"
start="<!--AppInsights-start-->"
end="<!--AppInsights-end-->"
%}


