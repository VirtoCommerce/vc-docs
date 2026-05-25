---
name: introducing-terms
description: Use when adding or defining a Virto Commerce vocabulary term, mapping a Virto Commerce concept to its industry name, or processing a batch of such terms. Triggers include "add term", "define term", "introduce term", "map to Shopify/Magento/commercetools name".
---

# Introducing terms

Workflow for adding terms to the Virto Commerce glossaries and, where warranted, to the abbreviation tooltips. One term or a batch.

Authoritative rules live in [CLAUDE.md](../../../CLAUDE.md) §Glossaries, §Abbreviation tooltips, §Verification before claims. This skill is the applying procedure; do not restate rules here.

## Iteration

Per-term full-pass. No batching of verification or drafting across terms: evidence decouples from claims.

## Inputs per term

- Term as the Virto code names it.
- Audience: business, developer, or both.
- Suspected industry analog (unverified).

## Workflow

### 1. Verify Virto vocabulary

Per CLAUDE.md §Verification before claims.

- Symbol existence: GitHub MCP search plus file fetch in the `VirtoCommerce` org. Org/repo filter plus quoted string is required; unfiltered queries return empty. Fetch the hit to confirm location.
- Prose form: grep the docs corpus for frequency. Highest count wins; record the count.

### 2. Verify cross-platform terminology

Per CLAUDE.md §Cross-platform comparison table and §Verification before claims.

- One primary-source fetch per cell (vendor's own docs).
- WebFetch returning 403 → fall back to WebSearch with `allowed_domains` on the vendor's primary docs host.
- Cell unverifiable → `n/a`. Most cells unverifiable → drop the table.

### 3. Decide ownership and draft the entry

Decide which glossary owns the term per CLAUDE.md §Glossaries → Ownership routing. Create the owning glossary file if absent.

Gate: no draft text until steps 1–2 have produced verified names from tool output. Before drafting, sample 2–3 adjacent entries at the insertion point; match sentence length, voice, density. Apply CLAUDE.md §Entry shape and §Cross-platform comparison table to the draft.

### 4. Add an abbreviation tooltip if applicable

Per CLAUDE.md §Abbreviation tooltips: eligibility, scope (base vs overlay), casing/plural variants.

### 5. Cross-link from every guide

Survey procedure for CLAUDE.md §Linking from other pages.

1. Per guide, recursive grep the term; group hits by first path segment under `docs/` to enumerate top-level sections (or standalone pages).
2. For each section, link first occurrence on its entry page to the owning glossary. Form per CLAUDE.md.
3. No relink in deeper pages of the same section; no self-link on the canonical glossary page.
4. Skip auto-rendered API references (e.g., `GraphQL-Storefront-API-Reference-xAPI/`) unless an authored overview exists; link from the authored overview only.

### 6. Per-term self-check

Evidence trail for CLAUDE.md rules:

- Fundamentals identified from code before drafting (§Entry shape).
- Every class/interface/namespace/vendor cell traces to a tool call this session (§Verification before claims).
- Entry shape, comparison table, bidirectional cross-link applied (§Glossaries).
- Tooltip eligibility decided (§Abbreviation tooltips).
- Owning glossary identified, link form correct (§Linking from other pages).
- All seven content guides surveyed.
- Scope locked; no drive-by edits.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Internal, schema-level, or developer-only vendor name instead of merchant-facing label. | Use the label from that vendor's admin-facing docs. |
| Developer jargon (runtime, schema, interface) in a user-facing entry. | Rewrite for a non-developer reader. |
| Enumerating every related interface in a developer-facing entry. | Move detail to the deep-dive page. |
| Backticking proper nouns like "Shopify" or "commercetools". | Plain text. |
| Drafting before identifying the concept's fundamental properties (user-defined? runtime? EAV?). | List shared properties with the sibling entry first; opener mirrors shared nature. |
| PascalCase identifier or implementation-pattern label in a dev-guide table cell. | Use general prose form, or `n/a (uses X)` if the platform collapses the distinction architecturally. |
| Adding a multi-word vocabulary term to abbreviations.yml because it has a short definition. | Glossary entry plus cross-link instead. |
| Linking the glossary on every page that mentions the term. | One link per top-level section, on its entry page. |
| Restating rules in this skill instead of pointing to CLAUDE.md. | Keep this file workflow-only; cite the rule section by name. |
