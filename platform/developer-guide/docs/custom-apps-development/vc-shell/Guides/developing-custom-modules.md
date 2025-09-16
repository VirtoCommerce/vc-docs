# Developing Custom VC-Shell Modules

Modules are the building blocks of your VC-Shell application, encapsulating specific features, business logic, and UI components. A well-designed modular architecture is key to creating scalable and maintainable applications.

This guide picks up after you understand the [Core Concepts of a Custom VC-Shell Application](./custom-application-core-concepts.md) and dives into the specifics of building modules.

## What is a Module in VC-Shell?

A module in VC-Shell represents a distinct piece of functionality within your application. Think of it as a mini-application focused on a particular domain or a set of related tasks. For example, in an e-commerce application, you might have modules for:

-   **Products**: Managing product listings, details, inventory.
-   **Orders**: Viewing and processing customer orders.
-   **Seller Profile**: Managing the vendor's information and settings.
-   **Fulfillment**: Handling shipping and logistics.

Each module typically contains its own components, composables for state and logic, pages (blades), routes, and localization files, all related to its specific purpose.

## Benefits of Modularity

Adopting a modular approach offers several significant advantages:

-   **Separation of Concerns**: Isolates different parts of your application, making the codebase easier to understand, debug, and test. Changes within one module are less likely to unintentionally affect others.
-   **Reusability**: While application-specific modules are tailored, the pattern encourages creating reusable components and composables within those modules.
-   **Team Collaboration**: Allows different developers or teams to work on separate modules concurrently with fewer merge conflicts and a clearer division of responsibilities.
-   **Scalability & Maintainability**: As the application grows, it's easier to add new features as new modules or to enhance existing ones. Maintenance becomes more manageable as you can focus on individual modules.
-   **Improved Build Times & Lazy Loading**: Modules can often be configured for lazy loading, meaning their code is only downloaded by the browser when the user navigates to a feature provided by that module. This can significantly improve the initial load time of your application.

## Anatomy of a Module

When you create a new application using `@vc-shell/create-vc-app`, it typically generates an initial module (e.g., `src/modules/your-module-name/`). The internal structure of a module generally follows these conventions (expanding upon the information in the "[Create first VC-Shell application](./../Getting-started/creating-first-custom-app.md)" guide):

```
src/
└── modules/
    └── your-module-name/            # Root folder for your module
        ├── components/              # Vue components specific to this module
        │   ├── notifications/       # Optional: Custom templates for notifications specific to this module
        │   └── ...                  # Other subfolders for component organization (e.g., widgets, forms)
        ├── composables/             # Vue composables for shared logic within this module
        │   └── useSpecificFeature.ts
        ├── locales/                 # Translation files for this module
        │   ├── en.json
        │   └── es.json
        ├── pages/                   # Vue components representing pages or blades for this module
        │   ├── MyMainBlade.vue
        │   └── MyDetailsPage.vue
        ├── types/                   # Optional: TypeScript type definitions specific to this module
        │   └── index.d.ts
        ├── router/                  # Optional: Module-specific route definitions (if not handled solely in index.ts)
        │   └── routes.ts
        └── index.ts                 # Module entry point: registration and exports
```

Let's break down these key directories and files within a module:

-   **`components/`**: Contains Vue components that are primarily used within this module.
    -   If a component is highly specific to a single page/blade, it might reside alongside that page file or in a subdirectory within `pages/`.
    -   If a component is reusable across multiple pages *within this module*, `components/` is the place for it.
    -   The `components/notifications/` subfolder is a conventional place for custom Vue components used to render specific types of push notifications relevant to this module (see "[Customizing Notifications](./../Essentials/Usage-Guides/customizing-notifications.md)").
-   **`composables/`**: This directory houses Vue Composition API functions (composables) that encapsulate reactive state and logic specific to the module. For example, a `useProductList.ts` composable in a "Products" module would handle fetching, filtering, and managing the state of the product list.
-   **`locales/`**: Stores translation files (e.g., `en.json`, `fr.json`) for all text strings used within this module. This ensures that your module can be localized independently. See "[Adding New Languages](./../Essentials/Usage-Guides/adding-new-languages.md)".
-   **`pages/`**: Contains the Vue components that act as top-level views or "blades" for the module. These are typically registered with the Vue Router. For example, `ProductListBlade.vue` or `OrderDetailsPage.vue`.
-   **`types/`** (Optional): If your module involves complex TypeScript types or interfaces that are specific to its domain and not intended for global use, you can place them here.
-   **`index.ts`**: This is the crucial entry point for your module. It serves several purposes:
    *   **Registration**: It typically exports a function (often using `createAppModule` from `@vc-shell/framework`) that registers the module with the main Vue application. This registration process makes the module's pages, locales, components, and services available to the application.
    *   **Exports**: It may also export key components, composables, or types from the module that need to be accessible by other parts of the application or other modules (though direct inter-module dependencies should be managed carefully).

This standardized structure promotes consistency and makes it easier to navigate and understand different modules within your application.

## Step-by-Step: Creating a New Module from Scratch

While the `@vc-shell/create-vc-app` generator creates an initial module for you, you'll often need to add more modules as your application grows. Here's a step-by-step guide to creating a new module manually within an existing VC-Shell application.

Let's imagine we're building a "Reviews" module to manage customer reviews for products.

### 1. Folder Creation

First, create a new directory for your module within the `src/modules/` folder of your application.

```
src/
└── modules/
    ├── reviews/                # Our new module
    │   ├── components/
    │   ├── composables/
    │   ├── locales/
    │   ├── pages/
    │   └── index.ts
    └── ...                     # Other existing modules
```

-   Create the main `reviews` folder.
-   Inside `reviews`, create the standard subdirectories: `components`, `composables`, `locales`, `pages`.
-   Create an empty `index.ts` file in the `reviews` root folder. This will be the module's entry point.

### 2. Defining Pages (Blades)

