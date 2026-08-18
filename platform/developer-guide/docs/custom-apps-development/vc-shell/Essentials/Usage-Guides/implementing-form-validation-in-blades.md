# How-To: Implementing Form Validation in Blades

This guide provides a practical walkthrough on implementing robust form validation within VC-Shell blades using VeeValidate, integrated with VC-Shell's UI components.

## Prerequisites

-   Understanding of Vue 3 Composition API.
-   Familiarity with VeeValidate v4 (specifically `useForm`, `Field`, and defining validation rules as strings, functions, or objects).
-   Knowledge of VC-Shell's blade system and UI components like `VcInput`, `VcSelect`, `VcButton`, `VcBlade`.
-   Refer to the [Validation Plugin documentation](../plugins/validation.md) for a comprehensive list of available pre-defined validation rules (both standard and VC-Shell custom) and setup details.
-   The `framework/core/plugins/validation/rules.ts` file also lists all VC-Shell custom rules and shows how standard rules are registered.

## Core Concepts in Blade Validation

Key aspects include:

-   Defining validation rules for individual fields using the `Field` component, primarily with string-based rules (e.g., `"required|email"`), custom rule functions, or object-based syntax (e.g., `:rules="{ required: true, min: 5 }"`).
-   Binding UI components to a local reactive state (`formData`).
-   Synchronizing local state changes with VeeValidate using `handleChange`.
-   Managing the overall form state (validity, dirtiness).
-   Handling form submission and potentially server-side validation feedback.
-   Integrating validation state with blade controls.

## Step-by-Step Implementation Example

Let's consider a blade for creating or editing a "Product" entity.

### 1. Setting up the Blade and Form Structure

```vue
// MyProductBlade.vue
<template>
  <VcBlade
    ref="bladeRef"
    :title="isNewProduct ? 'Create Product' : 'Edit Product'"
    :toolbar-items="bladeToolbar"
    @close="onCloseBlade"
  >
    <VcForm class="p-5 space-y-4" @submit.prevent="onSubmitForm">
      <!-- Product Name Field -->
      <Field
        name="name"
        v-slot="{ errors, handleChange }"
        :rules="{ required: true, min: 3 }"  // Object-based rules
        :model-value="formData.name"
      >
        <VcInput
          :model-value="formData.name"
          label="Product Name"
          required
          :error-message="errors[0]"
          @update:model-value="(value) => {
            formData.name = String(value);
            handleChange(value);
          }"
        />
      </Field>

      <!-- SKU Field -->
      <Field
        name="sku"
        v-slot="{ errors, handleChange }"
        rules="required|skuFormat" // String-based: Assuming 'skuFormat' is a globally defined custom rule
        :model-value="formData.sku"
      >
        <VcInput
          :model-value="formData.sku"
          label="SKU"
          required
          :error-message="errors[0]"
          @update:model-value="(value) => {
            formData.sku = String(value);
            handleChange(value);
          }"
        />
      </Field>

      <!-- Price Field -->
      <Field
        name="price"
        v-slot="{ errors, handleChange }"
        :rules="{ required: true, numeric: true, min_value: 0.01 }" // Object-based rules for clarity
        :model-value="formData.price"
      >
        <VcInput
          type="number"
          :model-value="formData.price"
          label="Price"
          required
          :error-message="errors[0]"
          @update:model-value="(value) => {
            const numValue = value === null || value === '' ? null : Number(value);
            formData.price = numValue;
            handleChange(numValue === null ? undefined : numValue); // Pass undefined for VeeValidate if null to clear, or the number
          }"
        />
      </Field>

      <!-- isActive Checkbox -->
      <Field
        name="isActive"
        v-slot="{ handleChange }" // Errors not typically shown for a standalone checkbox this way
        :model-value="formData.isActive"
        rules="boolean" // Optional: ensure it's a boolean if needed by backend
      >
        <VcCheckbox
          :model-value="formData.isActive"
          label="Product is Active"
          @update:model-value="(value: boolean) => {
            formData.isActive = value;
            handleChange(value);
          }"
        />
      </Field>
    </VcForm>
  </VcBlade>
</template>

<script setup lang="ts">
import { ref, computed, reactive, watch } from "vue";
import { Field, useForm, defineRule } from "vee-validate"; // defineRule for custom inline or setup rules
import {
  VcInput,
  VcCheckbox,
  VcBlade,
  VcForm,
  useModificationTracker,
  type IBladeToolbarItem,
} from "@vc-shell/framework";

// Example of defining a custom rule locally or in a setup script if not global
// For global rules, this would be in a plugin or rules.ts
// defineRule('skuFormat', (value: string) => {
//   if (!value) return true; // Handled by 'required' rule if present
//   if (!/^[A-Z0-9-]+$/.test(value)) return "SKU can only contain uppercase letters, numbers, and hyphens.";
//   return true;
// });
// Note: 'skuFormat' rule used in the template is assumed to be globally registered
// (e.g. in @vc-shell/framework) or defined as above for local use.
// For this example, we assume 'skuFormat' is available globally for cleaner template.

interface ProductForm {
  id?: string;
  name: string;
  sku: string;
  price: number | null;
  isActive: boolean;
}

export interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "close:blade"): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
}

const props = defineProps<{
  productData?: ProductForm;
}>();

const emit = defineEmits<Emits>();

const bladeRef = ref<InstanceType<typeof VcBlade>>();
const isSubmitting = ref(false);

const isNewProduct = computed(() => !props.productData?.id);

const defaultFormValues: ProductForm = {
  name: "",
  sku: "",
  price: null,
  isActive: true,
};

// formData is now the source of truth for the modification tracker
const formData = reactive<ProductForm>({
  ...defaultFormValues,
  id: props.productData?.id,
  ...(props.productData || {}),
});

// VeeValidate for validation state
const { handleSubmit, setValues, setFieldError, resetForm, meta } = useForm<ProductForm>({
  initialValues: { ...formData },
  validateOnMount: false,
});

// useModificationTracker for deep change detection
const {
  currentValue: form,
  isModified,
  resetModificationState,
} = useModificationTracker(formData);

watch(
  () => props.productData,
  (newData) => {
    if (newData) {
      const newValues = { ...defaultFormValues, ...newData };
      Object.assign(formData, newValues);
      // Synchronize both VeeValidate and useModificationTracker
      setValues(newValues, false);
      resetModificationState(newValues);
    }
  },
  { immediate: true, deep: true },
);

const isFormValid = computed(() => meta.value.valid);
// VeeValidate's `dirty` flag is also useful, but `isModified` from useModificationTracker
// provides more robust deep checking, especially for asynchronously loaded initial data.
// See the useModificationTracker documentation for more details.

const bladeToolbar = computed<IBladeToolbarItem[]>(() => [
  {
    id: "save",
    title: "Save",
    icon: "material-save",
    variant: "primary",
    // Button is enabled only if the form is valid AND data has been modified.
    disabled: !isFormValid.value || !isModified.value || isSubmitting.value,
    loading: isSubmitting.value,
    onClick: () => onSubmitForm(),
  },
  {
    id: "cancel",
    title: "Cancel",
    icon: "material-close",
    onClick: () => onCloseBlade(),
  },
]);

const onSubmitForm = handleSubmit(async (validatedValues) => {
  isSubmitting.value = true;
  try {
    const payload: ProductForm = { ...form.value, id: props.productData?.id };
    await new Promise((resolve) => setTimeout(resolve, 1000));
    console.log("Form submitted successfully with payload:", payload);

    // After successful submission, reset both the form and the modification state.
    resetForm({ values: { ...defaultFormValues, ...payload } });
    resetModificationState({ ...defaultFormValues, ...payload });

    bladeRef.value?.close();
  } catch (error) {
    console.error("Form submission error:", error);
  } finally {
    isSubmitting.value = false;
  }
});

const onCloseBlade = () => {
  emit("close:blade");
};

const handleReset = () => {
  const resetValues = { ...defaultFormValues, ...props.productData };
  resetForm({ values: resetValues });
  resetModificationState(resetValues);
};

defineExpose({
  submit: onSubmitForm,
  reset: handleReset,
});

</script>
```

