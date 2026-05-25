# State Machine Actions in Vendor Portal

The Vendor Portal provides vendor-facing state machine functionality, allowing vendors and external users to interact with workflows through a modern, responsive interface. This document explains how to integrate state machine actions into customer portals, implement permitted triggers, and create intuitive user experiences for workflow management.

The following example demonstrates how to implement state machine actions for product details in the Vendor Portal. It covers querying the state machine instance, refreshing the toolbar with permitted triggers, and handling trigger execution with real-time UI updates:

```typescript
...
// import classes and composables
import {
  StateMachineClient,
  GetStateMachineInstanceForEntityQuery,
  StateMachineInstance,
} from "@vcmp-vendor-portal/api/statemachine";

import { useStateMachines } from "../../../state-machines/composables";
...
export interface ProductDetailsScope extends DetailsBaseBladeScope {
...
  // define toolbar overrides
  toolbarOverrides: {
    ...
    stateMachineComputed: ComputedRef<IBladeToolbar[]>;
  };
}
...
const { getApiClient: getStateMachineApiClient } = useApiClient(StateMachineClient);
...
export function useProductDetails(...) {
...
  const stateMachineInstance = ref<StateMachineInstance>();
  const stateMachineLoading = ref(false);
  const toolbar = ref([]) as Ref<IBladeToolbar[]>;
  const { fireTrigger } = useStateMachines();

  // on load product - query state machine and call refresh toolbar
  const detailsFactory = useDetailsFactory<ISellerProduct & IProductDetails>({
    load: async (item) => {
      if (item?.id) {
        const resItem = await (await getApiClient()).getProductById(item.id);
        const resModel = await createModel(resItem);

        const publicationrequestId: string = resModel.publicationRequests[0].id!;
          stateMachineInstance.value = await (
            await getStateMachineApiClient()
          ).getStateMachineForEntity(
            new GetStateMachineInstanceForEntityQuery({
              entityId: publicationrequestId,
              entityType: "VirtoCommerce.MarketplaceVendorModule.Core.Domains.ProductPublicationRequest",
              locale: currentLocale.value,
            }),
          );
          refreshToolbar(stateMachineInstance.value ?? {});
        }
        return resModel;
      }
    },
    ...
  });

  // refresh toolbar
  const refreshToolbar = (sm: StateMachineInstance) => {
    toolbar.value.splice(0);

    sm?.currentState?.transitions?.forEach((transition, index) => {
      if (sm?.permittedTriggers?.includes(transition.trigger!)) {
        toolbar.value.push({
          id: transition.trigger,
          title: transition.localizedValue ?? transition.trigger,
          icon: transition.icon ?? "grading",
          disabled: computed(() => stateMachineLoading.value),
          separator: index === 0 ? "left" : undefined,
          async clickHandler() {
            try {
              stateMachineLoading.value = true;
              const currentStateMachine = await fireTrigger(sm.id!, transition.trigger!, sm.entityId!);
              args.emit("parent:call", {
                method: "reload",
              });
              //item.value!.status = transition.toState;
              validationState.value.resetModified(item.value, true);
              refreshToolbar(currentStateMachine);
            } catch (error) {
              console.error(error);
            } finally {
              stateMachineLoading.value = false;
            }
          },
        });
      }
    });
  };

  // override toolbar in scope
  const scope: ProductDetailsScope = {
    ...
    toolbarOverrides: {
      // other toolbar buttons
      ...
      // state machine buttons
      stateMachineComputed: computed(() => toolbar.value),
    },
  };

  // other part of blade logic
  ...
```

### Page implementation

The page component uses the `DynamicDetailsSchema` to configure the product details blade, including toolbar integration:

```typescript
import { DynamicDetailsSchema } from "@vc-shell/framework";

export const details: DynamicDetailsSchema = {
  settings: {
    url: "/product",
    id: "Product",
    localizationPrefix: "Products",
    composable: "useProductDetails",
    component: "DynamicBladeForm",
    toolbar: [
      // other toolbar buttons
      ...
      // state machine computed actions
      {
        id: "stateMachineComputed",
        method: "stateMachineComputed",
      },
    ],
    // other component content
    ...
  }
}
```

In the Vendor Portal, the applied modifications look as follows:

![Product Publication actions in Vendor Portal](media/vendor-product-publication-actions.png){: style="display: block; margin: 0 auto;" width="500"}

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../operator-portal-actions">← Operator Portal actions</a>
</div>