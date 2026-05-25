# Set Up Environment For Working With xAPI

This section explains how to prepare your environment for testing xAPI.

## Prerequisites

* VC Platform 3.0 or higher.
* The Platform is configured to use Elasticsearch engine.
  ```json title="appsettings.json"
  "Search": {
      "Provider": "ElasticSearch",
      "Scope": "default",
      "ElasticSearch": {
          "Server": "localhost:9200",
          "User": "elastic",
          "Key": "",
          "EnableHttpCompression": ""
      },
      "OrderFullTextSearchEnabled": true
  }
  ```

## Presettings

To start using xAPI:

1. Open the Platform and go to **Settings**.
1. Select **Catalog**.
1. Select **Search**.
1. Enable **Store serialized catalog objects in index** option:

    ![Catalog-enabled](media/catalog-index-enabled.png){: style="display: block; margin: 0 auto;" }

1. Rebuild index.

## Test environment

!!! note
    If the xAPI module is not installed out-of-the-box, you can [install it](https://github.com/VirtoCommerce/vc-module-x-api) on the Platform (version 3.0) or higher by following [this guide](../Tutorials-and-How-tos/Tutorials/deploy-module-from-source-code.md). Then restart the Platform.

Open GraphQL UI playground in the browser by navigating to **http://{platform url}/ui/graphiql**, and run some sample queries.


## Examples


=== "Example 1"
    <div class="grid" markdown>

    ```json title="Query 1"
    query {
      product(
        storeId: "B2B-store"
        id: "cc81104c-8528-490b-a7a8-d1fb53ca164b"
        cultureName: "en-US"
        currencyCode: "USD"
      ) {
        id
        name
        descriptions {
          content
        }
      }
    }
    ```

    ```json title="Return 1"
    {
      "data": {
        "product": {
          "id": "cc81104c-8528-490b-a7a8-d1fb53ca164b",
          "name": "Affligem Blond 6x75cl Bottle",
          "descriptions": [
            {
              "content": "qwetest123"
            }
          ]
        }
      }
    }
    ```

    </div>

=== "Example 2"

    <div class="grid" markdown>

    ```json title="Query 2"
    query {
      products(
        query: "test"
        storeId: "B2B-store"
        currencyCode: "USD"
        cultureName: "en-US"
      ) {
        items {
          id
          name
          seoInfo {
            metaDescription
          }
        }
      }
    }
    ```

    ```json title="Return 2"
    {
      "data": {
        "products": {
          "items": [
            {
              "id": "05a51f40-c26d-47d4-a0c5-c13ab8f644d9",
              "name": "TEST stock < min",
              "seoInfo": {
                "metaDescription": ""
              }
            },
            {
              "id": "cb05e425-ced1-41bb-a28a-a1d592551bbf",
              "name": "TEST min  < max < stock",
              "seoInfo": {
                "metaDescription": ""
              }
            },
            {
              "id": "b0be673b-61bc-4912-b207-f4c3336f86e7",
              "name": "TEST min < stock < max",
              "seoInfo": {
                "metaDescription": ""
              }
            },
            // more items...
        }
      }
    }
    ```

    </div>



## Authorization and token usage

Some GraphQL queries and mutations require additional authorization. To test the query or mutation without authorization errors:

1. Open the [Virto Commerce API Docs (v1)](https://virtostart-demo-admin.govirto.com/docs/index.html) in your browser.
1. **Authorize** as an administrator or manager.

    ![Auth](media/authorization.png){: style="display: block; margin: 0 auto;" }

1. Expand **VirtoCommerce platform/POST/connect/token** section to fill in the required fields with appropriate credentials, then click **Execute**.

    ![token](media/token-field.png){: style="display: block; margin: 0 auto;" }

1. Copy the token that appears in the field below:

    ![token](media/token-code.png){: style="display: block; margin: 0 auto;" }

Providing token in GraphiQL is described in the [GraphiQL](graphiql.md) section. 

Providing token in Postman is described in the [Postman](postman.md#authorization-and-token-usage) section.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../">← xAPI module overview </a>
    <a href="../custom-module-creation">Creating xAPI module  →</a>
</div>