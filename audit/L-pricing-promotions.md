# Group L — Pricing & Promotions

## Claim 1: Tier pricing / volume pricing is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I set up tier pricing or volume pricing / quantity-based pricing for products in VirtoCommerce?"):
Returned GraphQL/xAPI references (`TierPriceType`, `prices[].minQuantity`, `prices[].tierPrices[].quantity`), one how-to on overriding `SetLineItemTierPrice` in `CartAggregate`, and price-range filtering syntax. No user-guide page titled "Tier pricing" or "Volume pricing"; the merchandiser workflow to enter multiple quantity-break prices is not described. The price-list CSV mapping page mentions a `Min quantity` column but calls it neither "tier" nor "volume" pricing.

**WebSearch** (query: "'tier pricing' ecommerce B2B Magento Shopify documentation definition volume quantity break"):
"Tier pricing" is the industry standard term for quantity-break pricing in B2B. Magento and Shopify Plus both document it as a first-class pricing strategy (MOQs + volume discounts). Sometimes called "volume pricing" or "bulk pricing"; all variants common.

**Grep** (scope: DOCS):
- `grep -rli "tier pric" DOCS`: 2 files (both developer-oriented: xAPI Quote object, cart-validation how-to)
- `grep -rli "volume pric" DOCS`: 0 files
- `grep -rli "Min quantity" …/price-export-import`: 2 files (the CSV import docs)
- Top hits:
  - `PlatformDeveloperGuide/.../customizing-cart-validation-policies.md:77-108` — override `ValidateTierPrice`, `SetLineItemTierPrice`
  - `PlatformUserGuide/.../price-export-import/importing-price-lists.md:16` — "**Min quantity**… required" (unexplained)
  - `PlatformUserGuide/.../price-export-import/mapping-csv-files.md:9` — same, CSV field only

**Verdict**: 🟠 Implemented but undocumented
**Note**: Data model and xAPI fully support tier prices (`minQuantity` + `tierPrices[]`), but the merchandiser user-guide never names or explains the feature. A merchandiser searching "tier pricing" in the docs hits dev how-tos and CSV schema only.

---

## Claim 2: Customer-group / contract pricing is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure customer-group pricing or contract pricing in VirtoCommerce? What about price lists tied to user groups or companies?"):
Solid coverage. The user guide has a dedicated **Contracts** module section plus a **Pricing** example that walks through creating a user group, assigning contacts, and binding a price list via the *User group contains* condition. Contracts automatically create a per-contract user group + dedicated price list on activation.

**WebSearch** (query: "'contract pricing' B2B ecommerce Magento commercetools customer-specific price list"):
Industry-standard B2B feature; Magento and commercetools both document it extensively. VC's contracts concept maps cleanly onto this.

**Grep** (scope: DOCS):
- `grep -rli "contract"` inside `PlatformUserGuide/.../contracts`: 4 files — `overview.md`, `creating-and-terminating-contracts.md`, `managing-contract-customers.md`, `managing-contract-prices.md`
- `grep -rli "user group"` hits inside `pricing/` and `catalog-personalization/`
- Top hits:
  - `PlatformUserGuide/.../contracts/overview.md:36-44` — contract → user group → price list chain
  - `PlatformUserGuide/.../pricing/example.md:12-25` — VIP user-group example
  - `PlatformUserGuide/.../pricing/troubleshooting-guide.md:13` — "User group contains" condition

**Verdict**: ✅ Well documented
**Note**: Contracts module + price-list assignments with user-group conditions = full customer-group/contract pricing story. The *term* "contract pricing" isn't used explicitly (VC calls it "contracts" and "price list assignments"), but substance and examples are there.

---

## Claim 3: Dynamic pricing / rule-based pricing is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support dynamic pricing or rule-based pricing? How do conditional price rules work?"):
Pricing module overview says "price list assignments… associate specific price lists with catalogs based on rules and conditions". Marketplace landing page mentions "Dynamic Pricing & Personalization" as a feature bullet but with no drill-down. No dedicated page on dynamic or rule-based pricing (the rules mentioned are really *assignment* conditions).

**WebSearch** (via Claim 9): In competitor docs, "dynamic pricing" usually means algorithmic/time-based pricing or Magento's catalog price rules. VC has neither under that name.

**Grep** (scope: DOCS):
- `grep -rli "dynamic pric" DOCS`: 6 files — 2 marketing pages (`VirtoCommerce/marketplace.md`, `solutions/marketplace.md`), 1 architecture page, 3 B2BExperts articles (opinion pieces).
- `grep -rli "rule.based pric\|catalog rule\|cart rule\|pricing rule" DOCS`: 3 files — all generic marketing/features pages
- Top hits:
  - `VirtoCommerce/marketplace.md:66` — "Dynamic Pricing & Personalization" bullet, no body
  - `PlatformDeveloperGuide/.../atomic-architecture.md:24` — mentions custom molecules "such as dynamic pricing tools" as an example
  - `VirtoCommerce/features.md` — generic feature bullet

