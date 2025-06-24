# useBeforeUnload Composable

The `useBeforeUnload` composable provides a simple way to prevent users from accidentally navigating away from a page or closing a tab when they have unsaved changes. It leverages the browser's `beforeunload` event to prompt users with a confirmation dialog if they attempt to leave with modified data.

This composable is particularly useful in forms and editors where users might lose unsaved work if they accidentally navigate away. When the modified state is `true`, the browser will display a standard confirmation dialog asking users if they really want to leave the page.

## API Reference

### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `modified` | `ComputedRef<boolean>` | A computed reference to a boolean value indicating whether the content has been modified and has unsaved changes. |

### Return value

The `useBeforeUnload` composable returns an object with the following property:

```typescript
interface UseBeforeUnloadReturn {
  modified: ComputedRef<boolean>;  // The same modified state that was passed in
}
```

## Usage

```typescript
import { computed } from 'vue';
import { useBeforeUnload } from '@vc-shell/framework';

const isModified = computed(() => {
  // Your logic to determine if content has been modified
  return hasUnsavedChanges.value;
});

useBeforeUnload(isModified);
```

## How it works

The `useBeforeUnload` composable:

1. **Event Listener Management**: Adds a `beforeunload` event listener when the component mounts and removes it when unmounted
1. **Conditional Prevention**: Only triggers the browser confirmation dialog when the `modified` computed ref returns `true`
1. **Browser Integration**: Uses the native browser `beforeunload` event to show confirmation dialogs

When the modified state is `true` and the user attempts to navigate away or close the tab, the browser displays a standard confirmation dialog.

## Browser behavior

- **Dialog Text**: Browsers use standardized confirmation text for security reasons (custom messages are ignored)
- **User Interaction**: Some browsers only show the dialog if the page has been interacted with
- **Mobile Support**: Mobile browsers may handle the event differently or not show dialogs
- **Multiple Instances**: If multiple `useBeforeUnload` instances are active, only one dialog appears


