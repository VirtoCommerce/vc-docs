# Group S — CMS / Content / i18n

## Claim 1: Multi-language / i18n is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I run a multi-language storefront on VirtoCommerce? Set up i18n and translations per locale."):
Solid returns. Storefront-side: `storefront/developer-guide/docs/customization/localization.md` describes JSON-based locale files layout (`/locales/*.json`, `/client-app/ui-kit/locales/*.json`, module-level `locales`). Admin/VC-Shell side: multiple topics in `platform/developer-guide/docs/custom-apps-development/vc-shell/Essentials/` — `adding-new-languages.md`, `plugins/i18n.md`, `composables/useLanguages.md`, `Guides/internationalization.md` — cover `vue-i18n` integration, `useLanguages` composable, locale switching, flag icons, pluralization, merging app-specific locales.

**WebSearch** (skipped — Context7 returned abundant, concrete material).

**Grep** (scope: DOCS):
- `grep -rli "i18n\|internationaliz"` DOCS: 25 files
- `grep -rli "localization\|localisation"` DOCS: 64 files
- `grep -rli "locale"` DOCS: 46 files
- `grep -rli "multi-language\|multilanguage\|multilingual"` DOCS: 27 files
- Top hits: `PlatformUserGuide/.../getting-started.md:28` — "Virto Commerce Platform is multi-language, multi-currency, multi-theme, and multi-store"; `PlatformUserGuide/.../general-guidelines.md:18` — "Multilingual SEO URLs" section explaining URL-per-language behaviour for multi-language Frontends; `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/.../dynamic-property-type.md:17` — `isMultilingual` flag on dynamic properties.

**Verdict**: ✅ Well documented
**Note**: Both admin UI (VC-Shell) and storefront sides have dedicated i18n guides. Dynamic properties carry multi-language flags; GraphQL accepts `cultureName`. Claim rejected.

---

## Claim 2: Multi-currency is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce support multi-currency? How do I configure currency per store and price lists per currency?"):
Clear answer. GraphQL product/cart queries accept `currencyCode`. `platform/user-guide/docs/pricing/overview.md` — price list = prices in a **single** currency, with price-list assignments keyed on store/catalog/customer group. `platform/user-guide/docs/multiregional-ecommerce.md` — walks a USD/CAD/EUR three-store example. `Cart/overview.md` calls out "Multi-language and multi-currency capabilities" as a first-class cart feature.

**WebSearch** (skipped — Context7 sufficient).

**Grep** (scope: DOCS):
- `grep -rli "currency\|currencies"` DOCS: 158 files
- `grep -rli "multi-currency\|multicurrency"` DOCS: 8 files
- Top hits: `PlatformUserGuide/.../getting-started.md:28`; `PlatformUserGuide/.../multiregional-ecommerce.md:35` — explicit three-currency regional setup; `VirtoCommerce/portal/b2b-loyalty.md:50` — "Multi-Currency Support"; `MarketplaceUserGuide/.../products-management.md:98` — multi-currency vendor pricing.

**Verdict**: ✅ Well documented
**Note**: Currency is a pervasive first-class concept (price lists, GraphQL, multi-regional). Claim rejected.

---

## Claim 3: Multi-store / multi-brand is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I run multi-brand on VirtoCommerce? Multi-store setup with different domains and themes per brand."):
Two dedicated tutorials exist: `platform/developer-guide/docs/Tutorials-and-How-tos/How-tos/configuring-multiple-stores.md` (self-hosted) and `.../configuring-multiple-stores-on-virto-cloud.md` (Virto Cloud). Both discuss domains, catalogs, price lists, languages, themes shared via `LiquidThemeEngine:BaseThemePath`. Emphasis on headless + composable frontend.

**WebSearch** (skipped — competitor comparison not load-bearing here).

