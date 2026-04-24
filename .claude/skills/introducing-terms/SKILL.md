---
name: introducing-terms
description: Use when adding or defining a Virto Commerce vocabulary term, mapping a Virto Commerce concept to its industry name, or processing a batch of such terms. Triggers include "add term", "define term", "introduce term", "map to Shopify/Magento/commercetools name".
---

# Introducing terms

Adds terms to the Virto Commerce glossaries and, where warranted, to the abbreviation tooltips. Works for one term or a batch.

Rules live in [CLAUDE.md](../../../CLAUDE.md), sections "Glossaries", "Abbreviation tooltips", and "Verification before claims". This skill is the workflow that applies them.

## Iteration

For a batch, run the full workflow per term. Do not batch verification or drafting across terms: claims drift from the terms they support.

## Inputs per term

- Term as Virto Commerce code names it.
- Audience: business, developer, or both.
- Suspected industry analog, to be verified.

## Workflow

### 1. Verify Virto Commerce vocabulary

- Symbol existence: invoke GitHub MCP to search code and fetch files in the `VirtoCommerce` organization. Mentioning GitHub MCP in commentary without running it does not count. An org or repo filter plus a quoted string is required; unfiltered queries return nothing. Fetch the matching file to confirm the symbol is where you expect it.
- Prose wording: grep the local docs corpus for term frequency. Pick the form that wins and record the count.

### 2. Verify cross-platform terminology

Before writing any comparison-table cell, check that platform's own current docs (Shopify Help Center, Adobe Commerce, commercetools, BigCommerce). Use the merchant-facing label, not an internal schema or developer-only name. Vendor blogs are secondary. If a platform has no equivalent, the cell is `n/a`. If most cells cannot be verified from vendor docs, drop the whole comparison table rather than ship recall-based cells.

Match scope, not just label. If the Virto concept attaches to many object types (Product, Order, Cart, Company, etc.), the vendor analog must also. A multi-object Virto concept does not map to a single-object vendor feature, even when the label sounds closer. Example: Virto Dynamic property (multi-object) maps to BigCommerce Metafield (multi-object), not Custom field (product-only).

### 3. Draft the glossary entry or entries

No draft text until sections 1 and 2 have produced verified names from tool output. Every class, interface, namespace, and vendor cell in the draft must trace to a GitHub MCP result or a fetched vendor page. "To be confirmed" or "I would verify later" footnotes do not ship.

Apply the rules in CLAUDE.md "Glossaries" (entry shape, comparison table, linking from other pages).

### 4. Add a tooltip if warranted

Apply the rules in CLAUDE.md "Abbreviation tooltips" (when to add, files, authoring rules).

### 5. Self-check per term

- Every class, interface, namespace, and vendor cell traces to a tool call made in this session.
- Each vendor cell matches the Virto concept's scope (multi-object vs single-object, etc.), not just the label.
- User-facing entry has no developer jargon.
- Developer-facing entry does not enumerate full APIs.
- Comparison-table cells have no trailing periods.
- Cross-link present if both glossaries have the entry.
- Scope not expanded beyond the requested term.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Using a platform's internal, schema-level, or developer-only name instead of the merchant-facing label. | Use the label shown in that platform's admin-facing docs. |
| Developer jargon ("runtime", "schema", "interface") in a user-facing entry. | Rewrite for a non-developer reader. |
| Enumerating every related interface in a developer-facing entry. | Move detail to the deep-dive page. |
| Backticking product names like "Shopify" or "commercetools". | Plain text; they are proper nouns. |
