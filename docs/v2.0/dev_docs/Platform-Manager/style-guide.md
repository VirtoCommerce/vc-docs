## Introduction

This Virto Commerce Platform Style Guide will help you develop consistent modules for the platform. You can use the existing styles described in our online [Style Guide](https://virtocommerce.com/guides/style-guide) or, alternatively, create your own styles using the rules below.

Apart from our [Style Guide](https://virtocommerce.com/guides/style-guide) that refers to correctly using HTML and CSS when platform UI, we also have [Blade Constructor](https://virtocommerce.com/guides/blade-constructor) that you can use to create your custom blades.

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

### Style Tiers

There are four module style tiers:

* *Reset.css*: The basis of all styles with the default styles reset, fonts set, and base sizes defined. 
* *Base modules.css*: This tier has base elements, forms, and buttons defined.
* *Project modules.css*: Module style isolation tier with specific module styles defined.
* *Cosmetic.css*: Houses minor modifications of colors, as well as links.

## Naming conventions

+ Use **-** (hyphen) as a word separator, e.g. `input-field`.

+ Use **_** (underscore) as a logic part separator, e.g., `toolbar_logo`.

+ Use **__** (double underscore) as a modifier separator, e.g., `module_list.__modifier`.

## Module Modifier Example

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
  
In order to use the styling properly, you should also become familiar with the [Multilayer CSS organization methodology](http://operatino.github.io/MCSS/en/).
