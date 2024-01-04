# Creating Custom Templates

Custom templates are used to customize the appearance of the dynamic view's to your needs. You can create custom templates for the mobile view, empty list, and not found list. To do this, you need to specify the name of the custom template in the schema of the dynamic view.

!!! note
    To create any custom template mentioned in the schema, you need to create a new file in the `components` folder of your module. For example, if you specified the name `MobileGridView` in the schema, the component export should have the same name. Essentially, custom templates are regular Vue components that can use other components and markup.

## Mobile View Template

The component used as the mobile view template always has incoming parameters - `context`, which is passed from the dynamic view's table.

The `context` prop in Mobile View Template represents the context of the blade's table, containing the data for each specific `item` displayed in the table. It corresponds to a specific object in the table's data array.

Let's look at an example script block for the custom template component `MobileGridView`:

```typescript
<script setup lang="ts">
export interface Props {
  context: {
    item: Record<string, any>;
  };
}

defineProps<Props>();
</script>
```

You can find an example markup for the mobile view template in the `sample/vc-app` repository in the [@vc-shell](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/offers/components/OffersMobileGridView.vue) directory.

## Not Found Grid Template

The component used as the not found list template serves as a placeholder displayed when nothing is found using the search. It has a `reset` event that can be triggered when the `Reset` button in the dynamic view's table is clicked.

Let's look at an example script block for the custom template component `NotFoundGridTemplate`:

```typescript
<script setup lang="ts">
export interface Emits {
  (event: "reset"): void;
}

defineEmits<Emits>();
</script>
```

You can find an example markup for the not found list template in the `sample/vc-app` repository in the [@vc-shell](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/offers/components/OffersNotFoundGridTemplate.vue) directory.

## Empty Grid Template

The component used as the empty list template serves as a placeholder displayed when the list is empty. It has an `add` event that triggers the creation of a new item in the `DynamicBladeForm` view.

Let's look at an example script block for the custom template component `EmptyGridTemplate`:

```typescript
<script setup lang="ts">
export interface Emits {
  (event: "add"): void;
}

defineEmits<Emits>();
</script>
```

You can find an example markup for the empty list template in the `sample/vc-app` repository in the [@vc-shell](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/offers/components/OffersEmptyGridTemplate.vue) directory.

## Status in DynamicBladeForm

The component used as the status template that is displayed in the top right corner of the `DynamicBladeForm` view. It has `context` prop, that is passed from the `DynamicBladeForm` view.

```typescript
<script setup lang="ts">
export interface Props {
    context: Record<string, any>;
}

defineProps<Props>();
</script>
```

You can provide your own status component in the `DynamicBladeForm` view using the `status` option in the `settings` object:

```typescript
export const details: DynamicDetailsSchema = {
  settings: {
    // ...
    status: {
      component: "MpProductStatus",
    },
  },
```

!!! note
    More about `DynamicBladeForm` blade context you can read in the [DynamicBladeForm](./views/DynamicBladeForm.md#dynamicbladeform-blade-context) article.

## Registering Custom Templates

To use custom templates and components in dynamic views, you need to register them in the global component registry. Import them into the `index.ts` file of your module and register them in the global component registry in the initialization method of the dynamic module using the `moduleComponents` option in the `createDynamicAppModule` function:

```typescript
/**
 * Import your custom components and templates
 */
import * as components from "./components";
import { createDynamicAppModule } from "@vc-shell/framework";

export default createDynamicAppModule({
        // ...
        moduleComponents: components,
        // ...
    });
```

After this, all registered components and templates will be available for use in dynamic views.
