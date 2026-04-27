# VirtoCommerce Documentation Gap Audit — Master Plan

Fresh run. Do **not** read `docs/vc-gap-audit-negative.md` or `docs/vc-gap-audit-positive.md` — those are prior results and the user wants a clean rerun.

## Audit perspectives

1. **Unfamiliar e-commerce dev/manager** — strong general e-commerce knowledge, zero VirtoCommerce knowledge. What would they look up? Where would docs fail them?
2. **Comparison vs other platforms** — Shopify, commercetools, Adobe Commerce / Magento, SAP Commerce / Hybris, BigCommerce, Salesforce Commerce Cloud, Spryker, Shopware, VTEX, Elastic Path, CommerceTools, Oro, Sylius, Sana, Saleor. How does VC's vocabulary / topic coverage compare?

## Two deliverables per group

A. **Topics we support but poorly describe** — e.g. "AWS deployment is possible but barely mentioned."
B. **Terms widely used in e-commerce / dev that VC docs/site use rarely or not at all** — e.g. "polymorphism is what `AbstractTypeFactory` implements, but the term is never used in docs."

## Per-claim methodology (MUST follow for EVERY claim)

For each claim, the responsible subagent runs **3 actions**:

1. **Context7**: `mcp__context7__query-docs` with `libraryId: /virtocommerce/vc-docs`. Phrase the query as an unfamiliar dev/manager would ("How do I deploy VirtoCommerce to AWS EKS?", "What's the PIM module in VirtoCommerce?", "Does VirtoCommerce support BOPIS?"). One Context7 call per claim (hard cap: 3 per distinct question per Context7 tool rules — budget accordingly).
2. **WebSearch**: one query confirming either (a) the term's industry prevalence or (b) how competitors document it. Do this if Context7 returned nothing or contradictory.
3. **grep**: run on the offline doc corpus (see scope below) to count occurrences and confirm or reject the claim. Prefer `grep -rli` for file-count and `grep -rhc` or targeted `grep -rn ... | wc -l` for occurrence count. Cite file paths + line numbers for key matches.

Record each claim's 3 findings in the group's findings file before moving on.

## Grep scope

```bash
# User-facing docs + site (for "documented?" claims):
DOCS=(
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/VirtoCommerce"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/PlatformUserGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/PlatformDeveloperGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/StorefrontUserGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/StorefrontDeveloperGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/MarketplaceUserGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/DeploymentGuide"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/B2BExperts"
)

# Source code (only for "is concept actually implemented in VC?" cross-checks):
CODE=(
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/PlatformBackendSourceCode"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/PlatformFrontendSourceCode"
  "/mnt/Programming/AI chat/vc-ai-assistant/documentation/FrontendSourceCode"
)
```

Suggested invocation:
```bash
grep -rli "BOPIS" "${DOCS[@]}" | wc -l
grep -rhIi "abstracttypefactory" "${CODE[@]}" | wc -l
```

## Classification for each claim

- ✅ **Well documented** — multiple hits across guides + site + explanatory prose (claim rejected).
- 🟡 **Mentioned but thin** — hits exist but are shallow, scattered, or only in release notes / changelogs.
- 🟠 **Implemented but undocumented** — code/internal references present, docs/site silent or near-silent.
- 🔴 **Absent** — no hits, not mentioned, industry-common term missing from VC vocabulary.
- ⚪ **Not applicable** — VC genuinely doesn't do this, so absence is correct.

## Groups (each → its own findings file)

| #   | Group                                        | File                                  |
| --- | -------------------------------------------- | ------------------------------------- |
| A   | Deployment & Infrastructure                  | `A-deployment-infra.md`               |
| B   | Data, Storage, Persistence                   | `B-data-storage.md`                   |
| C   | Messaging & Integration                      | `C-messaging-integration.md`          |
| D   | Observability & Operations                   | `D-observability.md`                  |
| E   | Security, Auth, Compliance                   | `E-security-auth.md`                  |
| F   | Architecture Patterns                        | `F-architecture-patterns.md`          |
| G   | API Surface (REST/GraphQL/OpenAPI)           | `G-api-surface.md`                    |
| H   | Frontend, UX, Accessibility                  | `H-frontend-ux.md`                    |
| I   | Catalog, PIM, DAM                            | `I-catalog-pim.md`                    |
| J   | Search & Discovery                           | `J-search-discovery.md`               |
| K   | Cart & Checkout                              | `K-cart-checkout.md`                  |
| L   | Pricing & Promotions                         | `L-pricing-promotions.md`             |
| M   | Order / Inventory / Fulfillment              | `M-order-inventory-fulfillment.md`    |
| N   | Tax & Shipping                               | `N-tax-shipping.md`                   |
| O   | Payments                                     | `O-payments.md`                       |
| P   | B2B Specifics                                | `P-b2b-specifics.md`                  |
| Q   | Marketplace / Multi-vendor                   | `Q-marketplace.md`                    |
| R   | Marketing, SEO, Personalization              | `R-marketing-seo.md`                  |
| S   | CMS / Content / i18n                         | `S-cms-content-i18n.md`               |
| T   | Subscriptions & Recurring                    | `T-subscriptions.md`                  |
| U   | Modularity & Extensibility (incl. ATF)       | `U-modularity-extensibility.md`       |
| V   | Testing & QA                                 | `V-testing-qa.md`                     |
| W   | Domain-Driven Design & CQRS vocabulary       | `W-ddd-cqrs-vocabulary.md`            |
| X   | Modern architecture buzzwords (MACH, etc.)   | `X-modern-buzzwords.md`               |

## Output format (each findings file)

```markdown
# Group <X> — <title>

## Claim 1: <claim>
**Context7** (`/virtocommerce/vc-docs`, query: "<q>"):
<summary of what came back, or "no relevant results">

**WebSearch** (query: "<q>"):
<1-2 line summary>

**Grep** (scope: DOCS or CODE):
- `grep -rli "<term>" DOCS`: N files
- Top hits: `<path>:<line>` — `<snippet>`

**Verdict**: ✅ / 🟡 / 🟠 / 🔴 / ⚪
**Note**: <1-2 lines>

---
## Claim 2: ...
```

## Return value

Each subagent returns ≤400 words: bullet list of verdicts per claim, plus 2-3 sentences on the group's overall shape (what's strong, what's weak). The raw Context7/WebSearch dumps stay on disk.
