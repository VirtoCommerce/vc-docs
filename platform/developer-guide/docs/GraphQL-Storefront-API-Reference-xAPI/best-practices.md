# Best Practices

This technical guide distills key best practices for using GraphQL effectively in frontend development. It covers query optimization, strategic data fetching, reusability with fragments, caching/fetch policies, and advanced features like optimistic updates. These practices help avoid common pitfalls, reduce network overhead, and make your app feel responsive.

## Request only what you need

In GraphQL, every field costs bytes and processing time. Over-fetching bloats responses, slows apps, and wastes resources. Follow these rules strictly:

* Request fields only if:

    * They are displayed on screen (e.g., product name in a card).
    * Used for logic (e.g., price for sorting, even if not shown).
    * Needed as keys (e.g., ID/slug for routing or URLs).

* Don't query extras like full descriptions if unused - they increase load times and risk spreading inefficiencies (e.g., copied queries inherit bloat).

!!! tip
    When coding fast or copying queries, pause and ask: "Does this component *really* need this field?" Use TypeScript-generated types (covered later) to catch removals that break the app.

## Strategize queries

A common mistake is trying to fetch everything for a page in one giant query. Instead, use these two strategies:

* [Splitting queries by user flow.](#split-queries-by-user-flow)
* [Combining resources for single actions/blocks.](#combine-resources-for-single-actionsblocks)

### Split queries by user flow

Split queries when data serves different UI blocks or flows: load main content first, then secondary blocks asynchronously. This avoids blocking the user and makes the app feel faster.

For example, step-by-step flow in catalog page is as follows:

| Step name                  | Step description      | Action        | GraphQL strategy       | Benefit   |
| ----------------------------- | --------------------------| --------------| ------------------------------ | -------------|
| 1. Lightweight summary (Initial load)     | The first page load focuses on quick scanning rather than deep engagement. | User views a list or category page with a grid of products. | Request a lightweight `ProductSummary` query containing only essential fields (ID, name, price, thumbnail). | Extremely fast initial load due to minimal payload size.                                            |
| 2. Detailed view (Interest)               | Data is expanded only after the user shows interest in a specific item.    | User clicks on a product to view its details.               | Fetch `ProductDetails` with additional fields such as descriptions, full-size images, and specifications.   | Prevents over-fetching data for products the user does not interact with.                           |
| 3. On-demand heavy data (Specific intent) | Large or expensive data is loaded only when explicitly requested.          | User opens a “Read Reviews” or similar secondary tab.       | Trigger a separate `ProductReviews` query on demand.                                                        | Keeps the product page fast and responsive while still allowing access to rich content when needed. |


### Combine resources for single actions/blocks

If a single UI element (like a search dropdown) needs data from different sources, fetch them in **one** query to reduce network round-trips:

```graphql
query SearchAll($term: string!) {
    products: searchProducts(query: $term, first: 10) {
        items { id name price imageUrl }
    }
    categories: searchCategories(query:$term, first: 5) {
        items { id name slug }
    }
    pages: searchPages(query:$term, first: 3) {
        items { id title snippet }
    }
}
```

## Reuse fragments

As frontend applications grow, the same UI components often appear in multiple places and rely on the same data.

For example, a **Product card** component appears in many places:

* Catalog.
* Search results.
* Recommended products.
* Cart.
* Wish lists, etc.

Each product card needs the same fields:

* `id`
* `name`
* `price`
* `image`

The most common approach is to copy and paste these fields into every query. This works until it doesn’t.

When you add a new field to the product card (for example, a badge or rating), you update the catalog query, test it, and everything looks fine. But the search query still uses the old field set. Now search breaks in production.
This kind of inconsistency is one of the most common causes of frontend GraphQL errors.

Fragments allow you to define a set of fields once and reuse it across multiple queries. Instead of copying fields everywhere, you describe the data shape in one place and include it wherever needed. This is a direct application of the **DRY (Don’t Repeat Yourself)** principle.

Define a fragment once:

```graphql
fragment ProductSummary on Product {
  id
  name
  price
  image
}
```

... and reuse it across multiple queries:

```graphql
query CatalogProducts {
    products { ...ProductSummary }
}

query RecommendedProducts {
    recommended { ...ProductSummary }
  }
...
```

If the product card changes, you update the fragment and every query stays in sync automatically.

|:white_check_mark: **When to use** | :no_entry: **When not to use**|
|--- | ---|
|One part of query is used in multiple queries (for example, product cards in catalog, search, and recommendations). | Fields are used only once, making a fragment unnecessary overhead.|
|Consistent data shapes are required across features (for example, a shared `Money` or `Price` fragment used throughout the app). | Fragments are created for very small or single-field selections.|
|Multiple teams or features depend on the same data structure, with fragments acting as a shared contract. | Fields are grouped only by name rather than meaning (for example, reusing `id` and `name` across unrelated types such as `Product` and `Order`).|

Fragments should reflect **UI intent**, not just shared field names.

## GraphQL caching and fetching on the Frontend

This section explains how GraphQL caching works on the frontend, how Apollo Client manages cached data, and how fetch policies help balance performance, freshness, and reliability in real-world applications.

### Caching

Caching is where GraphQL truly shines - and also where many subtle bugs originate. When configured correctly, caching can make a web application feel as fast and responsive as a native mobile app. When misunderstood, it can lead to confusing UI behavior that is hard to debug.

GraphQL caching enables best experience on the web:

* The UI responds instantly.
* There are no spinners.
* Data feels immediately available.

When data is already in the client cache, Apollo Client can return it immediately without waiting for a network request. The result is an application that feels fast, fluid, and reliable.

Apollo Client uses a technique called **normalization**:

* Every object returned from GraphQL is stored in the cache using:
    * Its **__typename** (for example: `Product`, `Order`, `Category`).
    * Its **key**.  In many cases, the key is a simple `id`, but this is not a requirement. A cache key can also be derived from:

        * A combination of fields (for example, `errorCode + objectId + objectType` for error objects).
        * A domain-specific identifier (for example, a coupon code).

  For example, if you query a product with id `123`, Apollo stores it as `Product:123`-->{id: "123",...}

* Once this object is cached:

    * Any future query requesting `Product:123` receives it instantly.
    * No additional network request is needed.
    * The same object is reused everywhere.

This prevents data duplication and ensures that updates automatically propagate across the UI.


### Fetching

Fetch policies define how Apollo Client interacts with the cache and the network.

|**Fetch policy**|**Description**|
| --- | --- |
|**cache-first** (default)|Provides a fast response by returning data from the cache if it is available and **does not** send a network request in that case.|
|**cache-and-network** (recommended)|Initially shows data from the cache and then performs a background refresh from the network.|
|**network-only**|Always fetches data from the network and returns the server response. The result **is written to the cache**, replacing any existing cached data for the same fields.|
|**no-cache**| Always fetches data from the network and returns the server response, but **does not write the result to the cache**.|
|**cache-only**|Attempts to use the cache; if the data is not present, the request fails.|
|**standby**|The query does not run automatically; it must be triggered manually.|

![Read more](media/readmore.png){: width="20"} [Supported Fetch Policies](https://www.apollographql.com/docs/react/data/queries#supported-fetch-policies)


#### cache-and-network

This is the most commonly used and recommended policy:

* Data is returned from cache immediately (if available).
* A network request is sent in the background.
* If new data matches the cache, nothing changes.
* If data differs, the UI updates automatically.
* If the request fails, the UI safely reverts and shows an error.

This approach provides instant feedback while still ensuring freshness.

#### network-only

Some data changes frequently and should always be up to date, such as:

* Prices.
* Stock levels.
* Time-sensitive promotions.

In these cases, use `network-only` to bypass the cache entirely and always fetch from the server.

### Client-side cache configuration

All caching behavior is managed by **Apollo Client** on the frontend:

* The cache lives **in memory in the browser**.
* No custom cache implementation is required.
* Apollo handles normalization automatically.
* Most setups work well out of the box with minimal configuration.

You can define fetch policies per query depending on the data’s nature.

### Cache lifetime and updates

Apollo Client does **not** support time-based cache expiration (TTL). Cached data remains until the page is refreshed. This is usually acceptable since users refresh pages regularly.

For data that must refresh periodically, use **Polling** (refetch data every N seconds or minutes). This approach works well for dashboards, promotions, or live data.

### Common caching pitfalls

| Pitfall                          | Description           | Solution         |
| ---------------| --------------------------------------|------------------------------ |
| List and filter cache collisions | When switching filters (e.g., from **shoes** to **jackets**), users continue seeing the previous results. This happens when query arguments are not included in cache keys, causing different queries to overwrite each other in the cache. | Ensure all query arguments are included in cache keys. Use Apollo Cache DevTools to verify that cached entries are stored with their arguments. |
| Duplicate items in lists         | Users see the same product repeated multiple times in lists. This typically occurs when backend IDs are unstable or change between requests, causing the cache to treat the same item as different entities.                            | Inspect cached object IDs using Apollo Cache DevTools and ensure the backend returns stable, consistent identifiers for all entities.           |


### Debugging with Apollo Cache DevTools

Apollo Cache DevTools is one of the most valuable tools when working with GraphQL.

What it allows you to do:

* Inspect cache structure.
* View normalized entities.
* Check cache keys and arguments.
* Run queries with different variables.
* Debug list collisions and duplication.

It works as a browser extension and is available for Chrome and Firefox (and works in Chromium-based browsers).

If cached data behaves unexpectedly, this should be your first stop.


### Tools and automation

- **Apollo Cache DevTools**: Free browser extension for debugging cache, arguments, and running sandbox queries. Essential for spotting pitfalls.
- **TypeScript Integration**: Generate types from schema - removing unused fields throws errors, helping cleanup.
- **Linters/Automation**: No built-in tool for auto-highlighting unused fields yet, but search for GraphQL linters. Manually review with dev tools.

For automation, use TypeScript to enforce; consider custom scripts to analyze queries vs. component usage.


## Optimistic updates

Optimistic updates are a powerful GraphQL feature that makes web apps feel like native mobile apps - responsive and snappy. They provide immediate UI feedback by assuming a successful server response, then confirming in the background.

When a user performs an action (e.g., clicking "+" to increase quantity), Apollo Client updates the local cache instantly with an "optimistic" version of the data. The UI re-renders immediately. Meanwhile, the real network request runs. On success, the cache updates with actual data (often seamless if it matches). On error, it reverts and shows an error.

For example, in a cart, adding items or changing quantity updates the UI instantly without delays or spinners. Users sometimes think it's "too fast".

|:white_check_mark: **When to use** | :no_entry: **When not to use**|
|--- | ---|
|Instant UI feedback is required and waiting for the server would noticeably degrade the user experience. | Showing data before server confirmation would confuse or mislead the user with “false” or premature information.|
|The change can be safely undone if the server responds with an error or different data. | The change causes irreversible consequences in frontend logic.|

!!! tip
    In your mutation, add an `optimisticResponse` object mimicking the expected server response.

## Mutations

Mutations are GraphQL's way to modify data (like POST, PUT, or DELETE in REST):

* Add a product to cart.
* Change quantity.
* Update customer profile.
* Place an order.

They change server state and should return the new state for automatic cache updates. For example, when you add an item to the cart:

1. The mutation executes on the server.
1. The server returns the updated cart.
1. The frontend receives the new cart state.

### Mutations and cache updates

There are two strategies for updating cache:

| **Strategy**                            | **Use cases**                   |
| --------------------------------------- | --------------------------------- |
| **Automatic cache updates** (preferred) | Use when the mutation returns the **full updated entity**. Apollo can automatically merge the response into the cache, replacing the existing object. This is preferred when the payload size is acceptable and the entity already exists in the cache.|
| **Manual cache updates** (when needed)  | Use when the mutation returns only a confirmation (for example, `success: true`), when returning the full entity would be too heavy, or when you need to update only **a specific part of the cache** without refetching the entire object. |

This distinction is critical when designing your mutation API and frontend logic.

## GraphQL response structure

A GraphQL response can contain **both successful data and errors at the same time**. A typical response looks like this:

```graphql
{
  "data": {                        //Contains everything that was resolved successfully.
    "products": { "items": [...] },   
    "categories": { "items": [...] },
    "articles": null
  },
  "errors": [ ... ],               //Describes what failed, including error messages and reasons.
  "extensions": { ... }           //Metadata such as tracing, performance, or custom server info.
}
```

Even when errors occur, GraphQL responds with **HTTP 200**. This is because the HTTP status reflects **transport success**, not business logic success. Therefore, you must always inspect the **GraphQL response body**, not just the HTTP status code, to handle errors correctly.

One of GraphQL’s strengths is that **a single query can return partial data**. For example, a search request might fetch:

* Products.
* Categories.
* Articles.

If:

* Products and categories load successfully.
* The article service is temporarily down.

Then:

* `products` and `categories` contain data.
* `articles` is `null`.
* An error is included explaining why articles failed.

This is expected behavior - not a failure of GraphQL. The best strategy is this case will be **graceful degradation**.

### Graceful degradation

**Graceful degradation** is the practice of designing the UI to continue working with partial data when some parts of a GraphQL response fail.
Because GraphQL can return successful data alongside errors, the UI should render what succeeded instead of failing entirely, avoiding all-or-nothing error handling and ensuring one broken field or service does not break the whole page.

#### Bad approach: All-or-nothing rendering

```
<template>
  <div v-if="error">
    Something went wrong
  </div>
  <SearchResults v-else-if="data" />
</template>
```

This approach hides **all valid data** just because **one part failed**. It leads to poor user experience and wasted successful responses.


#### Recommended approach: Block-level rendering

Render each part of the response independently and handle errors locally without breaking the entire UI:

```
<template>
  <div class="search-results">
    <ProductResults
      v-if="data?.products"
      :products="data.products.items"
    />

    <CategoryResults
      v-if="data?.categories"
      :categories="data.categories.items"
    />

    <ArticleResults
      v-if="data?.articles"
      :articles="data.articles.items"
    />

    <!-- Articles failed -->
    <div v-else-if="articlesError" class="articles-error">
      Help articles temporarily unavailable
      <button @click="refetch">Try again</button>
    </div>
  </div>
</template>
```

#### Type safety

GraphQL schemas evolve. For example:

1. A backend team renames a field from `name` to `title`.
1. Your frontend still queries `name`.
1. Everything compiles, but the UI breaks in production.

This is a common and serious risk, which can be resolved with the **generated types**. GraphQL supports **automatic type generation** based on the schema. 

Using tools like **GraphQL Code Generator**, you can:

* Generate TypeScript types from the schema.
* Generate typed hooks and query results.
* Catch breaking schema changes at **build time**, not in production.

This protects you from:

* Field renames.
* Field removals.
* Type changes.
* Nullability changes.

If something changes in the schema, your build fails immediately, exactly when you want it to.

## Debugging 

When diagnosing issues, the most useful tools are:

* **Apollo Cache DevTools** (Browser Extension): Inspect cache structure, run queries with variables, simulate issues. Available for Chrome/Firefox (likely Edge). Essential for cache pitfalls.
   
* **Browser Network Tab**: Check request timings, sizes, and which code triggers them. Spot slow queries or bloat.

* **GraphQL Playground/Postman**: Test queries/mutations as documentation. Build, execute, and debug before coding.

Install Apollo DevTools immediately - it's free and saves hours.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../multiregional-development">← Multiregional development </a>
    <a href="../troubleshooting">Troubleshooting  →</a>
</div>