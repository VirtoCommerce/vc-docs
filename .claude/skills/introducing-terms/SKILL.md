---
name: introducing-terms
description: Use when adding or defining a Virto Commerce vocabulary term, mapping a Virto Commerce concept to its industry name, or processing a batch of such terms. Triggers include "add term", "define term", "introduce term", "map to Shopify/Magento/commercetools name".
---

# Introducing terms

Workflow for adding terms to the Virto Commerce glossaries and, where warranted, to the abbreviation tooltips. One term or a batch.

Authoritative rules live in [CLAUDE.md](../../../CLAUDE.md): Glossaries, Abbreviation tooltips, Verification before claims. This skill is the applying procedure.

## Iteration

Per-term full-pass. No batching of verification or drafting across terms: evidence decouples from claims.

## Inputs per term

- Term as the Virto code names it.
- Audience: business, developer, or both.
- Suspected industry analog (unverified).

## Workflow

### 1. Verify Virto vocabulary

- Symbol existence: GitHub MCP search plus file fetch in the `VirtoCommerce` org. Org/repo filter plus quoted string is required; unfiltered queries return empty. Fetch the hit to confirm location. Name-dropping the tool without invocation is not verification.
- Prose form: grep the docs corpus for frequency. Highest count wins; record the count.

### 2. Verify cross-platform terminology

Primary source per cell (Shopify Help Center, Adobe Commerce, commercetools, BigCommerce). No equivalent → `n/a`. Most cells unverifiable against primary sources → drop the table rather than ship recall-based cells.

WebFetch returning 403 → fall back to WebSearch with `allowed_domains` on the vendor's primary docs host.

Apply CLAUDE.md §Cross-platform comparison table for: scope match, audience split (merchant-facing in user-guide, same cells in dev-guide unless general prose differs), `n/a (uses X)` for architectural collapse.

### 3. Draft the glossary entry or entries

Gate: no draft text until sections 1–2 have produced verified names from tool output. Every class, interface, namespace, and vendor cell traces to a GitHub MCP result or a fetched vendor page. TBC footnotes do not ship.

Before drafting a user-guide entry, sample 2–3 adjacent entries at the insertion point; match sentence length, voice, density.

Apply CLAUDE.md §Glossaries (entry shape, comparison table, linking).

### 4. Add a tooltip if warranted

Apply CLAUDE.md §Abbreviation tooltips.

### 5. Per-term self-check

- Identified fundamental properties (user-defined? runtime-added? EAV? admin-configurable?) from code BEFORE drafting. Sampled adjacent entries and any parallel-concept sibling for opener cadence.
- Every class, interface, namespace, and vendor cell traces to a tool call in this session.
- CLAUDE.md §Entry shape applied: endonym, parallel-concept parity, code identifier discipline, no fabricated framing, scope qualified, register matched per audience.
- CLAUDE.md §Cross-platform comparison table applied: audience split, scope match, `n/a (uses X)` for architectural collapse, no trailing periods.
- Bidirectional cross-link present when both glossaries contain the entry.
- Scope locked to the requested term; no drive-by edits.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Internal, schema-level, or developer-only vendor name instead of merchant-facing label. | Use the label from that vendor's admin-facing docs. |
| Developer jargon (runtime, schema, interface) in a user-facing entry. | Rewrite for a non-developer reader. |
| Enumerating every related interface in a developer-facing entry. | Move detail to the deep-dive page. |
| Backticking proper nouns like "Shopify" or "commercetools". | Plain text. |
| Drafting before identifying the concept's fundamental properties (user-defined? runtime? EAV?). | List shared properties with the sibling entry first; opener mirrors shared nature. Differences belong in scope and modifiers, not framing words ("structured", "schema-defined") or "Unlike **X**" prose. |
| PascalCase identifier or implementation-pattern label in a dev-guide table cell. | Use general prose form, or `n/a (uses X)` if the platform collapses the distinction architecturally. |
