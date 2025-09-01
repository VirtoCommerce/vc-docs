# Theme Customization

Virto Commerce theme can be customized through **presets**. This guide explains how presets, variables, and styles are connected, and how to extend or override them safely.


## Presets

Presets are **JSON files** that define color palettes and other design tokens for the Frontend.

During project build, presets are converted into **CSS custom properties** (`--color-*` variables), which can be reused across all components.

For example, `"color_primary_50": "#f6f1ef"` becomes `--color-primary-50: #f6f1ef`.

The [default preset](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/mercury.json) uses the base palette without additional variables.

The [Coffee](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/coffee.json), [Black-Gold](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/black-gold.json), [Purple-Pink](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/purple-pink.json), [Watermelon](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/watermelon.json) presets redefine palettes and may introduce additional variables if needed.

## Customizable variables

The [CSS custom properties](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/styles/_colors.scss) are generated from presets and can be overridden in **_custom.scss**.

Below is the breakdown of some variables:

![Variables](media/colors-explanation.png)

## Styles customization

Component styles follow the **BEM methodology**. To avoid merge conflicts and keep your customizations centralized, **do not** edit the core style files. Instead, put all your overrides into the **client-app/assets/styles/_custom.scss** file:

```scss title="_custom.scss"

.vc-container {
  &__bg {
    background-color: red;
  }
}
```


## Border radius configuration

You can easily adjust border-radius values for all components or on a per-component basis using CSS custom properties.

* `--vc-radius`: Sets the global border-radius for all components. Default: 0.5rem (8px).
* Per-component overrides: If you need a different radius for a specific component, you can override the global value by defining a custom property scoped to that component. For example:

    * `--vc-button-radius`
    * `--vc-widget-radius`
    * etc.

!!! note
    Recommended maximum border-radius: **10px (0.625rem)**. Larger values may appear overly rounded and disrupt visual consistency.


```scss title="client-app/assets/styles/_custom.scss"

:root {
  // Change the global radius
  --vc-radius: 0.25rem; // now 4px

  // Override button radius only
  --vc-button-radius: 0.75rem; // now 12px
}
```

## Applying presets

In the **Platform Store Settings**, you can specify the **scheme name** in the **White labeling widget**.
The selected scheme will be applied as the default preset for that store.

