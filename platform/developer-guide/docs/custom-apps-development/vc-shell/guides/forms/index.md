# Forms

Recipes for the form layer inside a detail blade: layout, validation, dynamic properties, file upload, and unsaved-changes tracking.

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

- [VcForm full prop and event reference.](../../components/form/vc-form.md)

## Recipe: validation

VC-Shell uses **vee-validate v4** as its validation engine. The framework auto-registers every standard rule from `@vee-validate/rules` plus a handful of custom rules — you do not import them per file. Wrap each editable input in `Field`, apply rules through the `rules` prop, and bind the validation state to the input via the scoped slot.

### Wrap an input in Field

```vue title="pages/offer-details.vue (template fragment)"
<Field
  v-slot="{ errorMessage, handleChange, errors }"
  :model-value="offer.name"
  name="name"
  rules="required"
>
  <VcInput
    v-model="offer.name"
    :label="$t('OFFERS.PAGES.DETAILS.FIELDS.NAME.TITLE')"
    required
    :error="!!errors.length"
    :error-message="errorMessage"
    @update:model-value="handleChange"
  />
</Field>
```

The slot props are the contract:

- `errors` — array of error messages for the current field; bind to the input's `error` (boolean) prop.
- `errorMessage` — first error message; bind to the input's `error-message` prop.
- `handleChange` — call from `@update:model-value` so vee-validate sees every keystroke.
- `field` (also available) — a pre-built object combining `value`, `onInput`, `onBlur`. Use `v-bind="field"` as a shortcut when the input has a stable contract; the offers module uses the explicit form above to mix `v-model` with extra handlers.

`name` must match how you address the field elsewhere (server error mapping, `setFieldError(name, ...)`). It is not the label.

### Built-in rules (no imports needed)

The framework registers the full set from `@vee-validate/rules` at bootstrap, plus VC-Shell-specific rules. Compose them with pipes:

```vue
<Field name="email"    rules="required|email" v-slot="{ ... }">...</Field>
<Field name="username" rules="required|min:3|max:50" v-slot="{ ... }">...</Field>
<Field name="age"      rules="required|numeric|between:18,120" v-slot="{ ... }">...</Field>
<Field name="sku"      rules="required|alpha_dash|min:3|max:64" v-slot="{ ... }">...</Field>
<Field name="logo"     rules="mindimensions:200,200|fileWeight:500" v-slot="{ ... }">...</Field>
<Field name="endDate"  :rules="endDateRules" v-slot="{ ... }">...</Field>
```

Common pre-registered names: `required`, `email`, `numeric`, `integer`, `min`, `max`, `between`, `length`, `alpha`, `alpha_num`, `alpha_dash`, `regex`, `confirmed`, `url`, `is`, `is_not`, `one_of`. VC-Shell adds `mindimensions:W,H`, `fileWeight:KB`, `before:date`, `after:date`, `bigint`.

For the full surface (parameters, custom messages via i18n, file-upload caveats) see the [validation plugin reference](../../plugins/validation.md).

### Reactive rule parameters

When a rule depends on another field's value, drive the rules string from a `computed`:

```ts
const startDate = ref("2024-01-01");
const endDateRules = computed(() => `required|after:${startDate.value}`);
```

The `Field` will revalidate `endDate` automatically whenever `startDate` changes.

### Custom rule with async server validation

When the server is the source of truth (uniqueness checks, business-rule validation), register a custom rule that calls the API. Debounce so each keystroke does not hit the server, and gate **Save** until the in-flight check resolves:

