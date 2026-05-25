# Virto Commerce Docs Style Guide

This file defines the writing and formatting conventions for all documentation in this repository. Apply these rules to every new or edited Markdown file.

## Spelling

Use the following forms exactly:

- Virto Commerce (space separated; two words in text; alternatives allowed in code only).
- Platform / platform (capitalize Platform when referring to the Virto Commerce Platform; use lowercase platform for any other platform).
- Frontend (not storefront, not Frontend Application). Both "storefront" and "Frontend Application" are outdated and must not be used in Virto Commerce documentation. Use "Frontend" alone.
- ecommerce (within a sentence).
- eCommerce (in titles).
- xAPI (in text, not in code).
- xFrontend (in text, not in code).
- xCatalog (in text, not in code).
- xFile (in text, not in code).
- xCart (in text, not in code).
- ZIP.
- PDF.
- JPEG.
- CSV.
- dropdown (not drop-down list).

American spelling is preferable.

## Punctuation

- End every sentence with a period, including sentences inside table cells.
- Do not add a period after a single word or a code fragment that is not a sentence.
- Do not use the em dash surrounded by spaces (" — "). Replace it with other punctuation or start a new sentence.

## Formatting

### Bold

Use bold for:

- File names, for example, **appsettings.json**, **module.manifest**.
- Module names on their first mention in an overview article. Subsequent mentions in the same article use regular weight. For example, "The **Loyalty** module provides..." on first mention, then "With the Loyalty module, users can..." afterward.
- UI elements in step-by-step guides: buttons, widgets, menu items, tabs, field labels, toggle options, and dialog titles. For example, "Click **Save** in the toolbar." or "Click on the **Settings** widget."

### Italics

Do not use italics.

### Code ticks

Backticks are reserved for code only. Do not backtick file paths or file names; use bold instead.

### Images

Align images to center:

```markdown
![Alt text](media/image.png){: style="display: block; margin: 0 auto;" }
```

### Code blocks

Add the file name as a title on every code block that represents file contents:

````markdown
```json title="appsettings.json"
{ }
```
````

## Word usage

- Use "for example", never "for instance".
- Use "Open" instead of "Go to" or "Navigate to".
- For version ranges, use "higher", not "above". For example, "Version 1.0 and higher".
- Write verbs with the "re" prefix as a single closed word (for example, rewrite, reconfigure). Keep the hyphen only when removal causes ambiguity or awkward reading, for example, re-enter (not reenter), re-create (to create again, not recreate meaning "have fun").
- Write "pre" words as a single closed word with no hyphen.

## Headings

Do not place two consecutive headings without at least one sentence of introductory text between them. Every heading must be followed by at least one line of prose before descending to a lower heading level.

Correct:

```markdown
## Title

Short introduction to this section.

### Subtitle

Short introduction to this subsection.
```

Incorrect:

```markdown
## Title
### Subtitle
```

## Sentences

Avoid long sentences. If a sentence contains more than one comma, consider rewriting.

## Tables

- Capitalize only the first word of a column name.
- End each sentence in a cell with a period.
- Do not add a period after a single word or a code fragment.

## Lists

- Capitalize the first word of every list item.
- End each list item with a period, unless the item ends with a code fragment.
- Punctuation may be omitted in lists of one or two-word items.
- When a list item is a link, place the terminal period **inside** the link text, not after the URL. Correct: `1. [Name.](link)`. Incorrect: `1. [Name](link).`

## Steps

Do not use "Step 1", "Step 2", etc. in headings. Introduce a procedure with a numbered list of links to the corresponding sections, for example:

```markdown
To set up the Platform:

1. [Configure application strings](#link).
2. [Run the Platform](#link).
3. [Perform initial sign-in](#link).
```

## Prerequisites section

Use this intro phrase in every Prerequisites section:

> Before configuring the module, make sure you have:

## Interactive demos

Precede every interactive demo with this phrase:

> Try our interactive demo to explore key features in action:

## Glossaries

Per-guide, audience-partitioned. A term lives in the glossary that owns its topic; the audience-sibling cross-link sits once at the top of the glossary, never per entry.

Ownership routing:

- General VC concept (Module, Dynamic property, Catalog) → platform/{audience}-guide.
- Product-specific (storefront/marketplace/deployment-on-cloud) → that product's {audience}-guide. Create the file on first such term.
- Both audiences relevant → entry in each, scoped to audience, cross-linked.

Existing glossaries: [platform/user-guide](platform/user-guide/docs/glossary.md), [platform/developer-guide](platform/developer-guide/docs/glossary.md).

### Entry shape

- H2 per term, alphabetical insertion. 2 to 4 sentences max.
- Define by endonym, not exonym. Opening noun is a Virto-native label ("extra field", "user-defined field", "extension"). Vendor analogs ("custom field", "metafield") live only in the comparison table.
- User guide: business register. No developer jargon (runtime, code changes, schema, interface, data model). If the concept is partial (not universal across objects), qualify scope explicitly ("that supports X"); never use "any object" as shorthand.
- Developer guide: name canonical types, interfaces, services. When a known pattern from the GoF / DDD / EAA catalogs applies (for example, Entity-Attribute-Value, Specification), name it. Disambiguate via architectural shape; list supported modifiers and value types when part of the concept's signature. Terse. No API enumeration; link to the deep-dive.
- Internal synonyms (Admin UI / Platform / Back office) use inline "Same as **X**." Never in the comparison table.
- Identify the concept's fundamental properties (user-defined vs system; runtime-added vs compile-time; EAV vs columnar; admin-configurable vs dev-only) from code before drafting. With a parallel-concept sibling (for example, Catalog property and Dynamic property: both user-defined, runtime-registered, EAV-stored), opener mirrors shared nature; differences appear in scope, modifiers, or inheritance — never in inline "Unlike **X**" prose or in framing words ("structured", "schema-defined") that fabricate distinctions between equally-EAV concepts.
- Dev entry: code identifier only when the name IS the mechanism (interface consumers implement, scope discriminator type). Closed enumerable scopes go in prose.
- Per-entry "See also" lines may point to deep-dive pages within the same guide. They do not point to the audience-sibling glossary; the top-of-file cross-link covers that. Drop the entire "See also" line when nothing same-guide remains.