Pages in a module are typically Vue components that represent full views or blades. For a detailed breakdown of a blade's structure and its common UI elements (header, toolbar, content area), refer to the **[Understanding Blade Anatomy Guide](../Essentials/Usage-Guides/understanding-blade-anatomy.md)**.

Let's create a simple blade to list reviews and another to view/edit a single review.

**`src/modules/reviews/pages/ReviewListBlade.vue`**:
```vue
<template>
  <VcBlade
    :title="t('MODULE_REVIEWS.PAGES.LIST.BLADE_TITLE')"
    :expanded="props.expanded"
    :closable="props.closable"
    @close="$emit('close:blade')"
    @expand="$emit('expand:blade')"
    @collapse="$emit('collapse:blade')"
  >
    <div class="tw-p-5">
      <h2 class="tw-text-xl tw-font-semibold">{{ t('MODULE_REVIEWS.PAGES.LIST.HEADER') }}</h2>
      <!-- Add VcTable or other components to list reviews -->
      <div v-if="isLoading" class="tw-mt-4">{{ t('MODULE_REVIEWS.PAGES.LIST.LOADING') }}</div>
      <ul v-else-if="reviews.length" class="tw-mt-4 tw-list-disc tw-pl-5">
        <li v-for="review in reviews" :key="review.id" @click="openReviewDetails(review.id)">
          {{ review.productName }} - {{ review.rating }} stars - {{ review.comment }}
        </li>
      </ul>
      <p v-else class="tw-mt-4">{{ t('MODULE_REVIEWS.PAGES.LIST.NO_REVIEWS_FOUND') }}</p>
    </div>
  </VcBlade>
</template>

<script lang="ts" setup>
import { VcBlade, useBladeNaviation, type IParentCallArgs } from "@vc-shell/framework";
import { useReviewList } from "../composables/useReviewList";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

// Define Props for the blade, standard for VC-Shell blades
interface Props {
  expanded?: boolean;
  closable?: boolean;
  // param?: string; // Example if you need to pass a generic parameter
  // options?: Record<string, any>; // Example for more complex options
}

// Define Emits for the blade, standard for VC-Shell blades
interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
  (event: "close:blade"): void;
}

defineOptions({
  name: "ReviewListBlade",
  url: "/reviews",
  menuItem: {
    title: "MODULE_REVIEWS.MENU.TITLE", // Use translation keys
    icon: "material-rate_review",
    priority: 50,
    groupConfig: {
        id: "management-group",
        title: "MODULE_REVIEWS.REVIEWS_LIST_GROUPS_MANAGEMENT" // Use translation keys for group title
    }
  },
  permissions: ["reviews:view"], // Optional: Permissions required to access this blade
});

const props = withDefaults(defineProps<Props>(), {
  expanded: true,
  closable: true,
});

const emit = defineEmits<Emits>();
const { t } = useI18n({ useScope: "global" });
const router = useRouter();

const { reviews, isLoading, fetchReviews } = useReviewList();

const { openBlade } = useBladeNaviation();

async function openReviewDetails(reviewId: string) {
  // Example of calling another blade (ReviewEditBlade)

  await openBlade({
    blade: {
      name: "ReviewEditBlade",
    },
    param: reviewId,
    options: {
      source: "list",
    }
  })
}

// Example of how parent:call might be used if this blade was initiated by another
// function confirmSelection() {
//   emit("parent:call", {
//     method: "confirmSelection",
//     args: { selectedItems: reviews.value.filter(r => r.selected) }
//   });
//   emit("close:blade");
// }


onMounted(() => {
  fetchReviews();  // Load reviews when the blade is mounted
});
</script>
```

**`src/modules/reviews/pages/ReviewEditBlade.vue`**:
```vue
<template>
  <VcBlade
    :title="isNew ? t('MODULE_REVIEWS.PAGES.EDIT.BLADE_TITLE_NEW') : t('MODULE_REVIEWS.PAGES.EDIT.BLADE_TITLE_EXISTING')"
    :expanded="props.expanded"
    :closable="props.closable"
    @close="$emit('close:blade')"
    @expand="$emit('expand:blade')"
    @collapse="$emit('collapse:blade')"
  >
    <div class="tw-p-5">
      <h2 class="tw-text-xl tw-font-semibold">
        {{ isNew ? t('MODULE_REVIEWS.PAGES.EDIT.HEADER_NEW') : t('MODULE_REVIEWS.PAGES.EDIT.HEADER_EXISTING') }}
      </h2>
      <p v-if="props.param" class="tw-mt-1">Received param: {{ props.param }}</p>
      <p v-if="props.options?.source" class="tw-mt-1">Source: {{ props.options.source }}</p>
      <p class="tw-mt-2">Form to edit a review will go here.</p>
      <!-- Add VcForm, VcInput, VcTextarea, VcRating etc. -->
      <!-- Example for a save button -->
      <!--
      <div class="tw-mt-4">
        <VcButton @click="saveReview">Save Review</VcButton>
      </div>
      -->
    </div>
  </VcBlade>
</template>

<script lang="ts" setup>
import { VcBlade, type IParentCallArgs } from "@vc-shell/framework";
import { computed } from "vue";
import { useI18n } from "vue-i18n";
// Import a composable for handling single review logic (creation/editing)
// import { useReviewDetails } from "../composables/useReviewDetails";

interface Props {
  // reviewId?: string; // This will be passed from the route params via 'param' prop now
  expanded?: boolean;
  closable?: boolean;
  param?: string; // Optional generic parameter, used here for reviewId when opening programmatically or via routeResolver
  options?: { // Optional complex options
    source?: string;
  };
}

interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
  (event: "close:blade"): void;
}

const props = withDefaults(defineProps<Props>(), {
  expanded: true,
  closable: true,
  param: undefined,
  options: () => ({}),
});

const emit = defineEmits<Emits>();
const { t } = useI18n();

defineOptions({
  name: "ReviewEditBlade",
  url: "/review",
  permissions: ["reviews:edit"], // Or "reviews:create", "reviews:edit" depending on logic
});

const isNew = computed(() => !props.param); // Use param to determine if it's a new review

// const { review, isLoading, fetchReviewDetails, saveReview: saveReviewAction } = useReviewDetails(props.param);

// if (props.param) { // If param (reviewId) is present, fetch details
//   fetchReviewDetails();
// }

// function saveReview() {
//   saveReviewAction().then(() => {
//     emit("parent:call", { method: "refreshReviewList" }); // Notify parent to refresh
//     emit("close:blade");
//   });
// }

</script>
```

