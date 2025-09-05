# Visual Theme Customization

Visual theme customization in Virto Commerce Frontend is based on a flexible system of presets, CSS variables, and style overrides. Presets define the overall look of the Frontend by providing color palettes and design tokens that are automatically converted into reusable CSS custom properties. These variables can be fine-tuned or extended in custom styles, giving you full control over colors, spacing, and component appearance. Additionally, global and per-component options such as border radius ensure consistent, brand-aligned UI design.

## Presets

Presets are JSON files that define color palettes and other design tokens for the Frontend.

During project build, presets are converted into **CSS custom properties** (`--color-*` variables), which can be reused across all components.

For example, `"color_primary_50": "#f6f1ef"` becomes `--color-primary-50: #f6f1ef`.

You can use the following presets as a base to create own presets:

* The [default preset](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/mercury.json): Uses the base palette without additional variables.
* The [Coffee](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/coffee.json), [Black-Gold](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/black-gold.json), [Purple-Pink](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/purple-pink.json), [Watermelon](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/presets/watermelon.json) presets: Redefine palettes and may introduce additional variables if needed.

!!! note
    You can use AI to create color palettes - ask it to generate colors for an e-commerce website in JSON format based on presets. 

![Readmore](media/readmore.png){: width="25"} [Applying presets](../../../../platform/user-guide/content/managing-themes#apply-theme-color-scheme)


## Customizable variables

The [CSS custom properties](https://github.com/VirtoCommerce/vc-frontend/blob/dev/client-app/assets/styles/_colors.scss) are generated from presets and can be overridden in **_custom.scss**.

Below is the breakdown of some variables:

![Variables](media/colors-explanation.png)


## Border radius configuration

You can easily adjust border-radius values for all components or on a per-component basis using CSS custom properties.

* `--vc-radius`: Sets the global border-radius for all components. Default: 0.5rem (8px).
* Per-component overrides: If you need a different radius for a specific component, you can override the global value by defining a custom property scoped to that component. For example:

    * `--vc-button-radius`
    * `--vc-widget-radius`
    * etc.

!!! note
    Recommended maximum border-radius: **10px (0.625rem)**. Larger values may appear overly rounded and disrupt visual consistency.


```scss title="_custom.scss"

:root {
  // Change the global radius
  --vc-radius: 0.25rem; // now 4px

  // Override button radius only
  --vc-button-radius: 0.75rem; // now 12px
}
```

## Styles customization

Component styles follow the **BEM methodology**. To avoid merge conflicts and keep your customizations centralized, **do not** edit the core style files. Instead, put all your overrides into the **client-app/assets/styles/_custom.scss** file:

```scss title="_custom.scss"

.vc-container {
  &__bg {
    background-color: red;
  }
}
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Frontend customization overview</a>
    <a href="../functionality-customization">Functionality customization →</a>
</div>