# Group Q — Marketplace / Multi-vendor

Scope: VirtoCommerce has a dedicated Marketplace offering with Operator Portal + Vendor Portal + commission engine. User-facing docs live under `documentation/MarketplaceUserGuide/marketplace/user-guide/docs/` (Operator-portal / Vendor-portal subfolders, ~20 md files). Marketing pages live under `documentation/VirtoCommerce/marketplace/*.md`. Claims are assessed as "poorly documented or absent" against those corpora.

---

## Claim 1: Seller onboarding / KYC is thin
**Context7** (`/virtocommerce/vc-docs`, query on onboarding/KYC/Stripe Connect/payouts/order split/per-vendor shipping): returned only Commission overview and a generic mention from the state-machine module that onboarding is a supported use case. Nothing about KYC/KYB, tax-ID collection, identity verification, or regulated onboarding steps.

**WebSearch** (Mirakl / Sharetribe Stripe Connect KYC): confirms industry standard is explicit KYC/KYB workflows — Mirakl surfaces the KYC link in the seller back office, Sharetribe wires Stripe Connect custom accounts with whitelabel KYC collection. Sources: `sharetribe.com/academy/marketplace-payments/stripe-connect-overview/`, `stripe.com/docs/plugins/mirakl/onboarding-sellers`.

**Grep** (scope: DOCS):
- `grep -rli "KYC"` across all DOCS: **0 files**.
- `grep -rli "identity verification"`: 2 hits, both in `VirtoCommerce/industry/pharmaceutical.md` (user authentication, not vendor KYC).
- `grep -rli "onboarding"`: 37 files — but vendor-specific onboarding is one page: `MarketplaceUserGuide/marketplace/user-guide/docs/Operator-portal/Vendors-management/vendor-onboarding.md`. That page is ~35 lines: "fill in the fields, click Invite". No tax-ID, no document upload, no W-8/W-9, no compliance gate, no link to a real KYC provider.
- Related: `registration-requests.md` just covers an operator approving a self-submitted registration form.

**Verdict**: 🟡 Mentioned but thin
**Note**: Vendor invite + registration-request flow exists. KYC, identity/business verification, and compliance tooling are absent by name. Marketing page (`marketplace/multi-vendor.md`) lists "Custom Onboarding Pipelines" including "compliance and verification methods" but the user guide never follows up.

---

## Claim 2: Commission / payout split is thin
**Context7**: solid coverage for commissions — static vs dynamic fees, assignment to vendor / group / product / category, percentage or fixed amount. Zero results for payouts.

**WebSearch** (same call as Claim 1): Mirakl Payout, Stripe Connect, Adyen for Platforms all bundle commission config with a payout/disbursement engine and KYC. That pairing is the industry norm.

**Grep** (scope: DOCS):
- `grep -rli "commission"`: 20 files. Dedicated subfolder `Operator-portal/Commission-fees-setup/` with overview + static + dynamic pages (~80 lines total). Well-structured for the commission-calculation side.
- `grep -rli "payout"`: **0 files**. Not a single mention.
- `grep -rli "disbursement"`: 0 files.
- `grep -rli "payment.*split\|payments split"`: 3 hits, all in marketing pages (`marketplace/multi-vendor.md:84`, `marketplace/service-marketplace.md:122`, `marketplace/b2b-marketplace-platform.md:127`) — one-word feature-bullet on a datasheet, no explanation.

**Verdict**: 🟡 Mentioned but thin
**Note**: Commission *calculation* is well documented. The "what happens to the money after" half — payout schedule, ledger, reserve, Stripe/Adyen disbursement, refund-to-vendor clawback — is entirely missing. Marketing says "Payments split" but user guide is silent.

---

## Claim 3: Multi-vendor single cart / order splitting is thin
**Context7**: confirms vendors see only their part of the order in the Vendor portal.

**WebSearch**: not needed — confirmed by grep.

**Grep** (scope: DOCS):
- `grep -rli "order split\|split.*order\|order splitting"`: 4 files. Key hit: `MarketplaceUserGuide/marketplace/user-guide/docs/Operator-portal/operator-orders.md:20` — "The order automatically is split between vendors. Each vendor sees only their part of the order." Marketing pages add "Vendor order split" / "Order split by vendor" bullets.
- `grep -rli "sub-order\|suborder"`: 0 hits.
- No discussion of how items are grouped, whether carts allow mixed-vendor checkout, status-per-vendor semantics, split invoicing, or atomic vs per-vendor payment capture.

