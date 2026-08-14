# Curl

To interact with the GraphQL API from the command line, send POST requests to the `/graphql` endpoint with curl:

```text
POST https://{platform-url}/graphql
```

Include the query and any variables in the JSON body of the request:

| Field | Description |
| --- | --- |
| `query` | GraphQL query as a string. |
| `variables` | JSON object that defines variables for your query. |
| `operationName` | The name of the operation, if there is more than one in the query. |

## First API call

To make your first request, send a query in the JSON body of a POST to the `/graphql` endpoint. This example fetches a product by ID from the B2B-store:

```bash
curl -X POST https://{platform-url}/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"query { product(storeId: \"B2B-store\", id: \"cc81104c-8528-490b-a7a8-d1fb53ca164b\", cultureName: \"en-US\", currencyCode: \"USD\") { id name } }"}'
```

The response returns the requested fields:

```json
{
  "data": {
    "product": {
      "id": "cc81104c-8528-490b-a7a8-d1fb53ca164b",
      "name": "Affligem Blond 6x75cl Bottle"
    }
  }
}
```

!!! note
    Some queries and mutations require a signed-in user. Add the token as a header: `-H "Authorization: Bearer <token>"`. See [Authentication](authentication.md) to obtain one.

You have now made your first xAPI request with curl.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../postman">← Postman </a>
    <a href="../best-practices">Best practices →</a>
</div>
