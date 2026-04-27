# Vocabulary gap closure plan (audit Step 1)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the docs-vs-code vocabulary gap identified as priority 1 in [FINAL-negative.md](FINAL-negative.md) for audit groups F (architecture patterns), U (modularity/extensibility), W (DDD/CQRS), V (testing/QA). Outcome: a prospect or evaluator reading the dev guide can find every canonical .NET / DDD / testing pattern Virto Commerce ships, by its industry name.

**Architecture:** Content-only work on top of the existing glossary plus abbreviations infrastructure delivered by `feat/glossaries`. Every batch is independent; you can stop after any task and ship a coherent partial result. All term entries follow [.claude/skills/introducing-terms/SKILL.md](../.claude/skills/introducing-terms/SKILL.md) and the glossary rules in [CLAUDE.md](../CLAUDE.md).

**Tech stack:** Markdown, MkDocs (Material), python-markdown abbr extension, [overrides/hooks/abbreviations_loader.py](../overrides/hooks/abbreviations_loader.py).

**Out of scope for this plan:** Audit priorities 2 to 10 (B2B, payments, subscriptions, OMS, accessibility, deployment matrix, observability, API cross-cutting, CMS). Marketing-vs-substance reconciliations from §2 of FINAL-negative.md. Net-new how-to pages. Add those as separate plans.

---

## Inputs and references

- Audit verdicts: [F-architecture-patterns.md](F-architecture-patterns.md), [U-modularity-extensibility.md](U-modularity-extensibility.md), [V-testing-qa.md](V-testing-qa.md), [W-ddd-cqrs-vocabulary.md](W-ddd-cqrs-vocabulary.md).
- Existing dev glossary: [platform/developer-guide/docs/glossary.md](../platform/developer-guide/docs/glossary.md) (2 entries today).
- Existing user glossary: [platform/user-guide/docs/glossary.md](../platform/user-guide/docs/glossary.md) (~40 entries today).
- Base abbreviations: [overrides/abbreviations.yml](../overrides/abbreviations.yml).
- Term-introduction skill: `.claude/skills/introducing-terms/SKILL.md` (invoke as `/introducing-terms` in Claude Code).
- Code corpus for verification: `VirtoCommerce` GitHub org (use `mcp__github__search_code` plus file fetch). Primary-source vendor docs for Rosetta cells: vendor's own current help center.

---

## Task 1: Add architecture-pattern terms to dev glossary (group F)

**Files:**
- Modify: [platform/developer-guide/docs/glossary.md](../platform/developer-guide/docs/glossary.md)

**Terms to add** (alphabetical insertion, one H2 each, 2 to 4 sentences, with Rosetta table when industry analogs exist):

- [ ] Circuit breaker. Name Polly as the implementation; cite `VirtoCommerce.Platform.Caching.csproj` pin. No Rosetta table.
- [ ] CQRS. Disambiguate from MediatR; note that both REST and xAPI/GraphQL paths use it.
- [ ] Command handler. Pattern shape; reference `IRequestHandler<TRequest>`. List counts only if necessary.
- [ ] Query handler. Counterpart to command handler; same pattern shape.
- [ ] Mediator (MediatR). Library + role; flag the July 2025 commercial-license change once, neutrally.
- [ ] Modular monolith. Endonym for VC's runtime shape; contrast with microservices marketing-only claim.
- [ ] Multi-tenancy. Define VC's two senses (Azure AD SSO tenancy and per-org Weaviate isolation) explicitly.
- [ ] Repository. Pattern shape; mention Data Mapper as VC's preferred local label.
- [ ] Unit of Work. Pattern shape; reference EF `SaveChangesAsync` boundary.
- [ ] Strangler fig pattern. Mark as the pattern name VC's "replace legacy" positioning maps to.

**How to execute:**

1. Open Claude Code in this worktree.
2. Run `/introducing-terms Circuit breaker` (and so on for each term). The skill drives the GitHub MCP verification, picks the canonical opener, and produces the glossary entry plus Rosetta cells.
3. Review each draft against the rules in CLAUDE.md (endonym opener, no italics, sentence-final periods, fixed Tier-1 column order).
4. Commit per term or per ~3 terms.

---

## Task 2: Add DDD-core terms to dev glossary (group W)

**Files:**
- Modify: [platform/developer-guide/docs/glossary.md](../platform/developer-guide/docs/glossary.md)

