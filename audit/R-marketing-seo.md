# Group R — Marketing, SEO, Personalization

Scope: VirtoCommerce documentation corpus (`documentation/VirtoCommerce`, `PlatformUserGuide`, `PlatformDeveloperGuide`, `StorefrontUserGuide`, `StorefrontDeveloperGuide`, `MarketplaceUserGuide`, `DeploymentGuide`, `B2BExperts`).

---

## Claim 1: Personalization engine is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have a personalization engine? How do I personalize content and product recommendations per user segment?"):
Returned `pushHistoricalEvent` mutation + `recommendations` GraphQL query (xRecommend module), plus `evaluateDynamicContent` (xMarketing). VC positions personalization around two pillars: (a) user-group-driven catalog personalization / dynamic content, (b) xRecommend for product-level ML recommendations.

**WebSearch** — skipped for this claim; Context7 already confirmed in-product feature and grep gave strong evidence.

**Grep** (scope: DOCS):
- `grep -rli "personalization" DOCS`: **75 files**.
- Dedicated module page: `PlatformUserGuide/platform/user-guide/docs/catalog-personalization/overview.md`, `settings.md`, `user-groups.md`.
- Dynamic Content: `PlatformUserGuide/.../marketing/dynamic-content-overview.md:3` — "With the Dynamic Content feature you can create personalized shopping experiences for your customers."

**Verdict**: Well documented (personalization itself). A dedicated Catalog Personalization module, Dynamic Content subsystem in Marketing, plus xRecommend. Claim rejected — the topic is substantial and reachable.
**Note**: What VC lacks vs. Dynamic Yield / Adobe Target is the industry vocabulary: "personalization engine", "affinity profile", "audience", "experience" are rare; VC says "user groups" and "dynamic content" instead. Term-level gap, not feature-level.

---

## Claim 2: Recommendation engine is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have a recommendation engine? How do I set up product recommendations like related products and frequently bought together?"):
Returned `recommendations(storeId, model: "related-products", productId, maxRecommendations)` GraphQL query with full parameter reference, plus `pushHistoricalEvent`. The xRecommend module is documented end-to-end (query + ingestion).

**WebSearch** — not required.

**Grep** (scope: DOCS):
- `grep -rli "recommendation" DOCS`: **79 files**.
- `PlatformUserGuide/platform/user-guide/docs/recommend/overview.md:3` — module name "xRecommend (Recommendations)", explicit feature list including "Semantic similarity: Machine learning-based product recommendations using Elasticsearch".
- Source link: `https://github.com/VirtoCommerce/vc-module-x-recommend`.

**Verdict**: Well documented. Dedicated module page, GraphQL query, ingestion mutation, ML model listed.
**Note**: Models surface is lean (one "related-products" example). No docs on "frequently bought together", "customers also viewed", "cold-start strategy", or offline evaluation — those are competitor-standard terms (Dynamic Yield, Adobe Sensei) that VC docs don't use.

---

## Claim 3: A/B testing / experimentation is absent.

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support A/B testing or experimentation for storefront content, pricing, or promotions?"):
Returned xMarketing queries (`promotionCoupons`, `evaluateDynamicContent`). Nothing about experiments, variants, traffic splitting, or statistical significance.

**WebSearch** (query: "Adobe Sensei personalization Target A/B testing commerce platform"):
Confirms industry-standard: Adobe Target ships Auto-Allocate, Auto-Target, multivariate testing natively; Dynamic Yield and Shopify's built-in experiments do likewise. A/B is considered baseline commerce-platform functionality.

**Grep** (scope: DOCS):
- `grep -rli -E "a/b test|split test|experimentation" DOCS`: **22 files**.
- Only two hits treat A/B testing as an actual VC feature, both as a third-party hand-off: `PlatformUserGuide/.../managing-content.md:5` — "Builder.io module … offers advanced features such as A/B testing"; `PlatformUserGuide/.../integrations/google-analytics/integration.md:35` — lists "A/B testing tools" as a general GA4 benefit. One developer-side how-to: `PlatformDeveloperGuide/.../feature-flags.md:10` — feature flags mentioned as enabling A/B testing, but no runner / stats / traffic-split mechanism.

**Verdict**: Absent as a native VC feature. Documented only by referral to Builder.io / GA4 / feature flags.
**Note**: Confirmed gap. No "experiment", "variant", "traffic allocation", "conversion lift", "statistical significance" terminology in VC docs.

---

## Claim 4: Abandoned cart email is thin.

**Context7** — covered in Claim 5's combined query (no dedicated abandoned-cart page surfaced; only generic `EmailNotification` scaffolding).

