# Overview
This type of view enables the creation of blades containing a tabular list. Here is a list of features for this view:

1. Built-in pagination
2. Filters
3. Multiselect
4. Reorderable rows
5. Search field
6. Ability to create a custom mobile view template
7. Ability to create a custom empty list template
8. Ability to create a custom not-found list template

## Creating a composable for DynamicBladeList
To create a composable for `DynamicBladeList`, you need to use the built-in composable factory function named `useListFactory`. This factory returns a composable method that provides you with all the necessary methods and properties to work with the list.

### useListFactory API
The `useListFactory` function returns an object with the following properly typed properties:

| Property   | Type                        | Description                                              |
| ---------- | --------------------------- | -------------------------------------------------------- |
| `items`    | `ComputedRef<Items>`         | The readonly list of items loaded after running `load`. |
| `query`    | `Ref<Query>`                  | The query object used to load data.                       |
| `loading`  | `Ref<boolean>`                | Indicates whether the data is loading.                    |
| `pagination` | `ComputedRef<Pagination>`    | The pagination object containing currentPage, totalCount, pageSize, pages. |
| `load`     | `AsyncAction<Query>` | The method used to load data.                        |
| `remove`   | `AsyncAction<CustomQuery>` | The method used to remove data.                    |

This function accepts an object with callback methods `load` and `remove`, which you should implement. The `load` method is used to load data for the list, and the `remove` method is used to remove data from the list.

!!! note
    The `load` and `remove` methods must return a promise.

### Composable Anatomy

#### Implementing composable from `useListFactory`

Let's create a file named `useList.ts` in the `composables` folder of your module and add the following code:

```typescript
import { useListFactory, UseList } from "@vc-shell/framework";

const useList = (): UseList => {
    const factory = useListFactory({
        load: async (query) => {
            // return your load method here
        },
        remove: async (query, customQuery) => {
            // return your remove method here
        },
    });

    const { items, load, remove, loading, pagination, query } = factory();

    return {
        items,
        load,
        remove,
        loading,
        pagination,
        query,
    };
}
```

To implement the `load` and `remove` methods, you need to use `useApiClient` composable from `@vc-shell/framework` package. This composable returns a `getApiClient` method, that provides you with an  instance of the API client class, which you can use to make requests to your API.

Let's look at an example of using the `useApiClient` method with `useListFactory` in the `useList` composable:
```typescript
import { useApiClient } from "@vc-shell/framework";
import { SomeClient } from "@your-api-package";

const { getApiClient } = useApiClient(SomeClient);

export const useList = (): UseList => {
    const factory = useListFactory({
        load: async (query) => {
            return (await getApiClient()).someSearchFn(query);
        },
        remove: async (query, customQuery) => {
            return (await getApiClient()).someRemoveFn(query);
        },
    });
}
```

!!!note
    As you can see, this callback methods has arguments - `query` in `load` and `query, customQuery` in `remove`. These arguments are used to pass the query parameters to your API client. `useListFactory` also returns a `query` property, which contains the query parameters passed to the methods.

With the use of `useListFactory`, you get a ready-to-use composable, which already has all the necessary methods and properties to work with the list. All you need to do is just to implement the `load` and `remove` methods. Also you can add your own logic, methods and properties to the composable, as in other composable functions.

Since the `useListFactory` method is generic, you can provide your own types for your loaded `items` and `query` from your API client. Lets look at an example based on Offers module from `vc-app`:

```typescript
useListFactory<Offer[], ISearchOffersQuery>(
    // ...
)
```

`UseList` interface is also a generic type that accepts your loaded `Items`,  `Query` and your `scope` types:

```typescript
UseList<Offer[], ISearchOffersQuery, OffersListScope>
```

