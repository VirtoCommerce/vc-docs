# Group H — Frontend, UX, Accessibility

Scope: user-facing docs + marketing site (`DOCS` set). Per-claim 3-action methodology: Context7 `/virtocommerce/vc-docs`, WebSearch (competitor/industry signal), grep on DOCS.

---

## Claim 1: Progressive Web App (PWA) support is poorly documented.

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce storefront support Progressive Web App (PWA)? service workers, offline, installable app manifest"):
Two hits surface.
- `storefront/developer-guide/docs/customization/functionality-customization.md` describes `manifest.webmanifest` — lists PWA manifest fields (`name`, `start_url`, `icons`, `description`) but nothing about service workers, offline caching, push, install UX, Workbox, or Lighthouse PWA scoring.
- `platform/developer-guide/docs/skills-required-for-VC-developers.md` under "Progressive web applications" points OUT to a forum post (`virtocommerce.org/t/progressive-web-apps/426`) and mentions ServiceWorkers, webmanifest, ng-workers, Web-Push, offline mode — but as a *skills checklist*, not VC implementation docs.

**WebSearch** (not run — Context7 sufficient).

**Grep** (scope: DOCS):
- `grep -rli "progressive web app|\bPWA\b|service worker|web app manifest|manifest\.webmanifest"`: 6 files.
- Key hits:
  - `StorefrontDeveloperGuide/.../customization/functionality-customization.md:5,12,14,20,24,27` — manifest only.
  - `PlatformDeveloperGuide/.../skills-required-for-VC-developers.md:100,116,117` — skills list + external forum link.
  - `StorefrontDeveloperGuide/.../index.md:91` — `icons // for favicons, PWA, etc.` (parenthetical).
  - `VirtoCommerce/our-partners.md`, `B2BExperts/How-to-build-online-service-marketplace.md` — marketing copy.
- `grep -rli "service worker"`: 0 in DOCS; `grep -rli "offline"`: 0 for PWA-offline meaning.

**Verdict**: 🟡 Mentioned but thin.
**Note**: A PWA is asserted (manifest present), but the docs cover only the manifest file. No guidance on service workers, offline strategy, install prompt, push notification flow end-to-end, or Lighthouse/audit targets — all table-stakes for a PWA story.

---

## Claim 2: Server-Side Rendering (SSR) / Incremental Static Regeneration (ISR) is thin.

**Context7** (query: "Does VirtoCommerce storefront support server-side rendering (SSR), static site generation (SSG), incremental static regeneration (ISR), Nuxt, Next.js, prerendering?"):
VC explicitly does NOT do SSR in the Vue storefront. Hits:
- `storefront/developer-guide/docs/spa-architecture-for-seo-and-404-handling.md` — SPA + Prerender.io for bots.
- `storefront/developer-guide/docs/integrations/prerender_io.md` — "avoids the need for complex SSR frameworks like Nuxt.js."
- `storefront/developer-guide/docs/architecture.md` — SSR called out as optional enhancement.
- Builder.io setup mentions pre-rendering for static page versions.

**WebSearch** (not run — Context7 definitive; SSR/ISR terminology is standard across Next/Nuxt/Hydrogen).

**Grep** (scope: DOCS):
- `grep -rli "server-side rendering|\\bSSR\\b|incremental static regeneration|\\bISR\\b|prerender|Nuxt|Next\\.js"`: 13 files (mostly prerender.io / prerender).
- `grep -rni "\\bISR\\b|incremental static regeneration|\\bSSG\\b|static site generation"`: **0 hits**.
- Top hits: `StorefrontDeveloperGuide/.../spa-architecture-for-seo-and-404-handling.md`, `.../integrations/prerender_io.md`, `.../architecture.md`.

**Verdict**: 🟡 Mentioned but thin (and partly ⚪ NA — VC deliberately avoids SSR).
**Note**: SSR is intentionally not used — Prerender.io is the substitute for SEO. ISR/SSG concepts are *absent* from docs. Unfamiliar dev looking for "Does VC SSR like Hydrogen / Next Commerce?" gets no direct answer; they must infer from the prerender.io integration page. Positioning vs Next.js/Nuxt ISR is never made explicit.

---

## Claim 3: JAMstack positioning is absent.

