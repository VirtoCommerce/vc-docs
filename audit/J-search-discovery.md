# Group J — Search & Discovery

## Claim 1: Elasticsearch configuration (vs Azure Search, Lucene) is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure Elasticsearch vs Azure Search vs Lucene in VirtoCommerce?"):
Returned concrete `appsettings.json` snippets for Lucene, Azure Search, Elasticsearch 7.x with and without security (ApiKey auth), plus the xAPI getting-started config. Dedicated pages for each provider under `platform/developer-guide/docs/Fundamentals/Indexed-Search/integration/` and `platform/user-guide/docs/{elastic-search,azure-search,lucene}/`.

**WebSearch**: n/a — Context7 returned comprehensive content.

**Grep** (scope: DOCS):
- `grep -rli "elasticsearch" DOCS`: 48 files
- `grep -rli "azure search|azuresearch" DOCS`: 21 files
- `grep -rli "lucene" DOCS`: 30 files
- Top hits: `PlatformDeveloperGuide/.../Indexed-Search/integration/configuring-elasticsearch.md`, `configuring-azure-cognitive-search.md`, `integration/lucene.md`; `PlatformUserGuide/.../elastic-search/`, `azure-search/`, `lucene/` subtrees each with `overview.md` + `settings.md`.

**Verdict**: ✅ Well documented
**Note**: Multiple provider pages + `appsettings.json` recipes + xAPI integration notes. Claim rejected.

---

## Claim 2: OpenSearch support is absent

**Context7** (`/virtocommerce/vc-docs`, query bundled with claim 3 below): Returned a dedicated OpenSearch module page: "The Virto Commerce OpenSearch module implements the ISearchProvider interface... utilizes the OpenSearch engine." Also noted Amazon OpenSearch Service is a supported hosting target for the Elasticsearch module.

**WebSearch**: n/a.

**Grep** (scope: DOCS):
- `grep -rli "opensearch" DOCS`: 11 files
- Top hits: `PlatformUserGuide/.../opensearch/overview.md`, `PlatformUserGuide/.../opensearch/settings.md`, `PlatformDeveloperGuide/.../Indexed-Search/integration/opensearch.md`, plus mentions in `search/overview.md`, `search/managing-search.md`, `appsettingsjson.md`, and `elastic-search/overview.md`.

**Verdict**: ✅ Well documented
**Note**: First-class provider module with user and developer docs — claim clearly wrong.

---

## Claim 3: Algolia / Typesense / Meilisearch alternatives are absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support OpenSearch, Algolia, Typesense, Meilisearch, vector/semantic search, autocomplete/typeahead?"):
"Available providers include Elasticsearch (7.x, 8.x, 9.x/10.x), OpenSearch, Elastic App Search, Lucene (for local development), Azure Cognitive Search, and Algolia." Dedicated `integration/algolia.md` page. Typesense and Meilisearch: no results.

**WebSearch** (query: "e-commerce platform Typesense Meilisearch Shopify commercetools search integration 2026"): Typesense/Meilisearch are real commerce-adjacent alternatives to Algolia, widely adopted in storefront retrofits (e.g., Shopify→Typesense case study). Their absence from a commerce platform's provider matrix is a real gap, though not universal.

**Grep** (scope: DOCS):
- `grep -rli "algolia" DOCS`: 18 files (incl. `PlatformDeveloperGuide/.../Indexed-Search/integration/algolia.md`, `PlatformUserGuide/.../algolia/overview.md`)
- `grep -rli "typesense" DOCS`: 0 files
- `grep -rli "meilisearch" DOCS`: 0 files

**Verdict**: 🟡 Mentioned but thin (split)
**Note**: Algolia ✅ well documented. Typesense and Meilisearch 🔴 absent. Splitting the claim: Algolia is a full provider module; Typesense/Meilisearch genuinely missing from the provider catalogue.

---

## Claim 4: Faceted search / guided navigation docs are thin