**Grep** (scope: DOCS):
- `grep -rli "multi-store\|multistore"` DOCS: 7 files
- `grep -rli "multiple stores\|multi store"` DOCS: 9 files
- `grep -rli "multi-brand\|multibrand"` DOCS: 3 files (all marketplace-context, not storefront configuration)
- `grep -rli "white.label\|white-label\|whitelabel"` DOCS: 25 files
- Top hits: `VirtoCommerce/marketplace.md:41`, `VirtoCommerce/index.md:60` — "manufacturers and multi-brand enterprises"; `PlatformUserGuide/.../getting-started.md:28` — platform is "multi-store".

**Verdict**: 🟡 Mentioned but thin (on "multi-brand" vocabulary specifically) / ✅ on "multi-store"
**Note**: Multi-**store** is well covered with two full how-tos. Multi-**brand** as a term appears only 3× and only in marketplace marketing copy — a brand-focused customer searching the docs for "multi-brand setup" would land on marketplace pages, not the multi-store tutorial. Vocabulary gap, not capability gap.

---

## Claim 4: Content blocks / slots / widgets is thin
**Context7** (`/virtocommerce/vc-docs`, query: "CMS content blocks, slots, widgets, reusable content components for pages"):
All Context7 returns for "widget" are **VC-Shell admin dashboard widgets** (Vue components for merchant portal dashboards), not CMS content widgets. CMS content composition is covered through Page Builder (`Extensibility/cms-integrations/PageBuilder/overview.md`) and Builder.io/Sanity integrations. VC-Shell ships `VcBlade` with a "content slot", but that's admin UI, not storefront CMS slot semantics.

**WebSearch** (query: "commercetools Shopify CMS content blocks slots widget documentation"): commercetools Frontend explicitly models pages as "title, slug, and **slots**… containers of other elements"; Shopware docs have named blocks+slots+elements trio. VC does not expose the "block/slot" vocabulary at the storefront CMS level.

**Grep** (scope: DOCS):
- `grep -rli "content block"` DOCS: 2 files (one PageBuilder, one storefront product-page JSON reference)
- `grep -rli "widget"` DOCS: 174 files — but overwhelmingly VC-Shell dashboard widgets / chat-widget / vendor portal
- `grep -rli "\bslot\b\|\bslots\b"` DOCS: 43 files — mostly Vue `<template #slot>` or VcBlade content slot, not CMS slot
- Top hits: `PlatformDeveloperGuide/.../PageBuilder/search.md:3` — "enriching content blocks"; `StorefrontDeveloperGuide/.../functionality-customization.md:7` — product page JSON "content blocks"; VcBlade "content slot" is a Vue template slot.

**Verdict**: 🔴 Absent (as CMS vocabulary)
**Note**: VC has Page Builder + Builder.io + Sanity as CMS delivery channels, but the industry-standard "blocks/slots/widgets" page-composition vocabulary is absent. A CMS-oriented dev from Shopware/commercetools/Shopify would not find a "blocks & slots" model described; they'd instead find external-CMS integration docs.

---

## Claim 5: CMS page versioning / preview is thin
**Context7** (`/virtocommerce/vc-docs`, query: "CMS page versioning, preview mode, draft vs published content workflow"):
Preview: yes — Page Builder supports live iframe preview (`Extensibility/cms-integrations/PageBuilder/page-builder-setup.md` with CSP `frame-ancestors` + `Cross-Origin-Resource-Policy` headers); Storyblok integration fetches `{ version: "draft" }`. Versioning: returned results are about **marketplace product approval state machine** (Draft/PendingReview/Approved) and a vague "save draft" pattern for product workflows — **not** CMS page version history.

**WebSearch** (skipped — absence is the finding).

**Grep** (scope: DOCS):
- `grep -rli "page versioning\|version history\|content version\|page version"` DOCS: 0 files
- `grep -rli "preview"` DOCS: 49 files
- `grep -rli "draft"` DOCS: 27 files — almost all marketplace state machines / product draft / saving-a-draft UX, not CMS page drafts
- Top hits: `PlatformDeveloperGuide/.../PageBuilder/overview.md:11` — "Content preview exactly as seen by customers"; `StorefrontDeveloperGuide/.../integrations/storyblok/index-page-integration.md` — `version: "draft"` pass-through to Storyblok.

