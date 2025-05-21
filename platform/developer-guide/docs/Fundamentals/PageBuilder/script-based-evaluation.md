# Script-based Evaluation

Some settings support dynamic values that are evaluated at runtime. This includes:

* [Templating.](#templating)
* [Embedded JavaScript expressions.](#embedded-javascript)

These features allow settings to be context-aware, flexible, and reactive to runtime parameters like current store, theme, or user permissions.

This mechanism is not limited to the main Page Builder settings — it is also used across various UI controls, such as select, search, and url-based fields, enabling dynamic data loading and rendering logic.

You can use these tools to construct URLs, modify request payloads, conditionally show or hide options, or fetch external resources based on the current environment.

## Templating

Any string value in the settings can include **placeholders** in the format:

```txt
`some text/{{some value from the current context}}/some other text/{{the other value}}`
```


## Embedded JavaScript

You can also insert executable code using the `{{= ... }}` syntax. For example:

```txt
`some text/{{= js code where **this** is context}}/some other text/{{the other value}}`
```


!!! note
    Embedded scripts (`{{= ... }}`) are less secure and should be used only when you fully trust the source of the configuration. Avoid user-generated code unless properly sandboxed.

## Universal application

This evaluation behavior applies recursively to **all string values** in:

* Strings in objects.
* Elements of arrays.
* Nested properties of any depth.

If a string contains a `{{...}}` pattern, it will be interpreted using the templating engine. This allows full flexibility but also means you should structure your data carefully to avoid accidental substitutions.