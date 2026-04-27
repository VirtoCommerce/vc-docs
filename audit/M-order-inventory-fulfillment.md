# Group M — Order / Inventory / Fulfillment

Scope: `DOCS` = VirtoCommerce site + PlatformUserGuide + PlatformDeveloperGuide + StorefrontUserGuide + StorefrontDeveloperGuide + MarketplaceUserGuide + DeploymentGuide + B2BExperts.

## Claim 1: "OMS" (Order Management System) term usage is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have an OMS (Order Management System)? How is order management described?"):
Returned the `Approve Order` GraphQL mutation and scattered order-flow references. No canonical "OMS" landing / concept page surfaced; retrieved docs explain order operations but do not frame them under the industry label "OMS".

**WebSearch** (query: "OMS 'Order Management System' ecommerce platform Shopify commercetools Magento documentation"):
"OMS" is a first-class marketing and architecture term across Shopify, Magento, commercetools — each has a dedicated OMS product page or archived OMS doc portal. Industry-standard vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "\bOMS\b" DOCS`: 4 files
- `grep -rli "order management system" DOCS`: 6 files
- Top hits:
  - `VirtoCommerce/features.md:37-39` — marketing: "Order Management (OMS) ... Built-in OMS to manage complex B2B order flows"
  - `PlatformUserGuide/.../order-management/overview.md:34` — "the order management process in Virto Commerce OMS is not coded and not pre-determined. This system is designed as an Order Details Editor with no validation logics available. The system is implied to be an additional storage for customer orders details."
  - `B2BExperts/.../Marketplace-technology-...md:162,303,315` — OMS used in B2B thought leadership, not VC capability

**Verdict**: 🟡 Mentioned but thin
**Note**: Marketing calls it "Built-in OMS" but the authoritative user-guide page contradicts that framing — VC's Order module is a CRUD editor, not a workflow-driven OMS. No state-machine, no OMS capability matrix, no comparison-ready page. A buyer comparing vs Shopify / commercetools OMS will hit this contradiction first.

---

## Claim 2: "WMS" (Warehouse Management System) term usage is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce have a WMS (Warehouse Management System)? How are warehouses managed?"):
Only inventory configuration guidance ("multiple fulfillment centers ... navigate to a catalog, select a product, open the list of fulfillment centers") surfaced. No WMS concept page.

**WebSearch** (covered via omnichannel/WMS queries in prior digest): WMS is a distinct category (bins, putaway, pick-pack, cycle-count). Major competitors integrate with Manhattan / Logiwa / SAP EWM or declare themselves explicitly "not a WMS".

**Grep** (scope: DOCS):
- `grep -rli "\bWMS\b\|warehouse management system" DOCS`: 1 file
- Sole hit: `B2BExperts/.../Power-forward-five-make-or-break-truths-about-next-gen-e-commerce.md:61` — McKinsey quote about WMS growth, not VC capability.
- Zero hits in PlatformUserGuide, PlatformDeveloperGuide, MarketplaceUserGuide.

**Verdict**: 🔴 Absent (from VC's own capability docs)
**Note**: VC docs do not declare "we are not a WMS, integrate with X" nor "we provide WMS-lite features Y". A warehouse operator reading the docs cannot tell whether bin locations, pick lists, cycle counts, or wave picking exist. Fulfillment-center = stock-quantity-per-location only.

---

## Claim 3: Multi-warehouse fulfillment is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce support multi-warehouse fulfillment? Assigning orders to warehouses, fulfillment centers?"):
Returned `Retrieve Product Availability by Fulfillment Center` GraphQL + getting-started inventory config. Strong on **stock visibility** per FC; silent on **order routing / allocation rules**.

**WebSearch**: not re-run — industry-common; commercetools / Shopify have explicit "inventory mode" / "stock locations" + allocation docs.

**Grep** (scope: DOCS):
- `grep -rli "fulfillment center" DOCS`: 41 files — strong surface coverage
- `grep -rli "multi-warehouse\|multi warehouse" DOCS`: 7 files — all marketing-site bullets (`commerce-engine.md`, `industry/pharmaceutical.md`, `portal/b2b.md`, `solutions/b2b-portal-for-manufacturers.md`, `marketplace/procurement-marketplace.md`)
- No hits for fulfillment "rules / routing / allocation / sourcing".

**Verdict**: 🟡 Mentioned but thin
**Note**: Stock-per-fulfillment-center data model is well-documented at the GraphQL level. Multi-warehouse **order-routing logic** (which FC ships which line, fallback, proximity-based sourcing, split logic) is absent. Marketing says "multi-warehouse inventory"; docs stop at per-FC quantities.

---

## Claim 4: BOPIS (Buy Online Pickup In Store) is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support BOPIS (Buy Online Pickup In Store)? Click and collect in-store pickup?"):
Returned `pickupLocations` GraphQL query, `settings.md#bopis-settings`, and `managing-shipping-methods.md` BOPIS section. BOPIS is treated as a **shipping method** configuration.