**Verdict**: 🟠 Implemented but undocumented (preview) / 🔴 Absent (versioning)
**Note**: Preview exists (PageBuilder, Storyblok) but versioning/draft-published workflow for CMS pages is not described. What "draft" does exist is via external CMS (Storyblok) or marketplace product state machines — not the VC Pages module itself.

---

## Claim 6: Liquid templating documentation is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Liquid template syntax for themes, variables, filters, tags, how to customize storefront with Liquid"):
Returns are **all theming-unrelated** — color palette SCSS, `LiquidThemeEngine:BaseThemePath` config knob. Context7 returned no Liquid *syntax/filters/tags* guidance. Liquid in VC is now scoped almost entirely to **notification templates** (post-migration from Scriban) and **event-bus payload preprocessing**, not storefront theming.

**WebSearch** (skipped — clearly domain-shifted).

**Grep** (scope: DOCS):
- `grep -rli "\bliquid\b"` DOCS: 8 files
- `grep -rli "\bliquid\b" StorefrontUserGuide StorefrontDeveloperGuide`: 0 files
- Top hits: `PlatformDeveloperGuide/.../Notifications/overview.md:18` — Liquid for notification templates, links to Scriban Liquid reference; `PlatformDeveloperGuide/.../Notifications/registering-new-notification-type.md:46` — example `{greeting}` syntax; `PlatformUserGuide/.../event-bus/overview.md:21` — Liquid for event payload preprocessing; `PlatformDeveloperGuide/.../Back-End-Architecture/01-tech-stack.md:17` — Scriban "compatibility mode" for Liquid; `PlatformDeveloperGuide/.../skills-required-for-VC-developers.md:90` — single community-link bullet.

**Verdict**: 🟡 Mentioned but thin
**Note**: Liquid is acknowledged for notifications + event bus only; no storefront Liquid guide (because the Vue storefront doesn't use it — that's a MACH-era shift from the older legacy storefront). For readers arriving expecting Shopify-style Liquid theming, the docs don't explain the transition.

---

## Claim 7: RTL (Arabic, Hebrew) is absent
**Context7** (`/virtocommerce/vc-docs`, query: "RTL right-to-left language support for Arabic Hebrew storefront bidirectional text"):
Nothing on RTL. Context7 returned multi-language plumbing (`vue-i18n`, `useLanguages`, flag icons, locale switching) but zero mention of text direction, `dir="rtl"`, or Arabic/Hebrew.

**WebSearch** (query: "Shopify RTL Arabic Hebrew storefront documentation support"): Shopify itself has only limited native RTL and relies on third-party apps + theme support, so this is a genuinely underserved area industry-wide — but Shopify at least has blog content and store-direction guidance. commercetools Frontend and Shopware ship dir/locale scaffolding.

**Grep** (scope: DOCS):
- `grep -rli "\brtl\b\|right.to.left\|right-to-left\|arabic\|hebrew\|bidirectional"` DOCS: 1 file
- That single file is a B2B Experts long-form article tangentially mentioning "liquid metal" / "robot hands" — not RTL. **Effective hit count: 0.**
- `grep -rli "\brtl\b"` CODE (PlatformFrontendSourceCode + FrontendSourceCode): 6 files — so RTL markers exist in source code, but **docs are silent**.

**Verdict**: 🔴 Absent
**Note**: Absence is the finding. Even if VC admits 10 admin languages, none of them is RTL and no storefront RTL guide exists. A brand targeting GCC/Israel markets gets no help.

---