**Key points for blades:**
-   Use `defineOptions` to set metadata for the blade, such as its `name` (should be unique), optional `url` (for routing), optional `menuItem` configuration for automatic menu registration, and `permissions`.
-   The `url` property in `defineOptions` should specify the static path segment for that blade (e.g., `url: '/details'` or `url: '/review'`). When navigating to a URL like `/main/details/123`, the blade navigation system's `routeResolver` will first match `/main` to open the main blade/workspace. Then, from the remaining path `details/123`, it will match `/details` (the `url` defined in the child blade's `defineOptions`) to open the child blade. The subsequent part of the URL (`123` in this example) will then be passed as the `param` prop to this child blade. Thus, dynamic parameters are extracted by `routeResolver` from the browser's URL and passed via `param`, not by defining patterns like `/:id` within `defineOptions.url` itself.
-   **Standard Props**:
    -   `expanded?: boolean`: Controls if the blade is initially expanded (defaults to `true`).
    -   `closable?: boolean`: Controls if the blade shows a close button (defaults to `true`).
    -   `param?: string`: A generic string parameter you can pass when opening the blade programmatically.
    -   `options?: Record<string, any>`: For passing more complex, structured data when opening the blade.
-   **Standard Emits**:
    -   `close:blade`: Emitted when the blade's close button is clicked or when it should close itself.
    -   `expand:blade`: Emitted when the blade is expanded.
    -   `collapse:blade`: Emitted when the blade is collapsed.
    -   `parent:call`: A crucial emit for communication with the blade that opened this one (if any). It sends an `IParentCallArgs` object (`{ method: string, args?: any }`) to instruct the parent.
-   The `menuItem` object, if provided, allows the blade to be automatically added to the application's main navigation menu. See "[Building Navigation Menus with `useMenuService`](./../Essentials/Usage-Guides/building-navigation-menus-with-usemenuservice.md)" for more on `menuItem` properties.
-   Import and use UI components from `@vc-shell/framework` like `VcBlade`, `VcInput`, etc.
-   Use `withDefaults` to provide default values for your props.

### 3. Creating Composables for Business Logic

Composables encapsulate the state and logic related to your module's features.
We will now adjust `useReviewList.ts` to use the actual `useApiClient` and a hypothetical generated API client.

**`src/modules/reviews/composables/useReviewList.ts`**:
```typescript
import { ref } from 'vue';
import { useAsync, useApiClient } from '@vc-shell/framework';
// Import your generated API client and its types.
// The path assumes your generated client is in `src/api_client/`
// and follows the naming convention of `[ServiceName]ApiClient`.
import { ReviewsApiClient, type IReview } from '@/api_client';
// If IReview is part of a namespace in the generated client, it might be:
// import { VirtoCommercePlatformWebMarketplacesVendorsApiMarketplacevendorReviewsApiClient as ReviewsApiClient,
//          VirtoCommercePlatformWebMarketplacesVendorsApiMarketplacevendorIReview as IReview } from '@/api_client';

export function useReviewList() {
  const reviews = ref<IReview[]>([]);

  // Get the API client instance using useApiClient
  // Pass the constructor of your specific API client.
  const { getApiClient } = useApiClient(ReviewsApiClient);

  const { action: fetchReviews, loading: isLoading, error } = useAsync(async (searchCriteria?: any) => {
    try {
      const client = await getApiClient();
      // Call the appropriate method on your API client.
      // This example assumes a `searchReviews` method. Adjust as per your actual client.
      // You might pass search criteria, pagination, sorting, etc.
      const result = await client.searchReviews(searchCriteria || { /* default criteria */ });

      // Assuming the API returns a structure like { items: [], totalCount: 0 }
      // Adjust based on your actual API response.
      if (result && Array.isArray(result.items)) {
        reviews.value = result.items;
        // You might also want to store totalCount for pagination
        // totalCount.value = result.totalCount;
      } else {
        // Handle cases where the response might not be as expected
        reviews.value = Array.isArray(result) ? result : [];
      }

    } catch (err) { // Renamed error to err to avoid conflict with `error` from useAsync
      console.error("Failed to fetch reviews:", err);
      reviews.value = []; // Reset on error
      // Optionally, use the notification service to show an error to the user
      // import { VcNotificationService } from '@vc-shell/framework';
      // VcNotificationService.error({ title: 'Error', message: 'Could not load reviews.' });
      throw err; // Re-throw so useAsync can handle it
    }
  });

  // Expose any other state or methods needed by the component
  // For example, if you're handling pagination within the composable:
  // const currentPage = ref(1);
  // const itemsPerPage = ref(20);
  // const totalCount = ref(0);
  //
  // async function goToPage(page: number) {
  //   currentPage.value = page;
  //   await fetchReviews({
  //     skip: (page - 1) * itemsPerPage.value,
  //     take: itemsPerPage.value
  //   });
  // }

  return {
    reviews,
    isLoading,
    error, // Expose the error state from useAsync
    fetchReviews,
    // currentPage, // if handling pagination
    // totalCount,  // if handling pagination
    // goToPage,    // if handling pagination
  };
}
```
**Key points for composables:**

