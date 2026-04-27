# Group T — Subscriptions & Recurring

## Claim 1: Subscription product type is thin

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have a subscription product type? How do I sell recurring subscriptions like Netflix or a subscription box?"):
Returned the Subscription module overview: "The Subscription module enables retailers to sell subscription-based offerings and buyers to place recurring orders online." Otherwise, all hits are GraphQL **back-in-stock** subscriptions (notification subscriptions, not billing). No documented "subscription product type" concept — in VC, any product becomes a subscription via cart/order flags (`isRecuring`, `isReccuring` — with typos) rather than a distinct product type.

**WebSearch** (query: "Shopify subscriptions API Stripe Billing Chargebee dunning prorated metered billing documentation 2025"):
Competitors converge on "subscription product type" + explicit billing primitives: Shopify has `AppSubscriptionReplacementBehavior` / `createUsageRecord`; Chargebee has Subscriptions, Usages, proration, dunning; Adobe Commerce "turn any virtual or simple product into a subscription". VC's vocabulary is much lighter.

**Grep** (scope: DOCS):
- `grep -rli "subscription" DOCS`: 81 files — but dominated by **back-in-stock subscriptions** and marketing copy about "Virto Commerce subscription pricing" (SaaS pricing, not feature).
- Actual subscription module docs: 3 files totaling **95 lines** (`overview.md`, `enabling-subscriptions.md`, `settings.md`) under `PlatformUserGuide/.../subscription/`.
- Top hits: `PlatformUserGuide/platform/user-guide/docs/subscription/overview.md:3` — only defines the feature; no product-type modeling, no lifecycle, no billing cadence details.

**Verdict**: 🟡 Mentioned but thin
**Note**: The Subscription module exists and is wired through cart/order (`isRecuring` flag) + GraphQL, but there is no "subscription product type" article explaining modelling, SKU setup, or selling strategies. Buyer-facing storefront doc for subscriptions is effectively absent.

---

## Claim 2: Recurring order schedule is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure a recurring order schedule in VirtoCommerce — daily, weekly, monthly cadence?"):
Reused Claim 1 call — Context7 returned nothing beyond "buyers place recurring orders online." No interval/cadence article, no cron-like schedule documentation.

**WebSearch** (query "commercetools BigCommerce Adobe Commerce recurring subscription product type documentation"):
commercetools explicitly documents `RecurrencePolicies` and `RecurringOrders` with predefined intervals; commercetools even ships an open-source `commercetools-subscriptions` cron service. VC uses `Hangfire` / `RecurringJobId` (indexing context), not a scheduling concept for orders.

**Grep** (scope: DOCS):
- `grep -rli "recurring" DOCS`: 10 files. Nearly all irrelevant — sitemaps cron, indexing jobs (`IndexingJobs.IndexChangesJob`), B2B marketing prose.
- Only two schema-level hits for recurring orders: `GraphQL-Storefront-API-Reference-xAPI/Cart/objects/cart-type.md:20` (`isRecuring` on Cart) and `.../line-item-type.md:22` (`isReccuring` on LineItem). Both contain a one-line description and two typos (`isRecuring`, `isReccuring`).
- No schedule/interval/frequency/billing-cycle article in subscription docs: `grep -rin "schedule|interval|frequency|period" PlatformUserGuide/.../subscription/` returns 0 lines.

**Verdict**: 🟡 Mentioned but thin
**Note**: Recurring orders exist in the model (GraphQL flags + module) but are not documented: no article explains how to set cadence, when the next order runs, or how to change it. Typos in the API field names are propagated into docs.

---

## Claim 3: Dunning / failed-payment recovery is absent

**Context7** (`/virtocommerce/vc-docs`, query: "What happens when a recurring subscription payment fails in VirtoCommerce? Dunning, retries, grace period?"):
Reused Claim 1 call — nothing. Module overview doesn't discuss payment retries or failure handling.

**WebSearch** (shared Chargebee/Stripe query):
"Chargebee provides automatic dunning for payment failures." Stripe/Chargebee/Recurly all treat dunning as a named, first-class feature with retry schedules, email sequences, and grace periods. It's ubiquitous industry vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "dunning" DOCS`: **0 files**.
- No mention of "retry schedule", "grace period", "failed payment", or "recovery" in subscription context.

**Verdict**: 🔴 Absent
**Note**: Neither the term nor the capability is documented. If VC's subscription module has any retry behaviour, it is invisible to readers.

---

## Claim 4: Usage-based / metered billing is absent

**Context7** (`/virtocommerce/vc-docs`, query: reused T1 call about billing):
No result for metered / usage-based billing in the returned snippets.

