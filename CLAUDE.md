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