**Context7** (query: "Does VirtoCommerce use JAMstack architecture? static site, CDN, API-first, headless frontend"):
No JAMstack mention in returned chunks. Architecture is described as SPA + GraphQL (xAPI) + CDN + optional Prerender.io; uses terms "headless architecture," "composable frontend," but never "JAMstack."

**WebSearch** (not run — Context7 empty on the term itself is the finding).

**Grep** (scope: DOCS):
- `grep -rli "JAMstack|Jamstack|jam-stack|JAM stack"`: **0 files**.

**Verdict**: 🔴 Absent.
**Note**: The underlying shape (static SPA served by CDN, hitting APIs at runtime) is arguably JAMstack-adjacent, but VC never claims the label. Competitors (Shopify Hydrogen, commercetools Frontend / Frontastic) use "JAMstack" and "composable frontend" interchangeably in marketing; VC leans on "headless" + "composable" only.

---

## Claim 4: Micro-frontends / module federation is absent.

**Context7** (query: "Does VirtoCommerce support micro-frontends or Webpack module federation? single-spa, independently deployable frontends, MFE architecture"):
No micro-frontend / module-federation vocabulary. What *is* described is VC-Shell back-office modules (Vue `app.use(module)` style plugins) and a multi-app architecture where "isolated web apps" from different teams can coexist (`custom-apps-development/overview.md`). That is plugin-based composition inside a single Vue app, not federated MFEs.

**WebSearch** ("commercetools Frontend composable frontend micro-frontends module federation documentation"): commercetools Frontend / Frontastic emphasise "reusable UI components" and composable extensions but similarly do not advertise Webpack Module Federation explicitly. Micro-frontends remain a niche architecture in commerce.

**Grep** (scope: DOCS):
- `grep -rli "micro[- ]?frontend|module federation|single-spa"`: **0 files**.

**Verdict**: 🔴 Absent (term not used).
**Note**: There is a real story to tell — VC-Shell apps are independently developed Vue apps that mount into a shared Platform shell (arguably micro-frontend-shaped). But the *terminology* never lands, so a dev Googling "VirtoCommerce micro-frontends" finds nothing.

---

## Claim 5: Frontend modularity & extensibility is poorly documented.

**Context7** (query: "How do I extend the Virto Commerce storefront / Vue frontend? add custom pages, components, override templates, theme extensibility, custom modules frontend"):
Rich, multi-angle docs surface:
- `storefront/developer-guide/docs/customization/customization-overview.md` + `functionality-customization.md` + `visual-theme-customization.md` + `texts-customization.md` + `localization.md` + `accelerators-overview.md`.
- Page Builder theme structure (`PageBuilder/schemas.md`) with blocks/sections/objects.
- VC-Shell framework modularity (`vc-shell/Extensibility/modularity.md`, `custom-apps-development/vc-shell/Guides/developing-custom-modules.md`).
- Builder.io / Storyblok integration guides with footer-integration examples.

**WebSearch** (not run — Context7 positive).

**Grep** (scope: DOCS):
- `grep -rli "frontend customization|theme customization|frontend extensibility|storefront extensibility|override page|overriding template"`: 8 files — full storefront customization folder plus a how-to on multi-store.

**Verdict**: ✅ Well documented (claim rejected).
**Note**: Modularity docs are one of VC's strongest frontend areas — VC-Shell plugin registration, theme presets, Page Builder schemas, Builder.io/Storyblok adapters all have dedicated pages. The *unfamiliar dev* pain point is discoverability (content is scattered across Platform Dev Guide *and* Storefront Dev Guide), not depth.

---

## Claim 6: Design system / design tokens are thin.

**Context7** (query: "Does VirtoCommerce have a design system with design tokens (colors, spacing, typography)? component library, Figma kit, Storybook"):
Two design systems exist and are documented:
- **VC-Shell (back-office)** — `vc-shell-overview.md` says "Consistent design system with reusable components"; `custom-application-core-concepts.md` cites `VcButton/VcInput/VcTable/VcBlade/VcApp`; `application-architecture-best-practices.md:157` references "pre-configured design system" with Tailwind inheritance and CSS custom properties.
- **Storefront (vc-frontend)** — `visual-theme-customization.md` explicitly uses "design tokens" for presets (color palette + JSON). Hosted Storybook: `vc-shell-storybook.govirto.com` with Atoms/Molecules/Organisms structure.

