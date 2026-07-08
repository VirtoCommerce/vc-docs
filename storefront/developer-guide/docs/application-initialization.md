# Application Initialization

The Frontend bootstraps from a single GraphQL query, resolved by the store's domain, that returns a capability manifest for the Platform instance it is connected to. The manifest lists the store settings and the installed modules with their versions. With it, the Frontend plans every later query and includes or excludes optional features, for example white labeling, customer reviews, or quotes.

## Single bootstrap query benefits

Without a unified view of the backend, the Frontend (a Vue.js SPA) would start by making many independent GraphQL calls. That leads to several problems, which the bootstrap query prevents:

* Wasted requests for features that are not installed, for example querying `whiteLabeling` in `pageContext` when the module is absent.
* Runtime errors when the Frontend expects a GraphQL type that does not exist.
* No version compatibility contract between the Frontend and the backend modules.
* No single entry point describing the Platform instance the Frontend is connected to.

## Frontend initialization steps

At a high level, the Frontend initializes in four steps:

1. Load the SPA shell.
1. [Send the bootstrap query](#send-bootstrap-query) to fetch the capability manifest, then [cache the manifest](#cache-manifest) for the session.
1. [Build the feature map](#build-feature-map) from the manifest's installed-module list.
1. Run feature queries and [gate optional features](#gate-optional-features) down to the modules the feature map reports.

The sections below detail the query, caching, feature map, and gating.

## Send bootstrap query

The Frontend fires an anonymous `POST` to `{BACK_URL}/graphql` with the operation name `InitializeApplication`. The operation name is case-sensitive, so the browser Network panel can filter by it. The query is single-fire across navigations.

<div class="grid" markdown>

```json title="Query"
query InitializeApplication($domain: String!) {
  store(domain: $domain) {
    storeUrl
    settings {
      modules {
        moduleId
        version
        settings { name value }
      }
    }
  }
}
```

```json title="Variables"
{ "domain": "example.storefront.com" }
```
</div>

<br>
![Readmore](media/readmore.png){: width="25"} [Store query](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Store/queries/store/)

## Cache manifest

The manifest is cached per browser session under `localStorage["vc:initialStore:v1:<storefront-domain>"]` and is shared across tabs.

1. The Frontend loads **index.html**.
1. The Frontend checks the cached manifest for the current domain.
1. If a cached manifest exists, it is used.
1. Otherwise, the Frontend calls `InitializeApplication`, resolves the store and installed modules by domain, and stores the result under `vc:initialStore:v1:<domain>`.


## Build feature map

The feature map is the list of installed modules taken from the manifest. The Frontend builds it once from the cached manifest and uses it to decide which optional fields a query may request. Before a query is sent, the Frontend checks the map and removes any selection whose module is not installed.

## Gate optional features

Optional selections are gated with the `@needsModule` directive. The Apollo `apply-gates-link` strips any selection whose named module is absent from the manifest before the request leaves the browser, so there is no HTTP 400 and no "Cannot query field" error.

```graphql
query GetPageContext($domain: String, $userId: String, $permalink: String) {
  pageContext(domain: $domain, userId: $userId, permalink: $permalink) {
    user  { ...userTypeFields }
    store { ...storeResponseTypeFields }
    slugInfo { ...slugInfoResponseTypeFields }
  }
}
```

When `VirtoCommerce.WhiteLabeling` is absent from the manifest, both the inline `whiteLabelingSettings { ... }` selection and the dependent fragment definition are stripped from the outgoing request. Any field contributed by `VirtoCommerce.WhiteLabeling` is gated this way.

## Suppress version fingerprinting

The `XAPI.Security.ReturnModuleVersion` setting controls whether module versions are returned in the manifest. Open the Admin UI, then go to **Settings** → **Platform** → **Security** → **Return module version**. The default is on.

When the setting is off, `version` returns an empty string, which preserves the non-null `String!` contract, and modules without public settings drop from the list. Turn it off for public-facing production Frontends to suppress version fingerprinting.

## Validate module versions

In non-production builds, the Frontend compares the installed module versions from the manifest against the minimum versions it was built to require. When an installed module is older than the required minimum, the Frontend shows a warning so the operator can upgrade the backend.

The warning fires only when all of the following hold:

* `XAPI.Security.ReturnModuleVersion` is on. Otherwise versions are empty and the comparison is skipped.
* The Frontend is running in non-production mode, for example dev, QA, or staging. Production builds suppress the warning, so customers never see it.
* At least one installed module is strictly lower than the Frontend's required minimum.

The warning lists only the out-of-date modules. Each row reads as follows:

```
<moduleId>   <expected-minimum>   ≥   <installed-version>
```

For example, `VirtoCommerce.Catalog 3.1022.0 ≥ 3.1020.0` means the Frontend requires Catalog 3.1022.0 or higher but the Platform reports 3.1020.0, so Catalog must be upgraded. The warning reads from the live manifest, so rerunning `InitializeApplication` after an upgrade clears it on the next refresh without a manual cache purge.

When the warning appears, the operator should:

1. Click **Copy to clipboard** to capture the full mismatch list as plain text.
1. Share the list with the Platform team.
1. Upgrade each listed module to at least the expected minimum on the left of the row.
1. Hard-refresh the Frontend. The warning disappears on the next manifest fetch.

Once the manifest is cached and validated, the Frontend queries only the modules the Platform actually provides, which keeps requests lean and avoids runtime errors.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../architecture">← Frontend Application Architecture</a>
    <a href="../modules-architecture/modules-architecture">Modules Architecture →</a>
</div>