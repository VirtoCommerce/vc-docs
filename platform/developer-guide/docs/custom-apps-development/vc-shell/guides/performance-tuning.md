# Performance Tuning

A VC-Shell app gets fast defaults from the framework: blade-scoped reactivity, lazy module loading through Vite, and a small CSS surface. This guide covers the next layer — what to do once the app grows past a handful of modules and the bundle, the boot, or the runtime starts feeling heavy.

## Measure first

The three numbers that matter for back-office apps:

- **Cold boot.** Time from URL hit to the first blade visible.
- **Blade open.** Time from clicking a menu item to the workspace rendering.
- **Search-to-row.** Time from typing in a list's search box to filtered rows appearing.

Capture these with the browser's Performance tab, three runs each, before and after a change. Anything below 200ms feels instant; anything above 1s feels slow. Optimize what the user notices, not what looks ugly in the source.

## Persist only what helps

`VcDataTable`'s `state-key` persists column visibility, order, and sort to `localStorage`. The persistence is per state-key, app-wide. Two pitfalls:

- **Same state-key across blades.** If two list blades share `state-key="ORDERS"`, they share column state. Use a unique key per logical table, for example, `ORDERS_OPEN` and `ORDERS_ARCHIVED`.
- **Persisting everything by reflex.** Filters that are conceptually per-session do not belong in `localStorage`. Leave them as local state. The persistence layer's payload grows by user, not by app version, and a cluttered `localStorage` makes every blade slower to mount.

A pragmatic test: if a user would expect "I closed and reopened the browser, did my filter survive?" to answer "no", do not persist it.

## Debounce the right things

The sample module wires `useFunctions().debounce` to the search input with a 1000ms delay. Keep this for any input that triggers an API call. For purely client-side filters where the cost is cheap, drop the debounce or shorten it; users notice the lag.

```ts title="OrdersList.vue"
const onSearchList = debounce(async (keyword: string) => {
  await getItems({ ...searchQuery.value, keyword });
}, 1000);
```

For pagination, do not debounce. Users click page numbers expecting an immediate response.

## Avoid waterfalls in onMounted

A details blade that fetches the item, then the lookups, then the related records, serially, is a 3-network-roundtrip blade. Almost always you can parallelize:

```ts title="OrderDetails.vue"
onMounted(async () => {
  if (!param.value) return;
  await Promise.all([
    getItem({ id: param.value }),
    loadCustomers(),
    loadCurrencies(),
  ]);
});
```

The framework does not parallelize for you. The pattern is in the consumer's hands.

## Watch for hidden reactivity costs

Computed properties that touch a large array on every read get expensive when they back a data-table column. Three things to check when a blade feels janky during scroll or filter:

1. **`computed` that maps the entire list.** Move to `shallowRef` for lists with thousands of rows, or compute once and cache.
2. **`watch` with `deep: true` on a list ref.** Replace with a watcher on a derived shallow signal.
3. **Vue DevTools' Components tab during interaction.** Components re-rendering on every key press point at a too-coarse dependency.

## Production build flags

The scaffold ships with sensible defaults, but verify before going to prod:

| File | Setting | Why |
| --- | --- | --- |
| **vite.config.mts** | `build.sourcemap: false`. | Sourcemaps multiply the deployed size and leak source structure. |
| **.env.production** | `APP_ENV=production`. | The framework strips dev-only checks and console output. |
| **vite.config.mts** | `build.chunkSizeWarningLimit: 600`. | The default 500kB warning is noisy for shell apps; raising it suppresses false alarms but keep real outliers visible. |

## Related

- [Build the production module.](build-production-module.md)
- [Deployment.](deployment.md)
- [Best practices.](best-practices.md)
