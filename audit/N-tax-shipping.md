# Group N — Tax & Shipping

## Claim 1: Avalara AvaTax integration is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I integrate Avalara AvaTax with VirtoCommerce for sales tax calculation?"):
Multiple substantive hits: `appsettings.json` Tax.Avalara config (AccountNumber/LicenseKey), dedicated integration page in `integrations-configuration.md`, store-configuration page explains sending transactions and receiving real-time tax totals, and a dedicated `platform/user-guide/docs/integrations/avalara/taxes-calculation.md` page.

**WebSearch**: not run — Context7 + grep signal is strong.

**Grep** (scope: DOCS):
- `grep -rli "avalara\|avatax" DOCS`: 10+ files including dedicated folder `PlatformUserGuide/.../integrations/avalara/` with `overview.md`, `settings.md`, `taxes-calculation.md`, `address-validation.md`, `tax-type-configuration.md`.
- Occurrence count: **108** mentions across DOCS.
- Top hits: `PlatformUserGuide/.../integrations/avalara/overview.md`, `.../taxes-calculation.md`, `DeploymentGuide/.../store-configuration.md`, `PlatformDeveloperGuide/.../appsettingsjson.md`.

**Verdict**: Well documented
**Note**: Avalara has its own 5-page doc folder plus deployment/config references. The claim is rejected — Avalara is by far the best-documented tax topic in VC.

---
## Claim 2: TaxJar / Vertex alternatives are absent

**Context7**: not run (covered by tax-provider Context7 call in claim 5 — only Fixed Rate + Avalara named).

**WebSearch**: not needed — TaxJar and Vertex are industry-standard tax-calculation SaaS alternatives (TaxJar acquired by Stripe, Vertex Inc. is a major tax-engine vendor). Their absence is meaningful given VC targets US sales-tax compliance.

**Grep** (scope: DOCS):
- `grep -rli "taxjar" DOCS`: **0** files
- `grep -rli "sovos" DOCS`: **0** files
- `grep -rli "vertex.*tax\|vertex inc\|vertexinc" DOCS`: **0** files

**Verdict**: Absent
**Note**: VC docs mention only Avalara and the built-in Fixed Rate tax provider. TaxJar/Vertex/Sovos are zero-mention, although the extensibility model (`TaxProvider` abstract class documented in `new-tax-provider-registration.md`) makes them implementable. Absence of "you can build adapters for TaxJar/Vertex" guidance is a gap.

---
## Claim 3: EU VAT / VIES validation is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure EU VAT rates and VIES VAT number validation in VirtoCommerce?"):
No relevant results — Context7 returned package-manifest and dynamic-property examples, nothing about VAT.

**WebSearch** (query: "VirtoCommerce EU VAT VIES validation tax configuration"):
Only generic VIES/EU VAT explainers returned — zero VirtoCommerce-specific results, which corroborates the gap.

**Grep** (scope: DOCS):
- `grep -rli "\bVAT\b" DOCS`: **1** file (`B2BExperts/docs/Vertical-take-off-a-new-direction-for-b2b-marketplaces.md` — blog, incidental).
- `grep -rli "VIES" DOCS`: **2** files (both blog articles, not VIES-the-validation-service).
- `grep -rli "EU VAT\|european.*vat\|VAT MOSS\|OSS VAT" DOCS`: 4 files, all marketing/blog content.

**Verdict**: Absent
**Note**: VC docs have **zero** practical guidance on EU VAT configuration, VIES VAT-ID validation, reverse-charge B2B invoicing, or OSS/IOSS. For a platform claiming B2B focus in Europe this is a serious gap. Hits are blog-only false positives.

---
## Claim 4: GST (India, Australia, Canada) is thin

**Context7**: not run (budget reserved) — tax-provider model is extensible but Context7 answers focused on Avalara/Fixed Rate.

**WebSearch**: not run — industry prevalence of GST/HST/PST/QST is self-evident.

