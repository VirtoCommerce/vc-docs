# Group K — Cart & Checkout

Scope shorthand: `DOCS` = `VirtoCommerce`, `PlatformUserGuide`, `PlatformDeveloperGuide`, `StorefrontUserGuide`, `StorefrontDeveloperGuide`, `MarketplaceUserGuide`, `DeploymentGuide`, `B2BExperts` (under `/mnt/Programming/AI chat/vc-ai-assistant/documentation/`).

---

## Claim 1: Guest checkout is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support guest checkout for anonymous shoppers?"):
Returned a dedicated `storefront/developer-guide/docs/authentication/anonymous-authentication.md` page explicitly covering guest checkout via anonymous authentication (localStorage anonymous ID, `getMe` handshake, cart preservation, abandoned-cart recovery). Also surfaced "Purchase PBC Max" describing checkout/cart capabilities.

**WebSearch** (query: "ecommerce guest checkout vs express checkout Apple Pay Google Pay wallet best practices 2025"):
Guest checkout is industry-standard; mandatory account creation causes ~26% abandonment. 43% of shoppers prefer guest checkout. Every major platform (Shopify, BigCommerce, Magento, commercetools) documents it as a first-class flow.

**Grep** (scope: DOCS):
- `grep -rli "guest checkout"`: 1 file — `StorefrontDeveloperGuide/.../authentication/anonymous-authentication.md`.
- `grep -rli "anonymous"`: 21 files.
- Platform cart overview also mentions `Anonymous carts`: `PlatformUserGuide/platform/user-guide/docs/cart/overview.md:21`.
- Cart overview itself never uses the phrase "guest checkout"; the checkout walkthrough (`StorefrontUserGuide/.../shopping/checkout-process.md`) is written as an authenticated flow and doesn't call out a guest path.

**Verdict**: 🟡
**Note**: Supported, but "guest checkout" as a term appears in exactly one developer-guide page. User-facing guides describe checkout as an authenticated flow; no page says "here is how a guest finishes an order". The underlying mechanism (anonymous auth) is well described — the user-visible vocabulary is not.

---

## Claim 2: Multi-cart / saved carts / named carts is thin
**Context7** (covered by queries above; merge mutation + cart overview returned):
`PlatformUserGuide/.../cart/overview.md` lists "Multiple carts", "Named lists", and "Grouping multiple carts" as key features. `mergeCart` GraphQL mutation documented.

**WebSearch** (query: "B2B ecommerce saved cart multi-cart named carts Shopify Plus BigCommerce"):
Multi-cart with user-assigned names is a B2B differentiator. Shopify Plus has no native multi-cart — relies on third-party apps ("Extend B2B Buying", PluralCart). BigCommerce offers "save cart" via app. VC's native multi-cart + naming beats Shopify out of the box.

**Grep** (scope: DOCS):
- `grep -rli "named cart|multi-cart|multiple cart|saved cart|multicart"`: 2 files (cart overview; B2B whitepaper).
- `grep -rli -E "wishlist|wish list|save for later"`: 43+ files (dominated by GraphQL reference).
- Key hits: `PlatformUserGuide/platform/user-guide/docs/cart/overview.md:18,20`; `B2BExperts/docs/Elevating-customer-experience-in-b2b-ecommerce.md:135`.

**Verdict**: 🟡
**Note**: Feature exists and is listed, but there's one line in the overview + a whitepaper paragraph. No step-by-step "how a buyer names / switches / shares a cart" user-guide page. Developers get GraphQL fragments (`createWishlist`, `cartName` on `mergeCart`); buyers get almost nothing.

---

## Claim 3: One-page / accordion checkout guidance is thin
**Context7** (covered above): only hit is e2e testing doc mentioning `--checkout-mode single-page` CLI flag.

**WebSearch** (same as Claim 1): One-page/accordion/multi-step checkout patterns are a standard discussion in every commerce platform's docs.

**Grep** (scope: DOCS):
- `grep -rli "one-page checkout|single-page checkout|accordion checkout"`: 2 files — both only in passing.
- `PlatformDeveloperGuide/.../Testing/testing.md:19,182-223` — treats "single-page" vs "multi-step" as a test-matrix dimension without ever defining the terms.
- `B2BExperts/docs/How-to-acquire-more-b2b-customers-in-2024.md` — marketing prose.
- Actual storefront checkout is clearly multi-step (Cart → Delivery → Billing → Review → Place order per `checkout-process.md`), but the docs never explain the pattern choice or how to customize to a one-page layout.

**Verdict**: 🟡
**Note**: The storefront ships a multi-step wizard and the test harness knows about `single-page` mode, yet no documentation page explains what "single-page checkout" means in VC, how to enable it, or how to theme/accordion the flow. Claim holds.

---

## Claim 4: Cart abandonment tracking / emails is thin
**Context7** (query: "How does Virto Commerce handle cart abandonment, abandoned cart recovery emails, and cross-sell / upsell on the cart page?"):
Returned anonymous-authentication page highlighting abandoned-cart recovery benefit, but no dedicated abandonment-email setup page; main results were Page Builder / Google SSO / login-on-behalf.