**Terms to add:**

- [ ] Aggregate root. Cite `IAggregateRoot` (75 code hits, 0 docs) by name.
- [ ] Anti-corruption layer. Map to VC's `ToModel` / `FromModel` convention.
- [ ] Bounded context. Pair with module boundaries.
- [ ] Domain event. Distinguish from integration event in the same entry or in adjacent entries.
- [ ] Entity. Disambiguate the DDD base type vs the EF `*Entity` persistence type. Highest-impact entry — ambiguity is the single biggest source of confusion in W.
- [ ] Integration event. Counterpart to domain event; flag the asymmetric coverage (one paragraph in code, full page in docs).
- [ ] Specification pattern. Cite `ISpecification<T>` (18 code, 0 docs).
- [ ] Ubiquitous language. Brief, links the rest of the W cluster.
- [ ] Value object. Cite `ValueObject` base class.

**Execution:** same as Task 1, one `/introducing-terms` invocation per term. Commit at end of batch.

---

## Task 3: Add modularity/extensibility terms to dev glossary (group U)

**Files:**
- Modify: [platform/developer-guide/docs/glossary.md](../platform/developer-guide/docs/glossary.md)

**Terms to add:**

- [ ] AbstractTypeFactory. The single highest-impact U entry (693 code, 11 docs). Name it as "typed-factory pattern" and as VC's polymorphism mechanism. No Rosetta — VC-specific.
- [ ] Polymorphism. Pair entry; note "type inheritance" is VC's proprietary local label.
- [ ] Dependency injection. Generic .NET concept; brief, with `IServiceCollection` reference.
- [ ] Domain event subscriber. Synonyms: handler, listener. Cite `IEventHandler<>` shape.
- [ ] Liquid extensibility. Scope: notifications + event-bus payload preprocessing only (not storefront templating).
- [ ] Module package. Endonym for VC's distribution unit. Mention `vc-package.json` and the four supported sources (GitHub Releases, Azure Artifacts, Blob, Local). Mark explicitly that VC modules are NOT distributed via nuget.org.

**Execution:** same as Task 1.

---

## Task 4: Add testing terms to dev glossary (group V)

**Files:**
- Modify: [platform/developer-guide/docs/glossary.md](../platform/developer-guide/docs/glossary.md)

**Terms to add:**

- [ ] xUnit. Name the framework; brief.
- [ ] Moq. Name the mocking library; brief.
- [ ] Test fixture. Cover `IClassFixture<>`, `ICollectionFixture<>`. Mention `AutoFixture` and `Bogus` if used in code (verify before drafting).
- [ ] Integration test. Define VC's category convention (the `Category!=IntegrationTest` filter in vc-build); reference `WebApplicationFactory` and Testcontainers if codebase verifies them.
- [ ] Visual regression test. Cite `pixelmatch` via `pytest-image-snapshot`; baseline-management mention only if a worked example exists.

**Execution:** same as Task 1.

---

## Task 5: Add user-glossary entries (small)

**Files:**
- Modify: [platform/user-guide/docs/glossary.md](../platform/user-guide/docs/glossary.md)

Step 1 of the audit is dev-focused. Most §1 terms have no business-side analog. Add only the entries an admin or merchandiser might still encounter:

- [ ] Module. Verify whether already covered. If not, add as a 2-sentence business-register entry pointing to the dev-side **Module package** for runtime shape.
- [ ] Modular monolith. Optional; add only if marketing pages or PBC docs surface the term to non-developers. Otherwise skip.

**Execution:** invoke `/introducing-terms` per surviving term, with audience set to "user".

---

## Task 6: Add abbreviation tooltips for cross-page acronyms

**Files:**
- Modify: [overrides/abbreviations.yml](../overrides/abbreviations.yml)
- Modify (optional, only on per-audience divergence): per-guide overlays under `<guide>/abbreviations.yml`.

**Acronyms to add** (~50-char target, ~100-char hard cap, YAML anchors for casing/plural variants):

- [ ] DDD
- [ ] CQRS
- [ ] DI (dependency injection). Avoid clash with other DI senses; spell out fully.
- [ ] UoW (Unit of Work)
- [ ] ACL (anti-corruption layer). Disambiguate from access control list — write the full DDD form.
- [ ] EF / EF Core
- [ ] DTO

Skip acronyms that appear on a single page only (per CLAUDE.md rule).

