# Overview

The main function of the **Experience API (xAPI)** module is to serve as a middle layer connecting clients and enterprise services using the GraphQL protocol. 

It is closely associated with a particular user or touch point experience and ensures quick and dependable access. Additionally, it serves as an implementation of the backend for frontend (BFF) design pattern.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-x-api/)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-x-api/releases)

!!! note
    We have migrated to a new xAPI architecture to better support the evolving needs of our business API with GraphQL. The previously used [Experience API module](https://github.com/VirtoCommerce/vc-module-experience-api) has been replaced with a suite of new, more specialized modules. This change is part of our effort to simplify business API development and streamline our release cycle. The **ExperienceAPI module** will be archived and supported in Stable 8 and Stable 9 releases. Future developments will focus on the new xAPI module and related modules. 

    ![Readmore](media/readmore.png){: width="25"} [Migration to new xAPI modules](../Tutorials-and-How-tos/How-tos/migration-to-new-xapi-modules.md)

## GraphQL vs REST

GraphQL is a an API standard that provides a more efficient, powerful, and flexible alternative to REST. When the concept of REST was developed, client applications were relatively simple, and the development pace wasn't nearly where it is today. However, the API landscape has radically changed over the last years. In response to these evolving demands, GraphQL has emerged as a more adaptable solution. With GraphQL, each client can request precisely the data it needs, allowing for more tailored responses. In contrast, REST APIs often provide fixed sets of data, potentially leading to over-fetching or under-fetching of information. 

![graphQL-Rest](media/rest-graphQL.png){: style="display: block; margin: 0 auto;" }

Virto Commerce intentionally keeps both GraphQL and REST, each for different purposes.

| GraphQL is used for:|	REST is used for:|
| --------------------| -----------------|
|  Frontend applications. <br> Customer-facing experiences. <br> Business workflows (browse, search, cart, checkout). <br> Aggregated, contextual data. <br> High-performance read/write scenarios.| System integrations. <br> ERP synchronization. <br> Bulk data import/export. <br> Back-office operations. <br> Data migration and administrative APIs.|

## GraphQL core components

GraphQL’s power lies in its structured, declarative nature. Its fundamental elements are:

* [Schema.](#schema)
* [Query.](#query)
* [Mutation.](#mutation)
* [Subscription.](#subscription)
* [Variable.](#variable)

### Schema

The schema is the backbone of GraphQL, defining the API’s data structure in a strongly typed manner. It acts as a contract between client and server, specifying available types (e.g., objects like “Product” or “Order”), fields (e.g., “title” or “price”), and relationships. This self-documenting schema enables tools for auto-generating clients, validation, and introspection. Unlike REST’s often loosely defined endpoints, GraphQL schemas evolve predictably - new fields can be added without breaking existing queries - making it ideal for long-term API maintenance in ecommerce.

![schema](media/schema.png){: style="display: block; margin: 0 auto;" }

### Query

Query is a read-only operation used to fetch data. Clients specify exactly what data they need, and the server responds with a matching structure. For example, a query might request product details for a specific store and language context. Another to term to know is **Variable**. It is a placeholder that allows clients to pass values as arguments to a query or mutation without hard-coding those values directly into the query. Variables are defined in the query or mutation. They are then referenced in the query using the dollar sign ($). This feature makes GraphQL queries more reusable and flexible, as clients can change variable values when making requests.


```graphql
query GetOrdersForApproval ($storeId: String!,  $cultureName: String!) {​
  ordersForApproval(storeId: $ storeId, cultureName: $cultureName) {​
    id​
    number​
    status​
    total {​
      amount​
      currency​
    }​
  }​
}
```

This avoids REST’s over-fetching, ensuring efficient, targeted data retrieval.

??? "Sample queries"

    | Query                              	| Sample query                         	                        | Sample return                 	                        |
    |------------------------------------	|--------------------------------------------------------------	|--------------------------------------------------------	|
    | Total amount of items in B2B-store 	| ![total count query](media/total-count-query.png) 	          | ![total count return](media/total-count-return.png) 	  |
    | Names of all products in B2B-store 	| ![names query](media/names-products-query.png) 	              | ![names return](media/names-products-return.png) 	      |
    | Names, codes, ids of products in B2B-store | ![codes-ids-query](media/codes-ids-query.png)          | ![codes-ids-return](media/codes-ids-return.png)         | 
    | Show first 2 products from the list | ![first-products](media/first-products-query.png)             | ![first-products](media/first-products-return.png) |


### Mutation

Mutations handle write operations, such as creating, updating, or deleting data. They follow the same request-response pattern as queries but perform side effects. For instance, a mutation could approve an order:

```graphql
mutation ApproveOrder($storeId: String!,  $cultureName: String!, $orderId: String!) {​
  approveOrder(storeId: $ storeId, cultureName: $cultureName, orderId: $orderId) {​
    id​
    number​
    status​
    approvedBy {​
      id​
      name​
    }​
    approvedDate​
  }  ​
}
```

Mutations return data, allowing clients to fetch updated results in one request, reducing the need for follow-up queries common in REST.

### Subscription

Subscriptions enable real-time updates via WebSockets, pushing data to clients when events occur. This is perfect for dynamic e-commerce features like live inventory changes or order notifications:

```graphql
subscription OnOrderStatusChanged($userId: ID!) {​
  orderStatusChanged(userId: $userId) {​
    id​
    number​
    status​
    updatedDate​
  }​
}​
```

Unlike REST’s polling (which wastes resources), subscriptions provide efficient, event-driven real-time communication.

With GraphQL, clients can optimize their data queries, reducing network load, improving performance, and addressing the more complex and specific data requirements of modern applications. Clients customize the endpoints using schema, which provides a description of how the data is structured. Here is a part from Virto Commerce schema:



Our instruction provides Virto Commerce related guidelines. 

![Readmore](media/readmore.png){: width="25"} [Extensive GraphQL guide](https://graphql.org/learn/)


## Key principles

* Utilize GraphQL protocol for precise and flexible data retrieval control from the API.
* Achieve fast and dependable indexed search through integration with:
    * [Elasticsearch 9.x](https://www.elastic.co/downloads/elasticsearch)
    * [Elastic App Search](https://www.elastic.co/downloads/app-search)
    * [Azure Search](https://learn.microsoft.com/en-us/shows/azure/azure-search)
* Maintain autonomy by exclusively relying on the index data source, separate from the rest of the VC data infrastructure.
* Capture tracing and performance metrics for request monitoring.

## Key features

The xAPI project provides the following major features:

- [Back-in-stock](Back-in-stock/overview.md)
- [Cart](Cart/overview.md)
- [xCatalog](Catalog/overview.md)
- [xCMS, or Content](Content/overview.md)
- [xFrontend](xFrontend/overview.md)
- [xFile](File/overview.md)
- [Loyalty](Loyalty/overview.md)
- [xMarketing](Marketing/overview.md)
- [News](News/overview.md)
- [xOrder](Order/overview.md)
- [Pages](Pages/overview.md)
- [xPickup](xPickup/overview.md)
- [xProfile](Profile/overview.md)
- [Push messages](Push-messages/overview.md)
- [Quote](Quote/overview.md)
- [xRecommend](Recommend/overview.md)
- [Reviews](Reviews/overview.md)
- [Skyflow](Skyflow/overview.md)
- [Store](Store/overview.md)
- [Shipping](White-labeling/overview.md)
- [White labeling](White-labeling/overview.md)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Platform-Manager/style-guide">← Platform manager </a>
    <a href="../GraphQL-Storefront-API-Reference-xAPI/getting-started">Setting up environment for working with xAPI  →</a>
</div>