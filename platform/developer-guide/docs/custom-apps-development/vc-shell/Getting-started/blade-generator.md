# Blade Generator

The VC Shell CLI includes a powerful blade generator that helps you quickly create modules, blades, and widgets with proper architecture and best practices. This tool eliminates boilerplate code and ensures consistency across your application.

## Overview

The blade generator (`create-vc-app blade`) creates:

- **Complete Modules**: Full module structure with blades, composables, and locales
- **Blade Components**: Grid (list) or Details (form) views with full functionality
- **Composables**: Business logic with `useAsync`, `useApiClient`, and `useModificationTracker`
- **Widgets**: Optional widget components for blade integration
- **Localization**: i18n keys following framework conventions
- **Automatic Registration**: Modules in `main.ts`, blades in `pages/index.ts`, widgets in parent blades
- **Automatic Formatting**: All generated code is formatted with Prettier

## Installation

The blade generator is included in `@vc-shell/create-vc-app`:

```bash
npm install -g @vc-shell/create-vc-app
# or use npx directly
npx create-vc-app blade --help
```

## Quick Start

### Interactive Mode

Run the generator without arguments for an interactive wizard:

```bash
npx create-vc-app blade
```

The wizard will guide you through creating:

1. **New Module**: Complete module with Grid and/or Details blades
2. **New Blade**: Add a blade to an existing module
3. **New Widget**: Add a widget to an existing blade

### Non-Interactive Mode

Specify all options via command-line arguments for automation:

```bash
# Generate a complete module
npx create-vc-app blade \
  --module products \
  --type grid \
  --name products \
  --composable \
  --locales \
  --is-workspace

# Add a details blade to existing module
npx create-vc-app blade \
  --module products \
  --type details \
  --name product-details \
  --composable \
  --locales

# Generate a widget
npx create-vc-app blade --widget
```

## Creating a New Module

### Interactive Workflow

```bash
npx create-vc-app blade
# Select: "Module (with blades)"
```

You'll be prompted for:

- **Module name**: e.g., `products`, `orders` (kebab-case)
- **Entity name**: e.g., `Product`, `Order` (PascalCase)
- **Create both blades**: Generate both Grid and Details blades
- **Workspace blade**: Which blade should be the main module blade
- **Customize form fields**: Interactive form builder for Details blade

### What Gets Created

```
src/modules/products/
├── pages/
│   ├── index.ts                    # Blade exports
│   ├── products.vue                # Grid blade (list view)
│   └── product-details.vue         # Details blade (form view)
├── composables/
│   ├── index.ts                    # Composable exports
│   ├── useProductList.ts           # Grid blade logic
│   └── useProductDetails.ts        # Details blade logic
├── locales/
│   ├── index.ts                    # Locale exports
│   └── en.json                     # English translations
├── components/
│   └── widgets/                    # Widget components
│       └── index.ts
└── index.ts                        # Module definition
```

### Automatic Actions

The generator automatically:

1. ✅ Creates complete module structure
2. ✅ Registers module in `src/main.ts`
3. ✅ Registers blades in `pages/index.ts`
4. ✅ Formats all files with Prettier
5. ✅ Adds TODO comments for API integration

## Grid Blade (List View)

Grid blades are for displaying lists of items with:

- **Search & Filters**: Staged/applied filter architecture
- **Data Table**: VcTable with columns, sorting, pagination
- **Toolbar**: Actions like "Add", "Refresh", "Delete"
- **Composable**: `useList` with async data loading

### Example Generated Code

```typescript
// useProductList.ts
export const useProductList = (args: UseListArgs) => {
  const { load, loading, items } = useAsync(async () => {
    // TODO: Replace with your API client
    const response = await fetch('/api/products');
    return response.json();
  });

  // Staged filters
  const appliedFilters = ref({});
  const stagedFilters = ref({});

  // Apply filters
  const applyFilters = () => {
    appliedFilters.value = { ...stagedFilters.value };
    load();
  };

  return {
    load,
    loading,
    items,
    appliedFilters,
    stagedFilters,
    applyFilters,
  };
};
```

## Details Blade (Form View)

Details blades are for viewing/editing individual items with:

