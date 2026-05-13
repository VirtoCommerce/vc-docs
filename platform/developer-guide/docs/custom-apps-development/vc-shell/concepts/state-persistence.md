# State Persistence

VC-Shell lets a `VcDataTable` remember its column layout across reloads so users do not have to reset widths and visibility every time they open the same blade.

The mechanism is opt-in. Set a `state-key` prop on the table and persistence turns on. Omit it and the table renders stateless: widths, order, and hidden columns reset to defaults on every mount. There is no global default key, and there is no implicit hash based on column ids. The application chooses what gets remembered by naming it.

The `state-key` doubles as a storage namespace. The framework prepends `VC_DATATABLE_` and uppercases the key, so `state-key="orders"` writes to `VC_DATATABLE_ORDERS`. The composable behind the prop is a single source of truth for table layout across mount cycles: it reads storage eagerly during setup, applies the saved layout to the live column state, and then debounces writes back to storage at 150ms whenever the layout changes. Sort, filters, pagination, selection, and search input are deliberately excluded; the table treats those as session-scoped query state owned by the parent blade.

## What gets persisted

The persisted payload is a `PersistedStateV2` record, written as JSON under the storage key:

| Field              | Type                       | Meaning                                                                  |
| ------------------ | -------------------------- | ------------------------------------------------------------------------ |
| `v`                | `2`                        | Schema version literal.                                                  |
| `order`            | `string[]`                 | Column ids in the user's preferred display order.                        |
| `weights`          | `Record<string, number>`   | Proportional column widths, summing to 1 across visible columns.         |
| `hiddenColumnIds`  | `string[]` (optional)      | Columns the user has hidden via the column switcher.                     |
| `shownColumnIds`   | `string[]` (optional)      | Columns the user has explicitly turned on (when the column switcher distinguishes opt-in columns). |

Widths are stored as weights, not pixel values. The width engine recomputes pixels from weights on every mount, so a layout saved on a wide monitor restores cleanly on a narrow one without horizontal scrollbars or clipped columns.

Sort order, filter values, pagination position, and the search input are not in this payload. If a blade needs them to survive a reload, the blade itself must persist them, typically through the URL query string or a separate store.

![Readmore](../components/data-display/vc-data-table.md){: width="25"} VcDataTable component reference.

## Storage backend

The default backend is `localStorage`. To scope persistence to the browser tab, set `state-storage="session"` and the same payload is written to `sessionStorage` instead.

```vue title="OrdersList.vue"
<VcDataTable
  :items="orders"
  state-key="orders"
  state-storage="session"
/>
```

Both backends share the same key format and the same schema. The storage call is wrapped in a try/catch, so a quota error, a disabled storage API in private mode, or a SecurityError on a sandboxed iframe degrades silently: the table still works, it just stops persisting.

## Keying convention

The storage key is built from the prop value with a fixed transform:

```ts title="useDataTableState.ts"
return key ? `VC_DATATABLE_${key.toUpperCase()}` : null;
```

For an application with several tables, choose keys that describe the table's role, not the page that hosts it. A blade may render the same table on two routes, and a key tied to the route would split state across what users perceive as the same view. Prefix the key with the module name when names might collide across modules: `state-key="marketplace:orders"` becomes `VC_DATATABLE_MARKETPLACE:ORDERS`.

Two tables sharing a key will fight over the same slot. The last one to save wins, and the loser silently picks up the winner's column ids on next mount. Hidden-column lists in particular cause confusing bugs in this situation because columns the user never hid in table A vanish from table A after table B writes.

## Disabling persistence

Omit `state-key`. The composable still runs, but `getStorageKey()` returns `null` and every read and write short-circuits. The table is fully functional. Column resizes, reorders, and hides apply for the current mount and disappear on the next one.

This is the right mode for tables embedded inside a modal, a wizard step, or any short-lived surface where the layout is a one-shot view rather than a workspace the user returns to.

## Schema migration

The composable handles two schema versions. Payloads tagged `v: 2` are applied directly. Payloads tagged `v: 1` (pixel-based widths from an older shell version) are migrated on read: pixels are normalized to weights against the total stored width, then handed to the v2 code path. The migrated state is rewritten on the next save. Anything else — wrong type, missing required field, corrupted JSON, totalPx of zero — is discarded, and the table starts from defaults.

The framework does not run schema migrations for the application's own column changes. When a developer renames a column id, adds a new column, or removes one:

- Removed ids stay in storage but are filtered out on restore because the live column registry no longer contains them.
- Renamed ids are treated as removed-and-added: the user's saved width and position for the old id are dropped, and the new id falls back to its default at the end of the order array.
- Added ids are appended to the saved order with their default weight.

There is no automatic remap from old id to new id. When a schema change is large enough to invalidate stored layouts, bump the `state-key` to discard old state across all users:

```vue title="OrdersList.vue"
<VcDataTable :items="orders" state-key="orders_v2" />
```

The previous `VC_DATATABLE_ORDERS` entry remains in users' browsers until the application clears it explicitly or the user clears site data. It does no harm; it just stops being read.

## Common mistakes

!!! warning "Duplicate `state-key` across blades"
    Every table that opts into persistence needs a key unique within the application. Two tables sharing a key will overwrite each other's saved order, weights, and hidden columns. The conflict is silent until a user notices columns disappearing in one place after they interact with the other.

!!! warning "Saving sensitive filter values"
    Sort and filters are not part of the persisted payload today, but the `state-save` and `state-restore` events expose the full payload to user code. Do not extend persistence by writing filter values into `localStorage` in a `state-save` handler if those filters carry tenant ids, customer emails, or other data that does not belong in browser storage on a shared machine.

!!! warning "Forgetting to bump `state-key` after a schema change"
    Renaming a column id without bumping the key leaves existing users with the new column in its default position and width while the old saved entry is silently dropped. For minor changes this is fine, but for a redesign that swaps multiple columns it produces a layout users do not recognize as theirs. Bump the key to `_v2`, `_v3`, and treat it as part of the migration plan.
