# VcField Component

The `VcField` component is designed for displaying data in a read-only format with various presentation options. It's perfect for detail views, information displays, and data sheets where users need to view formatted information.

## Storybook

[VcField Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcfield--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcfield--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcField
    label="Customer Name"
    model-value="John Doe"
  />
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

## Props

| Prop             | Type                                        | Default     | Description                                     |
| ---------------- | ------------------------------------------- | ----------- | ----------------------------------------------- |
| `modelValue`     | `any`                                       | `undefined` | Content to display in the field                 |
| `label`          | `string`                                    | `undefined` | Label text for the field                        |
| `tooltip`        | `string`                                    | `undefined` | Tooltip text for additional information         |
| `type`           | `'text'` \| `'date'` \| `'date-ago'` \| `'link'` \| `'email'` | `'text'` | Type of field for formatting   |
| `copyable`       | `boolean`                                   | `false`     | Whether to show a copy button                   |
| `orientation`    | `'horizontal'` \| `'vertical'`              | `'vertical'`| Layout orientation of label and content         |
| `aspectRatio`    | `[number, number]`                          | `[1, 1]`    | Aspect ratio for label and content columns      |



## Examples

### Basic Text Field

```vue
<template>
  <VcField
    label="Customer Name"
    model-value="John Doe"
  />
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

### Different Field Types

```vue
<template>
  <div class="tw-space-y-4">
    <VcField
      label="Product Name"
      model-value="Premium Headphones"
      type="text"
    />
    
    <VcField
      label="Release Date"
      model-value="2023-05-15"
      type="date"
    />
    
    <VcField
      label="Last Updated"
      model-value="2023-08-29T14:30:00"
      type="date-ago"
    />
    
    <VcField
      label="Website"
      model-value="https://example.com"
      type="link"
    />
    
    <VcField
      label="Contact Email"
      model-value="support@example.com"
      type="email"
    />
  </div>
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

### Copyable Field

```vue
<template>
  <VcField
    label="Product ID"
    model-value="PROD-12345-XYZ"
    copyable
  />
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

### Horizontal Layout

```vue
<template>
  <VcField
    label="Status"
    model-value="Active"
    orientation="horizontal"
    :aspect-ratio="[1, 2]"
  />
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

### With Tooltip

```vue
<template>
  <VcField
    label="Tax ID"
    model-value="TAX-987654321"
    tooltip="The unique tax identifier for this organization"
    copyable
  />
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';
</script>
```

### Product Details Page Example

```vue
<template>
  <div class="tw-border tw-border-[var(--secondary-300)] tw-rounded-md tw-p-6">
    <h2 class="tw-text-xl tw-font-semibold tw-mb-4">Product Details</h2>
    
    <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 tw-gap-4">
      <VcField
        label="Product Name"
        :model-value="product.name"
      />
      
      <VcField
        label="Product ID"
        :model-value="product.id"
        copyable
      />
      
      <VcField
        label="Category"
        :model-value="product.category"
      />
      
      <VcField
        label="Price"
        :model-value="formatPrice(product.price, product.currency)"
      />
      
      <VcField
        label="Created Date"
        :model-value="product.createdDate"
        type="date"
      />
      
      <VcField
        label="Last Updated"
        :model-value="product.updatedDate"
        type="date-ago"
      />
      
      <VcField
        label="Manufacturer Website"
        :model-value="product.manufacturerWebsite"
        type="link"
      />
      
      <VcField
        label="Support Email"
        :model-value="product.supportEmail"
        type="email"
      />
    </div>
    
    <div class="tw-mt-6">
      <h3 class="tw-text-lg tw-font-medium tw-mb-2">Description</h3>
      <p class="tw-text-[var(--neutrals-700)]">{{ product.description }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcField } from '@vc-shell/framework';

const product = {
  id: 'PROD-12345',
  name: 'Premium Wireless Headphones',
  category: 'Electronics > Audio > Headphones',
  price: 199.99,
  currency: 'USD',
  createdDate: '2023-01-15',
  updatedDate: '2023-09-22T14:30:00',
  manufacturerWebsite: 'https://example.com',
  supportEmail: 'support@example.com',
  description: 'High-quality wireless headphones with noise cancellation, premium sound quality, and 24-hour battery life. Includes carrying case and charging cable.'
};

function formatPrice(price: number, currency: string) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency
  }).format(price);
}
</script>
```

### Customer Information Form

```vue
<template>
  <div class="tw-border tw-border-[var(--secondary-300)] tw-rounded-md tw-p-6">
    <div class="tw-flex tw-justify-between tw-items-center tw-mb-4">
      <h2 class="tw-text-xl tw-font-semibold">Customer Information</h2>
      <VcButton variant="secondary" icon="material-edit" @click="startEditing">
        Edit
      </VcButton>
    </div>
    
    <div v-if="isEditing">
      <!-- Edit form content -->
      <VcForm @submit.prevent="saveChanges">
        <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 tw-gap-4">
          <VcInput
            v-model="editedCustomer.firstName"
            label="First Name"
            required
          />
          
          <VcInput
            v-model="editedCustomer.lastName"
            label="Last Name"
            required
          />
          
          <VcInput
            v-model="editedCustomer.email"
            label="Email"
            type="email"
            required
          />
          
          <VcInput
            v-model="editedCustomer.phone"
            label="Phone"
          />
        </div>
        
        <div class="tw-mt-6 tw-flex tw-justify-end tw-space-x-2">
          <VcButton variant="secondary" @click="cancelEditing">
            Cancel
          </VcButton>
          <VcButton type="submit" variant="primary">
            Save Changes
          </VcButton>
        </div>
      </VcForm>
    </div>
    
    <div v-else>
      <!-- Read-only view -->
      <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 tw-gap-4">
        <VcField
          label="First Name"
          :model-value="customer.firstName"
        />
        
        <VcField
          label="Last Name"
          :model-value="customer.lastName"
        />
        
        <VcField
          label="Email"
          :model-value="customer.email"
          type="email"
          copyable
        />
        
        <VcField
          label="Phone"
          :model-value="customer.phone"
        />
        
        <VcField
          label="Customer Since"
          :model-value="customer.createdDate"
          type="date"
        />
        
        <VcField
          label="Last Purchase"
          :model-value="customer.lastPurchaseDate"
          type="date-ago"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue';
import { VcField, VcForm, VcInput, VcButton } from '@vc-shell/framework';

const isEditing = ref(false);

const customer = {
  firstName: 'Jane',
  lastName: 'Smith',
  email: 'jane.smith@example.com',
  phone: '+1 (555) 123-4567',
  createdDate: '2022-03-10',
  lastPurchaseDate: '2023-10-05T09:15:00'
};

const editedCustomer = reactive({ ...customer });

function startEditing() {
  Object.assign(editedCustomer, customer);
  isEditing.value = true;
}

function cancelEditing() {
  isEditing.value = false;
}

function saveChanges() {
  // Here you would save changes to the backend
  Object.assign(customer, editedCustomer);
  isEditing.value = false;
}
</script>
```