**WebSearch** (query: "Klaviyo Shopify integration abandoned cart email documentation 2025"):
Klaviyo ships pre-built flows ("Added to Cart" trigger, customizable branches by cart value, SMS+email multi-step). Industry standard: an abandoned-cart flow with multi-touch timing, product block, discount code injection.

**Grep** (scope: DOCS):
- `grep -rli -E "abandoned cart|cart abandonment|abandonment" DOCS`: **7 files**.
- `PlatformUserGuide/.../cart/settings.md:6,22,24` — "Abandoned cart reminder" configuration (globally), screenshot included.
- Changelog `versions/v3-2025-S11.md:19` — "3.814.0 Customers' notification of abandoned items in cart", "3.821.0 Links in abandoned cart email template fixed" — evidence the feature is actively developed.
- `StorefrontDeveloperGuide/.../authentication/anonymous-authentication.md:18` — "Abandoned cart recovery" mentioned as benefit.

**Verdict**: Mentioned but thin. One settings page, plus changelog breadcrumbs. No end-to-end guide (trigger schedule, template editing, multi-touch sequence, re-targeting coupon, unsubscribe compliance). No cross-link from Marketing module.
**Note**: Feature exists and is evolving, but documentation is a single settings blade — dramatically thinner than Klaviyo's dedicated playbook.

---

## Claim 5: Email marketing (Klaviyo, Mailchimp, Braze) integration is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce integrate with Klaviyo, Mailchimp, or Braze for email marketing? Is there an abandoned cart email feature?"):
No results for any ESP. Context7 returned only the custom email notification pattern (`EmailNotification` base class, `INotificationSender`) — transactional-only, not marketing ESP.

**WebSearch** — not required; absence is the finding.

**Grep** (scope: DOCS):
- `grep -rli -E "klaviyo|mailchimp|braze|sendgrid|hubspot|dotdigital|marketo" DOCS`: **2 files**, both SendGrid-only:
  - `PlatformDeveloperGuide/.../appsettingsjson.md:1407,1416,1417` — SendGrid listed as a transactional gateway option.
  - `PlatformDeveloperGuide/.../Post-Installation-Steps/02-configuring-email-notifications.md:2,41` — SendGrid as SMTP alternative.
- Zero hits for Klaviyo, Mailchimp, Braze, HubSpot, Marketo, Dotdigital.

**Verdict**: Absent (marketing ESPs); 🟡 for SendGrid, which is documented as a transactional SMTP replacement rather than a marketing-automation integration.
**Note**: The industry-standard ESPs (Klaviyo, Mailchimp, Braze) that a typical e-commerce manager would look for do not appear at all. Only transactional email via SMTP / SendGrid.

---

## Claim 6: SEO — canonical URLs / structured data / JSON-LD are thin.

**Context7** (`/virtocommerce/vc-docs`, query: "How do I set up SEO in VirtoCommerce? Does the storefront emit canonical URLs, JSON-LD structured data, sitemap.xml, and Open Graph tags?"):
Returned a detailed SEO module overview (slugs, titles, meta descriptions per catalog/category/product) + `useSeoMeta` Vue composable that sets title / keywords / description / Open Graph tags. A full "Add SEO to module" how-to with C# resolver + Vue page integration exists.

**WebSearch** — not required; grep disambiguates.

**Grep** (scope: DOCS):
- `grep -rli -E "canonical|json-?ld|structured data|schema\.org|og:|open graph|meta tag" DOCS`: **36 files**.
- Canonical URL: `grep -rni "canonical"` returns **zero** matches across all user/developer guides.
- JSON-LD / Schema.org: one-liner only — `PlatformDeveloperGuide/.../skills-required-for-VC-developers.md:28` lists "SEO principles (Schema.org, JSON-LD)" as developer prerequisites, not as implemented VC features.
- Open Graph: documented — `PlatformDeveloperGuide/.../Fundamentals/SEO/add-seo-to-module.md` "Frontend. Page meta and open graph" section (via `useSeoMeta`).

**Verdict**: Mentioned but thin. Meta title/description + Open Graph: well covered. Canonical URLs: absent from docs. JSON-LD / Schema.org structured data: absent (listed once as a skill, never as a VC feature).
**Note**: Product-detail JSON-LD (`Product`, `Offer`, `AggregateRating`, `BreadcrumbList`) is a shoppable-result baseline today — the biggest SEO gap in VC docs.

---

## Claim 7: Sitemap generation is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "Does the VirtoCommerce storefront generate a sitemap.xml or robots.txt automatically? How is sitemap generation configured?"):
Returned `PlatformUserGuide/.../sitemaps/overview.md` — "Users can schedule and configure recurring jobs to generate sitemap files automatically. Additionally, the module provides the functionality to download sitemap ZIP packages containing the XML files."