```vue title="pages/offer-details.vue (script fragment)"
<script setup lang="ts">
import { ref, computed } from "vue";
import { Field, defineRule } from "vee-validate";
import { useDebounceFn } from "@vueuse/core";
import { useBladeForm } from "@vc-shell/framework";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const { offer, validateOffer } = useOffer();
const isSkuValidating = ref(false);

const form = useBladeForm({
  data: offer,
  // Block Save while the async rule is in flight.
  canSaveOverride: computed(() => !isSkuValidating.value),
});

const debouncedSkuValidator = useDebounceFn(async (value: string) => {
  isSkuValidating.value = true;
  try {
    const failures = await validateOffer({ ...offer.value, sku: value });
    const skuFailures = failures?.filter((e) => e.propertyName?.toLowerCase() === "sku");
    if (skuFailures?.length) {
      // Map each ValidationFailure to a localized message under a known prefix.
      return skuFailures
        .map((e) => t(`OFFERS.PAGES.DETAILS.ERRORS.${e.errorCode}`, { value: e.attemptedValue }))
        .join("\n");
    }
    return true;
  } finally {
    isSkuValidating.value = false;
  }
}, 1000);

defineRule("validateSku", (value: string) => debouncedSkuValidator(value));
</script>
```

Then chain it after the synchronous rules:

```vue
<Field
  v-slot="{ errorMessage, handleChange, errors }"
  :model-value="offer.sku"
  name="sku"
  rules="required|min:3|validateSku"
>
  <VcInput
    v-model="offer.sku"
    :label="$t('OFFERS.PAGES.DETAILS.FIELDS.SKU.TITLE')"
    required
    :loading="isSkuValidating"
    :error="!!errors.length"
    :error-message="errorMessage"
    @update:model-value="handleChange"
  />
</Field>
```

Three points hold this pattern together:

- **Returning `true` means valid.** Returning a string means invalid; vee-validate uses the string as the error message. The custom rule above merges multiple `ValidationFailure` entries with `\n`.
- **Per-error-code i18n keys.** The server returns `errorCode` per failure; the rule maps it to a translation key (`OFFERS.PAGES.DETAILS.ERRORS.{errorCode}`). New error codes need new translation keys — they do not auto-localize.
- **`canSaveOverride`** keeps the toolbar **Save** button disabled while `isSkuValidating` is true. Without it, a fast typist can submit before the debounced check returns.

### Inspecting form state

`useBladeForm` exposes the underlying vee-validate primitives. Use them when the toolbar needs to react to form-level state or when you map server errors back into the form after a failed save:

```ts
const form = useBladeForm({ data: offer });
// form.formMeta.value.valid — true when every field passes its rules
// form.formMeta.value.dirty — true when any field has been touched
// form.setFieldError("sku", "Already taken")  — push a field-level error from outside
// form.errorBag.value — { fieldName: string[] } of every active error
```

A typical save handler maps server `ValidationFailure[]` to per-field errors after submit:

```ts
async function onSave() {
  const failures = await saveOffer(offer.value);
  if (failures?.length) {
    for (const failure of failures) {
      form.setFieldError(failure.propertyName, t(`OFFERS.PAGES.DETAILS.ERRORS.${failure.errorCode}`));
    }
  }
}
```

`canSave` already combines `formMeta.valid` with the other gates — you do not need to call it from the toolbar yourself; just bind the toolbar button's `disabled` to `!form.canSave.value`.

