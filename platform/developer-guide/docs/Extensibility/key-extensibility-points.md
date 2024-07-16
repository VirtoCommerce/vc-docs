# Key Extension Points

Our Platform is based on a collection of various modules and components that form the backbone of the Virto value proposition, which is to make each part of our system extensible and usable.

In order to provide solutions for many different use cases, we decided it was important to ensure that these core concepts were as flexible and extensible as possible.

The Virto platform encompasses the **extension concept** based on various techniques and practices. It can significantly reduce the implementation and upgrade effort for your custom solution.

!!! info
	The extension concept is the backbone of the Virto platform value proposition and has four main extensible point types.

To address crucial extension requirements, the platform contains various **extensions points** for all three main parts: the Platform application, Modules, and Frontend Application. Such extension points enable performing multiple customizations without direct code modification. The list below mentions the important ones:

* Domain and business logic extension:
    * [Extending domain models](../Tutorials-and-How-tos/Tutorials/extending-domain-models.md)
    * [Extending through domain events](../Fundamentals/Event-Driven-Development/using-domain-events.md)
    * [Dynamic properties](../Fundamentals/Dynamic-Properties/overview.md)
* Platform manager UI extension:
    * [Extending main menu](../Platform-Manager/Extensibility-Points/extending-main-menu.md)
    * [Working with widgets](../Platform-Manager/Extensibility-Points/widgets.md)
    * [Metaforms](../Platform-Manager/Extensibility-Points/metaform.md)
    * [Extending blade toolbar](../Platform-Manager/Extensibility-Points/blade-toolbar.md)
    * [Extending grid columns](../Platform-Manager/Extensibility-Points/extending-grid-columns.md)
* Extending commerce logic:
    * [New payment method registration](../Fundamentals/Payments/new-payment-method-registration.md)
    * [New shipping method registration](../Fundamentals/Shipments/new-shipping-method-registration.md)
    * [New tax provider registration](../Fundamentals/Taxes/new-tax-provider-registration.md)
* Security extensions:
    * [Extending authorization policies](../Fundamentals/Security/extensions/extending-authorization-policies.md)
    * [Extending ASP.NET Identity UserManager and RoleManager](../Fundamentals/Security/extensions/extending-usermanager-and-rolemanager.md)
    * [Adding New SSO Provider](../Fundamentals/Security/extensions/adding-new-sso-provider.md)
* Notification extensions:
    * [Extending notification types](../Fundamentals/Notifications/extending-notification-types.md)
* Logging extension:
    * [Using MS Azure Application Insights](../Fundamentals/Logging/application-insights.md)
    * [Using Seq log module](../Fundamentals/Logging/seq-module.md)


 