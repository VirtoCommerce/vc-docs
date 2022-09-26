# Overview
The project "Experience API" it is primarily a intermediated layer between clients and enterprise  services powered by GraphQL protocol and is tightly coupled to a specific user/touchpoint  experience with fast and reliable access, it represents an implementation of Backend for Frontend design pattern (BFF).

## Context Chart
Below, you can see the content chart for xAPI:

![image](https://user-images.githubusercontent.com/7566324/84039908-38258300-a9a2-11ea-9421-2c51462d69af.png)

## Key Concepts
- Use GraphQL protocol to leverage more selective and flexible control of resulting data retrieving from API;
- Fast and reliable indexed search thanks to integration with ES 7.x  and single data source for indexed search and data storage (<= 300ms);
- Autonomy. Shared nothing with rest VC data infrastructure except index data source;
- Tracing and performance requests metrics.

## Key Features
- [Catalog xAPI](Catalog/overview.md)
- [Cart xAPI](Cart/overview.md)
- [Order xAPI](Order/overview.md)

!!! warning
	The xAPI project can be integrated with Elastic Search 7.x and Azure Search Service for indexed search. Lucene search provider is not supported.

## How to use

### Playground IDE
To explore the GraphQL API, you can use an interactive  [graphql-playground](https://github.com/prisma-labs/graphql-playground) environment.
To open playground console open  `ui/playground` in the platform manager application.
```
http://localhost:10645/ui/playground
```

### Curl

```curl
POST https://{platform-url}/graphql
```

It accepts POST requests with following fields in a JSON body:
- `query` - String - GraphQL query as a string
- `variables` - Object - Optional - containing JSON object that defines variables for your query
- `operationName` - String - Optional - the name of the operation, in case you defined several of them in the query

Here is an example of a GraphQL query:

```curl linenums="1"
$ curl -X POST http://localhost:10645/graphql \
  -H "Content-Type:application/json" \
  -H "Authorization:Bearer ..." \
  -d '{"operationName":null,"variables":{},"query":"{ product(id: \"019e93d973cd4adab99b6f9cbb4ca97a\") { name }}"}'
```

## Next Steps

+ Learn how to get started with xAPI [here](getting-started.md)
+ Learn how to extend xAPI [here](x-api-extensions.md)