- [Validation plugin reference — full rule list and i18n keys.](../../plugins/validation.md)
- [useBladeForm reference.](../../composables/forms/useBladeForm.md)
- [vee-validate v4 docs.](https://vee-validate.logaretm.com/v4/)

## Recipe: dynamic properties

The Platform stores user-defined property values per object. **VcDynamicProperty** renders one property as the right input molecule based on `valueType`, `dictionary`, and `multivalue` flags. Pair it with `useDynamicProperties` to read and write property values without manual scaffolding. The composable exposes a strategy registry that handles regular, boolean, dictionary, measure, and color types, and cleans up empty value entries so `useBladeForm` does not report false modifications.

```vue title="components/PropertyGroup.vue"
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
import { CatalogClient } from "../../../api_client/catalog";

const { getApiClient } = useApiClient(CatalogClient);

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

- [VcDynamicProperty full prop reference.](../../components/form/vc-dynamic-property.md)

- [useDynamicProperties API reference.](../../composables/forms/useDynamicProperties.md)

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

- [VcGallery reference.](../../components/data-display/vc-gallery.md)

- [VcFileUpload reference.](../../components/form/vc-file-upload.md)

- [useAssetsManager API reference.](../../composables/data/useAssetsManager.md)

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

- [useBladeForm API reference.](../../composables/forms/useBladeForm.md)

## Recipe: multilanguage fields

When a single entity stores its content per language (`names: { "en-US": "...", "de-DE": "..." }`), the form lets the user switch the editing language without leaving the blade. This is separate from the UI locale switcher in the user menu — that one changes app labels; this one changes which language version of the entity's data the form binds to.

The pieces are:

- **VcLanguageSelector** — a compact flag-button dropdown placed in the blade's `#actions` slot.
- A `currentLocale` ref shared across the blade's fields.
- A writable `computed` per multilingual field that reads and writes through `currentLocale`.

```vue title="pages/offer-details.vue"
<script setup lang="ts">
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";
import { VcLanguageSelector, useBladeForm, useLanguages } from "@vc-shell/framework";

const { t } = useI18n();
const { item, loadItem, saveItem } = useOfferDetails();
const { getLocaleByTag, getFlag } = useLanguages();

const form = useBladeForm({
  data: item,
  closeConfirmMessage: computed(() => t("OFFERS.UNSAVED_CHANGES")),
});

const supportedLocales = ref<{ value: string; label: string; flag?: string }[]>([]);
const currentLocale = ref("en-US");
const isMultilanguage = computed(() => supportedLocales.value.length > 1);

async function loadLocales() {
  const tags = await fetchSupportedLocales();
  supportedLocales.value = await Promise.all(
    tags.map(async (tag) => ({
      value: tag,
      label: getLocaleByTag(tag) ?? tag,
      flag: await getFlag(tag),
    })),
  );
}

loadLocales();

const localizedName = computed({
  get: () => item.value?.names?.[currentLocale.value] ?? "",
  set: (value) => {
    if (!item.value) return;
    item.value.names ??= {};
    item.value.names[currentLocale.value] = value;
  },
});
</script>

<template>
  <VcBlade :title="t('OFFERS.PAGES.DETAILS.TITLE')">
    <template #actions>
      <VcLanguageSelector
        v-if="isMultilanguage"
        v-model="currentLocale"
        :options="supportedLocales"
      />
    </template>

    <VcForm class="tw-space-y-4">
      <VcInput
        v-model="localizedName"
        :label="t('OFFERS.PAGES.DETAILS.FIELDS.NAME')"
        multilanguage
        :current-language="currentLocale"
        required
      />
    </VcForm>
  </VcBlade>
</template>
```

`VcInput` and `VcEditor` accept `multilanguage` plus `:current-language` to render the active locale as a small badge on the field label. The components do not switch the underlying value; the writable `computed` above does. Reach for `useLanguages()` for `getLocaleByTag` (display name) and `getFlag` (async flag URL) so the selector renders flags consistently with the user-area language picker.

Hide the selector when only one locale is available — a one-option dropdown is noise. When the entity has no value for the current locale yet, the `??` fallback shows an empty field, which is the right cue for the user to type.

- [VcLanguageSelector reference.](../../components/form/multilanguage-selector.md)
- [useLanguages reference.](../../composables/user/useLanguages.md)

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

- [VcInput reference for text, number, and date inputs.](../../components/form/vc-input.md)

- [VcSelect reference for dropdowns.](../../components/form/vc-select.md)

- [VcTextarea reference for multiline text.](../../components/form/vc-textarea.md)

- [useModificationTracker for standalone dirty tracking outside a blade.](../../composables/forms/useModificationTracker.md)
