# Virto Commerce Platform Style Guide

This Virto Commerce Platform Style Guide will help you develop consistent modules for the Platform. You can create your own styles using the rules below.

## Rules

The purpose of these rules is to help developers easily make changes to CSS styles in a consistent manner.

### Naming

Any module name should match the purpose of the module in question to have good understanding of what it stands for.

### Inheritance

Inner module classes should be implemented only as part of the module:

`.block-module {}`

`.block-module .element-module {}`

`.block-module {}`

`.element-module {}`

### Style tiers

There are four module style tiers:

* **Reset.css**: The basis of all styles with the default styles reset, fonts set, and base sizes defined. 
* **Base modules.css**: This tier has base elements, forms, and buttons defined.
* **Project modules.css**: Module style isolation tier with specific module styles defined.
* **Cosmetic.css**: Houses minor modifications of colors, as well as links.

## Naming conventions

* Use **-** (hyphen) as a word separator, e.g. `input-field`.
* Use **_** (underscore) as a logic part separator, e.g., `toolbar_logo`.
* Use **__** (double underscore) as a modifier separator, e.g., `module_list.__modifier`.

## Module modifier example

Let's assume you have the following module defined:

```
.module {}

.module .module-t {}

.module .module-decsr {}
```

Once you need the module to get the red color theme, you have to add `__red` as a modifier separator:

```
.module.__red {}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Configuration-Reference/appsettingsjson">← Appsettings.json </a>
    <a href="../ui-scroll-directive">UI scroll directive  →</a>
</div>