**Verdict**: 🟡 Mentioned but thin
**Note**: The marketing pages use "Dynamic Pricing" as a buzzword without a how-to. There is no documented concept of a dynamic/rule-based *price calculation* (only price-list *assignment* conditions + discount *promotions*). A Magento user expecting catalog-price-rules will find no equivalent page.

---

## Claim 4: Discount stacking / priority rules are thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I stack promotions in VirtoCommerce with priorities? Can promotions combine and what's the priority order?"):
Strong coverage. Dedicated page **Promotion combination policies** with two modes: "Best reward policy" (default) and "Stackable policy". Explicitly describes behavior when rewards would make totals negative and the priority-settings fallback.

**WebSearch**: Not needed — Context7 returned crisp, direct content.

**Grep** (scope: DOCS):
- `grep -rli "stack.*promo\|combin.*promo\|exclusive promo" DOCS`: 7 files
- Top hits:
  - `PlatformUserGuide/.../marketing/combining-active-promotions.md:1-19` — full explainer
  - `PlatformUserGuide/.../marketing/promotions-overview.md:17` — "Setting promotion combination policies"
  - `PlatformUserGuide/.../marketing/combining-active-promotions.md:19` — skipping logic + priority settings

**Verdict**: ✅ Well documented
**Note**: Both stacking behaviors + priority-based fallback explicitly documented in the user guide. Term "discount stacking" isn't used (they say "combining / stackable") but the concept is fully there.

---

## Claim 5: Coupon / voucher management is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I manage coupons and vouchers in VirtoCommerce? Can I generate coupon codes in bulk and apply them to promotions?"):
Extensive coverage: `addCoupon` mutation, `promotionCoupons` query, `PromotionCouponType` object, user-guide "Create coupons and gift cards" with manual + CSV import, per-coupon expiry + usage limits.

**WebSearch**: Not needed — Context7 sufficient.

**Grep** (scope: DOCS):
- `grep -rli "coupon\|voucher" DOCS`: 31 files
- Top hits:
  - `PlatformUserGuide/.../marketing/managing-promotions.md:31-61` — add/import coupon flow
  - `PlatformDeveloperGuide/.../Marketing/mutations/addCoupon.md` — storefront mutation
  - `PlatformDeveloperGuide/.../Marketing/queries/promotionCoupons.md` — listing query
  - `PlatformDeveloperGuide/.../Marketing/objects/PromotionCouponType.md` — type schema

**Verdict**: ✅ Well documented
**Note**: Coupons (but not "vouchers" — that term is absent, though synonymous) are first-class citizens. CSV bulk import, storefront GraphQL mutations/queries, and admin UX all documented.

---

## Claim 6: Gift-card issuance / redemption is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support gift cards? How do I issue, sell, and redeem gift cards?"):
The only gift-card hit is a promotion-reward type labeled "gifts" and a section header "Create coupons and gift cards" — but the body of that section ONLY describes coupon codes; there is no stored-value card product, no balance tracking, no redemption tender, no recipient-email flow. The `addGiftItems` / `rejectGiftItems` GraphQL mutations refer to **promotional free gifts** added to a cart, not stored-value gift cards.

**WebSearch** (query: "Shopify commercetools 'gift card' product type issuance redemption balance e-commerce"):
Shopify has a dedicated gift-card product type with denominations, partial redemption, balance page, and POS support. Commercetools relies on a Voucherify connector for gift-card engine (issue, track, redeem, balance, expiry, partial).

**Grep** (scope: DOCS):
- `grep -rli "gift.card\|gift card" DOCS`: 4 files
- Top hits:
  - `PlatformUserGuide/.../marketing/managing-promotions.md:6, 31` — heading only; body is all coupons
  - `PlatformUserGuide/.../platform-overview.md:15` — same link (decorative nav bullet)
  - `B2BExperts/.../Support-non-product-search.md`, `Technical-debt-demands-your-attention.md` — opinion pieces, mention gift cards as generic e-commerce feature

**Verdict**: 🔴 Absent (as a product feature)
**Note**: "Gift cards" appears only as a heading without substance. No stored-value gift-card SKU type, no balance/redemption concept in VC docs. The `addGiftItems` GraphQL is about promotional freebies, not prepaid cards — a new user misled by the title will be disappointed.

---

## Claim 7: Loyalty program (points, tiers) is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have a loyalty program module with points and tiers? How is it configured?"):
Dedicated **Loyalty module** documented. Points accrual via fixed or % of order, conditions, priorities, activation periods, localized names, redemption of points as a payment method. GraphQL Loyalty API: `loyaltyBalance`, `loyaltyPointsHistory`.

**WebSearch**: Not needed.