**WebSearch** (query: "Shopify BigCommerce commercetools abandoned cart recovery email documentation feature"):
Shopify has dedicated help-center section + native abandoned-checkout automation, BigCommerce has "Abandoned Cart Saver" on Plus/Pro/Enterprise plans with a t-token API. commercetools has no first-party abandonment email. VC falls between.

**Grep** (scope: DOCS):
- `grep -rli "abandoned|abandonment"`: 13 files.
- Best hits: `PlatformUserGuide/platform/user-guide/docs/cart/settings.md:22-52` — configures a global + per-store cron expression and links to the Notifications module template (3 screenshots, no sample template content).
- Release note: `versions/v3-2025-S11.md:19` — "3.814.0 Customers' notification of abandoned items in cart", "3.821.0 Links in abandoned cart email template fixed".
- `login-on-behalf.md:14` and `anonymous-authentication.md:18` mention the business value in passing.

**Verdict**: 🟡
**Note**: VC ships the feature (cron, store-level override, email template via Notifications module), but documentation stops at "set a cron and open the template" — no walkthrough of template variables, delivery windows, multi-reminder cadences, or how to segment by customer. Shallow compared to Shopify/BigCommerce.

---

## Claim 5: Upsell / cross-sell on cart page is thin
**Context7** (see Claim 4 query): Dynamic Associations module surfaced implicitly via related-products blocks in `functionality-customization.md`.

**WebSearch** (see Claim 1 query): Industry best practice: cart-page cross-sell/upsell blocks with A/B testing; major platforms dedicate help articles to it.

**Grep** (scope: DOCS):
- `grep -rli "upsell|cross-sell|cross sell"`: 19 files (heavy in B2BExperts marketing corpus).
- User-guide: `PlatformUserGuide/platform/user-guide/docs/dynamic-associations/overview.md:3` — "facilitates sales growth ... through its upselling and cross-selling functionalities".
- `PlatformUserGuide/.../marketing/dynamic-associations-overview.md:3` — automatic suggestion on cart add example.
- Storefront customization: `StorefrontDeveloperGuide/.../customization/functionality-customization.md:128,162` — `related-products` block "encourages cross-selling".
- `checkout-process.md:25` mentions "recently browsed products" on the cart page, not cross-sell.
- `B2BExperts` has ~12 marketing mentions.

**Verdict**: 🟡
**Note**: The concept is named (Dynamic Associations) and a storefront block exists, but nothing ties it directly to the cart page: no "place cross-sell block on cart" recipe, no screenshots of cart-page upsell, no mention of positioning/layout. Claim stands.

---

## Claim 6: Express checkout (Apple Pay, Google Pay) is thin
**Context7** (query: "Apple Pay Google Pay express checkout wallets..."): CyberSource integration page lists "Card Payment, 3D Secure, Visa Click to Pay, Google Pay, eCheck, and Apple Pay" as supported methods.

**WebSearch** (see Claim 1): Apple Pay buttons yield +22% conversion; industry best practice is express buttons above the fold on cart + checkout pages. Every major platform has a dedicated wallet-integration guide.

**Grep** (scope: DOCS):
- `grep -rli "apple pay|google pay|express checkout|digital wallet"`: 2 files.
- `PlatformDeveloperGuide/.../Payments/cybersource.md:13` — single bullet listing them among CyberSource methods.
- `PlatformDeveloperGuide/.../Payments/new-payment-method-registration.md` — mentioned once.
- No dedicated Apple Pay / Google Pay setup page. No "express checkout button on cart" guidance. No Stripe / PayPal wallet docs despite wallets being ~49-56% of 2025 e-commerce value.

**Verdict**: 🟠 (borderline 🔴 on the "express checkout" concept specifically)
**Note**: Wallets are implemented via CyberSource and listed in exactly one bullet. No page explains how to enable/test them, where the express button renders, or the domain-verification / merchant-capability requirements Apple Pay mandates. Deeply under-documented vs industry norm.

---

## Claim 7: Clienteling / assisted selling is absent
**Context7** (see Claim 6 query): Returned `platform/user-guide/docs/security/login-on-behalf.md` — administrators/support engineers can log in as another user; "reducing cart abandonment rates" called out; full step-by-step via Contacts / Security modules.

**WebSearch**: "Clienteling" is industry-standard vocabulary (Salesforce Commerce, SAP, Oracle) for sales-assist flows — not used by VC.

**Grep** (scope: DOCS):
- `grep -rli "clienteling"`: **0 files**.
- `grep -rli "assisted selling"`: 0 files.
- `grep -rli "impersonat|login on behalf|on behalf of"`: 18 files — dominated by `login-on-behalf.md` + security / active-sessions pages + marketplace vendor management.
- `PlatformUserGuide/.../security/login-on-behalf.md:1-43` — feature walkthrough.
- `PlatformUserGuide/.../versions/v3-2026-S14.md` — release note.

