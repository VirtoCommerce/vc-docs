# Validation Plugin

The Validation Plugin provides form validation capabilities for VC-Shell applications. Built on top of [VeeValidate](https://vee-validate.logaretm.com/), it offers a comprehensive solution for validating user input with predefined rules, custom validations, and internationalization support.

Form validation is a critical part of any web application. The Validation Plugin simplifies this process by providing a declarative way to validate forms, display error messages, and manage validation state.

## Features

- **Built-in Rules**: Comes with a comprehensive set of validation rules from VeeValidate.
- **VC-Shell Custom Rules**: Includes additional rules specific to VC-Shell needs.
- **Custom Rules**: Support for defining application-specific validation rules.
- **i18n Integration**: Localized error messages across different languages.
- **Form State Management**: Tracks form validity, touched fields, and dirty state.
- **Async Validation**: Support for asynchronous validation rules (e.g., server-side checks).

## Available validation rules

The Validation Plugin includes all standard validation rules from [@vee-validate/rules](https://vee-validate.logaretm.com/v4/guide/global-validators) and custom rules provided by VC-Shell.

### Standard VeeValidate rules

| Rule             | Description                                                                 | Parameters Example (if any)          |
|------------------|-----------------------------------------------------------------------------|--------------------------------------|
| `alpha`          | Allows only alphabetic characters.                                          | `locale: 'en'` (optional)            |
| `alpha_dash`     | Allows alphabetic characters, numbers, dashes (-), or underscores (_).      | `locale: 'en'` (optional)            |
| `alpha_num`      | Allows only alphabetic characters or numbers.                               | `locale: 'en'` (optional)            |
| `alpha_spaces`   | Allows only alphabetic characters or spaces.                                | `locale: 'en'` (optional)            |
| `between`        | Requires a value to be between a minimum and maximum numeric value.         | `{ min: 1, max: 10 }` or `[1, 10]`   |
| `confirmed`      | Checks if a value matches another field's value (e.g., password confirmation). | `target: '@other_field_name'`        |
| `digits`         | Requires a specific number of digits.                                       | `{ length: 5 }` or `[5]`             |
| `dimensions`     | Validates the dimensions (width and height) of an image file.               | `{ width: 300, height: 200 }`        |
| `email`          | Validates email addresses.                                                  |                                      |
| `ext`            | Validates the extension of a file.                                          | `['jpg', 'png']`                     |
| `image`          | Validates if a file is an image (based on MIME type and extension).         |                                      |
| `integer`        | Validates integer values.                                                   |                                      |
| `is`             | Checks for exact value match with another value.                            | `{ other: 'some_value' }` or `['value']` |
| `is_not`         | Ensures value doesn't match another value.                                  | `{ other: 'some_value' }` or `['value']` |
| `length`         | Validates exact length of a string or array.                                | `{ length: 8 }` or `[8]`             |
| `max`            | Requires a maximum length for a string/array or a maximum numeric value.    | `{ length: 10 }` or `[10]` (for string/array) |
| `max_value`      | Requires a maximum numeric value.                                           | `{ max: 100 }` or `[100]`            |
| `mimes`          | Validates the MIME type of a file.                                          | `['image/jpeg', 'image/png']`        |
| `min`            | Requires a minimum length for a string/array or a minimum numeric value.    | `{ length: 5 }` or `[5]` (for string/array) |
| `min_value`      | Requires a minimum numeric value.                                           | `{ min: 0 }` or `[0]`                |
| `not_one_of`     | Ensures the value is not one of a list of specified values.                 | `['admin', 'root']`                  |
| `numeric`        | Allows only numeric values.                                                 |                                      |
| `one_of`         | Ensures the value is one of a list of specified values.                     | `['apple', 'banana', 'orange']`      |
| `regex`          | Validates against a regular expression.                                     | `{ regex: /^[A-Z]+$/ }` or `['^[A-Z]+$']` |
| `required`       | Requires a non-empty value.                                                 |                                      |
| `size`           | Validates the size of a file in kilobytes.                                  | `{ size: 2048 }` (for 2MB) or `[2048]` |
| `url`            | Validates URLs.                                                             | `pattern: undefined` (optional regex) |

!!! note
    For rules accepting a `locale` (like `alpha`, `alpha_dash`, etc.), if not provided, VeeValidate might use a default or try to infer it.*

### VC-Shell custom rules

These rules are defined in `framework/core/plugins/validation/rules.ts`.

| Rule            | Description                                                                 | Parameters Example                   |
|-----------------|-----------------------------------------------------------------------------|--------------------------------------|
| `mindimensions` | Checks if an image's dimensions (width and height) are not less than specified. | `[width, height]` e.g., `[640, 480]` |
| `fileWeight`    | Checks if a file's size does not exceed a given limit in kilobytes.         | `[sizeInKB]` e.g., `[1024]` (for 1MB) |
| `before`        | Checks if a date is before a specified target date.                         | `['targetDateString']` e.g. `['2025-01-01']` |
| `after`         | Checks if a date is after a specified target date.                          | `['targetDateString']` e.g. `['2023-12-31']` |
| `bigInt`        | Checks if a string value can be safely parsed as an integer.                |                                      |

## Usage

### Basic form validation

In VC-Shell applications, form validation is typically implemented using the VeeValidate's `Field` component along with the `useForm`, `useIsFormValid`, and `useIsFormDirty` composables:

```html
<template>
  <form @submit.prevent="onSubmit">
    <Field name="email" v-slot="{ field, errorMessage }">
      <VcInput
        v-bind="field"
        :error-message="errorMessage"
        label="Email"
      />
    </Field>
    
    <Field name="password" v-slot="{ field, errorMessage }">
      <VcInput
        v-bind="field"
        type="password"
        :error-message="errorMessage"
        label="Password"
      />
    </Field>
    
    <VcButton 
      type="submit" 
      :disabled="!isFormValid" 
      :loading="isSubmitting"
    >
      Sign In
    </VcButton>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Field, useForm, useIsFormValid, useIsFormDirty } from 'vee-validate';
import { VcInput, VcButton } from '@vc-shell/framework';

// Initialize form with validation disabled on mount
useForm({
  validateOnMount: false
});

// Get form validity state
const isFormValid = useIsFormValid();
const isDirty = useIsFormDirty();
const isSubmitting = ref(false);

// Form submission handler
const onSubmit = async () => {
  isSubmitting.value = true;
  try {
    // Submit form logic
    await submitFormData();
  } catch (error) {
    // Handle error
  } finally {
    isSubmitting.value = false;
  }
};
</script>
```

### Use validation with VC-Shell components

VC-Shell form components accept validation rules directly as props:

```html
<template>
  <VcInput
    v-model="formData.name"
    name="name"
    rules="required"
    label="Product Name"
  />
  
  <VcInput
    v-model="formData.email"
    name="email"
    rules="required|email"
    label="Email Address"
  />
  
  <VcInput
    v-model.number="formData.price"
    name="price"
    rules="required|numeric|min_value:0"
    label="Price"
  />
  
  <VcCheckbox
    v-model="formData.isActive"
    name="isActive"
    label="Active"
  />
</template>
```

### Form validation with field component

Using the VeeValidate `Field` component for more control over validation:

```html
<template>
  <Field name="productName" v-slot="{ field, errorMessage }">
    <VcInput
      v-bind="field"
      :error-message="errorMessage"
      label="Product Name"
    />
  </Field>
</template>

<script setup lang="ts">
import { Field } from 'vee-validate';
import { VcInput } from '@vc-shell/framework';
</script>
```

### Form validation state management

Use the validation state composables to manage form validity:

```typescript
import { useForm, useIsFormValid, useIsFormDirty } from 'vee-validate';

export default {
  setup() {
    // Initialize form with validation disabled on mount
    const { setFieldError, validateField } = useForm({
      validateOnMount: false
    });
    
    // Get form validity state
    const isFormValid = useIsFormValid();
    const isDirty = useIsFormDirty();
    
    // Manual validation
    const validateForm = async () => {
      await validateField('email');
      // Handle validation result
    };
    
    // Set field error manually
    const setError = () => {
      setFieldError('email', 'This email is already in use');
    };
    
    return {
      isFormValid,
      isDirty,
      validateForm,
      setError
    };
  }
};
```

### Custom validation rules

You can define custom validation rules:

```typescript
import { defineRule } from 'vee-validate';
import { i18n } from '@vc-shell/framework';

// Define a custom validation rule
defineRule('product_sku', (value) => {
  // SKU pattern validation
  if (!/^[A-Z0-9-]{5,20}$/.test(value)) {
    return i18n.global.t('validation.product_sku');
  }
  
  return true;
});
```

## Best practices

* **Initialize forms with `validateOnMount: false`**: In VC-Shell applications, it's standard practice to disable validation on mount to prevent showing validation errors before user interaction.
* **Use field component for complex scenarios**: For more control over validation display, use the `Field` component with scoped slots.
* **Check form state**: Use `useIsFormValid` and `useIsFormDirty` composables to track form validity and changes.
* **Consistent error messages**: Maintain consistent error message style and wording across your application.
* **Server validation**: Always implement server-side validation as well, since client-side validation can be bypassed.
* **Custom error display**: Customize error message display to match your application's design system.
* **Form reset**: Implement proper form reset functionality to clear validation state along with field values.

## Related resources

- [VeeValidate Documentation](https://vee-validate.logaretm.com/)
- [How-To: Implementing Form Validation in Blades](../Usage-Guides/implementing-form-validation-in-blades.md)
- [i18n Plugin](./i18n.md)
- [VcForm component](../ui-components/vc-form.md)
- [VcInput component](../ui-components/vc-input.md) 