**Verdict**: 🟡 Mentioned but thin
**Note**: The feature exists and is asserted, but the mechanism is one sentence + two screenshots. Developer-facing docs don't explain the data model (order → shipments-per-vendor? sub-orders? a single order with vendor-tagged line items?), which is the first question any integrator asks.

---

## Claim 4: Vendor product approval workflow is thin
**Context7**: surfaces the Vendor-portal "submit for approval" + Operator-portal "approve/decline with reason" flow.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rli "approval\|approve"` scoped to marketplace: hits in `Operator-portal/marketplace-products.md` (~50-line page covering Approve and Decline with reason) and `Vendor-portal/products-management.md` ("Submit for approval" button).
- No mention of: multi-step approval chains, auto-approval rules by vendor tier, bulk approval, change-set approval (edit to an already-approved product), approval SLA, or approval notifications.
- `grep -rli "moderation"`: 0 hits.

**Verdict**: 🟡 Mentioned but thin
**Note**: Binary approve/decline per-product is documented. Anything resembling a configurable moderation workflow — tiers, auto-approve on repeat vendors, editorial queue, content-policy rules — is absent.

---

## Claim 5: Marketplace SEO / vendor pages is thin
**Context7**: nothing relevant.

**WebSearch**: not run — strong absence in grep.

**Grep** (scope: DOCS):
- `grep -rli "vendor page\|vendor SEO\|seller page\|seller profile\|vendor storefront"` across marketplace + storefront docs: **0 files**.
- Marketing `marketplace/multi-vendor.md:86` lists "Advanced SEO management" as a feature bullet — but for the store as a whole, not per-vendor.
- `Vendor-portal/my-store.md` covers Profile (name, address, logo), People, Fulfillment centers. No mention of a public-facing vendor page with URL slug, description, hero banner, meta tags, canonical URL, structured data, or vendor-filtered product listing.

**Verdict**: 🔴 Absent
**Note**: The term "vendor page" or "seller page" does not appear in user-facing docs. Whether a public vendor landing page even exists on the Virto storefront is undiscoverable from docs.

---

## Claim 6: Vendor analytics / dashboards is thin
**Context7**: nothing on analytics.

**WebSearch**: not run.

**Grep** (scope: DOCS):
- `grep -rli "vendor analytics\|vendor dashboard\|seller dashboard\|vendor report\|vendor KPI\|marketplace analytics"` across DOCS: only a thought-leadership blog post in B2BExperts talking about the industry at large.
- `Vendor-portal/overview.md:7` and `Operator-portal/overview.md:7` each embed a `vendor-portal-dashboard.png` / `operator-portal-dashboard.png` image — but the prose doesn't describe what metrics, widgets, cohorts, or time ranges the dashboards contain. The word `dashboard` is used only in these image captions.
- Marketing bullets mention "Operator dashboard" / "Professional reporting" without detail.
- GMV, conversion rate, AOV, sell-through, top-sellers — none of these analytics terms appear in marketplace docs.

**Verdict**: 🟠 Implemented but undocumented
**Note**: Screenshots hint there is a dashboard; the user guide never lists its metrics or explains how to read/customize/export them. For vendors evaluating the platform, "what will I see" is unanswered.

---

## Claim 7: Return split across vendors is absent
**Context7**: nothing.

**WebSearch**: not run.

**Grep** (scope: DOCS):
- `grep -rli "return.*vendor\|vendor.*return\|return split\|split return\|RMA.*vendor\|vendor.*RMA"` across marketplace + VirtoCommerce + B2BExperts: **0 files**.
- `grep -rli "RMA"` inside MarketplaceUserGuide: 0 files.
- "Return" inside MarketplaceUserGuide appears only in unrelated contexts ("return to the Operator portal" navigation, Dynamics 365 package importer, logging levels).

**Verdict**: 🔴 Absent
**Note**: Who handles the refund when a multi-vendor order is partially returned — platform, vendor, both? What's the clawback on commission? These questions have no answer in the corpus.

---

## Claim 8: Stripe Connect / Adyen MarketPay is absent
**Context7**: nothing.

**WebSearch**: Stripe Connect, Adyen for Platforms (ex-MarketPay), and Mirakl Payout are the de-facto marketplace payment rails. Any competitor (Sharetribe, CS-Cart, Mirakl) leads with one of these.

**Grep** (scope: DOCS):
- `grep -rli "Stripe Connect\|MarketPay\|Adyen MarketPay"` across all DOCS: **0 files**.
- `grep -rli "Adyen for Platforms"`: 0.
- `grep -rli "Mirakl Payout"`: 0. (Mirakl itself is name-checked only in a competitor-comparison asset and a blog post.)
- No mention of PayPal Commerce Platform for marketplaces either.

**Verdict**: 🔴 Absent
**Note**: This is the single biggest hole for anyone evaluating VC-Marketplace vs Mirakl/Sharetribe/CS-Cart. Competitors document a named payment-rail integration; VC docs don't name any marketplace-grade one.

---

## Claim 9: Drop-ship vendor integration is thin
**Context7**: nothing on dropshipping.

**WebSearch**: not run — strong absence in grep.

**Grep** (scope: DOCS):
- `grep -rli "drop-ship\|dropship\|drop ship"` across DOCS: **0 files**.
- Closest concept in docs: per-vendor Fulfillment Centers (`Vendor-portal/my-store.md:33`) — ~6 lines describing that a vendor can add fulfillment centers and assign external IDs for inventory sync. No discussion of drop-ship product type, drop-ship-only vendors, ship-from-vendor vs ship-from-operator-warehouse, or drop-ship order routing.
- Mirakl (named in B2BExperts blog) explicitly markets "dropship businesses"; VC docs don't claim the term.

**Verdict**: 🔴 Absent
**Note**: The architecture plausibly supports dropship via per-vendor fulfillment centers and the order split, but the term and the workflow aren't documented.

---

## Claim 10: Vendor-specific shipping rules is thin
**Context7**: nothing.

**WebSearch**: not run.

**Grep** (scope: DOCS):
- `grep -rli "vendor shipping\|seller shipping\|per-vendor shipping\|vendor rates\|vendor fulfillment"` across DOCS: **0 files**.
- "Shipping" appears exactly twice in MarketplaceUserGuide — both in `Vendor-portal/orders.md:45-48` describing the per-order Shipping widget a vendor uses to create a shipment document. No discussion of vendor-specific shipping *rules*: methods, zones, carriers, thresholds, origin-country, weight/dimensional rating, or how the storefront presents cart-level shipping when products come from multiple vendors.
- Marketing bullet "Flexible shipments" (`marketplace/multi-vendor.md:108`) is never elaborated.

**Verdict**: 🔴 Absent
**Note**: Per-vendor shipping configuration — arguably the most common pain point in marketplace ops — has no topic in the user guide. Competitors (CS-Cart, WooCommerce Product Vendors, Marketplacer) all have dedicated chapters on this.

---

## Overall shape

**Strong**: Commission fees (static + dynamic, 80+ lines over 3 pages) and product approval (binary approve/decline with reason) are the two well-covered marketplace workflows. Vendor onboarding has a real page, and order-splitting is at least asserted. The Marketplace User Guide structure (Operator-portal vs Vendor-portal) is clean and discoverable.

**Weak**: Everything that touches money-out-the-door or public presentation is missing — payouts, disbursement, Stripe Connect / Adyen for Platforms / Mirakl Payout, vendor public pages / SEO, vendor analytics (beyond a screenshot), and return handling across vendors. Operational configuration gaps — per-vendor shipping rules, drop-ship, KYC/compliance — are the topics a real marketplace operator would hit first and the docs would fail them on. Marketing pages (`marketplace/multi-vendor.md`, etc.) list many of these as feature bullets ("Payments split", "Flexible shipments", "Advanced SEO management"), but the user guide never follows through, producing a bait-and-switch for anyone doing doc-based evaluation.

**Net**: 5 🔴, 1 🟠, 4 🟡, 0 ✅. VC-Marketplace ships a real operator+vendor admin UX but documents it like a demo — adequate for "yes, this exists" screenshots, inadequate for integration planning or competitive comparison against Mirakl/Sharetribe/Marketplacer/CS-Cart.
