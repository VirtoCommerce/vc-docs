# Getting started

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

1. Open [QraphQL playground]().
1. Open the **HTTP HEADERS** tab. 

    ![http headers](media/playground.png)

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