**Verdict**: 🟠
**Note**: The capability exists ("Login on behalf" = clienteling / impersonation / assisted selling). The industry terms "clienteling" and "assisted selling" never appear, so a merchandiser googling "clienteling in VirtoCommerce" gets zero hits. Claim accurate as stated (industry term absent); feature itself is well-documented under VC's own name.

---

## Claim 8: Minimum order quantity / order increments is thin
**Context7** (see Claim 6 query): No direct hit; related material came via catalog / variations.

**WebSearch** (Claim 3-adjacent): MOQ is a standard B2B feature; Shopify Plus, BigCommerce B2B, Magento Commerce have explicit MOQ + increment docs.

**Grep** (scope: DOCS):
- `grep -rli "minimum order quantity|MOQ"`: 0 files (the literal phrases).
- `grep -rli "minimum quantity"`: hits in pricing (`creating-new-price-list.md:70`, `managing-contract-prices.md:43`) — describes per-tier minimum quantity on a price list, not per-product MOQ.
- `grep -rli "pack size|packSize"`: 3 files — `PlatformUserGuide/.../catalog/managing-products.md:53-67` "Set up product pack size" (closest to order increment), `managing-properties.md:141`, `DeploymentGuide/.../catalog-creation.md:229,357`.
- GraphQL: `ProductType.md:13-14` documents `minQuantity` + `maxQuantity` fields (no prose).
- Term "order increment" / "quantity step" — 0 hits.

**Verdict**: 🟡
**Note**: Three separate concepts (tier-minimum-for-price, pack size, `minQuantity`/`maxQuantity` GraphQL fields) are each documented briefly and independently. There is no unifying page explaining B2B MOQ + order-multiple rules, and the industry abbreviation "MOQ" is absent from the corpus.

---

## Claim 9: Cart merging (guest → logged-in) is thin
**Context7** (see Claim 6 query): Returned full `mergeCart` mutation reference — "You can use it to merge an anonymous cart with a user cart after user authentication", with schema, variables example, and response example.

**WebSearch** (Claim 1 & 3 queries imply): Merging guest → logged-in cart is a standard ecommerce requirement.

**Grep** (scope: DOCS):
- `grep -rli "cart merg|merge cart|merging cart"`: 1 file — `PlatformDeveloperGuide/.../Cart/mutations/merge-cart.md` (GraphQL reference only).
- `anonymous-authentication.md` describes the anonymous → logged-in transition conceptually but does not explicitly say "cart merge happens here".
- No user-guide or storefront-guide page walks the merge flow end-to-end.

**Verdict**: 🟡
**Note**: API reference exists; conceptual prose does not. An implementer sees only `mergeCart` schema — no storefront walkthrough, no edge cases (duplicate SKUs? quantity addition vs replace? promo-code carry-over?). Shallow vs the feature's importance.

---

## Claim 10: Save-for-later / wishlist → cart flow is thin
**Context7** (Claim 2 indirectly): Returned extensive GraphQL references for wishlists (`changeWishlist`, `moveWishlistItem`, `cloneWishlist`, etc.).

**WebSearch**: Save-for-later and wishlist are table-stakes; Shopify/BigCommerce wishlist apps are ubiquitous.

**Grep** (scope: DOCS):
- `grep -rli "save for later|wishlist|wish list"`: 45 files.
- Dedicated user-guide: `StorefrontUserGuide/storefront/user-guide/docs/shopping/save-for-later.md` (short, includes Storylane demo embed).
- `StorefrontUserGuide/.../shopping/lists.md` — product lists ("Named lists" concept).
- ~25 GraphQL reference files covering every wishlist mutation/query.
- Google Analytics integration notes on wishlist events: `integrations/google-analytics/ga-events.md`.

**Verdict**: ✅ (claim rejected)
**Note**: Save-for-later has its own storefront page; wishlist has a dense GraphQL surface + platform cart overview mention ("Named lists: Creation of wishlists for later use in placing orders"). The "wishlist → cart" transition is covered via `moveWishlistItem`. This is actually one of the better-documented areas in Group K.

---

## Sources cited (WebSearch)

- [Shopify Help Center — Recovering abandoned checkouts](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/abandoned-checkouts)
- [BigCommerce Developer Center — Recovering Abandoned Carts](https://developer.bigcommerce.com/docs/storefront/headless/cart-checkout/abandoned-carts)
- [Introducing Multi-Cart for B2B on Shopify Plus — Codup](https://codup.co/blog/introducing-multi-cart-for-b2b-on-shopify-plus/)
- [Optimizing payments for mobile wallets (2025 guide) — GR4VY](https://gr4vy.com/posts/optimizing-payments-for-mobile-wallets-apple-pay-google-pay-etc-2025-guide/)
- [8 Ecommerce Checkout Best Practices for 2025 — CartBoss](https://www.cartboss.io/blog/ecommerce-checkout-best-practices/)
