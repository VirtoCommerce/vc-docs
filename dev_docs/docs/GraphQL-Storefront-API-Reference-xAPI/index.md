# Overview

The main function of the Experience API (xAPI) project is to serve as a middle layer connecting clients and enterprise services using the GraphQL protocol. 

It is closely associated with a particular user or touchpoint experience and ensures quick and dependable access. Additionally, it serves as an implementation of the back end for front end (BFF) design pattern.

## Key сoncepts

* Utilize GraphQL protocol for precise and flexible data retrieval control from the API.
* Achieve fast and dependable indexed search through integration with:
    * [Elasticsearch 8.x](https://www.elastic.co/downloads/elasticsearch)
    * [Elastic App Search](https://www.elastic.co/downloads/app-search)
    * [Azure Search]()
* Maintain autonomy by exclusively relying on the index data source, separate from the rest of the VC data infrastructure.
* Capture tracing and performance metrics for request monitoring.

## Key features

The xAPI project provides the following major features:

- [Catalog](Catalog/overview.md)
- [Cart](Cart/overview.md)
- [Order](Order/overview.md)
- [Content](Content/overview.md)
- [Profile](Profile/overview.md)
- [Marketing](Quote/overview.md)
- [Quote](Quote/overview.md)

## How to use

You can explore the GraphQL API via:

* [Playground IDE](index.md#playground-ide)
* [Curl commands](index.md#curl)

### Playground IDE
To use an interactive [graphql-playground](https://github.com/prisma-labs/graphql-playground) environment, open `ui/playground` in the platform manager application.

```
http://localhost:10645/ui/playground
```

### Curl
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

## Next steps

* [Getting started with xAPI](getting-started.md)
* [Extending xAPI](x-api-extensions.md)

