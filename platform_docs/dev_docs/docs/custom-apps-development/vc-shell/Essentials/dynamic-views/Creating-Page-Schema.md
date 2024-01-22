# Create Page Schema

Dynamic views enable the creation of new blades using a new style called `schemas`. This approach allows the creation of blades without a template. The built-in view types, such as `DynamicBladeList` and `DynamicBladeForm`, come with built-in templates and basic logic, including pagination, validation, etc. Creating a new module involves generating view schemas, composing logic used by these views, and creating additional custom templates if the built-in ones don't meet your requirements. New modules must adhere to a specific folder structure, which we will explore further in this guide.

## Folder Structure

The typical folder structure of modules looks as follows:

```
├─ module                // Custom module
  ├─ components          // Collection of components specific to this module
  │   ├─ notifications   // Dropdown notifications templates
  │   ├─ widgets         // Widgets components
  │   └─ ...             // Other components and custom templates
  ├─ composables         // Collection of shared logic written using Composable API pattern.
  │   ├─ useDetails      // useDetails composable to use with DynamicBladeForm view
  │   └─ useList         // useList composable to use with DynamicBladeList view
  ├─ locales             // Locale files used to provide translated content specific to this module
  ├─ schemaOverride      // Collection of schema overrides for the existing page schemas
  ├─ pages               // Set of module pages schemas
  └─ index.ts            // Module entry point
```

An example folder structure for the Offers module can be found in the `sample/vc-app` folder in the [@vc-shell](https://github.com/VirtoCommerce/vc-shell) repository.

## Create Schema

Dynamic views are built according to these principles:

1. Create a view schema.
2. Create a composable for the view.
3. Create localization files, additional custom templates, and other components used in the view schema, if necessary.

![Readmore](../../../media/readmore.png){: width="25"} [DynamicBladeForm](Dynamic-Blade-Form.md)

![Readmore](../../../media/readmore.png){: width="25"} [DynamicBladeList](Dynamic-Blade-List.md) 

To create a new view, create a new file in the `pages` folder of your module. In this example, we will create a schema for a `DynamicBladeList` view with its own URL. We want to include this view in the navigation menu, add a search bar and multiselect functionality, and have columns for `Name`, `Price`, `Status`, and `Created date`. Additionally, we want to enable sorting on all columns and include a `Create` button in the toolbar.

### Provide view settings

Let's create a file named `list.ts` and add the following view settings:

```typescript
import { DynamicDetailsSchema } from "@vc-shell/framework";

const schema: DynamicDetailsSchema = {
  settings: {
    url: "/my-list",
    id: "List",
    localizationPrefix: "MyList",
    titleTemplate: "My custom list",
    component: "DynamicBladeList",
    composable: "useList",
    isWorkspace: true,
    toolbar: [
      {
        id: "create",
        title: "Create",
        icon: "fas fa-plus",
        method: "create",
      },
    ],
  },
};
```

![Readmore](../../../media/readmore.png){: width="25"} [Schema Settings API](./views/schema-settings.md)


### Provide view content

Now, let's create the `content` for the view. In our case, since we are creating a `DynamicBladeList` view, we need to add `vc-table` as the `content` of the view. For this example, add the following code to the view schema:

```typescript
/**
 * The content of the view.
 */
content: [
  {
    /**
     * The unique ID of the view.
     */
    id: "offers",
    /**
     * The name of the Vue component used by the view.
     */
    component: "vc-table",
    /**
     * Indicates whether the header of `vc-table` is enabled.
     */
    header: true,
    /**
     * Indicates whether multiselect is enabled.
     */
    multiselect: true,
    /**
     * Provide a mobile view component.
     */
    mobileTemplate: {
      component: "MobileGridView",
    },
    /**
     * Provide a not found view component.
     */
    notFoundTemplate: {
      component: "NotFoundGridTemplate",
    },
    /**
     * Provide an empty view component.
     */
    emptyTemplate: {
      component: "EmptyGridTemplate",
    },
    /**
     * Columns settings.
     */
    columns: [
      {
        /**
         * The ID of the column, representing the key in the object of the blade's loaded data
         */
        id: "name",
        /**
         * The title of the column
         */
        title: "Name",
        /**
         * Indicates whether the column is sortable
         */
        sortable: true,
        /**
         * Indicates whether the column is always visible
         */
        alwaysVisible: true,
        /**
         * The type of the column
         */
        type: "text",
      },
      {
        id: "price",
        title: "Price",
        sortable: true,
        alwaysVisible: true,
        type: "text",
      },
      {
        id: "status",
        title: "Status",
        sortable: true,
        alwaysVisible: true,
        type: "text",
      },
      {
        id: "createdDate",
        title: "Created date",
        sortable: true,
        alwaysVisible: true,
        type: "date",
      },
    ],
  },
],
```

!!! note
    Since we specified that we want to use custom templates for the mobile view, empty list, and not found list, we need to create these templates. More details on creating these templates can be found in the [Custom Templates](./custom-templates.md) section.

As a result, we will have a table with columns `Name`, `Price`, `Status`, and `Created date`, as well as the ability for multiselect, search, and custom templates for different table states.

### Register view schema

After creating the view schema, you need to register it in the module. To do this, import the view schema into the `index.ts` file of your module and add it to the `schemas` array:

```typescript
/**
 * Import the view schema created earlier
 */
import * as schema from "./pages";
import { createDynamicAppModule } from "@vc-shell/framework";

/**
 * Register the view schema
 */
export default createDynamicAppModule({
  schema,
  // ...
});
```

Now, if you go to the URL `/my-list`, you will see the table we created earlier.

After creating the schema, create a composable used in the view schema. More details on creating composables can be found in the [Dynamic Views](./Dynamic-Views/views.md) guide.