### 2. Key Validation Concepts Applied

*   **Ways to Define Rules**: The `rules` prop on the `Field` component can accept rules in several formats:
    *   **Strings**: e.g., `rules="required|min:3"`. This is concise for common cases.
    *   **Objects**: e.g., `:rules="{ required: true, min: 3 }"`. This can be clearer for rules with parameters or when listing multiple rules. Parameters for rules are passed as the value (e.g., `{ min: 3 }`). For rules that are just flags (like `required`), `true` can be used as the value.
    *   **Functions**: For complex, field-specific logic not covered by global rules.
    These rules are either standard VeeValidate rules or custom ones globally defined. The `skuFormat` rule (used as a string in the example) must be globally registered or defined locally to work.
*   **Local Reactive `formData`**: `VcInput` and other form components are bound to this local state.
*   **`@update:model-value` and `handleChange`**: This synchronization mechanism remains crucial. When `formData` changes, `handleChange` informs VeeValidate.
*   **Flexibility with Rules**: While string rules are common, you can still define complex validation logic as a function and pass it to the `rules` prop of a `Field` component if a specific field requires highly custom validation not covered by existing global rules.
    ```typescript
    // Example of a complex function rule for a specific field
    // const validateComplexField = (value) => {
    //   if (!value || value.length < 10) return "This field needs more complex criteria.";
    //   // ... more logic
    //   return true;
    // };
    ```
    And in the template:
    ```html
    // <Field name="complexField" :rules="validateComplexField" ... />
    ```
*   **Controlling UI State with `useModificationTracker`**: While VeeValidate provides a `meta.dirty` flag, the `useModificationTracker` composable offers more robust deep-checking for complex objects and handles asynchronously loaded initial data more predictably. It is the recommended way to track if data has actually changed. You can then combine its `isModified` flag with VeeValidate's `meta.valid` to control the state of save buttons, as shown in the example.
*   **Toolbar Button State**: Control `disabled` state of save buttons using `isFormValid`, `isModified` (from `useModificationTracker`), and `isSubmitting`.
*   **Data Flow**: UI component updates local state -> `handleChange` updates VeeValidate for validation -> `useModificationTracker` independently tracks deep changes against the original state.
*   **Server-Side Validation**: Always re-validate on the server.
*   **Form Reset**: To fully reset the state, you must reset both VeeValidate (`resetForm`) and the modification tracker (`resetModificationState`).

This revised guide now emphasizes the primary use of string-based and object-based rules with `Field` components, aligning more closely with common VeeValidate practices and the existing VC-Shell validation infrastructure, while still allowing for function-based rules for custom scenarios.

## Related Resources

-   [Usage Guide: Tracking Data Changes with `useModificationTracker`](../composables/useModificationTracker.md)
-   [Validation Plugin Documentation](../plugins/validation.md) (Lists available rules and setup)
-   [VeeValidate v4 Documentation](https://vee-validate.logaretm.com/v4/)