**Execution:**

1. For each acronym, draft the gloss to fit the length budget.
2. Use `&name` / `*name` YAML anchors to DRY across casing variants.
3. Build site locally (`mkdocs serve` from each guide) and hover-test 2 to 3 occurrences per acronym before committing.

---

## Task 7: Cross-reference from existing pages to new glossary entries

The glossary entries are inert until the pages people actually read link to them. Wire the first mention of each term on each page to the glossary anchor. Per CLAUDE.md: relative paths only, first mention per page only, no self-link on the canonical entry.

**Pages to wire (target → terms to link on first mention):**

- [ ] Fundamentals/Modularity/* pages → AbstractTypeFactory, polymorphism, dependency injection, module package.
- [ ] xAPI overview and GraphQL handler pages → CQRS, MediatR, command handler, query handler.
- [ ] Event-Driven-Development folder (4 pages) → domain event, integration event, subscriber.
- [ ] Concurrency-handling page → Unit of Work, repository, optimistic concurrency (note: optimistic concurrency itself is a separate audit gap; skip if not yet in glossary).
- [ ] Resilience-related pages (search for Polly mentions) → circuit breaker.
- [ ] Testing pages (`ModulesDevelop` testing sections, vc-build docs) → xUnit, Moq, integration test, test fixture.
- [ ] Aggregate / domain modelling pages (search for `IAggregateRoot`, `ValueObject` references) → aggregate root, value object, specification pattern, entity disambiguation.
- [ ] Anti-corruption / model-mapping pages (search for `ToModel`, `FromModel`) → anti-corruption layer.
- [ ] Multi-tenant pages (Azure AD SSO; Weaviate per-org) → multi-tenancy.
- [ ] Deployment overview → modular monolith.

**Execution:**

1. For each term, run `grep -rn "<term>" platform/developer-guide/docs/` to find candidate pages.
2. For each candidate, link only the first occurrence to the glossary anchor: `[term](../glossary.md#kebab-anchor)`.
3. Skip pages where the term appears in code blocks only — backticks are reserved for code (CLAUDE.md).
4. Commit per term or per ~3 terms; small commits help diff review.

---

## Task 8: Verify build, links, and tooltips

**Files:** none modified; verification only.

- [ ] Run `mkdocs build --strict` from each affected guide root (`platform/developer-guide`, `platform/user-guide`). Expected: zero broken links, zero unrecognised anchors.
- [ ] Run `mkdocs serve` per guide; click 5 representative cross-references end-to-end and verify they land on the right H2.
- [ ] Hover-test 5 representative abbreviations across 3 different pages each; verify the tooltip text fits the popover and stays readable.
- [ ] Spot-check the dev glossary's alphabetical ordering and Rosetta-table column order.

---

## Task 9: Bookkeeping and handoff

- [ ] Update [FINAL-negative.md](FINAL-negative.md) prioritization section: mark Step 1 as complete or partially complete; list any §1 / B-8 terms that were deferred (for example, optimistic concurrency from group F is a real gap but lives in B group, not F).
- [ ] Open follow-up issues for:
  - Marketing-vs-substance reconciliation (audit §2; needs product-owner sign-off).
  - User-guide vocabulary backfill for B-1 to B-7 commerce-ops, B2B, payments, subscriptions, marketing/SEO terms (audit priority 2 to 4).
  - WCAG / observability / deployment-matrix expansions (priorities 6 to 8).
- [ ] Optional: post a short summary in your team's working channel — "Closed audit Step 1, X dev-glossary entries, Y abbreviations, Z pages cross-referenced."

---

## Self-review notes

- Spec coverage: every 🟠 finding from groups F, U, W, V in [FINAL-negative.md](FINAL-negative.md) maps to a term in Tasks 1 to 4. The `feat/glossaries` work already covers `DynamicProperty`, so it does not appear here.
- Out-of-scope but adjacent: optimistic concurrency (group B), domain event vs integration event asymmetric coverage (covered partially in Task 2, but the actual *content fix* of the asymmetry — adding integration-event runtime substance — is a code-side concern outside this plan).
- Type and naming consistency: glossary anchors are auto-derived by MkDocs from H2 text — keep H2 wording stable across tasks (e.g. "Unit of Work", not "Unit of work" then "UnitOfWork").
- All term lists are concrete and complete; no "TBD" or "similar to" placeholders remain.