-   Import your actual generated API client (e.g., `ReviewsApiClient`) and any related types (`IReview`) from your project's `api_client` directory. The exact import path and names will depend on your NSwag/OpenAPI configuration.
-   Use `const { getApiClient } = useApiClient(YourSpecificApiClientConstructor);` to get a function that returns an initialized instance of your API client.
-   In your data-fetching actions (like `fetchReviews`), call `await getApiClient()` to get the client instance, then call its methods (e.g., `client.searchReviews()`).
-   Adapt the method names (`searchReviews`) and parameter/response structures to match what your actual API client provides. The example from `AssociationsItems.vue` uses `searchQuery.value` which is a `ref` holding search parameters.
-   The `useAsync` composable from `@vc-shell/framework` is excellent for managing loading states and errors for asynchronous operations. It returns `action` (your async function), `loading` (a boolean ref), and `error` (a ref for any caught error).
-   Keep API interaction logic within composables rather than directly in Vue components. This improves separation of concerns and testability.
-   Define and export any reactive state (`ref`, `reactive`, `computed`) and methods that your Vue components will need to interact with the module's data and logic.

### 4. Adding Module-Specific Components

If your module requires UI pieces that are specific to it and reusable across its pages/blades, create them in the `src/modules/reviews/components/` directory.

For example, you might create a `ReviewCard.vue` component to display a single review in a standardized format.

**`src/modules/reviews/components/ReviewCard.vue`**:
```vue
<template>
  <div class="review-card tw-border tw-p-3 tw-rounded tw-shadow-sm">
    <h4 class="tw-font-semibold">{{ review.productName }} - {{ review.rating }}/5 stars</h4>
    <p class="tw-text-sm tw-text-gray-600">By User ID: {{ review.userId }} on {{ review.reviewDate }}</p>
    <p class="tw-mt-1">{{ review.comment }}</p>
  </div>
</template>

<script lang="ts" setup>
interface IReview { // Should match the IReview from your composable/API
  id: string;
  productName: string;
  userId: string;
  rating: number;
  comment: string;
  reviewDate: string;
}

interface Props {
  review: IReview;
}

defineProps<Props>();
</script>
```
This component can then be imported and used within `ReviewListBlade.vue` or other parts of the "Reviews" module.

### 5. Setting up Locales

For any text that needs to be translated, add entries to locale files within your module, following a structured approach similar to other modules in your application.

**`src/modules/reviews/locales/en.json`**:
```json
{
  "MODULE_REVIEWS": {
    "MENU": {
      "TITLE": "Product Reviews",
      "GROUP_MANAGEMENT": "Management"
    },
    "PAGES": {
      "LIST": {
        "BLADE_TITLE": "Product Reviews",
        "HEADER": "Manage Reviews",
        "LOADING": "Loading reviews...",
        "NO_REVIEWS_FOUND": "No reviews found."
      },
      "EDIT": {
        "BLADE_TITLE_NEW": "Add New Review",
        "BLADE_TITLE_EXISTING": "Edit Review",
        "HEADER_NEW": "Submit a Review",
        "HEADER_EXISTING": "Update Review"
      }
    }
    // Example for alerts, if needed:
    // "ALERTS": {
    //   "SAVE_SUCCESS": "Review saved successfully.",
    //   "DELETE_CONFIRMATION": "Are you sure you want to delete this review?"
    // }
  }
}
```

**`src/modules/reviews/locales/es.json`** (Example for Spanish):
```json
{
  "MODULE_REVIEWS": {
    "MENU": {
      "TITLE": "Reseñas de Productos",
      "GROUP_MANAGEMENT": "Gestión"
    },
    "PAGES": {
      "LIST": {
        "BLADE_TITLE": "Reseñas de Productos",
        "HEADER": "Gestionar Reseñas",
        "LOADING": "Cargando reseñas...",
        "NO_REVIEWS_FOUND": "No se encontraron reseñas."
      },
      "EDIT": {
        "BLADE_TITLE_NEW": "Añadir Nueva Reseña",
        "BLADE_TITLE_EXISTING": "Editar Reseña",
        "HEADER_NEW": "Enviar una Reseña",
        "HEADER_EXISTING": "Actualizar Reseña"
      }
    }
    // "ALERTS": {
    //   "SAVE_SUCCESS": "Reseña guardada con éxito.",
    //   "DELETE_CONFIRMATION": "¿Estás seguro de que quieres eliminar esta reseña?"
    // }
  }
}
```
These translations can then be used in your components/pages with `$t('MODULE_REVIEWS.PAGES.LIST.HEADER')` after `vue-i18n` is configured and the module's locales are loaded. Remember to use the `useScope: 'global'` with `useI18n()` if your keys are structured this way and merged into the global scope, or adjust your i18n setup if you plan to use module-scoped translations.

With these files and structures in place, the next step is to register the module with your application so its pages become accessible and its features are integrated. This is done in the module's `index.ts` file.

## Module Registration: `createAppModule`

Once you have created the basic structure and components of your module, the final step is to register it with your main VC-Shell application. This is done in the module's `index.ts` file using the `createAppModule` helper function provided by `@vc-shell/framework`.

### Explaining `createAppModule`

The `createAppModule` function is a utility that simplifies the process of integrating your module's various assets (pages, locales, etc.) into the main application. It takes a configuration object that describes your module and returns an object that the framework can use to initialize the module.

### Structuring `index.ts` for a Module

The `index.ts` file in the root of your module directory (e.g., `src/modules/reviews/index.ts`) is where you'll use `createAppModule`.

Here's an example for our "Reviews" module:

