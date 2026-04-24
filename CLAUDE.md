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

Two glossaries exist, one per audience. A term that belongs in both gets a guide-appropriate entry in each, with cross-links.

- [platform/user-guide/docs/glossary.md](platform/user-guide/docs/glossary.md): business and operations vocabulary.
- [platform/developer-guide/docs/glossary.md](platform/developer-guide/docs/glossary.md): DDD, .NET, code-pattern vocabulary.

### Entry shape

- H2 per term, alphabetical insertion. 2 to 4 sentences max.
- User guide: business language. No dev jargon such as "runtime", "code changes", "schema", "interface", "data model".
- Developer guide: name the canonical types, interfaces, services. Stay terse. Do not enumerate full APIs in a glossary entry; link to the deep-dive page.
- Internal Virto Commerce synonyms (for example, Admin UI / Platform / Back office) use inline "Same as **X**." Do not put internal synonyms in the comparison table.

### Cross-platform comparison table

For terms with industry analogs, append one one-row table after the prose:

```markdown
Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |
```

- Tier 1 columns, always in this order: Shopify, Adobe Commerce (Magento), commercetools, BigCommerce.
- Add a Tier 2 column (Salesforce Commerce Cloud, SAP Commerce Cloud, Spryker, VTEX, WooCommerce, Sylius, Elastic Path) only when that platform has a distinctively named equivalent.
- Cells are short labels, not sentences: no trailing periods.
- "commercetools" stays lowercase. It is the product's own spelling.
- Use the merchant-facing label, not an internal schema or developer-only name. For example, commercetools "Custom field" is the merchant-facing label, not "Custom type" which is the schema.

### Linking from other pages

- Use relative paths, for example **../glossary.md#fulfillment-center**. Never absolute paths like **/platform/user-guide/glossary#...** because they break under `mike` versioning.
- Link on first mention per page only. Do not repeat in nested articles when the parent overview already linked the term.
- Skip the link when the page is itself the canonical definition of the term.

## Abbreviation tooltips

Tooltip definitions live in YAML content files separated from `mkdocs.yml` configuration. The hook [overrides/hooks/abbreviations_loader.py](overrides/hooks/abbreviations_loader.py) injects them into python-markdown's abbr extension at build time.

### When to add a tooltip

Add a tooltip when the term is referenced across many pages. Skip for single-page mentions.

### Files

- [overrides/abbreviations.yml](overrides/abbreviations.yml): general definitions used by every guide that opts in.
- `<guide>/abbreviations.yml`, sibling of the guide's `mkdocs.yml`. Per-guide overrides. Same key replaces the general definition; new keys add to it. Do not create the override file unless the wording must genuinely differ for the audience. If an override becomes identical to the root, delete it.

### Authoring rules

- Length budget: aim for ~50 characters, hard cap ~100. Tooltips render as a non-interactive browser hover popup, roughly 1/4 of the screen width at most.
- The abbr extension matches case-sensitively. Use YAML anchors and aliases (`&name`, `*name`) to share one definition across casing and plural variants. The four common forms are "Term", "Terms", "term", "terms".
- Do not put links or "See the Glossary" hints inside a tooltip. They do not render.

### Opting a guide in

Add the hook to the guide's `mkdocs.yml`:

```yaml
hooks:
    - ../../overrides/hooks/abbreviations_loader.py
```

## Verification before claims

Every claim about a Virto Commerce class, interface, type, vocabulary preference, or third-party product name must be verified before any draft text is written. Unverified names do not appear in the draft; "to be confirmed" footnotes and "I would verify later" comments do not ship.

- Virto Commerce code: invoke GitHub MCP to search and fetch files in the `VirtoCommerce` organization, or grep a local source mirror. Mentioning the tool without running it is not verification.
- Virto Commerce vocabulary: grep the docs corpus for term frequency before choosing wording. For example, "object" (689 hits) versus "record" (14 hits) means the answer is "object".
- Third-party products: fetch the platform's own current docs (Shopify Help Center, Adobe Commerce, commercetools, BigCommerce) per cell before drafting. Vendor blogs and tutorials are secondary sources. If a platform has no equivalent, the cell is `n/a`. If most cells cannot be verified, drop the comparison table rather than ship recall-based cells.