**WebSearch** (query: "BOPIS BORIS ship-from-store endless aisle omnichannel retail terminology"):
BOPIS is canonical omnichannel terminology (IBM, Shopify, commercetools, unicommerce, fabric.inc). Multi-page dedicated guides on competitor platforms.

**Grep** (scope: DOCS):
- `grep -rli "BOPIS\|buy online.*pick.*up\|click and collect\|click-and-collect" DOCS`: 8 files
- Top hits:
  - `PlatformUserGuide/.../shipping/settings.md:7,42,44,49,51` — "BOPIS settings" section with Google-Maps integration
  - `PlatformUserGuide/.../shipping/managing-shipping-methods.md:7,17,44,46,48` — Edit BOPIS shipping method procedure
  - `StorefrontDeveloperGuide/.../pickupLocations.md` — pickup-location query reference

**Verdict**: 🟡 Mentioned but thin
**Note**: BOPIS exists as a named concept with a settings page, Google-Maps integration, and `pickupLocations` GraphQL. But no end-to-end BOPIS journey doc — no reserve-in-store, notify-for-pickup, timeout / no-show, pickup confirmation, staff-facing UI. Competitors treat BOPIS as a headline omnichannel capability.

---

## Claim 5: BORIS (Buy Online Return In Store) is absent
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support BORIS (Buy Online Return In Store)? In-store returns?"):
Returned generic `createOrderFromCart` mutation — i.e. no relevant result. Context7 did not surface any BORIS-specific content.

**WebSearch** (query covered in BOPIS/BORIS omnichannel search): BORIS is an established term alongside BOPIS in omnichannel playbooks (IBM, OneStock, skillnet, fabric).

**Grep** (scope: DOCS):
- `grep -rli "BORIS\|buy online.*return\|return in store\|in-store return" DOCS`: 1 file
- Sole hit: `B2BExperts/docs/Omnichannel-the-path-to-value.md:46` — McKinsey excerpt about the retail pattern ("order online and return in store"), not VC capability.

**Verdict**: 🔴 Absent
**Note**: Zero first-party coverage. A retail prospect asking "can I accept returns at any store?" gets nothing from VC docs or site.

---

## Claim 6: Ship-from-store / endless aisle is absent
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support ship-from-store or endless aisle fulfillment?"):
Returned `Retrieve Product Availability by Fulfillment Center` (same catalog GraphQL as claim 3). Neither "ship-from-store" nor "endless aisle" surfaced.

**WebSearch**: Both are industry-standard omnichannel terms; prior digest confirmed prevalence.

**Grep** (scope: DOCS):
- `grep -rli "ship.from.store\|endless aisle" DOCS`: 1 file
- Sole hit: `B2BExperts/docs/Retail-reset-a-new-playbook.md:74` — McKinsey quote ("ship-from-store could account for 30 to 50 percent of physical store volume"). Not VC capability.