**WebSearch** (not run — Context7 positive).

**Grep** (scope: DOCS):
- `grep -rni "design system|design token"`: 13 hits across 11 files. "design tokens" literally used in `visual-theme-customization.md:3,7`. No "Figma" or style dictionary mention in DOCS.

**Verdict**: 🟡 Mentioned but thin.
**Note**: A design system *exists* (CSS variables + presets + Storybook) and the term "design token" is used. What's missing: no Figma/design-file publication, no token taxonomy spec (JSON/W3C tokens), no "how to export tokens to your design team" guide, no multi-platform token pipeline (style-dictionary etc.). Good for devs, weak for designers.

---

## Claim 7: Theming / white-label / multi-brand is thin.

**Context7** (query: "VirtoCommerce white-label multi-brand theming, supporting multiple brands on single instance, store-specific themes, dark mode, brand customization"):
Strong coverage:
- `platform/user-guide/docs/white-labeling/overview.md` + `customizing-brand-elements.md` — dedicated White Labeling module, custom-domain-per-organization.
- `platform/developer-guide/docs/GraphQL-Storefront-API-Reference-xAPI/White-labeling/` — xAPI queries/objects (`whiteLabelingSettings`, `WhiteLabelingSettingsType`).
- `platform/developer-guide/.../configuring-multiple-stores-on-virto-cloud.md` — multi-store, per-store themes, shared catalog.
- `vc-shell/Essentials/Usage-Guides/managing-themes-with-usetheme.md` — full SCSS-variable theme system, dark/light palettes, `data-theme` selector.
- `storefront/.../customization/visual-theme-customization.md` — presets per store.
- `DeploymentGuide/.../store-branding.md`.

**WebSearch** (not run).

**Grep** (scope: DOCS):
- `grep -rli "white[- ]?label|multi[- ]?brand|dark mode|theming"`: 58 files.

**Verdict**: ✅ Well documented (claim rejected).
**Note**: White-labeling has its own module, xAPI surface, and admin UI docs. Multi-brand via multi-store is a first-class concept. Thin spots: the term "multi-brand" per se isn't used (it's "multiple stores"); no explicit dark-mode storefront guide (themes are template-based).

---

## Claim 8: Accessibility (WCAG, ARIA) is not called out.

**Context7** (query: "Is VirtoCommerce storefront WCAG 2.1 AA compliant? accessibility, ARIA landmarks, keyboard navigation, screen reader support, a11y"):
Almost nothing. Two hits: `platform/user-guide/docs/ada-compliance.md` — one short ADA page stating zoom/scaling is not disabled on login/Cart/Catalog; `storefront/.../navigation/homepage-layout.md` — mega menu "supports keyboard navigation" (one sentence).

**WebSearch** ("Shopify Hydrogen storefront WCAG accessibility 2.1 AA documentation 2026"): Industry baseline in 2026 is WCAG 2.1 AA; EAA (EU) since June 2025 *mandates* it for e-commerce services sold in the EU. Shopify tracks WCAG 2.2. Legal risk is real.

**Grep** (scope: DOCS):
- `grep -rli "\\bWCAG\\b|\\bARIA\\b|\\ba11y\\b|accessibility|screen reader|\\bADA\\b|section 508"`: many hits but mostly B2BExperts articles (marketing) + incidental uses of the word "access" in unrelated contexts.
- **Direct WCAG/ARIA/a11y specifically**: 4 hits total — 2 `aria-label="Footer"` code snippets in Builder.io/Storyblok integrations, 1 WCAG mention in a B2BExperts blog quoting Algolia, 1 in an inlined external link.
- `ada-compliance.md` is **13 lines total** — narrow scope (zoom only).
- `keyboard navigation`: 2 hits (homepage mega menu, vc-input-currency component).

**Verdict**: 🔴 Absent.
**Note**: Given EAA came into force 2025-06-28, this is a material gap. No WCAG 2.1 AA claim, no conformance statement, no ARIA pattern guidance, no a11y testing instructions, no VPAT, no screen-reader matrix. The one ADA page only covers zoom/scaling. For an e-commerce platform selling into EU in 2026 this is the single biggest frontend-docs hole.

