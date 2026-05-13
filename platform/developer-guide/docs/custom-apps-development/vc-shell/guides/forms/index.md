# Forms

Recipes for the form layer inside a detail blade: layout, validation, dynamic properties, file upload, and unsaved-changes tracking. Each recipe is trimmed from the vendor-portal offers and orders modules.

## Prerequisites

Before wiring a form, make sure you have:

- A detail blade scaffolded. See [Blades guide](../blades/index.md).
- An API client for the resource you edit. See [API clients](../../concepts/api-clients.md).
- Familiarity with **VcForm** and **VcField**. See [VcForm reference](../../components/form/vc-form.md) and [VcField reference](../../components/form/vc-field.md).

## Recipe: VcForm with field rows

A blade detail view wraps its inputs in **VcForm** and groups them with **VcRow** and **VcCol** for multi-column layouts. **VcForm** itself renders a native form element with `novalidate`. It does not validate fields; that is delegated to vee-validate. Read-only fields use **VcField**, which formats values type-aware without the input chrome.

```vue title="pages/offer-details.vue (template fragment)"
<VcForm class="tw-space-y-4">
  <VcRow>
    <VcCol>
      <VcInput
        v-model="offer.name"
        :label="$t('OFFERS.PAGES.DETAILS.FIELDS.NAME.TITLE')"
        required
      />
    </VcCol>
  </VcRow>

  <VcRow>
    <VcCol>
      <VcField
        label="SKU"
        :model-value="offer.sku"
        copyable
      />
    </VcCol>
    <VcCol>
      <VcField
        label="Created"
        :model-value="offer.createdDate"
        type="date-ago"
      />
    </VcCol>
  </VcRow>
</VcForm>
```

`VcCol` accepts a `:size` prop (1 = full width, 2 = half width) to control column spans. Reach for **VcField** instead of a disabled **VcInput** whenever the value is read-only; it renders without focus rings or placeholders and supports type-aware formatting for date, date-ago, link, and email.

![Readmore](../../components/form/vc-form.md){: width="25"} VcForm full prop and event reference.

## Recipe: validation

Wrap each editable input in vee-validate's `Field` component. The `Field` tracks the value under `name`, applies `rules`, and exposes `errors`, `errorMessage`, and `handleChange` through its scoped slot. The inner input uses `v-model` for two-way binding and calls `handleChange` on every update so vee-validate stays in sync.

```vue title="pages/offer-details.vue (template fragment)"
<Field
  v-slot="{ errorMessage, handleChange, errors }"
  rules="required|min:3"
  :model-value="offer.sku"
  name="sku"
>
  <VcInput
    v-model="offer.sku"
    :label="$t('OFFERS.PAGES.DETAILS.FIELDS.SKU.TITLE')"
    required
    :error="!!errors.length"
    :error-message="errorMessage"
    @update:model-value="handleChange"
  />
</Field>
```

For server-side validation errors, pull `setFieldError` from `useBladeForm` and apply per-field messages returned by the API. The offers module debounces an async SKU uniqueness check through a custom `defineRule`:

```ts title="pages/offer-details.vue (script fragment)"
import { Field, defineRule } from "vee-validate";
import { useDebounceFn } from "@vueuse/core";

const debouncedSkuValidator = useDebounceFn(async (value: string) => {
  const errors = await validateOffer({ ...offer.value, sku: value });
  const skuErrors = errors?.filter((e) => e.propertyName?.toLowerCase() === "sku");
  if (skuErrors?.length) {
    return skuErrors.map((e) => t(`ERRORS.${e.errorCode}`, { value: e.attemptedValue })).join("\n");
  }
  return true;
}, 1000);

defineRule("validateSku", (value: string) => debouncedSkuValidator(value));
```

Apply the rule with `rules="required|min:3|validateSku"` on the corresponding `Field`. The composable returns `formMeta`, `setFieldError`, and `errorBag` if you need direct access to vee-validate state outside the toolbar.

## Recipe: dynamic properties

The Platform stores user-defined property values per object. **VcDynamicProperty** renders one property as the right input molecule based on `valueType`, `dictionary`, and `multivalue` flags. Pair it with `useDynamicProperties` to read and write property values without manual scaffolding. The composable exposes a strategy registry that handles regular, boolean, dictionary, measure, and color types, and cleans up empty value entries so `useBladeForm` does not report false modifications.

```vue title="components/PropertyGroupOffers.vue"
<template>
  <VcDynamicProperty
    v-for="property in properties"
    :key="property.id"
    :property="property"
    :model-value="getPropertyValue(property, currentLocale)"
    :options-getter="loadDictionaries"
    :measurements-getter="loadMeasurements"
    :current-language="currentLocale"
    :value-type="property.valueType ?? ''"
    :dictionary="property.dictionary"
    :multivalue="property.multivalue"
    :multilanguage="property.multilanguage"
    :required="property.required ?? false"
    :rules="{
      min: property.validationRule?.charCountMin,
      max: property.validationRule?.charCountMax,
      regex: property.validationRule?.regExp,
    }"
    :name="getPropertyDisplayName(property)"
    :disabled="disabled"
    @update:model-value="(ev) => setPropertyValue({ property, ...ev })"
  />
</template>

<script setup lang="ts">
import { useApiClient, useDynamicProperties } from "@vc-shell/framework";

const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

async function searchDictionaryItems(criteria) {
  const client = await getApiClient();
  const res = await client.searchPropertyDictionaryItems(criteria);
  return res.results;
}

async function searchMeasurementItems(measureId: string, locale?: string) {
  if (!measureId) return;
  const client = await getApiClient();
  const data = await client.getMeasureById(measureId, locale);
  return data.units;
}

const { loadDictionaries, getPropertyValue, setPropertyValue, loadMeasurements } = useDynamicProperties({
  searchDictionary: searchDictionaryItems,
  searchMeasurements: searchMeasurementItems,
});
</script>
```

