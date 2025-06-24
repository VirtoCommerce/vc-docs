# VcRadioButton Component

The `VcRadioButton` component is a molecule used throughout the VC-Shell framework for creating radio button inputs. It allows users to select a single option from a set of related choices, supporting various states and customizations.

## Storybook

[VcRadioButton Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcradiobutton--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcradiobutton--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <div>
    <VcRadioButton
      v-model="selectedOption"
      value="option1"
      label="Option 1"
    />
    <VcRadioButton
      v-model="selectedOption"
      value="option2"
      label="Option 2"
    />
    <VcRadioButton
      v-model="selectedOption"
      value="option3"
      label="Option 3"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton } from '@vc-shell/framework';

const selectedOption = ref('option1');
</script>
```

## Props

| Prop           | Type      | Default      | Description                                      |
| -------------- | --------- | ------------ | ------------------------------------------------ |
| `modelValue`   | `any`     | `undefined`  | Current selected value (v-model)                 |
| `value`        | `any`     | `undefined`  | Value of this radio button                       |
| `binary`       | `boolean` | `false`      | Whether to use as a boolean toggle               |
| `checked`      | `boolean` | `false`      | Whether the radio button is checked              |
| `disabled`     | `boolean` | `false`      | Whether the radio button is disabled             |
| `name`         | `string`  | `'RadioField'` | Name attribute for the input element           |
| `label`        | `string`  | `undefined`  | Label text displayed next to the radio button    |
| `error`        | `boolean` | `false`      | Whether to show the component in error state     |
| `errorMessage` | `string`  | `undefined`  | Error message to display below the radio button  |

## Events

| Event               | Payload | Description                                      |
| ------------------- | ------- | ------------------------------------------------ |
| `update:modelValue` | `any`   | Emitted when the radio button state changes      |

## Slots

| Slot      | Description                                         |
| --------- | --------------------------------------------------- |
| `error`   | Custom content for error message display            |

## CSS Variables

The radio button component uses CSS variables for theming, which can be customized:

```css
:root {
  --radio-active: var(--primary-500);            /* Color of the radio button when active/checked */
  --radio-active-inner: var(--additional-50);    /* Color of the inner circle when checked */
  --radio-border: var(--neutrals-400);           /* Border color of the radio button in normal state */
  --radio-background: var(--additional-50);      /* Background color of the unchecked radio button */
  --radio-disabled: var(--secondary-100);        /* Background color when disabled */
  --radio-disabled-inner: var(--secondary-200);  /* Inner color when disabled and checked */
  --radio-error: var(--danger-500);              /* Border color when in error state */
  --radio-size: 20px;                            /* Size of the radio button */
  --radio-border-outline: var(--primary-50);     /* Outline color on hover */
}
```

## Examples

### Basic Radio Button Group

```vue
<template>
  <div class="tw-space-y-2">
    <div v-for="option in options" :key="option.value">
      <VcRadioButton
        v-model="selectedOption"
        :value="option.value"
        :label="option.label"
      />
    </div>
    
    <div class="tw-mt-4 tw-text-sm tw-text-[color:var(--neutrals-500)]">
      Selected: {{ selectedOption }}
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton } from '@vc-shell/framework';

const options = [
  { value: 'email', label: 'Email' },
  { value: 'phone', label: 'Phone' },
  { value: 'mail', label: 'Mail' },
];

const selectedOption = ref('email');
</script>
```

### Radio Buttons with Object Values

```vue
<template>
  <div class="tw-space-y-2">
    <div v-for="product in products" :key="product.id">
      <VcRadioButton
        v-model="selectedProduct"
        :value="product"
        :label="product.name"
      />
    </div>
    
    <div class="tw-mt-4 tw-p-3 tw-bg-[color:var(--neutrals-100)] tw-rounded">
      <p class="tw-font-medium">Selected Product:</p>
      <p>Name: {{ selectedProduct.name }}</p>
      <p>Price: ${{ selectedProduct.price }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton } from '@vc-shell/framework';

const products = [
  { id: 1, name: 'Basic Plan', price: 9.99 },
  { id: 2, name: 'Standard Plan', price: 19.99 },
  { id: 3, name: 'Premium Plan', price: 29.99 },
];

const selectedProduct = ref(products[0]);
</script>
```

### Radio Button with Binary Mode

```vue
<template>
  <div>
    <VcRadioButton
      v-model="acceptTerms"
      :binary="true"
      label="I accept the terms and conditions"
    />
    
    <div class="tw-mt-4">
      <VcButton :disabled="!acceptTerms" @click="proceedToNextStep">
        Continue
      </VcButton>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton, VcButton } from '@vc-shell/framework';

const acceptTerms = ref(false);

function proceedToNextStep() {
  // Handle form submission or navigation
  console.log('Proceeding to next step');
}
</script>
```

### Disabled Radio Button

```vue
<template>
  <div class="tw-space-y-2">
    <VcRadioButton
      v-model="selectedOption"
      value="option1"
      label="Available Option"
    />
    
    <VcRadioButton
      v-model="selectedOption"
      value="option2"
      label="Unavailable Option"
      disabled
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton } from '@vc-shell/framework';

