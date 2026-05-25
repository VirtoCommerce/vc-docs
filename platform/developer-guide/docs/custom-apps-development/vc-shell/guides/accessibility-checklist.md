# Accessibility Checklist

VC components are built with accessibility in mind: `VcButton` declares `aria-busy` and `aria-pressed`, `VcDataTable` exposes column-picker semantics, popups trap focus, and toolbars are keyboard-navigable. Most of this you get for free. This checklist covers what is left to you: the inputs you choose, the labels you write, the keyboard paths you do not break.

## Use the right component

The cheapest accessibility win is picking the framework's purpose-built component instead of rolling your own. The framework's input components ship the correct ARIA wiring, label-input association, and focus management.

| You need | Use this, not a custom one |
| --- | --- |
| A clickable action. | `VcButton`. Even icon-only — pass `aria-label`. |
| A form field. | `VcInput`, `VcSelect`, `VcTextarea`, `VcCheckbox`. They render labels associated with the input. |
| A destructive confirmation. | `usePopup().showConfirmation`. It traps focus and returns it to the trigger. |
| Tabular data. | `VcDataTable`. It announces sort changes and exposes a column picker. |
| A blade-level form. | `VcBlade` + `useBladeForm`. The unsaved-changes prompt is announced. |

If a component does not exist for what you need, compose from VC primitives rather than dropping to raw `<div>` and `<button>`.

## Label every interactive element

Icon-only buttons and toolbar entries are the most common gap. The framework cannot infer a label from `lucide-trash-2`.

```ts title="OrderList.vue"
const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "remove",
    icon: "lucide-trash-2",
    title: computed(() => t("ORDERS.LIST.TOOLBAR.REMOVE")),
    async clickHandler() { /* ... */ },
  },
]);
```

`title` is what gets announced. Localize it. Do not leave it as a bare `"Remove"` literal that lives outside the i18n bundle.

For inputs:

```vue title="OrderDetails.vue"
<VcInput
  v-model="item.number"
  :label="$t('ORDERS.DETAILS.FIELDS.NUMBER')"
  required
/>
```

Required fields get a programmatic `required` attribute, not just a red asterisk in the label.

## Keyboard paths you must preserve

A keyboard user reaches every interactive element with `Tab`, activates with `Enter` or `Space`, and dismisses overlays with `Escape`. Three test cases catch most regressions:

1. **Tab through a blade from top to bottom.** Every interactive element receives focus in source order, no traps, no skipped elements.
2. **Open a details blade, edit a field, press Escape.** The close confirmation appears (or the blade closes if pristine). Focus returns to the row that opened it.
3. **Open a popup, dismiss with Escape.** Focus returns to the trigger.

These are the paths the framework wires by default. They break when you call `e.preventDefault()` on key events, when you intercept `Escape` on a custom container, or when you set `tabindex="-1"` on a wrapper that contains real inputs.

## Color contrast and motion

VC themes ship WCAG-AA contrast in the default light and dark palettes. If you add a custom theme through `useTheme().register`, run the foreground / background pairs through a contrast checker before shipping.

For motion-sensitive users, avoid wiring auto-playing animations into blade entries. The framework's blade transitions respect `prefers-reduced-motion`; custom transitions added with `<Transition>` must too.

## Manual test pass

Before merging a module, spend ten minutes:

- Tab through every blade. Check focus order makes sense.
- Open and close one blade with the keyboard alone.
- Resize the browser to 320px wide. Check that toolbars collapse, not overlap.
- Switch the theme to dark. Check that custom inline colors still meet contrast.
- Toggle the OS "Reduce motion" preference. Check that nothing animates excessively.

For continuous coverage, axe DevTools or Lighthouse run against the local dev server catches the obvious issues a manual pass misses.

## Related

- [VcButton reference.](../components/misc/vc-button.md)
- [VcDataTable reference.](../components/data-display/vc-data-table.md)
- [Theming concept.](../concepts/theming.md)
