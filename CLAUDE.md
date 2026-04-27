# Virto Commerce Docs Style Guide

This file defines the writing and formatting conventions for all documentation in this repository. Apply these rules to every new or edited Markdown file.

## Spelling

Use the following forms exactly:

- Virto Commerce (space separated; two words in text; alternatives allowed in code only).
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

Use bold for file names, for example, **appsettings.json**, **module.manifest**.

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

Audience-partitioned, one per guide. Shared terms get a separate entry in each, with bidirectional cross-links.

- [platform/user-guide/docs/glossary.md](platform/user-guide/docs/glossary.md): business and operations vocabulary.
- [platform/developer-guide/docs/glossary.md](platform/developer-guide/docs/glossary.md): DDD, .NET, code-pattern vocabulary.

### Entry shape

- H2 per term, alphabetical insertion. 2 to 4 sentences max.
- Define by endonym, not exonym. Opening noun is a Virto-native label ("extra field", "user-defined field", "extension"). Vendor analogs ("custom field", "metafield") live only in the comparison table.
- User guide: business register. No developer jargon (runtime, code changes, schema, interface, data model). If the concept is partial (not universal across objects), qualify scope explicitly ("that supports X"); never use "any object" as shorthand.
- Developer guide: name canonical types, interfaces, services. When a known pattern from the GoF / DDD / EAA catalogs applies (for example, Entity-Attribute-Value, Specification), name it. Disambiguate via architectural shape; list supported modifiers and value types when part of the concept's signature. Terse. No API enumeration; link to the deep-dive.
- Internal synonyms (Admin UI / Platform / Back office) use inline "Same as **X**." Never in the comparison table.
- Identify the concept's fundamental properties (user-defined vs system; runtime-added vs compile-time; EAV vs columnar; admin-configurable vs dev-only) from code before drafting. With a parallel-concept sibling (for example, Catalog property and Dynamic property: both user-defined, runtime-registered, EAV-stored), opener mirrors shared nature; differences appear in scope, modifiers, or inheritance — never in inline "Unlike **X**" prose or in framing words ("structured", "schema-defined") that fabricate distinctions between equally-EAV concepts.
- Dev entry: code identifier only when the name IS the mechanism (interface consumers implement, scope discriminator type). Closed enumerable scopes go in prose.

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

- Relative paths only (**../glossary.md#fulfillment-center**). Absolute paths break under `mike` versioning.
- First mention per page only. No relink in child pages once the parent overview has linked the term.
- No self-link on the canonical definition page.

## Abbreviation tooltips

YAML content files, decoupled from `mkdocs.yml`. Hook [overrides/hooks/abbreviations_loader.py](overrides/hooks/abbreviations_loader.py) injects entries into python-markdown's abbr extension at build time.

### When to add a tooltip

Cross-page references only. Single-page mentions: skip.

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