**Grep** (scope: DOCS):
- `grep -rli "\bGST\b\|goods and services tax" DOCS`: **0** files.
- `grep -rli "\bHST\b\|\bPST\b\|\bQST\b" DOCS`: **0** files.

**Verdict**: Absent
**Note**: No mention of India GST, Australia GST, Canada GST/HST/PST/QST. Merchants in those jurisdictions must either write a custom `TaxProvider` or rely on Avalara — neither path is sign-posted in docs. Strong gap for non-US expansion.

---
## Claim 5: Tax-exempt customer groups is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure tax-exempt customers or tax-exempt customer groups in VirtoCommerce?"):
Two tax-provider overview pages plus a Promotion Rules page (re: customer conditions). No dedicated tax-exemption workflow; exemption is an Avalara-specific detail only.

**WebSearch**: not run.

**Grep** (scope: DOCS):
- `grep -rli "tax.exempt\|tax exempt" DOCS`: **2** files — both in Avalara folder.
- Occurrence count: **3**.
- Top hits:
  - `PlatformUserGuide/.../integrations/avalara/tax-type-configuration.md:26` — `## Tax exemptions`: instructs adding a `Tax exempt` **dynamic property** (ShortText) on the customer and setting exemption certificate number.
  - `PlatformUserGuide/.../integrations/avalara/overview.md` — lists exemptions as a feature.

**Verdict**: Mentioned but thin
**Note**: Tax-exempt handling is **Avalara-coupled only** and implemented via a generic dynamic property — not a first-class customer attribute or group-based exemption matrix. No discussion of tax-exempt customer *groups*, resale certificates lifecycle, or non-Avalara exemption. Industry-standard "tax class per customer group" vocabulary is absent.

---
## Claim 6: Carrier integrations (UPS, FedEx, DHL, USPS) are thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I set up UPS, FedEx, DHL, or USPS shipping carrier integrations in VirtoCommerce?"):
Only `new-shipping-method-registration.md` (abstract `ShippingMethod` class + DI registration) and `FixedRateShippingMethod` — no carrier modules returned.

**WebSearch**: not run — finding is already clear.

**Grep** (scope: DOCS):
- `grep -rli "UPS\|FedEx\|DHL\|USPS" DOCS`: ~30 files, but virtually all are false positives (`Start-Ups`, `setups`, unrelated prose).
- Word-boundary `grep -rlni "FedEx\|DHL\|USPS\|\bUPS\b"`: **3** files — and the only FedEx mention is in `DeploymentGuide/.../store-configuration.md:72` referencing `fedex.svg` **logo file** in a shipping-method config example (not an integration).
- Remaining matches are again `Start-Ups` prose.

**Verdict**: Absent
**Note**: VC ships only two shipping methods OOTB — `FixedRateShippingMethod` and `BOPIS`. No UPS/FedEx/DHL/USPS rate-shopping module exists in docs. Only a `fedex.svg` logo appears in a configuration screenshot example. Extensibility path (`ShippingMethod` abstract class) is documented but no built-in carrier adapters.

---
## Claim 7: ShipStation / EasyPost / Shippo are absent

**Context7**: not run (direct grep & page inspection already conclusive).

**WebSearch**: not run — carrier-aggregator absence is directly observable.

**Grep** (scope: DOCS):
- `grep -rli "shipstation\|easypost\|shippo" DOCS`: **3** files, all ShipStation.
- Dedicated folder `PlatformUserGuide/platform/user-guide/docs/shipstation/` with `overview.md` — links to `github.com/VirtoCommerce/vc-module-shipstation` module.
- EasyPost: **0** files. Shippo: **0** files.

**Verdict**: Mentioned but thin (ShipStation only); Absent (EasyPost, Shippo)
**Note**: ShipStation has a dedicated module + one-page overview describing order-sync one-way integration (rate-shopping *not* claimed). EasyPost and Shippo — two major shipping-aggregator APIs — are completely absent. The ShipStation page is minimal (no setup steps, just linking to external module README).