**Context7** (via follow-up): `Catalog/examples/facets.md` and `x-api-extensions.md` for xAPI; `Indexed-Search/search/faceted-search.md` for the backend.

**WebSearch**: n/a.

**Grep** (scope: DOCS):
- `grep -rli "facet" DOCS`: 51 files
- Top hits: `PlatformDeveloperGuide/.../Indexed-Search/search/faceted-search.md` (dedicated page), `GraphQL-Storefront-API-Reference-xAPI/Catalog/examples/facets.md`, `elastic-app-search-overview.md`, `elastic-search-8.md`, `elastic-search-9.md`, `Intent-Search/overview.md`, plus multiple release-notes entries for facet features.

**Verdict**: ✅ Well documented
**Note**: Dedicated faceted-search page, xAPI facet examples, provider-specific facet notes. "Guided navigation" as a marketing phrase is not used, but the capability is thoroughly covered.

---

## Claim 5: Synonym / stopword / stemming tuning is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I tune synonyms, stopwords, stemming, boosting/relevance, zero-result report, and merchandising rules in VirtoCommerce search?"):
"Elastic App Search allows you to adjust search relevance and promote or demote results... Key features for tuning include Synonyms, Curations, and Relevance Tuning." Synonym-set creation walkthrough with screenshots exists in the App Search docs. No hits for stopwords or stemming.

**WebSearch**: Adobe Commerce Live Search exposes all three (synonyms, stopwords, stemming implicit); it's industry-standard vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "synonym" DOCS`: 13 files
- `grep -rli "stopword|stop word|stemming|stemmer" DOCS`: 0 files
- Top hits: `PlatformUserGuide/.../elastic-app-search/search-relevance-tuning.md:30` — "The Synonym feature builds synonym sets containing two or more queries that have similar meanings. Each synonym set can contain up to 32 words." + step-by-step create/save UI.

**Verdict**: 🟡 Mentioned but thin (split)
**Note**: Synonyms ✅ via Elastic App Search. Stopwords and stemming 🔴 not mentioned at all — significant gap vs Adobe Commerce / Algolia / Shopify Search & Discovery, which all document these explicitly.

---

## Claim 6: Vector search / semantic search / embeddings is absent

**Context7**: `Fundamentals/Intent-Search/overview.md` describes an "Intent Search" module using Weaviate as the vector database for semantic search, intent classification, and product categorization. Elasticsearch docs describe ELSER + dense/sparse vector models for semantic search with ELSER as the default recommendation.

**WebSearch**: n/a.

**Grep** (scope: DOCS):
- `grep -rli "vector search|semantic search|vector database" DOCS`: 33 files
- Top hits: `PlatformDeveloperGuide/.../Fundamentals/Intent-Search/overview.md`, `Intent-Search/installation-and-configuration.md`, `Configuration-Reference/appsettingsjson.md:2415` ("Intent Search module uses Weaviate as its vector database for semantic search"), `PlatformUserGuide/.../intent-search/overview.md`, `PlatformUserGuide/.../elastic-search-9/overview.md:7` ("Elasticsearch provides semantic search capabilities using natural language processing (NLP) and vector search... ELSER").

**Verdict**: ✅ Well documented
**Note**: Claim clearly rejected. VC has a dedicated Intent Search module (Weaviate-backed) plus ELSER-based semantic search inside the Elasticsearch module. Embedding vocabulary appears throughout.

---

## Claim 7: Autocomplete / typeahead / "did you mean" is thin

**Context7**: Returned `productSuggestions` GraphQL query page ("This query provides product name suggestions based on partial user input. It is typically used for autocomplete functionality in search fields.") and product-feature copy about "AI-enhanced search with autocomplete, filtering, and voice queries."

**WebSearch**: n/a (capability clearly exists in industry).

**Grep** (scope: DOCS):
- `grep -rli "autocomplete|typeahead|type-ahead|did you mean" DOCS`: 10 files
- Top hits: `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/Catalog/queries/productSuggestions.md` (dedicated autocomplete query), `Catalog/objects/ProductSuggestionsQueryResponseType.md`, `VirtoCommerce/features.md:82`. No "did you mean" (spell-correct) doc beyond B2B marketing articles.