**Grep** (scope: DOCS):
- `grep -rli "loyalty" DOCS`: 99 files (release notes, guides, marketing pages, GraphQL refs)
- Top hits:
  - `PlatformUserGuide/.../loyalty/overview.md` — module overview + features
  - `PlatformUserGuide/.../loyalty/enable-and-configure-loyalty-programs.md` — configuration walkthrough
  - `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/Loyalty/queries/loyaltyBalance.md` + `.../loyaltyPointsHistory.md`
- `grep -rli "loyalty tier\|bronze\|silver\|gold.*member"` inside loyalty/: 0 hits

**Verdict**: 🟡 Mentioned but thin — **tiers** absent
**Note**: Points accrual + redemption: solid. **Membership tiers (bronze/silver/gold)** — a core loyalty-program primitive — are nowhere in the docs. The claim partially holds: loyalty is documented, but the "tiers" sub-claim is accurate.

---

## Claim 8: Bundle pricing is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle bundle pricing? Can bundles have their own price versus sum of components?"):
No result for product-bundle pricing. Context7 returned tier-price override code, zero-price buyability, multi-regional price-list blurb, and a "Digital Catalog Application Package" (module bundle, unrelated). No merchandiser page on creating a bundle SKU.

**WebSearch** (query: "Magento 'bundle product' 'kit product' dynamic pricing fixed pricing ecommerce"):
Magento's bundle product is a first-class product type with two pricing modes: **dynamic** (sum of components) or **fixed** (master-level price). Industry-standard pattern.

**Grep** (scope: DOCS):
- `grep -rli "bundle pric" DOCS`: 0 files
- `grep -rli "bundle" PlatformUserGuide StorefrontUserGuide VirtoCommerce`: 0 files
- Every "bundle" hit in `PlatformDeveloperGuide` refers to **module bundles** (package groupings like the "commerce" bundle) or JS bundles — not product bundles.

**Verdict**: 🔴 Absent
**Note**: No "bundle product" type, no bundle pricing concept in docs. If the platform supports it via generic dynamic-associations / main-product-variations, the docs do not surface it under this vocabulary. The term "bundle" is overloaded toward module packaging.

---

## Claim 9: Catalog-level vs cart-level promotions terminology is thin
**Context7** (`/virtocommerce/vc-docs`, query: "What is the difference between catalog-level promotions and cart-level promotions in VirtoCommerce?"):
VC does expose both in the promotion rule builder via `BlockCatalogCondition` (catalog-side conditions) and cart conditions (`promotion-rules.md` says "match different catalog and cart conditions"). But the distinction is not elevated to a named feature. There is no page titled "Catalog price rules" or "Cart price rules".

**WebSearch** (query: "Magento 'catalog price rule' vs 'cart price rule' terminology explained"):
Magento's dichotomy is a universal mental model: catalog price rules = visible on PDP/PLP before cart, no coupons; cart price rules = applied during checkout, can use coupons. Merchandisers think in these terms.

**Grep** (scope: DOCS):
- `grep -rli "catalog.level promo\|cart.level promo\|catalog rule\|cart rule" DOCS`: 0 files
- `grep -rni "catalog condition\|cart condition\|BlockCatalogCondition"` : hits in `promotion-rules.md:3` (one mention) and `extending-dynamic-expression-tree.md:25-34` (dev extensibility)

**Verdict**: 🟡 Mentioned but thin
**Note**: Implemented (condition blocks separate catalog matches from cart matches) but never framed as the widely-known "catalog price rule vs cart price rule" dichotomy. A Magento-veteran merchandiser will have to reverse-engineer the mapping.

---

## Claim 10: Price lists / currency-specific price lists is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I set up currency-specific price lists in VirtoCommerce? Can I have USD, EUR, and GBP prices per store?"):
Price list module documented; each price list stores prices in a single currency and multiple price lists per currency are supported. Multi-regional eCommerce architecture page explicitly calls out "supports multi-currency, allowing for the uploading and management of price lists in different currencies for different regions."

**WebSearch**: Not needed.

**Grep** (scope: DOCS):
- `grep -rli "price list\|pricelist" PlatformUserGuide`: 25 files
- Top hits:
  - `PlatformUserGuide/.../pricing/overview.md` — module overview (one-currency-per-price-list design)
  - `PlatformUserGuide/.../pricing/creating-new-price-list.md` — create/edit/delete flow
  - `PlatformUserGuide/.../pricing/adding-new-assignment.md` — assign to stores, catalogs, user groups
  - `PlatformUserGuide/.../pricing/viewing-price-list-in-catalog.md` — catalog preview
  - `PlatformUserGuide/.../multiregional-ecommerce.md` — multi-currency architecture

**Verdict**: ✅ Well documented
**Note**: Price lists are a core documented concept with assignments by store/catalog/user-group and per-currency lists. Good merchandiser coverage.