**WebSearch** (shared Chargebee/Stripe query):
"Usages API records usage for metered item prices... metered items are those billed based on service usage." Metered billing is a standard primitive in Stripe Billing, Chargebee, Recurly.

**Grep** (scope: DOCS):
- `grep -rli "metered|usage-based|usage based" DOCS`: **0 files**.

**Verdict**: 🔴 Absent
**Note**: VC has no documented concept of per-unit/metered consumption billing. Fits VC's B2B ordering model — likely ⚪ not-applicable in practice — but absence is notable given typical SaaS-adjacent expectations.

---

## Claim 5: Subscription upgrade / downgrade is thin

**Context7** (reused T1 call):
Nothing on plan changes/upgrades/downgrades.

**WebSearch**:
Shopify: `AppSubscriptionReplacementBehavior` enum; Chargebee: "For upgrades and downgrades of subscriptions with both metered and non-metered components, customers receive invoices with prorated charges." Standard competitor terminology.

**Grep** (scope: DOCS, inside subscription dir):
- `grep -rli "upgrade|downgrade" PlatformUserGuide/.../subscription/`: **0 files**.
- Broader DOCS: "upgrade" hits are all about platform version upgrades or SaaS plan upgrades — no subscription plan-change flow.

**Verdict**: 🔴 Absent
**Note**: No documented plan-change flow. The edit-subscription screenshot exists but the mechanics of switching a buyer between subscription plans are undocumented.

---

## Claim 6: Pause / skip / cancel is thin

**Context7** (reused T1 call):
No article on lifecycle actions (pause, skip-next, cancel).

**WebSearch**: Shopify Subscriptions, Ordergroove, Chargebee all expose pause/skip/cancel as documented buyer-portal actions.

**Grep** (scope: DOCS):
- `grep -rli "pause|skip|cancel" PlatformUserGuide/.../subscription/`: **0 files**.
- `grep -rin "cancel subscription|pause subscription|skip subscription"` across all DOCS: **0 lines**.

**Verdict**: 🔴 Absent
**Note**: The overview mentions "edit a subscription" but never names the actions. Storefront buyer flow for pausing/skipping/cancelling a subscription is not documented at all.

---

## Claim 7: Subscription boxes is absent

**Context7** (reused T1 call):
No results about subscription boxes, curated boxes, or box-of-the-month scenarios.

**WebSearch**: Crystallize, Ordergroove, Shopify (Shopify Subscriptions, Recharge) all position subscription boxes as a top named use case.

**Grep** (scope: DOCS):
- `grep -rli "subscription box|subscription boxes" DOCS`: **0 files**.

**Verdict**: 🔴 Absent
**Note**: No marketing or how-to content targets the subscription-box vertical — a sizable e-commerce segment.

---

## Claim 8: Subscription analytics / MRR is absent

**Context7** (reused T1 call):
No analytics/MRR/churn content returned.

**WebSearch**: Chargebee, Stripe Billing, Recurly all document SaaS metrics (MRR, ARR, churn, LTV, cohort retention) as native reports.

**Grep** (scope: DOCS):
- `grep -rli "\\bMRR\\b|monthly recurring revenue" DOCS`: **0 files**.
- No hits for ARR, churn rate, subscription cohort analysis.

**Verdict**: 🔴 Absent
**Note**: Zero subscription-metrics vocabulary. If reporting exists, it's invisible; VC's analytics docs speak in order-count terms, not SaaS metrics.

---

## Claim 9: Prorated billing is absent

**Context7** (reused T1 call):
No results on proration, mid-cycle adjustments, or credit calculation.

**WebSearch**: Chargebee has a dedicated "Billing Mode & Proration" doc page; Shopify explicitly "supports prorated charges when merchants upgrade or downgrade." Industry-standard term.

**Grep** (scope: DOCS):
- `grep -rli "prorat" DOCS`: **0 files** (covers proration, prorated, prorates).

**Verdict**: 🔴 Absent
**Note**: Neither the term nor the concept. Impossible for a reader to know if/how VC handles mid-cycle plan changes or partial refunds on subscriptions.

---

## Claim 10: Stripe Billing / Chargebee / Recurly comparison is absent

**Context7** (reused T1 call):
No comparison content returned. Module overview references only its own module, not third-party subscription platforms.

**WebSearch**: Crystallize publishes a "Top Subscription eCommerce Platforms" roundup; UniBee and others compare Stripe vs. Chargebee. Vendors typically position vs. these competitors.

**Grep** (scope: DOCS):
- `grep -rli "stripe billing|chargebee|recurly|zuora" DOCS`: **0 files**.

**Verdict**: 🔴 Absent
**Note**: No integration doc, no positioning doc, no "how VC's Subscription module compares/complements". This leaves buyers unable to see how VC fits next to the dedicated subscription-management category.