- **Form Fields**: VcInput, VcSelect, VcEditor, VcSwitch, etc.
- **Validation**: vee-validate integration
- **Modification Tracking**: Detects unsaved changes
- **Toolbar**: Save, Cancel, Delete actions
- **Composable**: `useDetails` with modification tracker

### Interactive Form Builder

When creating a Details blade, you can customize form fields interactively:

```bash
npx create-vc-app blade
# Select: "Module (with blades)"
# Choose: "Customize form fields interactively? › yes"
```

You'll be able to add fields with:

- **Field name**: Property name (e.g., `price`, `description`)
- **Field type**: Component type (see below)
- **Required**: Validation requirement

### Supported Form Components

| Component | Type | Use Case | Props |
|-----------|------|----------|-------|
| **VcInput** | `text`, `number`, `date` | Basic text input | `type`, `placeholder`, `required` |
| **VcTextarea** | `textarea` | Multi-line text | `rows`, `placeholder` |
| **VcSelect** | `select` | Dropdown selection | `options` (comma-separated) |
| **VcEditor** | `editor` | Rich text editor | `placeholder` |
| **VcSwitch** | `switch` | Toggle/Boolean | `label` |
| **VcGallery** | `gallery` | Image gallery | Includes `useAssets` composable |
| **VcInputCurrency** | `currency` | Money input | `currency-code` |
| **VcRadioButton** | `radio` | Radio group | `options` (comma-separated) |
| **VcCheckbox** | `checkbox` | Checkbox | `label` |
| **VcMultivalue** | `multivalue` | Multiple values | `placeholder` |
| **VcField** | `field` | Read-only display | `label`, `orientation` |

### Non-Interactive Form Fields (JSON)

You can provide form fields as JSON for automation:

```bash
npx create-vc-app my-app \
  --skip-form-editor \
  --form-fields '[
    {"name":"title","type":"text","required":true},
    {"name":"price","type":"currency","required":true},
    {"name":"description","type":"editor","required":false},
    {"name":"category","type":"select","required":true,"options":"Electronics,Clothing,Books"},
    {"name":"inStock","type":"switch","required":true},
    {"name":"images","type":"gallery","required":false}
  ]'
```

### VcGallery Special Handling

When you add a `VcGallery` field, the generator automatically includes:

```typescript
import { useAssets } from "@vc-shell/framework";
import type { ICommonAsset } from "@vc-shell/api-client";

// Assets handler
const assetsHandler = computed<ICommonAsset[]>({
  get: () => item.value.images || [],
  set: (files) => {
    item.value.images = files;
  },
});

// Gallery edit handler
const onGalleryItemEdit = (files: ICommonAsset[]) => {
  // TODO: Implement asset editing logic
};
```

## Widgets

Widgets are reusable components that can be added to blades for displaying additional information or actions.

### Creating a Widget

#### Interactive Mode

```bash
npx create-vc-app blade --widget
```

You'll be prompted for:

- **Module**: Select target module
- **Blade**: Select parent blade
- **Widget name**: e.g., `ProductStats`, `OrderSummary`

#### What Gets Created

```
src/modules/products/components/widgets/
└── product-stats/
    └── product-stats-widget.vue
```

### Automatic Widget Registration

The generator automatically:

1. ✅ Creates widget component
2. ✅ Imports widget in parent blade
3. ✅ Adds `useWidgets`, `useBlade`, `onBeforeUnmount` imports
4. ✅ Registers widget with `registerWidget()`
5. ✅ Unregisters widget in `onBeforeUnmount()`
6. ✅ Adds widget locales to module's `en.json`

### Widget Template

Widgets use only the `VcWidget` component with its props. No custom content inside:

```vue
<template>
  <VcWidget
    :value="count"
    :title="$t('PRODUCTS.WIDGETS.PRODUCT_STATS.TITLE')"
    icon="material-shoppingmode"
    @click="clickHandler"
  >
  </VcWidget>
</template>

<script setup lang="ts">
import { VcWidget, useBladeNavigation } from "@vc-shell/framework";
import { ref } from "vue";

const props = defineProps<{
  item: any; // Your entity type
}>();

const { openBlade, resolveBladeByName } = useBladeNavigation();
const widgetOpened = ref(false);
const count = ref(0);

function clickHandler() {
  if (!widgetOpened.value) {
    openBlade({
      blade: resolveBladeByName("ProductStatsList"),
      options: {
        productId: props.item?.id,
      },
      onOpen() {
        widgetOpened.value = true;
      },
      onClose() {
        widgetOpened.value = false;
      },
    });
  }
}

// Load count data
// ... your data loading logic
</script>
```