**Verdict**: 🟡 Mentioned but thin
**Note**: Autocomplete is a first-class xAPI query, but there is no end-to-end walkthrough (admin setup, trigger thresholds, field weighting). "Did you mean" / spell correction is not documented as a configurable feature at all.

---

## Claim 8: Boosting / relevance tuning is thin

**Context7**: `search-relevance-tuning.md` ("Synonyms, Curations, and Relevance Tuning"); `appsettingsjson.md` exposes a `SearchBoost` C# struct with `FieldName`, `Value`, `Preset`; Elastic App Search overview covers "Dynamic boosting concatenation, combining dynamic boosting with query and static boosting from the Search Relevance Tuning panel."

**WebSearch**: Adobe Commerce/Algolia document boost, bury, pin, hide as "merchandising rules" with up to 25 events per rule. VC uses the same vocabulary ("boost/bury" appears in App Search).

**Grep** (scope: DOCS):
- `grep -rli "boost|relevance" DOCS`: 78 files
- Top hits: `Indexed-Search/integration/elastic-app-search-overview.md:21`, `Indexed-Search/integration/search_relevance_tuning.md`, `PlatformUserGuide/.../elastic-app-search/search-relevance-tuning.md`, `appsettingsjson.md` (SearchBoost object).

**Verdict**: ✅ Well documented (but coupled to Elastic App Search provider)
**Note**: Capability is thoroughly documented, but only through the Elastic App Search provider and programmatic SearchBoost presets. There is no cross-provider "how to tune relevance with Azure/OpenSearch" guidance — a minor gap.

---

## Claim 9: Search analytics / zero-result report is thin

**Context7**: `search-relevance-tuning.md` explicitly contains a "Top queries with no results" section with screenshot.

**WebSearch**: Zero Results report is a standard Adobe Commerce Live Search metric — "measures the percentage of search queries... that return no results... lists the search queries that return no results and the number of times used during the specified date range."

**Grep** (scope: DOCS):
- `grep -rli "zero result|zero-result|no results|search analytics|search report" DOCS`: 11 files
- Top hits: `PlatformUserGuide/.../elastic-app-search/search-relevance-tuning.md:22` — "In the **Top queries with no results** section, you can find query results"; same text at `PlatformDeveloperGuide/.../integration/search_relevance_tuning.md:22`. Several B2B-Experts thought-leadership pieces also discuss the metric.

**Verdict**: 🟡 Mentioned but thin
**Note**: Zero-results report exists in Elastic App Search provider docs but is not surfaced as a platform-wide search-analytics feature. No dashboards for click-through rate, search-to-conversion, or trending queries across other providers.

---

## Claim 10: Personalized search / merchandising rules are thin

**Context7**: Elastic App Search docs list "Synonyms, Curations, and Relevance Tuning" — "Curations" is the feature that maps to merchandising (promote/demote/pin/hide). No dedicated merchandising page; no cross-provider personalization doc.

**WebSearch**: Adobe Commerce calls this "Search Merchandising" with dedicated rules admin — "boost, bury, pin, or hide products to calibrate search results in real time." Klevu, Searchspring, Algolia, Bloomreach all use "merchandising rules" as first-class vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "merchandising|personalized search|merchandiser|merchandise" DOCS`: 21 files
- Top hits: `PlatformUserGuide/.../pricing/adding-new-assignment.md:24` (pricing, not search), `VirtoCommerce/industry/retail.md:17` (marketing copy). Most hits are in B2B-Experts thought-leadership. No dedicated merchandising-rules page in user/developer guide.

**Verdict**: 🟡 Mentioned but thin
**Note**: "Curations" in Elastic App Search covers pin/promote, but the platform never uses the term "merchandising rules" in admin/dev docs, has no personalized-search feature page, and no documented segment-based or session-based ranking. Significant vocabulary gap vs Adobe/Shopify/Algolia.
