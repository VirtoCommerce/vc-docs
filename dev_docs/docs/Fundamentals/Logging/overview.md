# Overview

VC Platform supports two logging libraries:

* MS Azure Application Insights. 

    [Read more](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview){ .md-button }

* Serilog. 

    [Read more](https://serilog.net/){ .md-button }

[The VC Platform version 3.304.0](https://github.com/VirtoCommerce/vc-platform/releases) is making changes to its integration features. We are transitioning to Serilog libraries for enhanced logging capabilities (structured data, storing log events in various formats, data enrichment option, etc.), replacing MS Azure Application Insights. As part of this transition, Azure Application Insights has been moved to a dedicated Virto Commerce module, offering even more flexibility and control over your logging and telemetry. 

There are following options available for logging:

* If you install the [Platform version 3.304.0 and above](https://github.com/VirtoCommerce/vc-platform/releases), logging will be automatically performed via Serilog without extra setup needed.
* You can still use MS Azure Application Insights by installing it separately as a [module](https://github.com/VirtoCommerce/vc-module-app-insights/releases). No extra settings are needed.
* If you prefer a customized MS Azure Application Insights module, you can install it separately and [configure it](/application-insights-configuration.md) as needed.
* Perform [basic](serilog-configuration.md#basic-configuration) or [extended](serilog-configuration.md#extended-configuration) customization of Serilog logging.
