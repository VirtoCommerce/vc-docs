# Overview

GraphiQL is an interactive IDE for exploring and testing GraphQL APIs. It allows developers to inspect schemas, execute queries and mutations, and receive immediate feedback. Virto Commerce provides developers the flexibility to work with a fully integrated API for the entire Platform or with tailored APIs for specific modules.

## GraphiQL

By default, GraphiQL is disabled. To enable it, configure the following setting in the **appsettings.json** file:

```json title="appsettings.json"
"GraphQLPlayground": {
  "Enable": true
}
```

1. Access the interactive [GraphiQL](https://github.com/graphql/graphiql) environment at the following URL: http://localhost:10645/ui/graphiql or open it via **Developer tools** in the main menu:

    Once in the GraphiQL environment, you can send GraphQL queries or mutations. The interface is as follows:

    ![Playground fields](media/playground-fields.png)

1. Compose your GraphQL query or mutation in the left panel. Fields are autocompleted based on the schema.
1. If necessary, specify variables in the **Variables** tab. 

    !!! info
        Some variables can be obtained from other queries. For example, you can retrieve the user ID by executing the `createUser` mutation, and to obtain the cart ID, you can use the `cart` query.


1. To provide a token:
    1. Open the **Headers** tab. 

    1. Paste the token as follows:

        ```json linenums="1"
        {
            "authorization": "Bearer your-bearer-token"
        }
        ```

        ??? Example "View sample"
            ```json
            {
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkM5QjVEMTJENjNDREI5Qzg5RTk1NEVCNTcyRjdERkFBQTNFRjgyNEMiLCJ4NXQiOiJ5YlhSTFdQTnVjaWVsVTYxY3ZmZnFxUHZna3ciLCJ0eXAiOiJhdCtqd3QifQ.eyJuYW1lIjoiMWViMmZhOGFjNjU3NDU0MWFmZGI1MjU4MzNkYWRiNDYiLCJzdWIiOiJhZG1pbiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2VtYWlsYWRkcmVzcyI6ImFkbWluQHZjLWRlbW9zdG9yZS5jb20iLCJyb2xlIjoiX19hZG1pbmlzdHJhdG9yIiwibWVtYmVySWQiOiIiLCJvaV9hdV9pZCI6ImE3M2FkMzU3LTZlMTMtNDIxOS1hMzJmLTBhOWJiNjM4NmEyZSIsIm9pX3Rrbl9pZCI6ImE1YjA4ODQ5LWI1Y2MtNDAyZi04YTJmLTNjZDljYTQyMmJjNiIsImF1ZCI6InJlc291cmNlX3NlcnZlciIsInNjb3BlJbzSZkNLe_3pHA2zf_nPQBCwbum_wYPTbOEHNap-A"
            }
            ```

1. Execute your query or mutation by clicking the **Play** button.


## Partial GraphQL schema

A **partial GraphQL schema** refers to a modular and self-contained subset of the overall GraphQL schema that is specific to a particular module. Instead of a single schema for the entire Platform, modules like Cart, Catalog, or Quotes have their own schema that defines only the queries, mutations, types, and subscriptions relevant to that module.

Partial schema allows to:

* **Request schema by module**: Focus only on the API definitions related to a specific module, reducing unnecessary complexity.
* **Generate client-by-demand**: Create tailored GraphQL clients based on the module's schema, making the development process faster and more modular.

### Enable partial GraphQL schema

1. Install [Virto Commerce xApi, version 3.814+](https://github.com/VirtoCommerce/vc-module-x-api/releases/tag/3.814.0)
1. Add a `ScopedSchemaFactory` instance to the service collection:

    ```csharp
    serviceCollection.AddSingleton<ScopedSchemaFactory<AssemblyMarker>>();
    ```

1. Enable `UseSchemaGraphQL` in `PostInitialize` specifying the name of the parted module (**quote** in this example):

    ```csharp
    appBuilder.UseScopedSchema<AssemblyMarker>("quote");
    ```

Now, you can access partial GraphQL schema for the Quote module at the following URL:

http://localhost:10645/ui/graphiql/quote

Similarly, you can access other partial schemas by adding the appropriate slugs to the URL:

| Module          | Slug              |
|-----------------|-------------------|
| Push Messages   | /pushmessages     |
| Customer review | /customerreviews  |
| Catalog         | /catalog          |
| Cart            | /cart             |
| Order           | /order            |



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../update-xapi-modules">← Updating xAPI modules </a>
    <a href="../postman">Postman  →</a>
</div>