# Your First Blade

Hand-write a one-blade module, register it, open it from the sidebar. The output: a **Reservations** workspace that lists items from a Platform API.

## Module layout

```text
src/modules/reservations/
├─ index.ts                      defineAppModule({ blades, locales }).
├─ pages/
│  ├─ ReservationsList.vue       Workspace blade.
│  └─ index.ts
└─ locales/
   ├─ en.json
   └─ index.ts
```

## List blade

```vue title="src/modules/reservations/pages/ReservationsList.vue"
<template>
  <VcBlade :title="$t('RESERVATIONS.LIST.TITLE')" :loading="loading">
    <VcDataTable
      :items="items"
      :pagination="{ currentPage, pages }"
      :total-count="totalCount"
      :total-label="$t('RESERVATIONS.LIST.TABLE.TOTALS')"
      state-key="RESERVATIONS"
      @row-click="onRowClick"
      @pagination-click="onPageChange"
    >
      <VcColumn id="number" :title="$t('RESERVATIONS.LIST.TABLE.NUMBER')" :sortable="true" />
      <VcColumn id="customerName" :title="$t('RESERVATIONS.LIST.TABLE.CUSTOMER')" />
      <VcColumn id="reservedAt" :title="$t('RESERVATIONS.LIST.TABLE.RESERVED_AT')" type="date" />
      <VcColumn id="status" :title="$t('RESERVATIONS.LIST.TABLE.STATUS')" />
    </VcDataTable>
  </VcBlade>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import {
  useApiClient, useAsync, useBlade,
  VcBlade, VcColumn, VcDataTable,
} from "@vc-shell/framework";
import { ReservationClient, type Reservation } from "../../../api_client/reservations";

defineBlade({
  name: "ReservationsList",
  url: "/reservations",
  isWorkspace: true,
  menuItem: {
    title: "RESERVATIONS.MENU.TITLE",
    icon: "lucide-calendar-check",
    priority: 30,
  },
});

const { openBlade, exposeToChildren } = useBlade();
const { getApiClient } = useApiClient(ReservationClient);

const items = ref<Reservation[]>([]);
const totalCount = ref(0);
const currentPage = ref(1);
const pageSize = 20;

const { loading, action: load } = useAsync(async () => {
  const client = await getApiClient();
  const result = await client.searchReservations({
    skip: (currentPage.value - 1) * pageSize,
    take: pageSize,
    sort: "reservedAt:DESC",
  });
  items.value = result.results ?? [];
  totalCount.value = result.totalCount ?? 0;
});

const pages = computed(() => Math.max(1, Math.ceil(totalCount.value / pageSize)));

function onRowClick(event: { data: Reservation }) {
  openBlade({ name: "ReservationDetails", param: event.data.id });
}

async function onPageChange(page: number) {
  currentPage.value = page;
  await load();
}

exposeToChildren({ reload: load });
defineExpose({ reload: load, title: "Reservations" });

onMounted(load);
</script>
```

Three things to notice:

- `defineBlade` is a Vite-time macro. It rewrites the script so that the blade's config lands in `BladeRegistry` before mount.
- `useBlade()` gives you `openBlade` (works inside and outside blade context) and `exposeToChildren` (so a future details blade can `callParent("reload")`).
- `useApiClient` + `useAsync` is the standard data-loading pattern; `loading` flows directly into `<VcBlade :loading>`.

## Locale bundle

```json title="src/modules/reservations/locales/en.json"
{
  "RESERVATIONS": {
    "MENU": { "TITLE": "Reservations" },
    "LIST": {
      "TITLE": "Reservations",
      "TABLE": {
        "NUMBER": "Number",
        "CUSTOMER": "Customer",
        "RESERVED_AT": "Reserved at",
        "STATUS": "Status",
        "TOTALS": "Total reservations"
      }
    }
  }
}
```

```ts title="src/modules/reservations/locales/index.ts"
import en from "./en.json";
export { en };
```

!!! tip "Always namespace under your module name"
    Every locale key gets merged into the global `vue-i18n` instance. Without `RESERVATIONS.` as a prefix, two modules collide on `MENU.TITLE`.

## Module entry

```ts title="src/modules/reservations/pages/index.ts"
export { default as ReservationsList } from "./ReservationsList.vue";
```

```ts title="src/modules/reservations/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as blades from "./pages";
import * as locales from "./locales";

export default defineAppModule({ blades, locales });

export * from "./pages";
```

## Install in the app

```ts title="src/main.ts" hl_lines="2 6"
import VirtoShellFramework from "@vc-shell/framework";
import Reservations from "./modules/reservations";
// ...
const app = createApp(RouterView);
app.use(VirtoShellFramework, { router });
app.use(Reservations);
app.use(router);
```

`npx @vc-shell/create-vc-app add-module reservations` applies these edits automatically.

## Run

```bash
yarn serve
```

Sign in. A **Reservations** entry with the calendar icon appears in the sidebar at priority 30. Click it: the workspace blade opens, the data table loads, and clicking a row tries to open a `ReservationDetails` blade — that does not exist yet.

## Troubleshooting

!!! warning "Menu item missing"
    The blade has no `url`, or no `menuItem`, in `defineBlade`. Both are required to register a menu entry.

!!! warning "Blade silently replaced by another module's"
    Blade names are global in `BladeRegistry`. Prefix with the module domain (`ReservationsList`, not `List`).

!!! warning "Translation key shows as a raw string"
    The locale bundle did not merge. Confirm `locales` is passed to `defineAppModule` and the `en` key matches the env's `APP_I18N_LOCALE`.

![Readmore](../concepts/blade-navigation.md){: width="25"} Blade navigation in depth.

## What to try next

- **Add a details blade.** Create `ReservationDetails.vue` without `url` and `menuItem`. Pass `param` from the list. Wire `callParent("reload")` into the save handler.
- **Drop the menu item.** Remove `menuItem` from the config. The blade stays navigable via deep link (`/reservations`) and programmatic `openBlade({ name: "ReservationsList", isWorkspace: true })`.
- **Add a toolbar action.** Use `useToolbar()` to register a `New reservation` button that opens `ReservationDetails` in create mode (no `param`).
