# useUser Composable

The `useUser` composable provides essential functionality for accessing user information and managing the user's session state. It's a shared composable, meaning it maintains a single shared state across all component instances where it's used.

This composable primarily focuses on providing read-only access to user data and core session operations like signing out and reloading user information.

## Basic usage

```typescript
import { useUser } from '@vc-shell/framework';

export default {
  setup() {
    const { user, isAuthenticated, isAdministrator, loading, loadUser, signOut } = useUser();
    
    return { 
      user, 
      isAuthenticated,
      isAdministrator,
      loading,
      loadUser,
      signOut
    };
  }
};
```

## Properties

| Property         | Type                                   | Description                                                  |
| ---------------- | -------------------------------------- | ------------------------------------------------------------ |
| `user`           | `ComputedRef<UserDetail \| undefined>` | Current user information (e.g., `userName`, `firstName`, `lastName`, `email`, permissions), or `undefined` if not authenticated. |
| `loading`        | `ComputedRef<boolean>`                 | A boolean indicating if a user-related background operation (like `loadUser`) is currently in progress. Useful for showing loading indicators. |
| `isAdministrator`| `ComputedRef<boolean \| undefined>`    | A boolean indicating whether the current authenticated user has administrator privileges. Returns `undefined` if the user is not authenticated or the information is not yet available. |
| `isAuthenticated`| `ComputedRef<boolean>`                 | A boolean indicating whether a user is currently authenticated. This becomes `true` after a successful sign-in and `false` after a sign-out or if no session is active. |

## Methods

### `loadUser`

Asynchronously loads or reloads the current authenticated user's information from the server. This can be useful to refresh user data after certain operations or when the application initializes.

```typescript
function loadUser(): Promise<UserDetail>
```

**Returns:** A promise that resolves to the `UserDetail` object containing the user's information. If the user is not authenticated or an error occurs, the promise might be rejected or resolve to a state where `user.value` remains `undefined`.

**Example:**
```typescript
import { useUser } from '@vc-shell/framework';
import { onMounted } from 'vue';

const { user, loadUser, loading } = useUser();

onMounted(async () => {
  try {
    await loadUser();
    if (user.value) {
      console.log('User details loaded:', user.value);
    } else {
      console.log('No user is currently authenticated.');
    }
  } catch (error) {
    console.error('Error loading user details:', error);
  }
});
```

### `signOut`

Signs out the currently authenticated user, clearing their session information from the client-side state. This typically involves clearing local user data and also triggers a call to the backend to invalidate the session.

```typescript
function signOut(): Promise<void>
```

**Returns:** A promise that resolves when the sign-out process on the client side is complete.

**Example:**
```typescript
import { useUser } from '@vc-shell/framework';

const { signOut, isAuthenticated } = useUser();

async function handleLogout() {
  try {
    await signOut();
    console.log('Logout successful. IsAuthenticated:', isAuthenticated.value); // Should be false
    // Typically, you would redirect to a login page.
  } catch (error) {
    console.error('Logout error:', error);
    // Handle potential errors during sign-out, though primarily client-side.
  }
}
```

## UserDetail interface

While the exact `UserDetail` structure is defined by the backend API, a conceptual representation often includes:

```typescript
interface UserDetail {
  permissions?: string[] | undefined;
  userName?: string | undefined;
  isAdministrator?: boolean;
  passwordExpired?: boolean;
  daysTillPasswordExpiry?: number;
  authenticationMethod?: string | undefined;
  isSsoAuthenticationMethod?: boolean;
  id?: string | undefined;
}
```
The `user` property of the `useUser` composable will hold an object conforming to this (or a similar) structure when a user is authenticated.


## Best practices

* **Read-only data**: Treat the `user` object from `useUser` as read-only. Mutations to user data should happen via dedicated backend API calls, after which `loadUser()` can be called to refresh the local state if necessary (though often the state updates automatically after successful operations by internal mechanisms).
* **Loading state**: Always consider the `loading` state when accessing user information, especially during application startup or after calling `loadUser()`, to provide a good user experience.
* **Authenticated routes/views**: Use `isAuthenticated` in navigation guards (e.g., with Vue Router) to protect routes that require authentication.
* **Permissions**: If your application uses a permission system, the `user.value?.permissions` array (or similar, depending on `UserDetail` structure) should be used in conjunction with a permission checking utility (like `usePermissions`) to control access to features. `isAdministrator` is a convenient shortcut for a common administrative role check.
* **Session management**: Understand that `useUser` primarily manages the client-side representation of the user's session. True session validation and security are handled by the backend.