!!! note
    More information about `scope` can be found in the [Blade Scope](#blade-scope) section.

This allows you to get proper typing of your composable and data.

#### Access to Blade Component Props and Events
All composables created for dynamic views have incoming parameters by default, which are passed from the dynamic views component:

1. `props` - the `props` object of the dynamic views component, which includes all blade parameters.
2. `emit` - the `emit` object of the dynamic views component, which includes all blade events that it can emit.
3. `mounted` - a reactive value that returns `true` if the dynamic views component has been mounted, otherwise `false`.

To obtain types, you also need to import `DynamicBladeList`. It looks like this:

```typescript
import { Ref } from "vue";
import { DynamicBladeList } from "@vc-shell/framework";

const useList = (args: {
    props: InstanceType<typeof DynamicBladeList>["$props"];
    emit: InstanceType<typeof DynamicBladeList>["$emit"];
    mounted: Ref<boolean>;
}) => {
    // your composable code here
}
```

Thanks to this, you always have access to all incoming blade parameters and can use events `emit` directly from your composable.

#### Blade Scope
Each composable created for dynamic views can have a special variable - `scope`, which can contain all additional methods, computed values, reactive variables, toolbar overrides that you want to use in your blade.

To use `scope`, you need to return it from your composable:

```typescript
const useList = (args: // ...): UseList => {
    const scope = ref<ListScope>({
        // your scope here
    });

    return {
        // ...,
        scope: computed(() => scope.value),
    }
}
```

Also, you need to create an interface, for example, `ListScope`, which should extend from the `ListBaseBladeScope` interface to provide type-check for the `scope` and should include all additional methods, computed values, reactive variables, toolbar overrides that you want to use in your blade:

```typescript
import { ListBaseBladeScope } from "@vc-shell/framework";

interface ListScope extends ListBaseBladeScope {
    // scope types here
}
```

!!! note
    The `ListBaseBladeScope` interface has an `openDetailsBlade` method that you should implement. This method is used to open the details blade for the selected item.

#### `openDetailsBlade` Method

If you want to open the details blade for a selected item, you should implement the `openDetailsBlade` method and add it to your `scope` object. With the use of the `openDetailsBlade` method, you can pass additional options to the details blade.

The base implementation looks like this:

```typescript
const useList = (args: // ...): UseList => {
    const { openBlade, resolveBladeByName } = useBladeNavigation();

    function openDetailsBlade(data?: Omit<Parameters<typeof openBlade>["0"], "blade">) {
        openBlade({
            blade: resolveBladeByName("YourDetailsBladeName"),
            options: {
                // any options you want to pass to the details blade
            },
            ...data,
        });
  }

    const scope = ref<ListScope>({
        openDetailsBlade,
    });

    return {
        // ...,
        scope: computed(() => scope.value),
    }
}
```

#### `toolbarOverrides` object

When you define toolbar object in schema, you probably want to add some custom actions to it or change its visibility or disabled state. To do this, you can use `toolbarOverrides` object in your `scope`:

```typescript
const useList = (args: // ...): UseList => {
    const scope = ref<ListScope>({
        // ...
        toolbarOverrides: {
            // your toolbar overrides here
        },
    });
}
```

!!! note
    More information about toolbar creation can be found in the [Toolbar schema creation](./../toolbar.md#toolbar-schema-creation) section.

#### Default toolbar buttons

`DynamicBladeList` has a built-in toolbar buttons, which you can use. All this toolbar button objects has methods, visibility and disabled state already implemented, so you just need to add in in your view schema. Also you can override this methods in `toolbarOverrides` object by its names.

This method names are: `openAddBlade`, `refresh`, `removeItems`, `save`

!!! note
    More information about toolbar overriding can be found in the [Overriding default toolbar methods and properties](./../toolbar.md#overriding-default-toolbar-methods-and-properties) section.

## DynamicBladeList Blade Context
`DynamicBladeList` blade context is an object that contains all methods and properties, returned from composable and settings from view schema.

## DynamicBladeList API
This view is implemented using the `DynamicGridSchema` interface, which includes `settings` and `content`:

```typescript
interface DynamicGridSchema {
  settings: SettingsGrid;
  content: [ListContentSchema];
}
```

| Property   | Type               | Description          |
| ---------- | ------------------ | -------------------- |
| `settings` | `SettingsGrid`       | The settings of the view. |
| `content`  | `ListContentSchema[]`| The content of the view. |

### SettingsGrid
`SettingsGrid` is an extension of `SettingsBase` with additional settings for `DynamicBladeList`:

```typescript
interface SettingsGrid extends SettingsBase {
  component: "DynamicBladeList";
}
```

### ListContentSchema
`ListContentSchema` is an interface that contains settings for the tabular list:

```typescript
interface ListContentSchema {
  id: string;
  component: "

vc-table";
  filter?: FilterSchema;
  multiselect?: boolean;
  header?: boolean;
  columns?: (ITableColumns & {
    id: string;
    title: string;
    sortable?: boolean;
    alwaysVisible?: boolean;
    type?: string;
    customTemplate?: GridTemplateOverride;
  })[];
  reorderableRows?: boolean;
  mobileTemplate?: {
    component: string;
  };
  notFoundTemplate?: {
    component: string;
  };
  emptyTemplate?: {
    component: string;
  };
}
```

| Property          | Type                                                                                                 | Description                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `id`              | `string`                                                                                               | The unique ID of the view.                            |
| `component`       | `"vc-table"`                                                                                           | The name of the Vue component used by the view.        |
| `filter`          | `FilterSchema`                                                                                        | The filter settings.                                  |
| `multiselect`     | `boolean`                                                                                              | Indicates whether multiselect is enabled.             |
| `header`          | `boolean`                                                                                              | Indicates whether the header of `vc-table` is enabled. When `true` - enables the search bar and provides the possibility to use `Filter`. |
| `columns`         | `(ITableColumns & { id: string; title: string; sortable?: boolean; alwaysVisible?: boolean; type?: string; customTemplate?: GridTemplateOverride; })[]` | The columns settings.                             |
| `reorderableRows` | `boolean`                                                                                              | Indicates whether reorderable rows are enabled.        |
| `mobileTemplate`  | `{ component: string; }`                                                                              | The mobile template settings. The component must be registered globally. |
| `notFoundTemplate`| `{ component: string; }`                                                                              | The not found template settings. The component must be registered globally.|
| `emptyTemplate`   | `{ component: string; }`                                                                              | The empty template settings. The component must be registered globally.|

### FilterSchema
`FilterSchema` is an interface that contains settings for filters:

```typescript
type FilterSchema = FilterCheckbox | FilterDateInput
```

At the moment, two types of filters are supported: `FilterCheckbox` and `FilterDateInput`, which we will discuss in the following sections.

#### FilterCheckbox
`FilterCheckbox` is an interface that contains settings for checkbox filters:

```typescript
type FilterCheckbox = {
  columns: {
    title: string;
    controls: {
        field: string;
        component: "vc-checkbox";
        data?: { value: string; displayName: string }[];
    }[];
  }[];
};
```

Since filters represent columns with their own title and controls, they can be multiple. Let's look at the settings for the `FilterCheckbox` control:

| Property       | Type                                             | Description                                                      |
| -------------- | ------------------------------------------------ | ---------------------------------------------------------------- |
| `field`        | `string`                                           | Name of the property that we want to pass for filtering          |
| `component`    | `"vc-checkbox"`                                    | Component used in the schema                                     |
| `data`         | `{ value: string; displayName: string }[]` | Array of objects that represent data for checkbox. `value` - value of the checkbox, `displayName` - text that will be displayed near the checkbox |

Let's consider an example of using the `FilterCheckbox` filter. To do this, create a `filter` object in the `vc-table` component schema:

```typescript
filter: {
        columns: [
          {
            id: "statusFilter",
            title: "Status filter",
            controls: [
              {
                id: "statusCheckbox",
                field: "status",
                component: "vc-checkbox",
                data: [
                  {
                    value: "None",
                    displayName: "None",
                  },
                  { value: "Published", displayName: "Published" },
                  { value: "HasStagedChanges", displayName: "Has staged changes" },
                  { value: "WaitForApproval", displayName: "Wait for approval" },
                  { value: "RequiresChanges", displayName: "Requires changes" },
                  { value: "Rejected", displayName: "Rejected" },
                ],
              },
            ],
          },
        ],
      },
```

As a result, you will get the following result:

![FilterCheckbox](./../../../../media/filter-checkbox.png)

When one or more values of the filter are selected, their `value` will be recorded in the `status` field, which will be passed to the `query` when requesting data.

#### FilterDateInput

`FilterDateInput` is an interface that contains settings for date input filters:

```typescript
type FilterDateInput = {
  columns: {
    title: string;
    controls: {
      field: string;
      component: "vc-input";
      label?: string;
    }[];
  }[];
};
```

Since filters represent columns with their own title and controls, they can be multiple. Let's look at the settings for the `FilterDateInput` control:

| Property       | Type             | Description                              |
| -------------- | ---------------- | ---------------------------------------- |
| `field`        | `string`           | Name of the property that we want to pass for filtering |
| `component`    | `"vc-input"`       | Component used in the schema             |
| `label`        | `string`           | Text that will be displayed as input label. |

