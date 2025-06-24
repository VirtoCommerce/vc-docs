# VcInputCurrency Component

The `VcInputCurrency` component is a specialized input component for handling monetary values with proper formatting. It combines a number input with currency selection via a dropdown, enabling users to enter monetary amounts in various currencies.

## Storybook

[VcInputCurrency Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcinputcurrency--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcinputcurrency--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcInputCurrency
    v-model:model-value="amount"
    v-model:option="currency"
    label="Price"
    placeholder="Enter price"
    :options="currencies"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1000);
const currency = ref('USD');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' },
  { title: 'JPY', value: 'JPY' }
];
</script>
```

## Props

| Prop             | Type                                   | Default     | Description                                     |
| ---------------- | -------------------------------------- | ----------- | ----------------------------------------------- |
| `modelValue`     | `number \| null \| undefined`          | `undefined` | Numeric value of the input                      |
| `label`          | `string`                               | `undefined` | Text label for the input field                  |
| `placeholder`    | `string`                               | `undefined` | Placeholder text for the input field            |
| `hint`           | `string`                               | `undefined` | Helper text displayed below the input field     |
| `clearable`      | `boolean`                              | `false`     | Enables a clear button to reset the field       |
| `prefix`         | `string`                               | `undefined` | Prefix displayed before the input value         |
| `suffix`         | `string`                               | `undefined` | Suffix displayed after the input value          |
| `name`           | `string`                               | `'Field'`   | Name attribute for the input element            |
| `loading`        | `boolean`                              | `false`     | Shows a loading indicator                       |
| `debounce`       | `string \| number`                     | `0`         | Debounce amount for input changes in ms         |
| `disabled`       | `boolean`                              | `false`     | Disables the input field                        |
| `autofocus`      | `boolean`                              | `false`     | Focus field on initial component render         |
| `error`          | `boolean`                              | `false`     | Indicates an error state                        |
| `errorMessage`   | `string`                               | `undefined` | Error message to display                        |
| `maxlength`      | `string \| number`                     | `undefined` | Maximum length of input value                   |
| `tooltip`        | `string`                               | `undefined` | Tooltip text for additional information         |
| `required`       | `boolean`                              | `false`     | Makes the field required                        |
| `option`         | `string`                               | `undefined` | Selected currency option                        |
| `options`        | `unknown[]`                            | `[]`        | Available currency options                      |
| `optionValue`    | `string \| ((option: unknown) => string)` | `undefined` | Property or function to get option value     |
| `optionLabel`    | `string \| ((option: unknown) => string)` | `undefined` | Property or function to get option label     |
| `currencyDisplay`| `'symbol' \| 'code' \| 'name' \| 'hidden'` | `'hidden'`  | How to display the currency symbol          |
| `precision`      | `0 to 15`                              | `2`         | Number of decimal places for the currency value |
| `searchable`     | `boolean`                              | `false`     | Enable search in dropdown                       |

## Events

| Event                | Payload             | Description                                     |
| -------------------- | ------------------- | ----------------------------------------------- |
| `update:modelValue`  | `number \| null`    | Emitted when the input value changes            |
| `update:option`      | `unknown`           | Emitted when the selected currency changes      |
| `change`             | `number \| string \| null` | Emitted when the input value changes     |
| `blur`               | `Event`             | Emitted when the input field loses focus        |

## CSS Variables

The component uses CSS variables for styling that can be customized:

```css
:root {
  --input-curr-toggle-color: var(--primary-500);  /* Color of the currency dropdown toggle button */
}
```

## Implementation Details

The component is built on top of the `VcInputDropdown` component and uses the `vue-currency-input` library for formatting. It:

- Automatically formats numbers according to the user's locale settings
- Prevents entering negative values or non-numeric characters
- Handles keyboard navigation with Tab and Enter keys
- Automatically formats pasted values

## Examples

### Basic Currency Input

```vue
<template>
  <VcInputCurrency
    v-model:model-value="amount"
    v-model:option="currency"
    label="Price"
    placeholder="Enter price"
    :options="currencies"
  />
  
  <div class="tw-mt-4">
    <p>Current value: {{ amount }} {{ currency }}</p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1000);