const selectedOption = ref('option1');
</script>
```

### Radio Buttons with Error State

```vue
<template>
  <form @submit.prevent="validateForm">
    <div class="tw-mb-4">
      <p class="tw-font-medium tw-mb-2">Select your preferred contact method:</p>
      <div class="tw-space-y-2">
        <VcRadioButton
          v-for="option in contactOptions"
          :key="option.value"
          v-model="selectedContactMethod"
          :value="option.value"
          :label="option.label"
          :error="formSubmitted && !selectedContactMethod"
          :errorMessage="formSubmitted && !selectedContactMethod ? 'Please select a contact method' : ''"
        />
      </div>
    </div>
    
    <VcButton type="submit">
      Submit
    </VcButton>
  </form>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRadioButton, VcButton } from '@vc-shell/framework';

const contactOptions = [
  { value: 'email', label: 'Email' },
  { value: 'phone', label: 'Phone' },
  { value: 'mail', label: 'Mail' },
];

const selectedContactMethod = ref('');
const formSubmitted = ref(false);

function validateForm() {
  formSubmitted.value = true;
  
  if (selectedContactMethod.value) {
    // Form is valid, proceed
    console.log('Form submitted with:', selectedContactMethod.value);
  }
}
</script>
```

### Grouped Radio Buttons with Custom Error Slot

```vue
<template>
  <form @submit.prevent="submitForm">
    <fieldset class="tw-border tw-border-[color:var(--neutrals-300)] tw-p-4 tw-rounded">
      <legend class="tw-px-2 tw-font-medium">Delivery Method</legend>
      
      <div class="tw-space-y-2">
        <VcRadioButton
          v-for="option in deliveryOptions"
          :key="option.value"
          v-model="selectedDelivery"
          :value="option.value"
          :label="option.label"
          :error="errors.delivery"
        >
          <template #error v-if="errors.delivery && option.value === deliveryOptions[0].value">
            <div class="tw-flex tw-items-center tw-mt-1">
              <VcIcon 
                icon="material-error_outline" 
                class="tw-mr-1 tw-text-[color:var(--danger-500)]" 
                size="s" 
              />
              <span class="tw-text-[color:var(--danger-500)] tw-text-sm">
                Please select a delivery method
              </span>
            </div>
          </template>
        </VcRadioButton>
      </div>
    </fieldset>
    
    <VcButton type="submit" class="tw-mt-4">
      Submit Order
    </VcButton>
  </form>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue';
import { VcRadioButton, VcButton, VcIcon } from '@vc-shell/framework';

const deliveryOptions = [
  { value: 'standard', label: 'Standard Delivery (3-5 business days)' },
  { value: 'express', label: 'Express Delivery (1-2 business days)' },
  { value: 'same-day', label: 'Same Day Delivery (where available)' },
];

const selectedDelivery = ref('');
const errors = reactive({
  delivery: false
});

function submitForm() {
  errors.delivery = !selectedDelivery.value;
  
  if (!errors.delivery) {
    // Form is valid, proceed with submission
    console.log('Order submitted with delivery method:', selectedDelivery.value);
  }
}
</script>
```

### Integration with Other Form Components

```vue
<template>
  <form @submit.prevent="submitForm" class="tw-space-y-4">
    <div>
      <VcLabel>Payment Method</VcLabel>
      <div class="tw-space-y-2 tw-mt-2">
        <VcRadioButton
          v-for="method in paymentMethods"
          :key="method.value"
          v-model="formData.paymentMethod"
          :value="method.value"
          :label="method.label"
        />
      </div>
    </div>
    
    <div v-if="formData.paymentMethod === 'card'">
      <VcLabel>Card Details</VcLabel>
      <VcInput 
        v-model="formData.cardNumber" 
        placeholder="Card Number" 
        class="tw-mb-2" 
      />
      <div class="tw-flex tw-gap-2">
        <VcInput v-model="formData.expiryDate" placeholder="MM/YY" />
        <VcInput v-model="formData.cvv" placeholder="CVV" />
      </div>
    </div>
    
    <div v-if="formData.paymentMethod === 'paypal'">
      <VcLabel>PayPal Email</VcLabel>
      <VcInput v-model="formData.paypalEmail" placeholder="Email" />
    </div>
    
    <VcButton type="submit">
      Proceed to Payment
    </VcButton>
  </form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { VcRadioButton, VcButton, VcLabel, VcInput } from '@vc-shell/framework';

const paymentMethods = [
  { value: 'card', label: 'Credit/Debit Card' },
  { value: 'paypal', label: 'PayPal' },
  { value: 'bank', label: 'Bank Transfer' },
];

const formData = reactive({
  paymentMethod: 'card',
  cardNumber: '',
  expiryDate: '',
  cvv: '',
  paypalEmail: '',
});

function submitForm() {
  console.log('Form submitted with data:', formData);
}
</script>
```