`setPropertyValue` mutates the property in place because dynamic properties travel as part of a larger entity object saved as a whole. Always pass `dictionary` when setting dictionary values; without dictionary items, the composable cannot resolve `valueId` to the correct alias and localized values.

![Readmore](../../components/form/vc-dynamic-property.md){: width="25"} VcDynamicProperty full prop reference.

![Readmore](../../composables/forms/useDynamicProperties.md){: width="25"} useDynamicProperties API reference.

## Recipe: file upload

For multi-file image management with preview, reorder, and remove, use **VcGallery** paired with `useAssetsManager`. The composable owns the asset list, runs the upload against the Platform asset endpoint, and emits reorder and remove handlers wired to the gallery events. **VcFileUpload** is the lower-level drop zone for single-purpose uploads such as CSV import.

```vue title="pages/offer-details.vue (template fragment)"
<VcGallery
  :images="offer.images"
  :disabled="readonly"
  :loading="assetsLoading"
  multiple
  :label="$t('OFFERS.PAGES.DETAILS.FIELDS.GALLERY.TITLE')"
  @upload="assets.upload"
  @sort="assets.reorder"
  @remove="assets.remove"
/>
```

```ts title="pages/offer-details.vue (script fragment)"
import { useAssetsManager, usePopup } from "@vc-shell/framework";

const { showConfirmation } = usePopup();

const assets = useAssetsManager(
  computed({
    get: () => offer.value.images ?? [],
    set: (val) => {
      offer.value.images = val;
    },
  }),
  {
    uploadPath: () => `offers/${offer.value?.id ?? "new"}`,
    confirmRemove: () => showConfirmation(t("OFFERS.PAGES.ALERTS.IMAGE_DELETE_CONFIRMATION")),
  },
);
const assetsLoading = assets.loading;
```

For one-off uploads, **VcFileUpload** emits a `FileList` on the `upload` event after validation. Convert it with `Array.from(files)` before chaining array methods.

```vue title="One-shot CSV import"
<VcFileUpload
  accept=".csv"
  icon="lucide-file-spreadsheet"
  :loading="isImporting"
  :error-message="importError"
  @upload="importCsv"
/>
```

![Readmore](../../components/data-display/vc-gallery.md){: width="25"} VcGallery reference.

![Readmore](../../components/form/vc-file-upload.md){: width="25"} VcFileUpload reference.

![Readmore](../../composables/data/useAssetsManager.md){: width="25"} useAssetsManager API reference.

## Recipe: dirty tracking with useBladeForm

`useBladeForm` collapses `useForm`, modification tracking, browser unload guard, and blade close guard into one composable. Call `setBaseline()` after loading data; the composable snapshots that state as pristine and computes `isModified` against it on every deep change. The blade's close prompt fires only when `isModified.value` is true. Re-snapshot with `setBaseline()` after a successful save.

```ts title="pages/offer-details.vue (script fragment)"
import { useBladeForm } from "@vc-shell/framework";

const form = useBladeForm({
  data: offer,
  canSaveOverride: computed(() => !isSkuValidating.value),
  closeConfirmMessage: computed(() => t("OFFERS.PAGES.ALERTS.CLOSE_CONFIRMATION")),
});

onMounted(async () => {
  await loadOffer({ id: param.value });
  form.setBaseline();
});

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "save",
    title: t("TOOLBAR.SAVE"),
    icon: "lucide-save",
    disabled: computed(() => !form.canSave.value),
    async clickHandler() {
      await saveOffer(offer.value);
      form.setBaseline();
      callParent("reload");
    },
  },
]);
```

`canSave` already combines `isReady`, `formMeta.valid`, `isModified`, and `canSaveOverride`. Do not redo the conjunction in the toolbar. For a pre-filled new entity (for example, a new offer cloned from a template), call `markReady()` instead of `setBaseline()`. It marks the form as ready while keeping the setup-time snapshot, so the pre-fill counts as a real modification and the save button activates immediately.

The blade auto-injects modification state from `useBladeForm`, so you do not need to pass `:modified="..."` to **VcBlade** when the composable is in scope.

![Readmore](../../composables/forms/useBladeForm.md){: width="25"} useBladeForm API reference.

## Variations

| Variation | Change |
| --- | --- |
| Readonly blade. | Set `canSaveOverride` to a falsy ref and `autoBeforeClose` to `false`. |
| Custom revert handler. | Pass `onRevert: () => loadOffer({ id: param.value })` to reload from the server. |
| Tab-close guard disabled. | `autoBeforeUnload: false` on `useBladeForm`. |
| Disable browser validation. | Already off. **VcForm** renders `novalidate` and relies on vee-validate. |
| Multi-column row. | `<VcCol :size="2">` halves the row width per column. |
| Required boolean. | Render as **VcSwitch** and enforce in your save handler. The switch has no required indicator. |
| Non-validated toggle. | Bind directly with `v-model`; do not wrap **VcSwitch** or **VcCheckbox** in `Field`. |
| Per-field server error. | `form.setFieldError("fieldName", "Message")`. |

![Readmore](../../components/form/vc-input.md){: width="25"} VcInput reference for text, number, and date inputs.

![Readmore](../../components/form/vc-select.md){: width="25"} VcSelect reference for dropdowns.

![Readmore](../../components/form/vc-textarea.md){: width="25"} VcTextarea reference for multiline text.

![Readmore](../../composables/forms/useModificationTracker.md){: width="25"} useModificationTracker for standalone dirty tracking outside a blade.
