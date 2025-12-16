# Conceptual Overview

The chart below shows the high level architecture of the Platform:

![Back end architecture](media/01-back-end-architecture-chart.png){: style="display: block; margin: 0 auto;" }

The Virto Commerce Platform's core components are:

* **Platform manager (SPA)**: A web-based user interface packed into an SPA allowing you to manage your application. It also provides back office capabilities that enable master data management, configuring products, prices, inventories, employees, workflows, and other functionality required for ecommerce applications. It works with all data through REST API the Platform runtime provides.

* **Platform application (Runtime)**: An [ASP.NET](http://asp.net/) Core application that bootstraps the modules and manager GUI and acts as a host for all Platform capabilities. It integrates various components to deliver a seamless ecommerce experience, including support for different databases, search engines, and caching mechanisms.

* **Modules**: Each module is a portion of the application's overall functionality. Multiple modules get organized into independent and interchangeable [software packages hosted by the Platform Application](../Fundamentals/Modularity/01-overview.md). All modules can be divided into three main categories depending on the tasks they are intended for:
	- **Business modules**: Contain the implementation of business functionality.
	- **Integration modules**: Implement various kinds of integration with third-party services.
	- **Custom solution modules**: Usually contain an extension of the existing logic other modules have.

* **Supported databases**: The Platform is database-agnostic, supporting multiple databases for flexibility and scalability:
	- PostgreSQL.
	- MySQL.
	- Microsoft SQL Server.

* **Supported search engines**: Virto Commerce supports various search engines to provide efficient and scalable search capabilities:
	- Elasticsearch.
	- Elasticsearch 8.
	- Elasticsearch 9.
	- Elastic App Search.
	- Azure Search.
	- Algolia.
	- Lucene.

* **Caching**: Virto Commerce integrates Redis for efficient caching to improve performance and scalability.

* **REST and GraphQL API**: A set of APIs used to manage resources. [REST API](https://virtostart-demo-admin.govirto.com/docs/index.html) is mainly used to build integration and interact with Virto resources, while [GraphQL](../GraphQL-Storefront-API-Reference-xAPI/index.md) represents an implementation of the Back End for Front End design pattern and provides a lightweight access to ecommerce capabilities for various Frontend applications.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../01-tech-stack">← Technical stack</a>
    <a href="../../CLI-tools/overview">CLI tools overview →</a>
</div>