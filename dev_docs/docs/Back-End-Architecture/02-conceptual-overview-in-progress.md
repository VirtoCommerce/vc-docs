# Conceptual Overview

The chart below shows the high level architecture of the platform:

![Back end architecture](media/01-back-end-architecture-chart.png){: width="650" }

The Virto Commerce platform's core components are:

- **Platform Manager (SPA):** A web-based user interface packed into an SPA allowing you to manage your application. It also provides back office capabilities that enable master data management, configuring products, prices, inventories, employees, workflows, and other functionality required for ecommerce applications. It works with all data through REST API the platform runtime provides. <!---TBA: link to Platform manager(legacy)--->
    
- **Platform application (runtime):** An [ASP.NET](http://asp.net/) Core application that bootstraps the modules and manager GUI and acts as a host for all platform capabilities.
    
- **Modules:** Each module is a portion of the application's overall functionality. Multiple modules get organized into independent and interchangeable [software packages hosted by the Platform Application](../Fundamentals/Modularity/01-overview.md). All modules can be divided into three main categories depending on the tasks they are intended for:
    
	- Business modules: Contain the implementation of business functionality.
    
	- Integration modules: Implement various kinds of integration with third party services.
    
	- Custom solution modules: Usually contain an extension of the existing logic other modules have.
    
- **REST and GraphQL API:** A set of APIs used to manage resources. REST API <!---TBA: link to Rest API reference--->is mainly used to build integration and interact with Virto resources, while [GraphQL](../GraphQL-Storefront-API-Reference-xAPI/index.md) represents an implementation of the Back End for Front End design pattern and provides a lightweight access to ecommerce capabilities for various storefront applications.
