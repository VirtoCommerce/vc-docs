# useAsync Composable

The `useAsync` composable provides a structured way to handle asynchronous operations in Vue components while managing loading states. It helps simplify working with asynchronous API calls, data fetching, and other operations that involve promises.

The primary purpose of `useAsync` is to encapsulate the loading state management around an asynchronous function (`innerAction`). It does **not** inherently handle data assignment or error display logic; this responsibility remains within the `innerAction` or the calling context.

## Core behavior

When the returned `action` function is invoked:

1.  The `loading` ref is set to `true`.
1.  The provided `innerAction` is executed with the given payload (if any) and any additional arguments.
    - If `payload` is `undefined`, an empty object `{}` (cast to `Payload` type) is passed to `innerAction`.
1.  If `innerAction` throws an error:
    - The error is logged to the console via `console.error(e)`.
    - The error is **re-thrown**, allowing the caller of `action` to also catch and handle it.
1.  Regardless of success or failure, `loading` is set to `false` in a `finally` block.
1.  The `action` function returns the `Promise` from `innerAction`, so the caller can `await` its result or chain `.then()` / `.catch()`.

## Usage

```typescript
import { useAsync } from '@vc-shell/framework';

const { action, loading } = useAsync(async (payload) => {
  // Your async operation here
  const result = await someAsyncOperation(payload);
  return result;
});
```

## Returns

| Name        | Type                                        | Description                                     |
| ----------- | ------------------------------------------- | ----------------------------------------------- |
| `action`    | `(payload?: Payload, ...rest: any[]) => Promise<Result>` | Function to execute the `innerAction`. It manages the `loading` state and re-throws errors from `innerAction`. Returns the promise from `innerAction`. |
| `loading`   | `Readonly<Ref<boolean>>`                    | Reactive boolean indicating if `innerAction` is currently executing.       |

## Parameters

| Name          | Type                                       | Description                                      |
| ------------- | ------------------------------------------ | ------------------------------------------------ |
| `innerAction` | `(payload?: Payload, ...rest: any[]) => Promise<Result>` | The asynchronous function to be wrapped. This function is responsible for performing the actual async task, including its own data handling and error management (e.g., updating refs, try-catch blocks). If `payload` is not provided to `action`, `innerAction` receives `{}`. |

## Type parameters

| Name       | Description                                               |
| ---------- | --------------------------------------------------------- |
| `Payload`  | Type of the payload passed to the action (default: `void`) |
| `Result`   | Return type of the async operation (default: `void`)       |

## Key features

### Loading State Management
- Automatically sets `loading` to `true` when the async operation starts
- Sets `loading` to `false` when the operation completes (success or failure)
- Provides reactive loading state for UI feedback

### Error handling
- Logs errors to console via `console.error()`
- Re-throws errors for caller to handle
- Does not inherently handle error display - this is the responsibility of `innerAction`

### Promise return
- Returns the original promise from `innerAction`
- Allows chaining with `.then()` / `.catch()` or using `await`
- Enables access to the resolved value or caught errors

## Important notes

- `useAsync` does **not** handle data assignment or error display logic
- The `innerAction` is responsible for updating reactive state and error handling
- If no payload is provided to `action`, an empty object `{}` is passed to `innerAction`
- The composable is generic and supports TypeScript type parameters for `Payload` and `Result`

## Related resources

- [Managing Async Operations with useAsync](../Usage-Guides/managing-async-operations-with-useasync.md)