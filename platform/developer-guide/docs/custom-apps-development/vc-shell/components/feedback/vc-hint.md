<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/atoms/vc-hint/vc-hint.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcHint

A small text component for displaying helper text, validation messages, or supplementary guidance below form fields. It renders as a lightweight `<div>` with muted styling in its default state and switches to a danger color with `role="alert"` when the `error` prop is set, ensuring screen readers announce validation problems immediately.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vchint--default&viewMode=story"
    loading="lazy"
    title="data-display-vchint--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vchint--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Show helper text beneath input fields explaining expected format or constraints
- Display validation error messages in a consistent style
- Provide supplementary guidance like file size limits or password requirements
- Present character counts or remaining quota
- When NOT to use: for prominent alert messages, use [VcBanner](./vc-banner.md); for field labels, use [VcLabel](../misc/vc-label.md)

## Basic Usage

```vue
<VcHint>Maximum file size: 5MB</VcHint>
```

## Key Props

| Prop    | Type      | Default | Description                                                             |
| ------- | --------- | ------- | ----------------------------------------------------------------------- |
| `id`    | `string`  | --      | Optional id for linking with `aria-describedby` on the associated input |
| `error` | `boolean` | `false` | Shows the hint in error state (danger color)                            |

## CSS Variables

| Variable             | Default               | Description               |
| -------------------- | --------------------- | ------------------------- |
| `--hint-color`       | `var(--neutrals-500)` | Default text color        |
| `--hint-error-color` | `var(--danger-500)`   | Text color in error state |
| `--hint-font-size`   | `12px`                | Font size                 |
| `--hint-line-height` | `1.4`                 | Line height               |

## Common Patterns

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vchint--form-field-hint&viewMode=story"
    loading="lazy"
    title="data-display-vchint--form-field-hint"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vchint--form-field-hint" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

### Helper Text Below an Input

```vue
<VcInput label="Email" v-model="email" aria-describedby="email-hint" />
<VcHint id="email-hint">We'll never share your email with anyone else.</VcHint>
```

### Validation Error Message

```vue
<VcInput label="SKU" v-model="sku" :error="!isValid" aria-describedby="sku-hint" />
<VcHint v-if="!isValid" id="sku-hint" error>SKU must be unique and non-empty.</VcHint>
```

### Multiple Requirement Hints

```vue
<VcLabel>Password</VcLabel>
<VcInput type="password" v-model="password" />
<VcHint>Must be at least 8 characters long</VcHint>
<VcHint>Must include at least one number</VcHint>
<VcHint>Must include at least one special character</VcHint>
```

### Hint with Inline Link

```vue
<VcHint>
  This field is optional. Learn more in our
  <a href="/docs" class="tw-text-[color:var(--primary-500)] tw-underline">documentation</a>.
</VcHint>
```

## Recipe: Dynamic Character Counter

Combine VcHint with a computed property to show a live character count:

```vue
<script setup lang="ts">
import { ref, computed } from "vue";

const description = ref("");
const maxLength = 500;
const remaining = computed(() => maxLength - description.value.length);
const isOverLimit = computed(() => remaining.value < 0);
</script>

<template>
  <VcTextarea
    label="Description"
    v-model="description"
  />
  <VcHint :error="isOverLimit"> {{ remaining }} characters remaining </VcHint>
</template>
```

## Recipe: Conditional Helper vs. Error

Show helper text by default, but swap to an error message when validation fails:

```vue
<template>
  <VcInput
    label="Slug"
    v-model="slug"
    :error="!!slugError"
    aria-describedby="slug-hint"
  />
  <VcHint
    id="slug-hint"
    :error="!!slugError"
  >
    {{ slugError || "URL-friendly identifier. Use lowercase letters and hyphens." }}
  </VcHint>
</template>
```

## Tips

- Always pair the `id` prop on VcHint with `aria-describedby` on the associated input. This creates a programmatic link that screen readers use to announce the hint when the input is focused.
- When `error` is true, VcHint renders with `role="alert"`, which causes assistive technology to announce the content immediately. Avoid toggling `error` rapidly, as each transition triggers a new announcement.
- VcHint accepts any slot content, including HTML elements. Use inline `<a>` tags for documentation links or `<code>` for format examples.
- Multiple VcHint components can stack below a single field. They render as block-level elements with no built-in margin, so add `tw-mt-1` or a parent with `tw-space-y-1` for spacing.

## Accessibility

- When `error` is true, the hint renders with `role="alert"` for live screen reader announcement
- Use the `id` prop with `aria-describedby` on the associated input to create a programmatic link
- Muted color styling differentiates hints from primary content visually

## Related Components

- [VcLabel](../misc/vc-label.md) -- field label component, typically placed above the input
- [VcBanner](./vc-banner.md) -- for longer or more prominent alert messages
- [VcInput](../form/vc-input.md) -- form input component often paired with VcHint


