<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: core/composables/useMenuExpanded/index.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# useMenuExpanded

Manages the sidebar menu expanded/collapsed and hover-expanded state with localStorage persistence. This is the low-level composable that powers the sidebar pin/unpin behavior in the vc-shell admin UI. It tracks two independent states: the permanent "pinned" state (persisted across sessions) and the transient "hover-expanded" state (active only while the user hovers over a collapsed sidebar).

## When to Use

- Low-level control over sidebar pin and hover state
- Building a custom sidebar component that needs expand/collapse persistence
- When NOT to use: prefer `useSidebarState` which wraps this composable and adds mobile menu support, derived `isExpanded` computed, and responsive breakpoint handling

## Basic Usage

```typescript
import { useMenuExpanded } from "@vc-shell/framework";

const { isExpanded, toggleExpanded, isHoverExpanded, toggleHoverExpanded } = useMenuExpanded();

// Toggle pin state (persisted to localStorage)
toggleExpanded();

// Hover expand with 200ms delay
toggleHoverExpanded(true); // opens after delay
toggleHoverExpanded(false); // closes immediately
```

## API

### Returns

| Property              | Type                               | Description                                                      |
| --------------------- | ---------------------------------- | ---------------------------------------------------------------- |
| `isExpanded`          | `Ref<boolean>`                     | Pinned state, persisted via `useLocalStorage`                    |
| `toggleExpanded`      | `() => void`                       | Toggle the pinned state                                          |
| `isHoverExpanded`     | `Ref<boolean>`                     | Temporary hover expansion (not persisted)                        |
| `toggleHoverExpanded` | `(shouldExpand?: boolean) => void` | Set hover state; opening has a 200ms delay, closing is immediate |

## Recipe: Custom Sidebar with Hover Expand

A common pattern is binding mouse events on the sidebar rail so the menu previews its full width on hover, without permanently pinning it open:

```vue
<script setup lang="ts">
import { computed } from "vue";
import { useMenuExpanded } from "@vc-shell/framework";

const { isExpanded, toggleExpanded, isHoverExpanded, toggleHoverExpanded } = useMenuExpanded();

// The sidebar is visually expanded if pinned OR hover-expanded
const isVisuallyExpanded = computed(() => isExpanded.value || isHoverExpanded.value);
</script>

<template>
  <aside
    :class="{ 'sidebar--expanded': isVisuallyExpanded }"
    @mouseenter="toggleHoverExpanded(true)"
    @mouseleave="toggleHoverExpanded(false)"
  >
    <nav>
      <!-- menu items -->
    </nav>
    <button @click="toggleExpanded">
      {{ isExpanded ? "Unpin" : "Pin" }}
    </button>
  </aside>
</template>
```



## Tips

- If you call `toggleHoverExpanded(true)` and then `toggleHoverExpanded(false)` within the 200ms window, the expansion is canceled -- the timeout is cleared before it fires.
- The composable does not handle mobile breakpoints. For responsive behavior, use `useSidebarState` instead, which combines `useMenuExpanded` with mobile detection.
- Each call to `useMenuExpanded()` creates a new instance with its own timeout tracking, but they share the same localStorage-backed `isExpanded` ref (via `useLocalStorage`). Multiple instances will stay in sync for the pinned state.

## Related

- `useSidebarState` -- higher-level composable that adds mobile menu and derived `isExpanded` computed
