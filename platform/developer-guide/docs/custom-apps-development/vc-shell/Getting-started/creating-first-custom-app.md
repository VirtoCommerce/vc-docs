# Creating Your First VC Shell Application

This guide will walk you through creating your first VC Shell application from scratch using the `create-vc-app` CLI tool.

## Prerequisites

Before you begin, ensure you have:

- **Node.js 18+**: [Download Node.js](https://nodejs.org/)
- **Yarn package manager**: The CLI uses Yarn (installed with Node.js)
- **Code editor**: VS Code recommended with Vue.js extensions

## Quick Start

### Step 1: Create Your Application

Run the scaffolding tool:

```bash
npx create-vc-app@latest my-shop
```

Or with a specific version:

```bash
npx create-vc-app my-shop
```

### Step 2: Follow the Interactive Prompts

The CLI will guide you through setup:

```text
╔══════════════════════════════════════════════════╗
║  create-vc-app v1.1.x                            ║
╚══════════════════════════════════════════════════╝

✔ Project name: … my-shop
✔ Base path: … /apps/my-shop/

📦 Scaffolding app in ./my-shop...
✅ Created 60 files

🎨 Formatting files with Prettier...
✅ All files formatted

🏗️  Creating module with blade generator...

✔ Module name (e.g., products, orders): … products
✔ Entity name (e.g., Product, Order): … Product
✔ Create both Grid and Details blades? … yes
✔ Which blade should be the workspace blade? › Grid blade
✔ Customize form fields interactively? … no

✅ Module generated successfully!

==================================================
✨ Application created successfully!
==================================================

📊 Summary:
   Location: /path/to/my-shop
   Package: my-shop
   Base path: /apps/my-shop/
   Files created: 85

🚀 Next steps:

  1. cd my-shop
  2. yarn
  3. yarn serve
```

### Step 3: Install Dependencies

```bash
cd my-shop
yarn
```

### Step 4: Start Development Server

```bash
yarn serve
```

Your app will be available at `http://localhost:8080/apps/my-shop/`

## What Was Created?

### Application Structure

```
my-shop/
├── src/
│   ├── main.ts                     # App entry point
│   ├── router/                     # Vue Router configuration
│   │   ├── index.ts
│   │   └── routes.ts
│   ├── locales/                    # i18n translations
│   │   ├── index.ts
│   │   └── en.json
│   ├── modules/                    # Your modules
│   │   └── products/
│   │       ├── pages/
│   │       │   ├── index.ts
│   │       │   ├── products.vue           # Grid blade
│   │       │   └── product-details.vue     # Details blade
│   │       ├── composables/
│   │       │   ├── index.ts
│   │       │   ├── useProductList.ts
│   │       │   └── useProductDetails.ts
│   │       ├── locales/
│   │       │   ├── index.ts
│   │       │   └── en.json
│   │       ├── components/
│   │       │   └── widgets/
│   │       │       └── index.ts
│   │       └── index.ts               # Module definition
│   ├── api_client/                   # API client placeholder
│   │   └── README.md
│   ├── components/                   # Shared components
│   │   └── dashboard-widgets/
│   │       └── Welcome.vue
│   ├── pages/                        # App pages
│   │   ├── App.vue
│   │   └── Dashboard.vue
│   ├── styles/                       # Global styles
│   │   ├── custom.scss
│   │   └── index.scss
│   └── composables/
│       └── index.ts
├── public/                           # Static assets
│   ├── assets/
│   └── img/
├── package.json
├── tsconfig.json
├── vite.config.mts
├── .prettierrc
├── .eslintrc.js
└── README.md
```

### Module Structure

Each module contains:

#### Grid Blade (`products.vue`)
- **Purpose**: List view for browsing items
- **Features**:
  - Search and filters (staged/applied architecture)
  - Data table with sorting and pagination
  - Toolbar with actions (Add, Refresh, Delete)
  - Composable with async data loading

#### Details Blade (`product-details.vue`)
- **Purpose**: Form view for viewing/editing items
- **Features**:
  - Form fields with validation
  - Modification tracking (detects unsaved changes)
  - Toolbar with Save/Cancel/Delete
  - useModificationTracker integration

#### Composables
- **`useProductList.ts`**: Business logic for Grid blade
  - Data loading with `useAsync`
  - Filter management (staged/applied)
  - Search functionality
  - Pagination support

- **`useProductDetails.ts`**: Business logic for Details blade
  - Item loading/saving
  - Modification tracking
  - Form state management

#### Locales
- **`en.json`**: English translations
  - Organized by namespace (LIST, DETAILS, FORM)
  - Ready for additional languages

## Customizing Your Application

### Adding Custom Form Fields

When creating your module, choose "Customize form fields interactively":

```bash
✔ Customize form fields interactively? … yes

Add form fields (press ESC or Enter with empty name to finish):

✔ Field name: … name
✔ Field type: › Text
✔ Is required? … yes

✔ Field name: … price
✔ Field type: › Currency
✔ Is required? … yes

✔ Field name: … description
✔ Field type: › Editor (Rich Text)
✔ Is required? … no

✔ Field name: … category
✔ Field type: › Select (Dropdown)
✔ Options (comma-separated): … Electronics,Clothing,Books
✔ Is required? … yes

✔ Field name: … inStock
✔ Field type: › Switch (Toggle)
✔ Is required? … yes

✔ Field name: … images
✔ Field type: › Gallery (Images)
✔ Is required? … no

✔ Field name: … (press Enter to finish)
```

This generates a Details blade with all specified components.

### Available Form Components

| Component | Type | Description |
|-----------|------|-------------|
| **VcInput** | text, number, date | Basic text input |
| **VcTextarea** | textarea | Multi-line text |
| **VcSelect** | select | Dropdown selection |
| **VcEditor** | editor | Rich text editor (WYSIWYG) |
| **VcSwitch** | switch | Boolean toggle |
| **VcGallery** | gallery | Image gallery with upload |
| **VcInputCurrency** | currency | Money input with formatting |
| **VcRadioButton** | radio | Radio button group |
| **VcCheckbox** | checkbox | Single checkbox |
| **VcMultivalue** | multivalue | Multiple value input |
| **VcField** | field | Read-only display field |

## Adding More Modules

After creating your initial app, you can add more modules:

```bash
npx create-vc-app blade
```

Select "Module (with blades)" and follow the prompts.

Example: Adding an orders module

```text
✔ What would you like to generate? › Module (with blades)
✔ Module name: … orders
✔ Entity name: … Order
✔ Create both Grid and Details blades? … yes
✔ Which blade should be the workspace blade? › Grid blade
✔ Customize form fields interactively? … yes

Add form fields:
- orderNumber (text, required)
- customerName (text, required)
- orderDate (date, required)
- status (select, required) → Pending,Processing,Shipped,Delivered
- totalAmount (currency, required)
- notes (textarea, optional)
```

The new module will be automatically:
- ✅ Created in `src/modules/orders/`
- ✅ Registered in `src/main.ts`
- ✅ Formatted with Prettier

## Adding Widgets

Widgets are reusable components that can be added to blades:

```bash
npx create-vc-app blade --widget
```

Example: Adding a statistics widget to product details

```text
✔ Select module: › products
✔ Select blade to add widget to: › product-details
✔ Widget name: … ProductStats
```

The widget will be automatically:
- ✅ Created in `src/modules/products/components/widgets/`
- ✅ Registered in the parent blade
- ✅ Added to locales

## Integrating Your API

The generated code includes TODO comments guiding you to integrate your API:

### Example: Update Grid Blade Composable

```typescript
// src/modules/products/composables/useProductList.ts

// Replace this placeholder
const { load, loading, items } = useAsync(async () => {
  // TODO: Replace with your API client
  // Example:
  // const response = await apiClient.products.list({
  //   filters: appliedFilters.value,
  //   page: currentPage.value,
  // });
  // return response.data;

  return {
    results: [],
    totalCount: 0,
  };
});
```

### Example: Update Details Blade Composable

```typescript
// src/modules/products/composables/useProductDetails.ts

const saveChanges = async () => {
  // TODO: Replace with your API client
  // Example:
  // if (item.value.id) {
  //   await apiClient.products.update(item.value.id, item.value);
  // } else {
  //   await apiClient.products.create(item.value);
  // }
};
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
# API Configuration
VITE_API_URL=https://api.example.com
VITE_APP_PLATFORM_URL=https://platform.example.com

# App Configuration
VITE_BASE_URL=/apps/my-shop/
```

### Router Configuration

Update `src/router/routes.ts` to add custom routes:

```typescript
import type { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Dashboard",
    component: () => import("../pages/Dashboard.vue"),
  },
  // Add custom routes here
];

export default routes;
```

## Development Workflow

### Running the App

```bash
yarn serve      # Start dev server
yarn build      # Build for production
yarn lint       # Run linter
yarn format     # Format code with Prettier
```

### Adding a New Blade

```bash
npx create-vc-app blade \
  --module products \
  --type details \
  --name product-variants \
  --composable \
  --locales
```

### Adding a Widget

```bash
npx create-vc-app blade --widget
```

## Best Practices

### 1. Module Organization

Keep modules self-contained:
- Business logic in composables
- UI components in pages
- Shared code in module root
- Locales in module locales folder

### 2. API Integration

Use a centralized API client:

```typescript
// src/api_client/index.ts
import { createApiClient } from "@vc-shell/api-client";

export const apiClient = createApiClient({
  baseURL: import.meta.env.VITE_API_URL,
});
```

### 3. State Management

Use Vue's Composition API:
- `ref` for reactive primitives
- `reactive` for objects
- `computed` for derived state
- Composables for reusable logic

### 4. Localization

Follow the namespace convention:

```json
{
  "PRODUCTS": {
    "PAGES": {
      "LIST": { "TITLE": "Products" },
      "DETAILS": {
        "TITLE": "Product Details",
        "FORM": {
          "INFO": {
            "NAME": "Name",
            "NAME_PLACEHOLDER": "Enter product name"
          }
        }
      }
    }
  }
}
```

### 5. TypeScript

Define types for your data:

```typescript
// src/types/product.ts
export interface Product {
  id: string;
  name: string;
  price: number;
  description?: string;
  inStock: boolean;
}
```

## Deployment

### Building for Production

```bash
yarn build
```

This creates an optimized build in the `dist/` directory.

### Deployment Options

1. **Static Hosting**: Deploy `dist/` to any static host
2. **CDN**: Upload to CDN with proper caching headers
3. **Docker**: Create a Docker image with nginx

Example nginx configuration:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /usr/share/nginx/html;

    location /apps/my-shop/ {
        try_files $uri $uri/ /apps/my-shop/index.html;
    }
}
```

## Troubleshooting

### Module Not Appearing

**Problem**: New module doesn't appear in the application.

**Solution**: Verify module is registered in `src/main.ts`:

```typescript
import ProductsModule from "./modules/products";
app.use(ProductsModule);
```

### Build Errors

**Problem**: TypeScript errors during build.

**Solution**:
1. Check for `@ts-expect-error` comments
2. Replace placeholders with actual types
3. Ensure all imports are correct

### API Not Working

**Problem**: API calls fail or return errors.

**Solution**:
1. Check API URL in `.env`
2. Verify CORS configuration
3. Check network tab in DevTools
4. Ensure API endpoints exist

## Next Steps

Now that you have your first VC Shell application:

1. **Explore Generated Code**: Review the generated modules and composables
2. **Integrate Your API**: Replace TODO placeholders with real API calls
3. **Customize UI**: Modify blades and components to match your needs
4. **Add More Modules**: Use the blade generator to add more functionality
5. **Read Documentation**: [Blade Generator Guide](./blade-generator.md)

## Additional Resources

- [Blade Generator](./blade-generator.md) - Detailed guide
- [VC Shell Components](../../components/) - Component library
- [VC Shell Framework](../../) - Framework documentation
- [Vue.js Guide](https://vuejs.org/guide/) - Vue.js documentation
- [TypeScript Handbook](https://www.typescriptlang.org/docs/) - TypeScript docs

## Support

Need help? Check out:

- [GitHub Issues](https://github.com/VirtoCommerce/vc-shell/issues)
- [Documentation](https://docs.virtocommerce.org/)
- [Community Forum](https://www.virtocommerce.org/community)