**`src/modules/reviews/index.ts`**:
```typescript
import { createAppModule } from "@vc-shell/framework";
// Import BladeInstanceConstructor for typing pages, as shown in modularity.md guide
import type { BladeInstanceConstructor } from "@vc-shell/framework/shared/components/blade-navigation/types";

// 1. Import Pages (Blades)
//    Vue components defined in your module's `pages` directory.
//    The static properties on these components (url, menuItem, permissions)
//    will be used for routing, menu registration, and permissions.
import ReviewListBlade from "./pages/ReviewListBlade.vue";
import ReviewEditBlade from "./pages/ReviewEditBlade.vue";

// 2. Import Locales
//    These are objects where keys are language codes (e.g., 'en', 'es')
//    and values are the imported JSON content for that language.
import enMessages from "./locales/en.json";
import esMessages from "./locales/es.json"; // Example for Spanish

// 3. Import Notification Templates (Optional)
//    If your module has custom Vue components for rendering push notifications.
//    Example: import ReviewNotificationTemplate from "./components/notifications/ReviewNotificationTemplate.vue";

// 4. Import Module-Specific Global Components (Optional)
//    Example: import MyReviewGlobalWidget from "./components/MyReviewGlobalWidget.vue";

// Prepare arguments for createAppModule:

// Pages: An object where keys are typically component names (or other unique identifiers)
// and values are the Vue component constructors for your module's pages.
const pages: Record<string, BladeInstanceConstructor> = {
  ReviewListBlade, // Using the imported component variable name as the key
    ReviewEditBlade,
  // Add other pages from this module here, e.g.:
  // SomeOtherPage: SomeOtherPageImport,
};

// Locales: An object where keys are language codes.
const locales = {
    en: enMessages,
    es: esMessages,
    // Add other languages here
};

// Notification Templates: An object for custom notification renderers.
// Keys are typically component names. Each component should have a static `notifyType` property.
// For this "Reviews" module example, we'll assume none for now.
const notificationTemplates = {};
// Example if we had one:
// const notificationTemplates = {
//   ReviewNotificationTemplate, // Component itself, expecting ReviewNotificationTemplate.notifyType to be set
// };

// Module Components: An object for components to be registered globally.
// Keys are component names, values are component constructors.
// For this "Reviews" module example, we'll assume none for now.
const moduleComponents = {};
// Example if we had one:
// const moduleComponents = {
//  MyReviewGlobalWidget,
// };

// Create the module definition using positional arguments
const reviewsModule = createAppModule(
  pages,
  locales,
  notificationTemplates, // Pass even if empty, or undefined if API handles it
  moduleComponents     // Pass even if empty, or undefined if API handles it
);

// Export the Module
export default reviewsModule;
```

**Breakdown of the `createAppModule` arguments:**

The `createAppModule` function accepts the following arguments in order:

1.  **`pages`** (Required, `Record<string, BladeInstanceConstructor>`)
    *   An object where keys are typically the component names (matching the keys used in the `pages` object passed to `createAppModule`) and values are the Vue component constructors for your module's pages. These pages are often "blades" in VC-Shell terminology.
    *   **Automatic Routing & Blade Properties**: Page components should have static properties defined on them, such as:
        *   `url` (string, optional): Defines the blade's path segment.
            *   **For workspace blades (`isWorkspace: true`)**: This property is **required**, as workspaces are typically entry points accessible via a direct URL.
            *   **For child/non-workspace blades**: This property is **optional**. If provided, the blade can be part of a deep-linked URL (e.g., `/workspace-url/child-url`). If omitted, the blade can only be opened programmatically and will not have its own distinct URL segment. When a URL is resolved, the part of the path following a matched child blade's `url` is passed as the `param` prop to that child blade.
        *   `name` (string, **required**): A unique name for the blade, often matching its component name. This property is **required for all blades** as it's used for programmatic opening (e.g., `useBladeNavigation().openBlade({ blade: { name: 'MyBladeName' } })`) and internal identification.
        *   `menuItem` (object, optional): Configuration if this blade should appear in the application's main navigation menu (e.g., `{ title: 'My Page', icon: 'mdi-icon', permissions: ['my:permission'] }`). See `useMenuService` for details.
        *   `permissions` (string[] | string, optional): Permissions required to access this blade. These are associated with the automatically generated route and checked by `usePermissions` and blade navigation.
        *   `isWorkspace` (boolean, optional): Set to `true` if this blade should function as a top-level workspace.
    *   The framework processes this `pages` object to register routes, integrate with the menu system, and make blades available to the navigation system.

2.  **`locales`** (Optional, `Record<string, object>`)
    *   An object where keys are locale codes (e.g., `"en"`, `"es"`) and values are the corresponding imported JSON-like objects containing translation strings for your module.
    *   **Automatic Merging**: These locales are automatically merged into the global `vue-i18n` instance when the module is registered. This makes them available throughout the application via `$t()` or `useI18n()` (typically with `useScope: 'global'` or if your i18n is configured to merge all module locales into the global scope).

3.  **`notificationTemplates`** (Optional, `Record<string, Component & { notifyType?: string }>`)
    *   An object for registering custom Vue components to be used as templates for specific notification types.
    *   The keys in this object are typically the component names (e.g., `MyCustomNotification`).
    *   Each registered component should have a static property `notifyType` (string) that matches the notification type string it is designed to handle (e.g., `MyCustomNotification.notifyType = 'review-submitted';`).
    *   When a push notification with a matching `notifyType` is received, this custom component will be used for rendering it. See "[Customizing Notifications](./../Essentials/Usage-Guides/customizing-notifications.md)" for more details.

4.  **`moduleComponents`** (Optional, `Record<string, Component>`)
    *   An object where keys are the names under which you want to register the components globally, and values are the Vue component constructors.
    *   **Global Registration**: Components provided here are registered globally using `app.component()`. This is useful for components that are logically part of this module but need to be available for use in templates throughout the entire application or by other modules without explicit import (e.g., a shared widget or a common UI element specific to a suite of modules).

By providing these arguments to `createAppModule`, you declare the core assets of your module, and the framework handles their integration into the main application.

### How Modules Are Loaded into the Main Application

After defining your module in its `index.ts` file and exporting the result of `createAppModule`, you need to register it with your main Vue application instance. This typically happens in your application's entry point, often `src/main.ts`.

The specific way modules are imported and registered can vary based on your project's structure, especially if you are building a package of modules or an application with a specific build process for modules.

A common pattern for loading modules (especially when they are bundled or imported from a specific package) looks like this:

