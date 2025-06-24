# VcForm Component

The `VcForm` component is a simple wrapper around the standard HTML form element. It provides a consistent way to implement forms in VC-Shell applications and serves as a container for form components.

## Storybook

[VcForm Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcform--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcform--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcForm @submit.prevent="handleSubmit">
    <VcInput
      v-model="form.name"
      label="Name"
      required
    />
    
    <div class="tw-mt-4">
      <VcButton type="submit">
        Submit
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { VcForm, VcInput, VcButton } from '@vc-shell/framework';

const form = reactive({
  name: ''
});

function handleSubmit() {
  console.log('Form submitted with:', form);
}
</script>
```

## Slots

| Slot Name | Description |
|-----------|-------------|
| `default` | Content of the form |

## Events

VcForm uses native HTML form events:

| Event     | Payload   | Description                   |
|-----------|-----------|-------------------------------|
| `submit`  | `Event`   | Emitted when form is submitted |

## Examples

### Basic Form

```vue
<template>
  <VcForm>
    <div class="tw-space-y-4">
      <VcInput
        v-model="form.name"
        label="Full Name"
      />
      
      <VcInput
        v-model="form.email"
        label="Email"
        type="email"
      />
      
      <VcButton @click="handleSubmit">
        Submit
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { VcForm, VcInput, VcButton } from '@vc-shell/framework';

const form = reactive({
  name: '',
  email: ''
});

function handleSubmit() {
    console.log('Form submitted successfully:', form);
    // Process the form data...
}
</script>
```

## Styling

The `VcForm` component is a minimal wrapper around the HTML `<form>` element and doesn't include specific CSS styling or variables. The component itself consists of only a `<form>` element with a default slot.

For styling forms in your application:

- Apply Tailwind CSS classes to the form container or child elements
- Use the appropriate spacing and layout utilities for form elements
- Style individual form input components (like `VcInput`, `VcSelect`, etc.) using their respective CSS variables