**Important:** Widgets only use `VcWidget` component props (`value`, `title`, `icon`, `loading`, etc.). Do not add custom HTML content inside `VcWidget`.

### Widget Registration in Parent Blade

```typescript
import { useWidgets, useBlade, onBeforeUnmount } from "@vc-shell/framework";
import ProductStatsWidget from "../components/widgets/product-stats/product-stats-widget.vue";

const { registerWidget, unregisterWidget } = useWidgets();
const { blade } = useBlade();

// Register widget
registerWidget({
  id: "productStats",
  component: ProductStatsWidget,
  // isVisible: () => true, // Uncomment to control visibility
  // clickHandler: () => { /* Handle click */ },
});

// Cleanup
onBeforeUnmount(() => {
  unregisterWidget("productStats");
});
```

## Adding Blades to Existing Modules

### Interactive Mode

```bash
npx create-vc-app blade
# Select: "Blade (in existing module)"
```

### Non-Interactive Mode

```bash
npx create-vc-app blade \
  --module products \
  --type details \
  --name product-variants \
  --composable \
  --locales
```

The blade will be:

1. ✅ Created in `src/modules/products/pages/`
2. ✅ Registered in `src/modules/products/pages/index.ts`
3. ✅ Formatted with Prettier

## Command-Line Options

### Common Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `--module <name>` | string | Target module name | - |
| `--type <grid\|details>` | string | Blade type | - |
| `--name <name>` | string | Blade name | - |
| `--composable` | boolean | Generate composable | `true` |
| `--locales` | boolean | Generate locales | `true` |
| `--is-workspace` | boolean | Mark as workspace blade | `false` |
| `--widget` | boolean | Generate widget instead | `false` |

### Form Builder Options

| Option | Type | Description |
|--------|------|-------------|
| `--skip-form-editor` | boolean | Skip interactive form builder |
| `--form-fields <json>` | string | JSON array of form field definitions |

## Localization

All generated blades include proper i18n structure:

```json
{
  "PRODUCTS": {
    "PAGES": {
      "LIST": {
        "TITLE": "Products",
        "TABLE": {
          "HEADER": {
            "NAME": "Name",
            "PRICE": "Price"
          }
        }
      },
      "DETAILS": {
        "TITLE": "Product Details",
        "FORM": {
          "INFO": {
            "NAME": "Name",
            "NAME_PLACEHOLDER": "Enter product name",
            "PRICE": "Price"
          }
        }
      }
    },
    "WIDGETS": {
      "PRODUCT_STATS": {
        "TITLE": "Product Statistics"
      }
    }
  }
}
```

## Module Registration

### Automatic Registration in main.ts

The generator automatically adds your module to `src/main.ts`:

```typescript
// Before
app.use(router);

// After
import ProductsModule from "./modules/products";

app.use(ProductsModule);
app.use(router);
```

### Manual Registration (if needed)

If automatic registration fails, add manually:

```typescript
import { createAppModule } from "@vc-shell/framework";
import * as pages from "./pages";
import * as locales from "./locales";

export default createAppModule(pages, locales);
```

## Best Practices

### 1. Naming Conventions

- **Module names**: kebab-case (`products`, `customer-orders`)
- **Entity names**: PascalCase (`Product`, `CustomerOrder`)
- **Blade files**: kebab-case (`product-details.vue`)
- **Composables**: camelCase with `use` prefix (`useProductDetails`)

### 2. API Integration

Replace TODO comments with your API client:

```typescript
// Replace this
const response = await fetch('/api/products');

// With your API client
const response = await apiClient.products.list();
```

### 3. Form Validation

Use vee-validate for form validation:

```vue
<Field
  v-slot="{ field, errorMessage, handleChange, errors }"
  :label="$t('PRODUCTS.PAGES.DETAILS.FORM.INFO.NAME')"
  :model-value="item.name"
  name="name"
  rules="required|min:3"
>
  <VcInput
    v-bind="field"
    v-model="item.name"
    :label="$t('PRODUCTS.PAGES.DETAILS.FORM.INFO.NAME')"
    required
    :error="!!errors.length"
    :error-message="errorMessage"
    @update:model-value="handleChange"
  />
</Field>
```

