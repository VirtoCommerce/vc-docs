# VcCheckbox Component

The `VcCheckbox` component is a molecule used throughout the VC-Shell framework for creating customizable checkbox inputs. It supports different sizes, states, and styles to meet various UI requirements.

## Storybook

[VcCheckbox Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vccheckbox--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vccheckbox--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcCheckbox v-model="isChecked" label="Accept Terms">
    I agree to the terms and conditions
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const isChecked = ref(false);
</script>
```

## Props

| Prop            | Type                | Default     | Description                                      |
| --------------- | ------------------- | ----------- | ------------------------------------------------ |
| `modelValue`    | `boolean`           | `undefined` | Current value of the checkbox (v-model)          |
| `disabled`      | `boolean`           | `false`     | Whether the checkbox is disabled                 |
| `required`      | `boolean`           | `false`     | Whether the checkbox is required                 |
| `name`          | `string`            | `'Field'`   | Name attribute for the input element             |
| `errorMessage`  | `string`            | `undefined` | Error message to display below the checkbox      |
| `trueValue`     | `boolean`           | `true`      | Value representing the checked state             |
| `falseValue`    | `boolean`           | `false`     | Value representing the unchecked state           |
| `label`         | `string`            | `undefined` | Label displayed above the checkbox               |
| `tooltip`       | `string`            | `undefined` | Tooltip text displayed with the label            |
| `size`          | `'s' \| 'm' \| 'l'` | `'s'`       | Size of the checkbox                             |
| `indeterminate` | `boolean`           | `false`     | Whether to show the checkbox in indeterminate state |

## Events

| Event              | Payload   | Description                                      |
| ------------------ | --------- | ------------------------------------------------ |
| `update:modelValue` | `boolean` | Emitted when the checkbox state changes          |

## Slots

| Slot       | Description                                           |
| ---------- | ----------------------------------------------------- |
| `default`  | Content displayed next to the checkbox                |
| `error`    | Custom content for error message display              |
| `icon`     | Custom icon for the checked state                     |

## CSS Variables

The checkbox component uses CSS variables for theming, which can be customized:

```css
:root {
  /* Checkbox size */
  --checkbox-size-s: 14px;                          /* Size for small checkbox variant */
  --checkbox-size-m: 18px;                          /* Size for medium checkbox variant */
  --checkbox-size-l: 24px;                          /* Size for large checkbox variant */

  /* Main colors */
  --checkbox-border-color: var(--neutrals-400);     /* Border color in normal unchecked state */
  --checkbox-bg-color: var(--additional-50);        /* Background color in normal unchecked state */
  --checkbox-text-color: var(--neutrals-900);       /* Text color for checkbox label */

  /* Checkbox checked state */
  --checkbox-checked-bg-color: var(--primary-500);  /* Background color when checkbox is checked */
  --checkbox-checked-border-color: var(--primary-500); /* Border color when checkbox is checked */
  --checkbox-icon-color: var(--additional-50);      /* Color of the checkmark icon */

  /* Indeterminate state */
  --checkbox-indeterminate-bg-color: var(--neutrals-500); /* Background color in indeterminate state */
  --checkbox-indeterminate-border-color: var(--neutrals-500); /* Border color in indeterminate state */
  --checkbox-indeterminate-line-color: var(--additional-50); /* Color of the indeterminate indicator line */

  /* Error state */
  --checkbox-error-border-color: var(--danger-500); /* Border color when checkbox has an error */
  --checkbox-error-text-color: var(--danger-500);   /* Text color for error message */

  /* Disabled state */
  --checkbox-disabled-bg-color: var(--neutrals-200); /* Background color when checkbox is disabled */
  --checkbox-disabled-border-color: var(--neutrals-200); /* Border color when checkbox is disabled */
  --checkbox-disabled-opacity: 0.7;                  /* Opacity value for disabled state */

  /* Focus */
  --checkbox-focus-shadow-color: var(--primary-50); /* Color of focus ring shadow */
  --checkbox-focus-shadow-size: 2px;                /* Size of focus ring shadow */

  /* Other */
  --checkbox-border-radius: 2px;                    /* Border radius of checkbox box */
  --checkbox-required-color: var(--danger-500);     /* Color of required indicator asterisk */
  --checkbox-transition-duration: 0.2s;             /* Duration of transition animations */
  --checkbox-margin-spacing: 0.5rem;                /* Margin spacing around the checkbox */
  --checkbox-text-margin: 0.5rem;                   /* Margin between checkbox and label text */
}
```



## Examples

### Basic Checkbox

```vue
<template>
  <VcCheckbox v-model="isChecked">
    Enable notifications
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const isChecked = ref(false);
</script>
```

### Checkbox with Label

```vue
<template>
  <VcCheckbox v-model="isSubscribed" label="Newsletter">
    Subscribe to our weekly newsletter
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const isSubscribed = ref(false);
</script>
```

### Required Checkbox

```vue
<template>
  <VcCheckbox v-model="termsAccepted" required label="Terms and Conditions">
    I accept the <a href="#" class="tw-text-[color:var(--primary-500)]">terms and conditions</a>
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const termsAccepted = ref(false);
</script>
```

### Checkbox Sizes

```vue
<template>
  <div class="tw-space-y-4">
    <VcCheckbox v-model="isCheckedSmall" size="s">
      Small checkbox
    </VcCheckbox>
    
    <VcCheckbox v-model="isCheckedMedium" size="m">
      Medium checkbox
    </VcCheckbox>
    
    <VcCheckbox v-model="isCheckedLarge" size="l">
      Large checkbox
    </VcCheckbox>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const isCheckedSmall = ref(true);
const isCheckedMedium = ref(true);
const isCheckedLarge = ref(true);
</script>
```

### Disabled Checkbox

```vue
<template>
  <div class="tw-space-y-4">
    <VcCheckbox v-model="isChecked" disabled>
      Disabled unchecked
    </VcCheckbox>
    
    <VcCheckbox v-model="isCheckedDisabled" disabled>
      Disabled checked
    </VcCheckbox>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const isChecked = ref(false);
const isCheckedDisabled = ref(true);
</script>
```

### Checkbox with Error

```vue
<template>
  <VcCheckbox 
    v-model="termsAccepted" 
    :errorMessage="termsAccepted ? '' : 'You must accept the terms to continue'"
  >
    I agree to the terms and conditions
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const termsAccepted = ref(false);
</script>
```

### Checkbox with Tooltip

```vue
<template>
  <VcCheckbox 
    v-model="receiveUpdates" 
    label="Product Updates" 
    tooltip="You will receive emails about product updates and new features"
  >
    Keep me updated about new features
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const receiveUpdates = ref(false);
</script>
```

### Indeterminate Checkbox

```vue
<template>
  <div class="tw-space-y-4">
    <VcCheckbox 
      v-model="parentChecked" 
      :indeterminate="indeterminate"
      @update:modelValue="updateChildCheckboxes"
    >
      Select all items
    </VcCheckbox>
    
    <div class="tw-pl-8 tw-space-y-2">
      <VcCheckbox 
        v-for="(item, index) in items" 
        :key="index"
        v-model="item.checked"
        @update:modelValue="updateParentCheckbox"
      >
        {{ item.label }}
      </VcCheckbox>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive, computed } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const items = reactive([
  { label: 'Item 1', checked: false },
  { label: 'Item 2', checked: false },
  { label: 'Item 3', checked: false }
]);

