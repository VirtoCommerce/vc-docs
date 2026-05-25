# Test a VC-Shell Module

This guide sets up unit tests for a VC-Shell module using Vitest and Vue Test Utils, then walks through three common test patterns: a composable that wraps `useApiClient`, a list blade, and a details blade with form validation. The scaffold does not ship a test runner by default; you add one once and reuse the setup across modules.

## Install the test runner

From the root of your VC-Shell app:

```bash
yarn add -D vitest @vue/test-utils jsdom @testing-library/jest-dom
```

Add a Vitest config in **vitest.config.ts**:

```ts title="vitest.config.ts"
import { defineConfig } from "vitest/config";
import vue from "@vitejs/plugin-vue";
import path from "node:path";

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./vitest.setup.ts"],
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});
```

```ts title="vitest.setup.ts"
import "@testing-library/jest-dom/vitest";
```

Add a script in **package.json**:

```json title="package.json"
"scripts": {
  "test": "vitest"
}
```

## Pattern 1: a data composable

A composable that calls `useApiClient` is the most common unit to test. Mock the client and assert that your composable shapes the response correctly.

```ts title="src/modules/orders/composables/useOrders/index.test.ts"
import { describe, it, expect, vi } from "vitest";
import { ref } from "vue";
import useOrders from ".";

vi.mock("@vc-shell/framework", async (orig) => {
  const actual = await orig<typeof import("@vc-shell/framework")>();
  return {
    ...actual,
    useApiClient: () => ({
      getApiClient: () =>
        Promise.resolve({
          searchOrders: vi.fn().mockResolvedValue({
            results: [{ id: "o-1", number: "RDR-001" }],
            totalCount: 1,
          }),
        }),
    }),
  };
});

describe("useOrders", () => {
  it("loads orders into data ref", async () => {
    const orders = useOrders();
    await orders.getItems({});
    expect(orders.data.value).toHaveLength(1);
    expect(orders.totalCount.value).toBe(1);
  });
});
```

The pattern is module-scoped `vi.mock` plus a thin factory that returns a stub for the methods the composable touches. Do not mock the entire framework; carry through `actual` so unrelated exports still resolve.

## Pattern 2: a list blade

A list blade composes a `useList` composable with `VcDataTable`, search, and pagination. The interesting tests are the user-visible behaviors: clicking a row opens a details blade, search debounces, the toolbar's remove button disables when nothing is selected.

```ts title="src/modules/orders/pages/list.test.ts"
import { describe, it, expect, vi } from "vitest";
import { mount } from "@vue/test-utils";
import OrdersList from "./list.vue";

const openBlade = vi.fn();

vi.mock("@vc-shell/framework", async (orig) => {
  const actual = await orig<typeof import("@vc-shell/framework")>();
  return {
    ...actual,
    useBlade: () => ({
      param: { value: undefined },
      openBlade,
      exposeToChildren: vi.fn(),
    }),
  };
});

describe("OrdersList", () => {
  it("opens details on row click", async () => {
    const wrapper = mount(OrdersList);
    // Wait for useList to resolve mock data...
    await wrapper.find('[data-test-row="o-1"]').trigger("click");
    expect(openBlade).toHaveBeenCalledWith(
      expect.objectContaining({ name: "OrderDetails", param: "o-1" }),
    );
  });
});
```

Selectors like `data-test-row` are worth adding to your templates. CSS classes and structural selectors drift; `data-test-*` attributes do not.

## Pattern 3: a details blade with validation

For details blades, the high-value tests cover form rules: required-field validation, save-button enable state, and the save-then-reload flow.

```ts title="src/modules/orders/pages/details.test.ts"
import { describe, it, expect, vi } from "vitest";
import { mount } from "@vue/test-utils";
import OrderDetails from "./details.vue";

vi.mock("./../composables", () => ({
  useDetails: () => ({
    item: { value: { id: undefined, number: "" } },
    loading: { value: false },
    isModified: { value: false },
    saveItem: vi.fn(),
    removeItem: vi.fn(),
    getItem: vi.fn(),
  }),
}));

describe("OrderDetails", () => {
  it("disables Save when form is pristine", async () => {
    const wrapper = mount(OrderDetails);
    const saveButton = wrapper.find('[data-test-action="save"]');
    expect(saveButton.attributes("disabled")).toBeDefined();
  });
});
```

For richer assertions on validation messages, type into the field and let vee-validate flush its async rule queue with `await flushPromises()`.

## What to test, what to skip

| Worth testing | Skip |
| --- | --- |
| Composables that shape API responses or coordinate side effects. | Pure rendering of VC components -- they are tested in the framework. |
| Click handlers that open blades, save data, or trigger destructive actions. | Internal blade-navigation mechanics. |
| Form validation rules and save-button enable conditions. | The `@vc-shell/framework` exports themselves. |
| Permission checks that gate UI. | Vue Router setup; trust the framework's router integration. |

## Related

- [useApiClient composable.](../composables/data/useApiClient.md)
- [Best practices.](best-practices.md)
