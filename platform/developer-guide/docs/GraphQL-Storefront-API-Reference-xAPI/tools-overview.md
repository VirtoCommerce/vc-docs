# Overview

The Storefront API (xAPI) is served over a single GraphQL endpoint, `POST /graphql` (locally, `http://localhost:10645/graphql`). You can browse its schema and run queries and mutations with any GraphQL client. This section covers the three tools used throughout this guide, each suited to a different task:

| Tool | Task |
| --- | --- |
| [GraphiQL](graphiql.md) | Interactive, in-browser exploration with live schema introspection and autocompletion. The quickest way to compose and run a query. |
| [Postman](postman.md) | Organized, repeatable testing: request collections, environments, variables, and setups you can share across a team. |
| [Curl](curl.md) | Scripted or command-line calls, for example in CI or quick one-off requests. |

A common path is to explore and compose queries in **GraphiQL** first, then move them into **Postman** (which can import the schema directly from GraphiQL) for repeatable testing, or into **Curl** for scripting.

All three send requests to the same `/graphql` endpoint and authenticate the same way, with a bearer token in the **Authorization** header.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../troubleshooting">← Troubleshooting</a>
    <a href="../graphiql">GraphiQL →</a>
</div>