const parentChecked = ref(false);
const indeterminate = ref(false);

function updateParentCheckbox() {
  const checkedCount = items.filter(item => item.checked).length;
  
  if (checkedCount === 0) {
    parentChecked.value = false;
    indeterminate.value = false;
  } else if (checkedCount === items.length) {
    parentChecked.value = true;
    indeterminate.value = false;
  } else {
    indeterminate.value = true;
  }
}

function updateChildCheckboxes(value) {
  items.forEach(item => {
    item.checked = value;
  });
  indeterminate.value = false;
}
</script>
```

### Custom Icon

```vue
<template>
  <VcCheckbox v-model="isSelected">
    <template #icon>
      <VcIcon 
        v-if="isSelected" 
        icon="material-star" 
        class="tw-text-[color:var(--additional-50)]" 
        size="s"
      />
    </template>
    Add to favorites
  </VcCheckbox>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcCheckbox, VcIcon } from '@vc-shell/framework';

const isSelected = ref(false);
</script>
```

### Checkbox Group

```vue
<template>
  <div>
    <h3 class="tw-text-lg tw-font-medium tw-mb-2">Select preferences:</h3>
    
    <div class="tw-space-y-2">
      <VcCheckbox 
        v-for="(option, index) in options"
        :key="index"
        v-model="selectedOptions[index]"
        @update:modelValue="updateSelection(index)"
      >
        {{ option }}
      </VcCheckbox>
    </div>
    
    <div class="tw-mt-4 tw-text-sm tw-text-[color:var(--neutrals-500)]">
      Selected: {{ selectedCount }} of {{ options.length }}
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive, computed } from 'vue';
import { VcCheckbox } from '@vc-shell/framework';

const options = [
  'Email notifications',
  'SMS alerts',
  'Browser notifications',
  'Weekly digest reports'
];

const selectedOptions = reactive(Array(options.length).fill(false));

const selectedCount = computed(() => {
  return selectedOptions.filter(opt => opt).length;
});

function updateSelection(index) {
  // You could perform additional logic here if needed
  console.log(`Option ${options[index]} ${selectedOptions[index] ? 'selected' : 'deselected'}`);
}
</script>
```