**`src/main.ts`** (Example snippet showing module registration):
```typescript
import { createApp } from "vue";
import App from "./App.vue"; // Or RouterView if used directly
import router from "./router";
import VirtoShellFramework /*, { type FrameworkOptions } */ from "@vc-shell/framework";

// 1. Import all modules from your modules package/directory
// This path will depend on how your modules are structured and exported.
// For example, if you have a local modules directory or a scoped package:
import * as appModules from "./modules"; // Or, e.g., "@my-org/feature-modules"

// ... other imports like locales, bootstrap functions, etc.

const app = createApp(App); // Or createApp(RouterView)

// Initialize VirtoShellFramework first
// Note: The `modules` array in FrameworkOptions is not used in this specific loading pattern.
// Instead, modules are registered individually later.
app.use(VirtoShellFramework, {
  router, // Pass the router instance to the framework
  i18n: {
    locale: import.meta.env.APP_I18N_LOCALE, // Example i18n config
    fallbackLocale: import.meta.env.APP_I18N_FALLBACK_LOCALE,
  },
  // ... other framework options
});

// 2. Register each application module
// The exact structure to access the list of modules might vary.
// In the example, modules are under a `default` export
// from the `appModules` import, and each module itself is also under a `default` export.
if (appModules.default) {
  Object.values(appModules.default).forEach((moduleDefinition: any) => {
    // Ensure you are accessing the correct module object that was returned by createAppModule.
    // It might be moduleDefinition.default if each module file also uses `export default`.
    const moduleToRegister = moduleDefinition.default || moduleDefinition;

    // Pass any necessary options to the module during registration, e.g., the router instance.
    app.use(moduleToRegister, { router });
  });
} else {
  // Fallback or error handling if modules are not found as expected.
  // This structure might also be different, e.g., if appModules itself is the array/object of modules:
  // Object.values(appModules).forEach((moduleToRegister: any) => { ... });
  console.warn("No modules found or modules are not structured as expected.");
}

app.use(router); // Ensure router is used by the app

// ... other app setup like bootstrap, global error handling, mounting ...

// Example: bootstrap(app);
// Example: app.mount("#app");
```

**Key aspects of this loading pattern:**

*   **Centralized Module Import**: Modules are often imported collectively (e.g., `import * as appModules from "./modules";` or a specific package name like `"@my-org/feature-modules"`).
*   **Iterative Registration**: You iterate over the imported modules and register each one with `app.use()`.
*   **Accessing Module Definition**: Pay attention to how the actual module object (the one returned by `createAppModule`) is accessed. If your module files use `export default createAppModule(...)`, and your collective import also wraps them (e.g., in another `default` object), you might need `module.default` or similar to get to the registrable module instance, as seen with `moduleDefinition.default || moduleDefinition` and `appModules.default` in the example.
*   **Passing Options to Modules**: When calling `app.use(moduleToRegister, options)`, you can pass an options object to your module. The example shows passing `{ router }`. If your module's `setup` function (the one *inside* the object passed to `createAppModule`, if you were using that pattern, or a similar mechanism if `createAppModule` itself can accept options for its setup phase) is designed to receive options, this is where they would be provided.

**Important**: The exact import paths and the way you access the list of modules (`appModules.default`, `Object.values(...)`, `moduleDefinition.default`) **must be adapted** to how your specific project and its modules are structured and exported.

By registering your modules this way, their pages, routes, locales, and other assets become available to the application, integrated by the VC-Shell framework and Vue itself.

### Module-Specific Routing

As shown in the `createAppModule` section, when you list your page components (blades) in the `pages` object, the framework automatically handles their route registration based on the `url` property within each page's `defineOptions`.

**How it Works:**

1.  **`defineOptions` in Blades**: Each blade component (e.g., `ReviewListBlade.vue`) uses `defineOptions` to declare its intended URL, unique name, and other metadata.
    ```typescript
    // Inside ReviewListBlade.vue
    defineOptions({
      name: "ReviewListBlade",
      url: "/reviews",       // This becomes the path
      // ... other options
    });
    ```
2.  **`createAppModule`**: When your module is processed via `createAppModule` and subsequently registered in `main.ts`, the framework iterates through the `pages` object.
3.  **Route Generation**: For each page, it generates a Vue Router route record.
    -   The `path` of the route is taken from the `url` in `defineOptions`.
    -   The `name` of the route is typically derived from the `name` in `defineOptions` (e.g., "ReviewListBlade").
    -   The `component` for the route is the page component itself.
    -   Any `props: true` or similar routing options can also be inferred or configured if needed (though `defineOptions` primarily focuses on discoverability and menu integration).
    -   Permissions defined in `defineOptions` are used to automatically add navigation guards if the permissions plugin is active.

**Example Route Registration (Conceptual):**

If `ReviewListBlade.vue` has `url: "/reviews"` and `ReviewEditBlade.vue` has `url: "/review"`, the framework will effectively add routes similar to this to the Vue Router configuration:

```typescript
// Conceptual representation of routes added by the framework
const moduleRoutes = [
  {
    path: "/reviews",
    name: "ReviewListBlade",
    component: ReviewListBlade, // The imported .vue component
    meta: { permissions: ["reviews:view"] } // Example if permissions are set
  },
  {
    path: "/review",
    name: "ReviewEditBlade",
    component: ReviewEditBlade,
    meta: { permissions: ["reviews:edit"] },
  }
];
```

**Accessing Module Pages:**

Once registered, blade pages with a defined `url` become accessible via their URLs (e.g., `your-app.com/reviews` or `your-app.com/review`). Programmatic navigation to blades (whether they have a URL or not) should be done using the `useBladeNavigation` composable to ensure they are correctly integrated into the blade system.

### Module-Specific State Management

For managing state **within** a module, the primary approach is to use Vue 3's Composition API, specifically by creating **composables**.

**Key Principles:**

1.  **Colocation**: Keep composables that manage module-specific state within that module's `composables/` directory. For example, `useReviewList.ts` in our "Reviews" module handles the state and logic for the list of reviews.
2.  **Encapsulation**: Composables should encapsulate their reactive state (`ref`, `reactive`, `computed`) and the methods to modify that state. This makes the state logic self-contained and easier to reason about.
3.  **Reusability within the Module**: These composables can be imported and used by any component or page within the same module that needs access to that particular piece of state or its related logic.

