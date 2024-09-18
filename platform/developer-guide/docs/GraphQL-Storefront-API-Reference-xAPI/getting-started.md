# Get Started

This section explains how to prepare your environment for testing xAPI.

## Prerequisites

* VC platform 3.0 or higher.
* The platform is configured to use ElasticSearch engine.
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

    ![Catalog-enabled](media/catalog-index-enabled.png)

1. Rebuild index.

## Test environment

To set up the test environment:

1. Install `vc-module-experience-api` on the platform version 3.0 or higher, using [this guide](https://github.com/VirtoCommerce/vc-platform/blob/master/docs/developer-guide/deploy-module-from-source-code.md).
1. Restart the platform instance.
1. Open GraphQL UI playground in the browser: **http://{platform url}/ui/playground**

??? "View sample request"
    ```json
    {
      product(id: "0f7a77cc1b9a46a29f6a159e5cd49ad1")
      {
        id
        name

        properties {
          name
          type
          values
        }
      }

      products(query: "sony" fuzzy: true filter: "price.USD:(400 TO 1000]")
      {
        totalCount
        items {
          name
          id
          prices (currency: "USD") {
            list
            currency
          }
        }
      }
    }
    ```

## Authorization and token usage

Some GraphQL queries and mutations require addition authorization. To test the query or mutation without authorization errors:

1. Open the [Virto Commerce API Docs (v1)](https://virtostart-demo-admin.govirto.com/docs/index.html) in your browser.
1. **Authorize** as an administrator or manager.

    ![Auth](media/authorization.png)

1. Expand `POST/connect/token` section to fill in the required fields with appropriate credentials, then click **Execute**.

    ![token](media/token-field.png)

1. Copy the token that appears in the field below:

    ![token](media/token-code.png)

Providing token in Playground is decribed in the [Playground](playground.md) section. 

Providing token in Postman is described in [Postman](postman.md#authorization-and-token-usage) section.