**WebSearch** — not required.

**Grep** (scope: DOCS):
- `grep -rli "sitemap" DOCS`: **28 files**.
- Dedicated module: `PlatformUserGuide/platform/user-guide/docs/sitemaps/` — overview + `configuring-sitemaps.md:66` documents sitemap.xml format and ZIP packaging.
- `PlatformUserGuide/.../store/custom-robot-txt.md` — dedicated page for custom `robots.txt` upload, including cross-reference to sitemap URL.

**Verdict**: Well documented. Dedicated Sitemaps module with its own user-guide section, plus a paired custom `robots.txt` page. Claim rejected.
**Note**: Coverage is solid for a merchant audience. Developer-facing customization (per-entity priority, changefreq, lastmod generation) is thinner.

---

## Claim 8: Customer segmentation is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "How do I create customer segments in VirtoCommerce to target promotions or content to specific groups of users?"):
Returned user-group-based targeting: `evaluateDynamicContent` accepts `userGroups`; Promotions support "customer conditions" (first-time, registered, members of group); Marketing module docs explicitly call this out.

**WebSearch** (query: "Dynamic Yield personalization e-commerce segmentation recommendations 2025"):
Industry vocabulary: "Audience Hub", "shopper behavior segments", "affinity profiles", "demographic segments". Dynamic Yield segmentation is a first-class product pillar.

**Grep** (scope: DOCS):
- `grep -rli -E "customer segment|member segment|user segment|segmentation" DOCS`: **22 files**.
- Hits are almost entirely the word "segment" applied to either (a) "member of company segment" (B2B org structure) or (b) prose descriptions. No dedicated Segmentation module or page.
- Actual mechanism = User Groups (`contacts/overview.md` — "User groups can be created to include specific users, beneficial for targeted promotions or offering special pricing"). Dynamic content + promotions both target by user group.

**Verdict**: Mentioned but thin — on a vocabulary level. The feature exists (User Groups) and is used across Dynamic Content, Catalog Personalization, Promotion Rules. But the term "segmentation" is not used as a top-level concept, and there is no behavioral / RFM / lifecycle-stage segmentation UI.
**Note**: Merchant-side gap: no "segments" UI with rule builder (recency, frequency, monetary, purchase history). Only admin-maintained groups.

---

## Claim 9: Google Analytics / GTM / GA4 is thin.

**Context7** (`/virtocommerce/vc-docs`, query: "How do I add Google Analytics 4, Google Tag Manager, or Meta/Facebook Pixel tracking to my VirtoCommerce storefront? Is there a Conversions API integration?"):
Returned a rich, multi-page GA4 integration: native GA4 + GTM support, `Force.Global.GoogleAnalytics4.MeasurementId` / `GtmContainerId` global enforcement in `appsettings.json`, "Direct GA4 integration" setup, "GTM setup for GA4" setup, e-commerce event tracking in the Virto Frontend.

**WebSearch** — not required.

**Grep** (scope: DOCS):
- `grep -rli -E "google analytics|GA4|gtag|gtm|google tag manager" DOCS`: **22 files**.
- Dedicated module: `PlatformUserGuide/.../integrations/google-analytics/integration.md` + `overview.md`.
- Developer-side: `appsettingsjson.md` documents force-global enforcement of Measurement ID and GTM Container ID.

**Verdict**: Well documented. GA4 and GTM are a first-class native integration with its own user-guide section and config-reference entry. Claim rejected.
**Note**: No gap for GA/GTM/GA4.

---

## Claim 10: Meta pixel / conversion API is absent.

**Context7** — covered by claim 9's combined query. No dedicated page for Meta Pixel / Facebook CAPI; the only reference is implicit ("Multiple tracking tools" as a GA4-integration benefit).

**WebSearch** — not required; grep disambiguates.

**Grep** (scope: DOCS):
- `grep -rli -E "meta pixel|facebook pixel|fbq\(|conversion api|conversions api|capi" DOCS`: **zero hits** for explicit Meta Pixel or Conversions API pages.
- The only mention is `PlatformUserGuide/.../integrations/google-analytics/integration.md:33` — "Multiple tracking tools (GA4, Facebook Pixel, LinkedIn Insight, etc.)" — a feature bullet of the GA4 module, with no setup guide.

**Verdict**: Absent. Mentioned once in passing as a GTM-routed capability, never documented as a direct integration.
**Note**: No server-side Conversions API documentation at all. Given iOS/Safari client-side tracking loss, CAPI is table-stakes for modern performance marketing — a clear gap.

---
