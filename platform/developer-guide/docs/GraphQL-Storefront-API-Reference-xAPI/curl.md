# Curl

To interact with the GraphQL API, use Curl commands: 

```curl
POST https://{platform-url}/graphql
```

By sending POST requests to the specified endpoint and including the necessary fields in the JSON body, you can retrieve the desired data. Here's an example of how to structure your Curl command to query the API.

| Field           	| Description                                                    	|
|-----------------	|----------------------------------------------------------------	|
| `query`         	| GraphQL query as a string.                                     	|
| `variables`     	| JSON object that defines variables for your query.             	|
| `operationName` 	| The name of the operation, if there are over one in the query. 	|

**Sample query**

```curl linenums="1"
$ curl -X POST http://localhost:10645/graphql \
  -H "Content-Type:application/json" \
  -H "Authorization:Bearer ..." \
  -d '{"operationName":null,"variables":{},"query":"{ product(id: \"019e93d973cd4adab99b6f9cbb4ca97a\") { name }}"}'
```