const currency = ref('USD');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' },
  { title: 'JPY', value: 'JPY' }
];
</script>
```

### With Helper Hint

```vue
<template>
  <VcInputCurrency
    v-model:model-value="amount"
    v-model:option="currency"
    label="Total Amount"
    placeholder="Enter amount"
    hint="Enter the amount in the selected currency"
    :options="currencies"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1250.75);
const currency = ref('EUR');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];
</script>
```

### With Validation

```vue
<template>
  <VcForm @submit.prevent="validateForm">
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="Payment Amount"
      placeholder="Enter amount"
      :error="!!amountError"
      :errorMessage="amountError"
      required
      :options="currencies"
    />
    
    <div class="tw-mt-4">
      <VcButton type="submit">
        Submit
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency, VcForm, VcButton } from '@vc-shell/framework';

const amount = ref(null);
const currency = ref('USD');
const amountError = ref('');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];

function validateForm() {
  amountError.value = '';
  
  if (!amount.value) {
    amountError.value = 'Amount is required';
    return;
  }
  
  if (amount.value <= 0) {
    amountError.value = 'Amount must be greater than zero';
    return;
  }
  
  console.log('Form submitted:', { amount: amount.value, currency: currency.value });
}
</script>
```

### With Different Precision Options

```vue
<template>
  <div class="tw-space-y-4">
    <VcInputCurrency
      v-model:model-value="amount0"
      v-model:option="currency"
      label="No decimals (precision: 0)"
      :precision="0"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount1"
      v-model:option="currency"
      label="One decimal (precision: 1)"
      :precision="1"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount2"
      v-model:option="currency"
      label="Two decimals (precision: 2)"
      :precision="2"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount3"
      v-model:option="currency"
      label="Three decimals (precision: 3)"
      :precision="3"
      :options="currencies"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount0 = ref(1234.5678);
const amount1 = ref(1234.5678);
const amount2 = ref(1234.5678);
const amount3 = ref(1234.5678);
const currency = ref('USD');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];
</script>
```

### With Currency Symbol Display

```vue
<template>
  <div class="tw-space-y-4">
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Currency Symbol"
      currencyDisplay="symbol"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Currency Code"
      currencyDisplay="code"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Currency Name"
      currencyDisplay="name"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Hidden Currency"
      currencyDisplay="hidden"
      :options="currencies"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1000);
const currency = ref('USD');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];
</script>
```

### With Prefix and Suffix

```vue
<template>
  <div class="tw-space-y-4">
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Prefix"
      prefix="$"
      :options="currencies"
    />
    
    <VcInputCurrency
      v-model:model-value="amount"
      v-model:option="currency"
      label="With Suffix"
      suffix="USD"
      :options="currencies"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1000);
const currency = ref('USD');
const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];
</script>
```

### Searchable Currency Dropdown

```vue
<template>
  <VcInputCurrency
    v-model:model-value="amount"
    v-model:option="currency"
    label="With Searchable Dropdown"
    :searchable="true"
    :options="allCurrencies"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputCurrency } from '@vc-shell/framework';

const amount = ref(1000);
const currency = ref('USD');
const allCurrencies = [
  { title: 'US Dollar (USD)', value: 'USD' },
  { title: 'Euro (EUR)', value: 'EUR' },
  { title: 'British Pound (GBP)', value: 'GBP' },
  { title: 'Japanese Yen (JPY)', value: 'JPY' },
  { title: 'Canadian Dollar (CAD)', value: 'CAD' },
  { title: 'Australian Dollar (AUD)', value: 'AUD' },
  { title: 'Swiss Franc (CHF)', value: 'CHF' },
  { title: 'Chinese Yuan (CNY)', value: 'CNY' },
  { title: 'Swedish Krona (SEK)', value: 'SEK' },
  { title: 'New Zealand Dollar (NZD)', value: 'NZD' },
  // More currencies can be added here
];
</script>
```