**Verdict**: 🔴 Absent
**Note**: A retailer looking to model "stores-as-mini-DCs" (ship-from-store, endless aisle to fulfill from another store's stock) finds no VC-side guidance. The fulfillment-center data model could support it, but the terminology and the pattern are undocumented.

---

## Claim 7: Backorder / preorder is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support backorders or preorders? How are out-of-stock products handled?"):
Returned auth / appsettings.json snippets — i.e. essentially no direct concept hit. Context7 did not find a dedicated backorder / preorder page.

**WebSearch**: not required — terms are ubiquitous e-commerce vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "backorder\|back-order\|back order\|preorder\|pre-order" DOCS`: 2 files
- `grep -rli "allowPreorder\|allowBackorder\|preorderAvailability\|backorderAvailability"`: 4 files (API reference only)
- Top hits:
  - `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/InventoryInfo.md:13-16` — four API fields: `allowPreorder`, `allowBackorder`, `preorderAvailabilityDate`, `backorderAvailabilityDate`. Bare reference only.
  - `MarketplaceUserGuide/.../products-management.md:18` — single table row showing "Pre-Order Price" as a product-attribute example.

**Verdict**: 🟠 Implemented but undocumented
**Note**: Data model clearly supports preorder + backorder (4 explicit InventoryInfo fields). But zero narrative on how to enable the capability in admin, how the storefront should render "available on 2026-06-01 via backorder", how reservation / charge-on-ship works. Classic code-has-it-docs-don't.

---

## Claim 8: Returns / RMA flow is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do returns / RMA (Return Merchandise Authorization) work in VirtoCommerce?"):
Returned auth / cloud-auth snippets — no direct concept hit for RMA.

**WebSearch**: not required — RMA is universal fulfillment vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "\bRMA\b\|return merchandise\|return authoriz" DOCS`: 2 files — both B2B thought-leadership, not VC-authored
- `grep -rli "return policy\|return flow\|return process\|return request" DOCS`: 15 files
- Dedicated doc: `PlatformUserGuide/.../order-management/managing-returns.md` — "Manage Returns": create a return, check items, enter reason, click Make return; "View and Process Returns". Short UI-click-through. No state machine / statuses / refund linkage / exchange flow / restocking logic.

**Verdict**: 🟡 Mentioned but thin
**Note**: Returns exist as an admin operation with one dedicated short page. Industry term "RMA" is **never** used in first-party docs. No modeled return lifecycle (requested → approved → received → inspected → refunded / restocked), no customer-facing self-serve return portal, no exchanges, no partial returns, no return-to-different-warehouse.

---

## Claim 9: Split shipments / partial fulfillment is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support split shipments or partial fulfillment of orders?"):
Returned `Add or Update Cart Shipment` GraphQL — cart supports multi-shipment via `InputShipmentType` with per-shipment `fulfillmentCenterId`. Demonstrates data model; no conceptual walkthrough.

**WebSearch**: not re-run — split shipment is standard B2B fulfillment vocabulary.

**Grep** (scope: DOCS):
- `grep -rli "split shipment\|partial fulfillment\|partial shipment" DOCS`: 3 files
- Top hits:
  - `VirtoCommerce/features.md:39` — marketing bullet ("from split shipments to approvals")
  - `B2BExperts/.../Elevating-customer-experience-in-b2b-ecommerce.md:183` — external article explaining split shipment conceptually
  - One xAPI cart-shipment reference

**Verdict**: 🟡 Mentioned but thin
**Note**: Cart data model supports multiple shipments with different FCs / addresses — a real capability. No first-party guide titled "Split shipments" / "Partial fulfillment" explaining when the cart auto-splits, how admin releases shipment #1 before #2, how partial invoicing / payment interacts, or how the customer experiences staggered deliveries. Marketing claims it; docs don't teach it.

---

## Claim 10: Stock reservations / ATP (Available-to-Promise) is thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support stock reservations, inventory reservations, or ATP (Available-to-Promise)?"):
Returned `Retrieve Product Inventory by Store` (`inStockQuantity` per FC). No ATP concept, no reservation timeout, no soft-vs-hard reservation explained.

**WebSearch** (query: "'Available-to-Promise' ATP stock reservation ecommerce Shopify commercetools documentation"):
ATP is first-class on Shopify, shipbob, speedcommerce, logiwa, hulkapps. commercetools exposes reservation primitives in the Carts API.

**Grep** (scope: DOCS):
- `grep -rli "stock reservation\|inventory reservation\|available.to.promise\|\bATP\b" DOCS`: 2 files
- Top hits:
  - `PlatformUserGuide/.../cart/overview.md:22` — single line: "Stock reservation: Products added to the cart are reserved in stock for checkout." No timeout / hard-vs-soft / contention / release policy.
  - `B2BExperts/.../Pharma-b2b-ecommerce-what-it-takes-to-win-online.md:7,12,14,16` — external Corevist article discussing ATP in an SAP context. Not VC capability.

**Verdict**: 🟡 Mentioned but thin (stock reservation) / 🔴 Absent (ATP terminology)
**Note**: Reservation is mentioned in **one sentence** in the cart overview with no mechanics. ATP (allocation-proportional-to-customer, promise dates, future-receipts) appears only in a third-party SAP article — VC docs never use the term. Surprising for a B2B platform: ATP is the textbook B2B inventory-promising concept.

---

## Group M overall shape

- **Strong**: the **data model** and **xAPI GraphQL surface** around fulfillment centers, inventory quantities, preorder / backorder flags, multi-shipment carts, and pickup locations. Anyone reading xAPI references can implement against it.
- **Weak**: the **omnichannel retail vocabulary layer** — WMS, BORIS, ship-from-store, endless aisle, ATP — is almost entirely absent from first-party docs (mentions are McKinsey / B2BExperts external excerpts). BOPIS is the only named omnichannel pattern with real doc coverage, and even it is shipping-config level only.
- **Contradictions & undocumented code**: `features.md` markets "Built-in OMS" while `order-management/overview.md` explicitly calls the module "not coded ... Order Details Editor with no validation logics ... additional storage for customer orders details" — a buyer hitting this will lose trust. Preorder / backorder is the clearest "implemented but undocumented" item: 4 dedicated API fields, zero narrative.