### 4. Modification Tracking

Details blades include modification tracking:

```typescript
const { item, saveChanges, resetItem, loading, isModified } =
  useProductDetails(props);

// Save handler
const onSave = async () => {
  await saveChanges();
  // TODO: Call your API
};

// Modified state in blade toolbar
:modified="isModified"
```

### 5. Widget Visibility

Control widget visibility dynamically:

```typescript
registerWidget({
  id: "productStats",
  component: ProductStatsWidget,
  isVisible: () => {
    // Show only when product is published
    return item.value?.status === "published";
  },
});
```

## Examples

### Complete Module with Custom Form

```bash
# Interactive mode with custom form
npx create-vc-app blade

# Follow prompts:
# 1. Select: "Module (with blades)"
# 2. Module name: products
# 3. Entity name: Product
# 4. Create both blades: yes
# 5. Workspace blade: Grid blade
# 6. Customize form: yes
# 7. Add fields:
#    - name (text, required)
#    - price (currency, required)
#    - description (editor, optional)
#    - category (select, required) → Electronics,Clothing,Books
#    - inStock (switch, required)
#    - images (gallery, optional)
```

### Adding Widget to Blade

```bash
# Interactive mode
npx create-vc-app blade --widget

# Follow prompts:
# 1. Select module: products
# 2. Select blade: product-details
# 3. Widget name: ProductStats
```

### Non-Interactive with JSON Form Fields

```bash
npx create-vc-app my-shop \
  --skip-form-editor \
  --form-fields '[
    {"name":"title","type":"text","required":true},
    {"name":"price","type":"currency","required":true},
    {"name":"description","type":"editor","required":false},
    {"name":"category","type":"select","required":true,"options":"Electronics,Clothing,Books"},
    {"name":"featured","type":"switch","required":false},
    {"name":"images","type":"gallery","required":false}
  ]'

# Then input:
# Module name: products
# Entity name: Product
# Create both blades: yes
# Workspace blade: Grid blade
```

## Troubleshooting

### Module Not Appearing in App

**Problem:** Generated module doesn't appear in the application.

**Solution:** Check that module is registered in `src/main.ts`:

```typescript
import ProductsModule from "./modules/products";
app.use(ProductsModule);
```

### TypeScript Errors

**Problem:** TypeScript errors after generation.

**Solution:** The generator uses `@ts-expect-error` for placeholder types. Replace with your actual types:

```typescript
// Replace
// @ts-expect-error TODO: Replace with your actual type
const item = ref<any>({});

// With
import type { Product } from "@/types";
const item = ref<Product>({});
```

### Widget Not Showing

**Problem:** Widget doesn't appear in blade.

**Solution:** Check widget registration:

1. Widget imported correctly
2. `registerWidget()` called
3. `isVisible` returns true (if specified)
4. Widget ID is unique

### Form Fields Missing

**Problem:** Custom form fields not generated.

**Solution:**
- Use `--skip-form-editor` flag
- Provide valid JSON in `--form-fields`
- Check JSON syntax (proper quotes, commas)

## Advanced Usage

### Custom Templates

You can customize generated code by modifying templates in:

```
cli/create-vc-app/src/templates/
├── blades/
│   ├── grid/
│   └── details/
└── widgets/
```

### Programmatic Usage

Import the generator in your Node.js scripts:

```typescript
import { generateBlade } from "@vc-shell/create-vc-app";

await generateBlade({
  module: "products",
  type: "grid",
  name: "products",
  composable: true,
  locales: true,
  path: process.cwd(),
});
```

## What's Next?

- [Creating Your First Custom App](./creating-first-custom-app.md)
- [VC Shell Framework Documentation](../../)
- [Component Library](../components/)

## Support

For issues or questions:

- GitHub: [vc-shell repository](https://github.com/VirtoCommerce/vc-shell)
- Documentation: [VC Shell Docs](https://docs.virtocommerce.org/platform/developer-guide/custom-apps-development/vc-shell/)