---
## Claim 8: Shipping zones / rate tables are thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure shipping zones, rate tables, and free shipping thresholds in VirtoCommerce?"):
Returned only `FixedRateShippingMethod`, DI registration, "fixed shipping rate" setup, and "global shipping settings". No zone or rate-table concept mentioned.

**WebSearch**: not run — competitors (Shopify, Magento, BigCommerce) treat shipping zones as a first-class concept, so absence is significant.

**Grep** (scope: DOCS):
- `grep -rli "shipping zone\|rate table\|shipping rate" DOCS`: 4 files (quote mgmt, new-shipping-method-registration, shipping/settings, store-configuration) — but none actually define a **shipping-zone feature**; they just use "shipping rate" as generic prose.
- `grep -rli "zone" PlatformUserGuide/.../shipping/`: **0** files.
- "shipping zone" occurrence count: **0**.

**Verdict**: Absent (as a first-class concept)
**Note**: VC's OOTB shipping is a flat `FixedRate` or `BOPIS` — **no shipping-zone matrix**, **no weight/dimension-based rate table UI**, **no postal-code-based zone mapping** documented. Competitors (Magento/Shopify/BigCommerce) all have shipping-zone editors. VC merchants would need a custom `ShippingMethod` implementation.

---
## Claim 9: Free-shipping thresholds are thin

**Context7**: covered by claim 8 query — no free-shipping-threshold concept returned.

**WebSearch**: not run — direct grep covers it.

**Grep** (scope: DOCS):
- `grep -rli "free.shipping\|free shipping" DOCS`: **2** files (UI slider component docs + a B2B blog) — **neither** is a "free shipping threshold" config doc.
- Occurrence count: **2** (both irrelevant).
- **However**, `marketing/promotion-rules.md` does list rewards like `$... off for shipping at ...` and `% off for shipping at ...` and "shipping discounts" — so free shipping is achievable via the Promotion Rules engine, just **never explicitly labeled** as "free shipping threshold".

**Verdict**: Mentioned but thin (indirectly, via promotions)
**Note**: Free shipping is implementable via promotion rewards (`$X off shipping` when cart conditions met), but the docs never use the industry-standard phrase "free shipping threshold" nor provide a worked example. A merchant searching "how do I set up free shipping over $100" would not find a direct answer.

---
## Claim 10: Click-and-collect / in-store pickup is thin

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure click-and-collect or in-store pickup (BOPIS) in VirtoCommerce storefront?"):
Multiple substantive hits: `Settings > BOPIS settings`, `Edit BOPIS shipping method`, `Add or edit pickup location`, full `Manage Shipping Methods` page walks through pickup points.

**WebSearch**: not run.

**Grep** (scope: DOCS):
- `grep -rli "BOPIS\|pickup in store\|click.and.collect\|in.store.pickup" DOCS`: 4 files.
- BOPIS occurrence count: **14**.
- Top hits:
  - `PlatformUserGuide/.../shipping/managing-shipping-methods.md` — full walkthrough for editing BOPIS shipping method, adding pickup locations, frontend display.
  - `PlatformUserGuide/.../shipping/settings.md` — BOPIS settings section (Google Maps integration).
  - `StorefrontUserGuide/.../shopping/checkout-process.md` and `StorefrontUserGuide/.../account/checkout-defaults.md` — pickup on the storefront side.
- "click-and-collect" literal: **0** files (VC exclusively uses BOPIS terminology).

**Verdict**: Well documented (under BOPIS)
**Note**: BOPIS/in-store pickup is a first-class OOTB shipping method with admin + storefront docs, pickup-location management, and Google Maps integration. The **terminology gap** is that "click-and-collect" (the European / UK standard term) never appears — only the US "BOPIS" abbreviation is used. A European merchant searching "click and collect" would miss the feature.