**Example (`useReviewDetails.ts` - a new composable for fetching a single review):**
```typescript
import { ref } from 'vue';
import { useAsync, useApiClient } from '@vc-shell/framework';
// Assume: IReview interface and a specific ReviewDetailsApiClient are defined elsewhere
// and can be imported, similar to useReviewList.ts
import { type IReview, ReviewDetailsApiClient } from '@/api_client'; // Adjust path and names as needed

export function useReviewDetails(reviewId: string | undefined) {
  const review = ref<IReview | null>(null);

  const { getApiClient } = useApiClient(ReviewDetailsApiClient); // Use the actual (hypothetical) client

  const { action: fetchReview, loading: isLoading, error } = useAsync(async () => {
    if (!reviewId) {
      review.value = null;
      return;
    }
    try {
      const client = await getApiClient();
      // Assume client has a method like getReviewById or similar
      review.value = await client.getReviewById(reviewId);
    } catch (err) {
      console.error("Failed to fetch review details:", err);
      review.value = null;
      throw err;
    }
  });

  // Call fetchReview when reviewId changes or on setup if reviewId is present
  // For example, in the component using this composable:
  // watch(() => props.param, (newId) => { if (newId) fetchReview(); }, { immediate: true });
  // or onMounted(() => { if (props.param) fetchReview(); });

  return {
    review,
    isLoading,
    error,
    fetchReview,
  };
}
```
This `useReviewDetails` composable could then be used in `ReviewEditBlade.vue` to load and manage the data for the review being edited.

### Inter-Module Communication

While modules are designed to be self-contained, there are scenarios where one module might need to trigger an action or share a small piece of information with another. It's crucial to manage inter-module communication carefully to avoid creating tight coupling, which undermines the benefits of modularity.

**Recommended Approaches (from most to least coupled):**

1.  **Vue Router Navigation (for Actions/Views):**
    -   If one module needs to navigate to a blade in another module, it can do so using `useBladeNavigation().openBlade()` with the known route name or path (assuming the target module's blade is registered and accessible).
    -   Parameters can be passed via `param` or `options` properties of the `openBlade` function.
    -   **Use Case**: Module A has a button "View Product Details" which navigates to a product details blade in Module B.

2.  **Shared Composables or Services (for Shared State/Logic - Use Sparingly):**
    -   If multiple modules truly need to react to or share the exact same piece of global-like state, you can create a composable in the application-level `src/composables/` directory.
    -   This composable is then imported and used by any module that needs it.
    -   **Caution**: This creates a shared dependency. Only use this for genuinely global state. Avoid using it for module-to-module specific interactions if possible.
    -   **Example**: A `useShoppingCart.ts` in `src/composables/` used by a "ProductListing" module and a "Checkout" module.

**Anti-Patterns to Avoid:**

-   **Directly Importing Components/Composables from *within* another module's `src/modules/another-module/...` path**: This creates tight coupling. If something needs to be shared, it should be explicitly exposed by the source module (e.g., via its `index.ts` if it's a utility meant for wider use, though this is rare for module-to-module specifics) or be promoted to an application-level shared composable/service if its scope is truly global.

Choose the communication strategy that best fits the level of coupling and the nature of the interaction required. Prioritize a clear separation of concerns between modules. Communication from a child blade to its immediate parent should typically be handled via the `parent:call` event mechanism, as described in the blade navigation documentation.

### Props and Emits

Standard props for a blade component often include:

-   `expanded?: boolean`: Controls if the blade is initially expanded (defaults to `true`).
-   `closable?: boolean`: Controls if the blade shows a close button (defaults to `true`).
-   `param?: string`: A generic string parameter you can pass when opening the blade programmatically.
-   `options?: Record<string, any>`: For passing more complex, structured data when opening the blade.

Standard emits for a blade component include:

-   `close:blade`: Emitted when the blade requests to be closed.
-   `expand:blade`: Emitted when the blade is expanded.
-   `collapse:blade`: Emitted when the blade is collapsed.
-   `parent:call`: A crucial emit for communication with the blade that opened this one (if any). It sends an `IParentCallArgs` object (`{ method: string, args?: any }`) to instruct the parent.

#### Exposing the Blade Title

In addition to standard props and emits, a blade component **must** expose its title via `defineExpose` to integrate correctly with the navigation system, particularly `useBreadcrumbs`. This allows the application's breadcrumbs and other navigation elements to display a dynamic, reactive title for the current blade.

**Example:**
```vue
<script setup lang="ts">
import { computed, ref } from 'vue';

const props = defineProps<{ param?: string }>();
const entity = ref({ name: '' }); // Assume this is loaded from an API

// A computed property makes the title reactive
const bladeTitle = computed(() => {
  return props.param ? entity.value.name : 'Create New Entity';
});

// Expose the title for the navigation system
defineExpose({
  title: bladeTitle,
});
</script>
```

### Accessing Blade-Specific Context with `useBlade()`

While `param` and `options` are passed as props to your blade component, VC-Shell provides a more comprehensive way to access the current blade's context through Vue's dependency injection mechanism. You can use `useBlade()` composable to get an `ComputedRef<IBladeInstance>` object.

**Importing `useBlade()`:**

```typescript
import { useBlade } from '@vc-shell/framework';
```

**Using `useBlade()`:**

```typescript
// Inside your blade's <script setup lang="ts">
const currentBlade = useBlade();

if (currentBlade?.value) { // Check if currentBlade and currentBlade.value are defined
  console.log('Current Blade ID:', currentBlade.value.id); // e.g., "revieweditblade"
  console.log('Current Blade Param:', currentBlade.value.param); // Same as props.param
  console.log('Current Blade Options:', currentBlade.value.options); // Same as props.options
  console.log('Is Blade Maximized?:', currentBlade.value.maximized);
  console.log('Blade Title:', currentBlade.value.title);
  // currentBlade.value.navigation contains the blade's navigation object,
  // including its own .instance (a ref to the blade component's exposed members), onOpen, onClose.
}
```