---

## Claim 9: Mobile apps / React Native / Flutter SDKs are absent.

**Context7** (query: "Does VirtoCommerce have native mobile apps, React Native SDK, Flutter SDK, iOS, Android, Swift, Kotlin client?"):
No mobile SDK or native-app references surface. Everything returned is Vue/web-app centric (VC-Shell modules, API clients in TypeScript).

**WebSearch** (not run — the term absence is the finding).

**Grep** (scope: DOCS):
- `grep -rli "react native|\\bFlutter\\b|iOS app|Android app|Swift SDK|Kotlin SDK|Xamarin|MAUI|Capacitor|Ionic"`: 3 files, all false positives.
  - `GraphQL-Storefront-API-Reference-xAPI/best-practices.md:124,245` — uses phrase "feels like a native mobile app" as a *caching* quality metaphor.
  - `vc-shell/.../customizing-notifications.md` — matches "native" in a different context.
  - `B2BExperts/Empowering-the-marketing-function-in-b2b-sales.md` — marketing prose.
- **Zero hits** for React Native, Flutter, Swift SDK, Kotlin SDK, Xamarin, MAUI, Capacitor, or Ionic as actual integrations.

**Verdict**: ⚪ Not applicable (absence is correct) / bordering 🔴 Absent (term not even discussed).
**Note**: VC has no first-party mobile SDK and doesn't document how to build one. The docs should at minimum say "use GraphQL xAPI with Apollo Client for React Native / ferry for Flutter" — currently there's no signpost at all. Given xAPI is explicitly "optimized for frontend applications," the absence of mobile-client guidance is a documentation gap even if the product scope is intentional.

---

## Claim 10: Storybook / component catalog discoverability is thin.

**Context7** (query: "Does VirtoCommerce publish a Storybook? component catalog, UI kit, how to discover available UI components"):
Two Storybooks are published and documented:
- **Storefront Storybook** — dedicated page `storefront/developer-guide/docs/storybook.md`: "interactive component library," Atomic Design (Atoms/Molecules/Organisms), `yarn storybook:dev` / `yarn storybook:build`.
- **VC-Shell Storybook** — hosted at `vc-shell-storybook.govirto.com`, embedded via iframe in every `vc-*.md` component doc (vc-button, vc-input, vc-grid, vc-field, etc.).

**WebSearch** (not run).

**Grep** (scope: DOCS):
- `grep -rni "\\bStorybook\\b|UI kit|UI Kit"`: 30+ hits across Platform Developer Guide component pages + dedicated storefront page + `accelerators-overview.md`.

**Verdict**: ✅ Well documented (claim rejected).
**Note**: Storybook is actually one of the strongest *discoverability* stories in VC docs: each vc-* component page embeds its Storybook preview via iframe. Minor weakness: no single top-level "Component Index" that lists all ~40 vc-* atoms in one place — dev must navigate VC-Shell Essentials/ui-components folder.

---

## Group shape (summary)

**Strong**: Theming & white-labeling (dedicated module, xAPI, multi-store, SCSS variable themes), Storybook (two published, embedded per-component), frontend customization path (presets, CSS variables, Page Builder, VC-Shell modular apps).

**Weak**: Accessibility is the glaring hole — a 13-line ADA-zoom page is the full extent of a11y docs, with no WCAG 2.1 AA conformance statement despite EU EAA mandating it since 2025-06. PWA coverage stops at the manifest file (no service-worker / offline / push end-to-end). SSR/ISR/JAMstack/micro-frontends/module-federation vocabulary never appears — VC is opinionated against SSR (Prerender.io instead) but doesn't position itself clearly against Next.js/Nuxt/Hydrogen peers. Mobile SDK story (React Native, Flutter) is a pure blank — not even "bring your own GraphQL client" signposts.

**Verdicts**:
- ✅ Claims 5, 7, 10 (claims rejected — VC documents these adequately)
- 🟡 Claims 1, 2, 6 (thin or scope-limited)
- 🔴 Claims 3, 4, 8 (absent terminology or content)
- ⚪/🔴 Claim 9 (no mobile SDK product; no docs either)