### Cross-platform comparison table

For terms with industry analogs, append one one-row Rosetta table after the prose:

```markdown
Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |
```

- Tier 1 columns, fixed order: Shopify, Adobe Commerce (Magento), commercetools, BigCommerce.
- Tier 2 column (Salesforce Commerce Cloud, SAP Commerce Cloud, Spryker, VTEX, WooCommerce, Sylius, Elastic Path) only when that vendor has a distinctively named equivalent.
- Cells are labels, not sentences: no trailing periods.
- "commercetools" stays lowercase (vendor's own orthography).
- Merchant-facing label, not internal schema or developer-only name. For example, commercetools "Custom field" (merchant-facing), not "Custom type" (schema).
- Audience split: user-guide table = merchant-facing labels; dev-guide table = same cells unless dev community uses a different general prose term. PascalCase identifiers (`AttributeDefinition`) and implementation-pattern labels ("EAV attribute") stay excluded.
- `n/a (uses X)` when a vendor's architecture collapses the distinction at the dev level (one mechanism, many object types). Example: Magento unified EAV across product, category, customer.

### Linking from other pages

- Target = owning glossary (§Ownership routing), audience-matched.
- Same-guide: relative path (**../glossary.md#anchor**). Mike versioning breaks site-internal absolute paths.
- Cross-guide: absolute with `/latest/` (**/platform/user-guide/latest/glossary#module**); the `/latest/` alias is mike-stable.
- First occurrence per top-level section, on its entry page (overview/index, or first page mentioning the term). Top-level section = immediate subdir of `docs/` or top-level standalone page.
- Apply across every guide where the term appears, not just the owning one. No relink in deeper pages of the same section. No self-link on the canonical page.
- Concept use vs label use. Phrasings like "the **Catalog** module" or "the **Quote** module" on a named-module overview page use "module" as a suffix to a specific named module; the substantive concept there is the named module (Catalog, Quote), not the abstract Module type. Do not link the suffix. Link only when the abstract concept is the subject ("separate modules", "modular Platform", "loaded as Virto Commerce modules"). Same rule applies to any term that doubles as concept and label suffix.

## Abbreviation tooltips

YAML content files, decoupled from `mkdocs.yml`. Hook [overrides/hooks/abbreviations_loader.py](overrides/hooks/abbreviations_loader.py) injects entries into python-markdown's abbr extension at build time.

### When to add a tooltip

Acronyms, initialisms, letter-based shorthands only (EAV, DDD, SKU, GTIN, xAPI). Native Virto and external industry: same rules. Threshold: cross-page reach.

Multi-word vocabulary terms (Dynamic property, Module) → glossary entry, not here. The abbr extension renders a non-interactive popover — wrong affordance for clickable definitions.

Definition leads with WHAT (concept type) and WHY (use case), not HOW (mechanism). Mechanism belongs in the glossary entry, which has room for it.

### Files

- [overrides/abbreviations.yml](overrides/abbreviations.yml): base layer, shared across opted-in guides.
- `<guide>/abbreviations.yml`, sibling of the guide's `mkdocs.yml`: per-guide overlay. Same key overrides base; new key extends. Create an overlay only for audience-driven divergence (pattern name for developers, "without code" for merchants); not for stylistic rewording of the same information. Delete an overlay that has drifted back to parity with the base.

### Authoring rules

- Length budget: ~50 char target, ~100 char hard cap. Renders as a non-interactive hover popover, ~1/4 viewport wide max.
- Abbr extension matches case-sensitively. Use YAML anchors and aliases (`&name`, `*name`) to DRY one definition across casing and plural variants. Four common forms: "Term", "Terms", "term", "terms".
- No links, no "See the Glossary" pointers. They do not render.
- Define by endonym, not exonym (same rule as glossary entries).

### Opting a guide in

Register the hook in the guide's `mkdocs.yml`:

```yaml
hooks:
    - ../../overrides/hooks/abbreviations_loader.py
```

## Verification before claims

Every Virto Commerce class, interface, type, vocabulary form, or third-party product name is verified before drafting. Unverified names do not appear in drafts; TBC footnotes do not ship.

- Virto code: GitHub MCP search plus file fetch in the `VirtoCommerce` org, or grep a local source mirror. Name-dropping the tool without invocation is not verification.
- Virto vocabulary: grep the docs corpus for term frequency; highest count wins. For example, "object" (689) beats "record" (14).
- Third-party products: fetch the vendor's own current docs (primary source: Shopify Help Center, Adobe Commerce, commercetools, BigCommerce) per cell. Blogs and tutorials are secondary. No equivalent → cell is `n/a`. If most cells cannot be verified against primary sources, drop the table rather than ship recall-based cells.