The `IBladeInstance` (accessed via `currentBlade.value`) typically provides the following reactive properties:

*   `id: string`: The unique identifier of the blade instance (usually the component name, lowercased).
*   `param: any`: The `param` object passed when opening the blade.
*   `options: Record<string, any>`: The `options` object passed when opening the blade.
*   `expandable: boolean`: Indicates if the blade can be expanded.
*   `maximized: boolean`: Indicates if the blade is currently maximized.
*   `error?: string`: Any error message associated with the blade.
*   `navigation?: object`: The internal navigation object associated with the blade, which itself can contain an `instance` ref to the blade component for advanced inter-blade communication or control.
*   `breadcrumbs?: Breadcrumbs[]`: An array of breadcrumb items relevant to this blade.
*   `title?: string`: The current title of the blade.

Using `useBlade();` can be particularly useful for accessing properties like `id`, `maximized` state, or the blade's `title` directly within your blade's logic, beyond what's passed via standard props. It provides a richer, reactive view of the blade's current state within the navigation system.

### Blade Lifecycle and Navigation

Blades in VC-Shell have a defined lifecycle, managed by the framework and influenced by user interactions or programmatic calls. Understanding how to hook into these lifecycle moments is key for robust blade development.

**Key Lifecycle Events & Interactions:**

1.  **Opening/Mounting a Blade:**
    *   **Inside the Blade Component**: Use the standard Vue `onMounted` hook to perform actions when the blade component is added to the DOM and becomes visible. This is the place for initial data fetching or setup specific to the blade instance.
        ```typescript
        // Inside your blade's <script setup lang="ts">
        import { onMounted } from 'vue';

        onMounted(() => {
          console.log('Blade has been mounted (opened).');
          // Fetch initial data, set up listeners, etc.
        });
        ```
    *   **For the Caller**: When you open a blade using `useBladeNavigation().openBlade()`, you can provide an `onOpen` callback in the `navigation` options. This function will be executed after the blade component has been successfully mounted.
        ```typescript
        const { openBlade } = useBladeNavigation();
        await openBlade({
          blade: { name: 'MyTargetBlade' },
          onOpen: () => {
            console.log('MyTargetBlade was opened by the navigation system.');
          }
        });
        ```

2.  **Closing/Unmounting a Blade:**
    *   **Inside the Blade Component**: Use the standard Vue `onUnmounted` hook to perform cleanup actions when the blade component is removed from the DOM. This is where you should clean up event listeners, timers, or any other resources.
        ```typescript
        // Inside your blade's <script setup lang="ts">
        import { onUnmounted } from 'vue';

        onUnmounted(() => {
          console.log('Blade has been unmounted (closed).');
          // Cleanup resources, listeners, etc.
        });
        ```
    *   **For the Caller**: Similar to `onOpen`, you can provide an `onClose` callback in the `navigation` options when opening a blade. This function is called when the blade is unmounted (e.g., after it emits `close:blade` and the navigation system processes the closure, or if closed programmatically).
        ```typescript
        const { openBlade } = useBladeNavigation();
        await openBlade({
          blade: { name: 'MyTargetBlade' },
          onClose: () => {
            console.log('MyTargetBlade was closed by the navigation system.');
            // Perform actions after the target blade has closed, e.g., refresh data.
          }
        });
        ```

3.  **Expanding and Collapsing:**
    *   Blades can signal their intent to expand or collapse by emitting `expand:blade` or `collapse:blade` events respectively (typically in response to user interaction with controls within the blade, like header buttons).
    *   The `VcBlade` component itself handles these events and updates its internal state, which can also be reflected in the `maximized` property of the `IBladeInstance` (accessible via `useBlade()`).
    *   If a blade needs to react internally to being expanded or collapsed, it can watch its `expanded` prop (if passed and managed by a parent) or the `maximized` state from its injected `BladeInstance`.

**Programmatic Navigation with `useBladeNavigation`:**

The `useBladeNavigation` composable allows for programmatic control of blades, primarily for opening one blade from another within or between modules. Here's a concise example:

```typescript
import { useBladeNavigation } from '@vc-shell/framework';

// Destructure methods commonly used for basic inter-blade navigation.
const { openBlade, closeBlade } = useBladeNavigation();

// Example: Opening another blade and providing lifecycle callbacks
async function openAnotherBlade(targetId: string) {
  await openBlade({
    blade: { name: 'TargetBladeName' }, // The 'name' from TargetBladeName.vue's defineOptions
    param: targetId,
    options: { openedFrom: 'MyCurrentBlade' },
    // Callbacks are direct properties of the options object
    onOpen: () => console.log('TargetBladeName was opened'),
    onClose: () => console.log('TargetBladeName was closed, perhaps refresh data here.')
  });
}

// Example: Closing the current blade (if needed from within complex logic)
// async function closeThisBladeProgrammatically() {
//   await closeBlade(); // Closes the blade at the top of the navigation stack
// }
```

The `useBladeNavigation` composable offers more functionalities such as `expandBlade`, `collapseBlade`, and provides access to `currentBladeNavigationData` information. These, along with detailed patterns for managing the blade stack, inter-blade communication via `parent:call`, and advanced navigation scenarios, are thoroughly covered in the dedicated navigation guides:

*   **Main Navigation Overview**: [`Essentials/navigation.md`](./../Essentials/navigation.md)
*   **Working with Blade Navigation**: [`Essentials/Usage-Guides/working-with-blade-navigation.md`](./../Essentials/Usage-Guides/working-with-blade-navigation.md)
*   **Blade Navigation**: [`Essentials/shared/components/blade-navigation.md`](./../Essentials/shared/components/blade-navigation.md)

Refer to these guides for a comprehensive understanding of VC-Shell's navigation capabilities.

By using Vue's standard lifecycle hooks (`onMounted`, `onUnmounted`) within your blade components and the callbacks (`onOpen`, `onClose`) provided by `useBladeNavigation` for the calling context, you can effectively manage the lifecycle and behavior of your blades.