## Claim 8: Page speed / Core Web Vitals is absent
**Context7** (`/virtocommerce/vc-docs`, query: "page speed optimization Core Web Vitals LCP CLS FID INP performance storefront"):
Vue starter theme goal: "reach and hold green metrics provided by Google PageSpeed Insights." Prerender.io integration mentions "Web Vitals metrics" improvement. AppInsights telemetry example for custom load-time metrics. That's all — no LCP/CLS/INP guidance, no performance budget, no checklist.

**WebSearch** (skipped — absence confirmed via grep).

**Grep** (scope: DOCS):
- `grep -rli "core web vitals\|web vitals\|lcp\|cls\|fid\|inp\|lighthouse\|pagespeed\|page speed"` DOCS: 5 files
- Top hits: `StorefrontDeveloperGuide/.../index.md:50` — "high performance metrics as provided by Google PageSpeed Insights" (aspirational, one line); `StorefrontDeveloperGuide/.../integrations/prerender_io.md:5,23` — "improving… Web Vitals metrics" and a PageSpeed comparison; `PlatformDeveloperGuide/.../skills-required-for-VC-developers.md:125` — single link to Lighthouse; `PlatformDeveloperGuide/.../setting-up-prerender-io-with-azure-app-gateway.md:178` — bot-UA regex mentions "google page speed" (incidental).

**Verdict**: 🟡 Mentioned but thin (skewing 🔴)
**Note**: VC aspires to green PageSpeed scores but never names **LCP/CLS/INP/TTFB**, never publishes measured baselines, never gives optimization cookbook. Industry-standard vocabulary is absent.

---

## Claim 9: AMP / Mobile pages is absent
**Context7** (`/virtocommerce/vc-docs`, query: "AMP Accelerated Mobile Pages mobile-first storefront support"):
No AMP. Returns describe responsive Vue layouts (`VcRow`, `VcCol`, VcApp mobile stacking), SPA architecture for SEO, and Page Builder mobile preview. Mobile-responsive yes; AMP no.

**WebSearch** (skipped — absence is the finding; AMP is industry-deprecated anyway).

**Grep** (scope: DOCS):
- `grep -rli "\bamp\b\|accelerated mobile"` DOCS: 0 files

**Verdict**: ⚪ Not applicable
**Note**: AMP was deprecated by Google-search ranking in 2021 and is no longer industry-relevant; a modern headless SPA correctly prioritizes SSR/Prerender + Core Web Vitals instead. Absence is correct. Claim rejected as "should be absent."

---

## Claim 10: Headless CMS comparison (Contentful, Sanity, Strapi) is absent
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce CMS compare to Contentful, Sanity, Strapi headless CMS? Integration with external headless CMS."):
No comparison exists. Integration docs exist for: **Builder.io** (full integration + Vue component registration + A/B testing), **Sanity** (full integration, webhook endpoint, `virtoPage` document schema), **Storyblok** (storefront-side example). Contentful and Optimizely are marked "coming soon" in the Pages module overview. Strapi is **entirely absent**.

**WebSearch** (skipped).

**Grep** (scope: DOCS):
- `grep -rli "contentful"` DOCS: 2 files (one "coming soon" mention; one FCP = First Contentful Paint — unrelated)
- `grep -rli "sanity"` DOCS: 7 files (full integration)
- `grep -rli "strapi"` DOCS: 0 files
- `grep -rli "storyblok\|optimizely\|builder.io"` DOCS: 46 files
- Top hits: `PlatformUserGuide/.../pages/overview.md:27` — "Contentful: Coming soon"; `platform/user-guide/docs/sanity/overview.md` — Sanity module full write-up; Builder.io across many storefront/platform guides.

**Verdict**: 🟠 Implemented but undocumented (at the comparison level)
**Note**: Integration depth is strong for Builder.io/Sanity/Storyblok. But no "how does VC CMS compare to headless CMS X?" positioning doc exists. Contentful is "coming soon" vaporware, Strapi is completely missing. A buyer-side evaluator gets no comparison matrix; a dev-side evaluator lucks into Sanity/Builder.io docs only if they know to look.
