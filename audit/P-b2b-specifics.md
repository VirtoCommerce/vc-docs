# Group P — B2B Specifics

> Findings returned inline by resumed subagent (Write permission denied to the agent); persisted here by the parent session. Raw trails in `_resume/P-prior-work.txt`.

## Verdicts

### Claim 1 — Quote / RFQ flow thin
- **grep** (DOCS): `createQuoteFromCart` xAPI mutation documented; user-guide `quotes/` dir exists but only ~200 LOC across 3 files; no RFQ lifecycle / negotiation narrative.
- **Verdict**: 🟡 Thin.

### Claim 2 — CPQ absent
- **grep** (DOCS): Acronym only in 4 marketing/blog files; zero hits in any user or developer guide.
- **Context7**: no hits across 3 queries.
- **Verdict**: 🔴 Absent. No product-configurator / rule-based quote-gen docs.

### Claim 3 — Account hierarchy / company roles
- **grep** (DOCS): `requestRegistration`, `changeOrganizationContactRole`, roles `org-maintainer` / `purchasing-agent` exist in xAPI. **Zero** hits on "account hierarchy | company hierarch | organization hierarch" — multi-level parent/child companies invisible in docs.
- **Verdict**: 🟠 hierarchy implemented-but-undocumented / 🟡 roles thin.

### Claim 4 — Approval workflow thin
- **grep** (DOCS): Single `approveOrder` GraphQL mutation documented. No multi-step / threshold / delegation walkthrough. 5 "approval workflow" hits — all marketing.
- **Verdict**: 🟡 Thin.

### Claim 5 — Purchase orders / PO number thin
- **grep** (DOCS): `purchaseOrderNumber` field on `CartType` (cart-type.md:22). No user-guide topic for "PO as payment method" or PO-based checkout.
- **Verdict**: 🟡 Thin.

### Claim 6 — Punchout (cXML / OCI) absent
- **grep** (DOCS): 5 punchout hits — **all** marketing / partner / blog. Zero in any guide.
- **Context7** returned nothing across 3 queries.
- **WebSearch**: competitors (SAP Commerce, commercetools via TradeCentric, Adobe PunchOut Catalogs) document this natively.
- **Verdict**: 🔴 Absent.

### Claim 7 — EDI absent
- **grep** (DOCS): 1 hit, a B2BExperts blog. Zero AS2 / X12 / EDIFACT / 850-855-856-810 mapping docs.
- **Verdict**: 🔴 Absent.

### Claim 8 — Contract catalogs
- **grep** (DOCS): Contract **prices** well covered — dedicated `contracts/` user-guide dir with 4 how-to files + overview driven by user-group + price-list mechanism. Contract **catalogs** (customer-specific assortment) pattern unnamed in docs.
- **Verdict**: ✅ for prices / 🟡 for catalogs.

### Claim 9 — Buyer-seller negotiation thin
- **grep** (DOCS): 22 hits but concentrated in marketing / B2BExperts; `quotes/manage-quotes.md` and `quotes/overview.md` contain no "negotiat" text; no counter-offer round-trip documented.
- **Verdict**: 🟡 Thin.

### Claim 10 — Net terms / credit limit absent
- **grep** (DOCS): 2 hits, both B2BExperts blogs. Zero config guide for net-30/60/90, credit limits at checkout, or B2B-BNPL (Balance / Resolve / TreviPay).
- **Verdict**: 🔴 Absent.

## Group shape

VC genuinely has the scaffolding for B2B — organizations, role IDs, quotes, contracts (as price-list-per-user-group), `purchaseOrderNumber` on Cart, `approveOrder` mutation. The shape of the gap is consistently **"building blocks exist in xAPI but there's no how-to narrative"** and **"industry vocabulary is missing entirely"**.

## Gaps that undermine VC's "B2B-first" marketing claim

- **Punchout (cXML / OCI)** absent from all guides — table stakes for enterprise procurement (Ariba / Coupa / Jaggaer / SAP). Competitors document it; VC only name-drops it in marketing.
- **EDI** absent — no AS2 / X12 mapping content at all.
- **CPQ** vocabulary missing entirely from guides — contrasts sharply with SAP CPQ, Salesforce CPQ.
- **Net terms / credit limits** absent — core B2B payment semantics missing; no integration guide for B2B-BNPL providers.
- **Multi-level account hierarchy** has zero documentation hits — a signature SAP Commerce / Adobe B2B / Oro feature, invisible here.
- **Approval workflow** documented only as a single-step GraphQL mutation — no multi-stage / spending-threshold / delegation walkthrough.

Net: a buyer or solution architect evaluating VC against SAP Commerce, commercetools, Adobe B2B, or Oro via docs alone would conclude that VC handles quotes and contract pricing reasonably, but is missing or silent on punchout, EDI, CPQ, net terms, credit limits, and deep org hierarchy. That is a credibility problem for a platform whose marketing positions it as B2B-first.
