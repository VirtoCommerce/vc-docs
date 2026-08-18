# Implementing Custom Authentication Providers

## Overview

The VC Shell framework provides a pluggable authentication system that allows you to implement custom authentication providers while maintaining full compatibility with all framework features. This enables you to use alternative authentication methods such as file-based credentials, custom APIs, OAuth/OIDC providers, or mock authentication for testing.

By default, the framework uses the platform authentication provider (`PlatformAuthProvider`), which integrates with the Virto Commerce platform API. However, you can replace it with your own implementation by implementing the `IAuthProvider` interface.

## Key Features

- ✅ **Pluggable Architecture** - Replace the default authentication with your own implementation
- ✅ **Full Page Support** - All authentication pages (Login, Reset Password, Change Password, Invite) work with any provider
- ✅ **Type Safety** - Strong TypeScript interfaces ensure compatibility
- ✅ **Backward Compatible** - Existing applications continue to work without modifications
- ✅ **Early Initialization** - Works both before and after framework initialization
- ✅ **No Platform Dependency** - Custom providers are not tied to platform-specific APIs

## When to Use Custom Authentication

Consider implementing a custom authentication provider when you need to:

- **Use file-based authentication** for development or simple deployments
- **Integrate with existing authentication infrastructure** outside the Virto Commerce platform
- **Implement OAuth/OIDC** authentication for enterprise single sign-on
- **Create mock authentication** for automated testing
- **Build standalone applications** that don't depend on the platform API

## Architecture

### Dependency Injection Pattern

The authentication system uses Vue's dependency injection combined with a global singleton to enable provider access throughout the application lifecycle:

```typescript
// Framework provides default or custom auth provider
VirtoShellFramework.configure({
  authProvider: customAuthProvider
});

app.use(VirtoShellFramework, { router, i18n: {...} });

// Composables access the provider through hybrid injection
const { user, signIn } = useUser();
```

### Hybrid Provider Access

The framework uses a hybrid approach to access authentication providers:

1. **Global Singleton** (`AuthProviderManager`) - For early access before Vue initialization
2. **Vue Dependency Injection** - For component usage after framework installation

This ensures that composables like `useUser()` work both:
- Before `app.use(VirtoShellFramework)` during application initialization
- Inside components after the framework is fully initialized

## Quick Start

### 1. Create a Custom Provider

Create a new file `src/auth/custom-auth-provider.ts`:

```typescript
import { computed, ref, ComputedRef, Ref } from "vue";
import type {
  IAuthProvider,
  IUserDetail,
  SecurityResult,
  IdentityResult,
  SignInResult,
  LoginType,
  RequestPasswordResult
} from "@vc-shell/framework";

export class CustomAuthProvider implements IAuthProvider {
  private _user: Ref<IUserDetail | undefined> = ref();
  private _loading: Ref<boolean> = ref(false);

  public user: ComputedRef<IUserDetail | undefined>;
  public loading: ComputedRef<boolean>;
  public isAdministrator: ComputedRef<boolean | undefined>;
  public isAuthenticated: ComputedRef<boolean>;

  constructor() {
    this.user = computed(() => this._user.value);
    this.loading = computed(() => this._loading.value);
    this.isAdministrator = computed(() => this._user.value?.isAdministrator);
    this.isAuthenticated = computed(() => this._user.value?.userName != null);
  }

  async loadUser(): Promise<IUserDetail> {
    // Implement your user loading logic
    this._loading.value = true;
    try {
      const storedUser = sessionStorage.getItem("customUser");
      if (storedUser) {
        this._user.value = JSON.parse(storedUser);
        return this._user.value as IUserDetail;
      }
      throw new Error("No authenticated user");
    } finally {
      this._loading.value = false;
    }
  }

  async signIn(username: string, password: string): Promise<SignInResult> {
    // Implement your sign-in logic
    this._loading.value = true;
    try {
      // Your authentication logic here
      if (username === "demo" && password === "demo") {
        this._user.value = {
          id: "demo_user",
          userName: username,
          email: username + "@example.com",
          isAdministrator: true,
        } as IUserDetail;

        sessionStorage.setItem("customUser", JSON.stringify(this._user.value));
        return { succeeded: true };
      }
      return { succeeded: false, error: "Invalid credentials" };
    } finally {
      this._loading.value = false;
    }
  }

  async signOut(): Promise<void> {
    this._user.value = undefined;
    sessionStorage.removeItem("customUser");
  }

  // Implement other required methods...
  async validateToken(userId: string, token: string): Promise<boolean> {
    return true; // Your validation logic
  }

  async validatePassword(password: string): Promise<IdentityResult> {
    return { succeeded: true };
  }

  async resetPasswordByToken(
    userId: string,
    password: string,
    token: string
  ): Promise<SecurityResult> {
    return { succeeded: true };
  }

  async requestPasswordReset(loginOrEmail: string): Promise<RequestPasswordResult> {
    return { succeeded: true };
  }

  async changeUserPassword(
    oldPassword: string,
    newPassword: string
  ): Promise<SecurityResult | undefined> {
    return { succeeded: true };
  }

  async getLoginType(): Promise<LoginType[]> {
    return []; // Return supported login types
  }
}
```

### 2. Configure the Framework

In your `main.ts`, configure the framework to use your custom provider:

```typescript
import { createApp } from "vue";
import VirtoShellFramework, { useUser } from "@vc-shell/framework";
import { CustomAuthProvider } from "./auth/custom-auth-provider";

// Import application modules
import router from "./router";
import App from "./App.vue";
// ... other module imports

async function startApp() {
  // 1. Configure the custom auth provider
  VirtoShellFramework.configure({
    authProvider: new CustomAuthProvider()
  });

  // 2. Load the user (after provider configuration)
  const { loadUser } = useUser();
  try {
    await loadUser();
  } catch (e) {
    console.log("No authenticated user, redirecting to login");
  }

  // 3. Initialize the application
  const app = createApp(App);

  app.use(VirtoShellFramework, {
    router,
    i18n: {
      locale: "en",
      fallbackLocale: "en",
    },
  });

  app.mount("#app");
}

startApp();
```

### 3. Using Platform Authentication (Default)

If you don't need custom authentication, simply don't call `configure()`. The framework will automatically use the platform authentication provider:

```typescript
import { createApp } from "vue";
import VirtoShellFramework, { useUser } from "@vc-shell/framework";
import router from "./router";

async function startApp() {
  // Load user with default platform authentication
  const { loadUser } = useUser();
  try {
    await loadUser();
  } catch (e) {
    console.log("Not authenticated");
  }

  // Initialize with default platform provider
  const app = createApp(App);
  app.use(VirtoShellFramework, {
    router,
    i18n: { locale: "en", fallbackLocale: "en" },
  });

  app.mount("#app");
}

startApp();
```

## API Reference

### IAuthProvider Interface

All authentication providers must implement the `IAuthProvider` interface:

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `user` | `ComputedRef<IUserDetail \| undefined>` | The currently authenticated user |
| `loading` | `ComputedRef<boolean>` | Loading state indicator |
| `isAuthenticated` | `ComputedRef<boolean>` | Whether a user is authenticated |
| `isAdministrator` | `ComputedRef<boolean \| undefined>` | Whether the user has administrator privileges |

#### Methods

##### Core Methods

```typescript
// Load the current user
loadUser(): Promise<IUserDetail>

// Sign in with credentials
signIn(username: string, password: string): Promise<SignInResult | { succeeded: boolean; error?: any; status?: number }>

// Sign out the current user
signOut(): Promise<void>
```

##### Password Management Methods

```typescript
// Validate a password reset token
validateToken(userId: string, token: string): Promise<boolean>

// Validate password strength
validatePassword(password: string): Promise<IdentityResult>

// Reset password using a token
resetPasswordByToken(userId: string, password: string, token: string): Promise<ISecurityResult>

// Request a password reset email
requestPasswordReset(loginOrEmail: string): Promise<RequestPasswordResult>

// Change the current user's password
changeUserPassword(oldPassword: string, newPassword: string): Promise<ISecurityResult | undefined>
```

##### Additional Methods

```typescript
// Get supported login types (password, external, etc.)
getLoginType(): Promise<ILoginType[]>
```

### Framework Configuration

```typescript
VirtoShellFramework.configure(options: {
  authProvider?: IAuthProvider;
}): void
```

Configure the framework with a custom authentication provider. Must be called **before** `app.use(VirtoShellFramework)`.

**Parameters:**
- `options.authProvider` - Optional custom authentication provider. If not provided, `PlatformAuthProvider` will be used by default.

**Example:**
```typescript
import VirtoShellFramework from "@vc-shell/framework";
import { CustomAuthProvider } from "./auth/custom-provider";

VirtoShellFramework.configure({
  authProvider: new CustomAuthProvider()
});

app.use(VirtoShellFramework, { router, i18n: {...} });
```

### Composables

#### useUser()

Access the current user and core authentication methods:

```typescript
const {
  user,              // ComputedRef<IUserDetail | undefined>
  loading,           // ComputedRef<boolean>
  isAuthenticated,   // ComputedRef<boolean>
  isAdministrator,   // ComputedRef<boolean | undefined>
  loadUser,          // () => Promise<IUserDetail>
  signIn,            // (username: string, password: string) => Promise<SignInResult>
  signOut,           // () => Promise<void>
} = useUser();
```

#### useUserManagement()

Access password management functionality:

```typescript
const {
  validateToken,           // (userId: string, token: string) => Promise<boolean>
  validatePassword,        // (password: string) => Promise<IdentityResult>
  resetPasswordByToken,    // (userId: string, password: string, token: string) => Promise<ISecurityResult>
  requestPasswordReset,    // (loginOrEmail: string) => Promise<RequestPasswordResult>
  changeUserPassword,      // (oldPassword: string, newPassword: string) => Promise<ISecurityResult | undefined>
  getLoginType,            // () => Promise<ILoginType[]>
} = useUserManagement();
```

### Provider Utilities

The framework provides utility functions for checking authentication provider types:

```typescript
import {
  isPlatformProvider,
  shouldEnablePlatformFeatures,
  getSafeProvider
} from "@vc-shell/framework";

// Check if the provider is a platform provider
const isPlatform = isPlatformProvider(authProvider);

// Check if platform-specific features should be enabled
const enableFeatures = shouldEnablePlatformFeatures(authProvider);

// Get a safe provider instance with fallback
const safeProvider = getSafeProvider(authProvider);
```

These utilities are used internally by the framework to conditionally enable/disable platform-specific features like SignalR, App Switcher, and Platform Notifications.

## Platform-Specific Features

When using a custom authentication provider, certain platform-specific features are automatically disabled:

### Disabled Features

1. **SignalR Integration** - Real-time push notifications are disabled for custom providers
2. **App Switcher** - The application switcher in the UI is hidden
3. **Platform Notifications** - Push notification loading and management is disabled for custom providers

These features are automatically detected using centralized utility functions (`shouldEnablePlatformFeatures()`) and will only be enabled when using the default platform provider.

When using a custom authentication provider:
- ✅ **Local notification state** still works (marking as read, adding notifications)
- ❌ **Platform API calls** are skipped (`loadFromHistory`, `markAllAsRead` API calls)
- ❌ **Real-time notifications** via SignalR are disabled
- ❌ **App switching** functionality is hidden

## Types and Interfaces

The framework provides common types that should be used by all authentication providers to ensure compatibility:

### IUserDetail

```typescript
interface IUserDetail {
  id?: string;
  userName?: string;
  email?: string;
  firstName?: string;
  lastName?: string;
  isAdministrator?: boolean;
  permissions?: string[];
  userType?: string;
  // ... additional properties
}
```

### SignInResult

```typescript
interface SignInResult {
  succeeded: boolean;
  error?: any;
  status?: number;
  requiresTwoFactor?: boolean;
  // ... additional properties
}
```

### ISecurityResult / SecurityResult

```typescript
interface ISecurityResult {
  succeeded?: boolean;
  errors?: string[];
  // ... additional properties
}
```

### IdentityResult

```typescript
interface IdentityResult {
  succeeded?: boolean;
  errors?: Array<{ code?: string; description?: string }>;
}
```

### RequestPasswordResult

```typescript
interface RequestPasswordResult {
  succeeded: boolean;
  error?: string;
}
```

### ILoginType / LoginType

```typescript
interface ILoginType {
  authenticationType?: string;
  // ... additional properties
}

enum LoginType {
  Password = "Password",
  External = "External",
}
```

## Complete Examples

### Example 1: File-Based Authentication

A simple provider that validates against hardcoded credentials:

```typescript
import { computed, ref } from "vue";
import type { IAuthProvider, IUserDetail, SignInResult } from "@vc-shell/framework";

export class FileBasedAuthProvider implements IAuthProvider {
  private _user = ref<IUserDetail | undefined>();
  private _loading = ref(false);

  // Hardcoded users for demonstration
  private users = {
    "admin": { password: "admin123", isAdmin: true },
    "user": { password: "user123", isAdmin: false },
  };

  user = computed(() => this._user.value);
  loading = computed(() => this._loading.value);
  isAuthenticated = computed(() => !!this._user.value);
  isAdministrator = computed(() => this._user.value?.isAdministrator);

  async loadUser(): Promise<IUserDetail> {
    const storedUser = sessionStorage.getItem("user");
    if (!storedUser) throw new Error("Not authenticated");

    this._user.value = JSON.parse(storedUser);
    return this._user.value as IUserDetail;
  }

  async signIn(username: string, password: string): Promise<SignInResult> {
    const user = this.users[username as keyof typeof this.users];

    if (user && user.password === password) {
      this._user.value = {
        id: username,
        userName: username,
        email: `${username}@example.com`,
        isAdministrator: user.isAdmin,
      } as IUserDetail;

      sessionStorage.setItem("user", JSON.stringify(this._user.value));
      return { succeeded: true };
    }

    return { succeeded: false, error: "Invalid credentials" };
  }

  async signOut(): Promise<void> {
    this._user.value = undefined;
    sessionStorage.removeItem("user");
  }

  // Implement other required methods with basic logic...
  async validateToken() { return true; }
  async validatePassword() { return { succeeded: true }; }
  async resetPasswordByToken() { return { succeeded: true }; }
  async requestPasswordReset() { return { succeeded: true }; }
  async changeUserPassword() { return { succeeded: true }; }
  async getLoginType() { return []; }
}
```

### Example 2: Mock Provider for Testing

A comprehensive mock provider with multiple test users:

```typescript
import { computed, ref, ComputedRef, Ref } from "vue";
import type {
  IAuthProvider,
  IUserDetail,
  SignInResult,
  IdentityResult,
  SecurityResult,
  LoginType,
  RequestPasswordResult
} from "@vc-shell/framework";

export class MockAuthProvider implements IAuthProvider {
  private _user: Ref<IUserDetail | undefined> = ref();
  private _loading: Ref<boolean> = ref(false);

  user: ComputedRef<IUserDetail | undefined>;
  loading: ComputedRef<boolean>;
  isAdministrator: ComputedRef<boolean | undefined>;
  isAuthenticated: ComputedRef<boolean>;

  // Mock users database
  private mockUsers = {
    "admin@test.com": {
      password: "Admin123!",
      user: {
        id: "mock_admin_id",
        userName: "admin@test.com",
        email: "admin@test.com",
        firstName: "Admin",
        lastName: "User",
        isAdministrator: true,
        permissions: ["platform:security", "platform:asset:create"],
        userType: "Administrator",
      } as IUserDetail,
    },
    "vendor@test.com": {
      password: "Vendor123!",
      user: {
        id: "mock_vendor_id",
        userName: "vendor@test.com",
        email: "vendor@test.com",
        firstName: "Vendor",
        lastName: "User",
        isAdministrator: false,
        permissions: ["platform:asset:create"],
        userType: "Vendor",
      } as IUserDetail,
    },
  };

  constructor() {
    console.log("[MockAuth] Available users:", Object.keys(this.mockUsers));

    this.user = computed(() => this._user.value);
    this.loading = computed(() => this._loading.value);
    this.isAdministrator = computed(() => this._user.value?.isAdministrator);
    this.isAuthenticated = computed(() => !!this._user.value?.userName);

    // Restore from session storage
    const stored = sessionStorage.getItem("mockUser");
    if (stored) {
      this._user.value = JSON.parse(stored);
    }
  }

  async loadUser(): Promise<IUserDetail> {
    this._loading.value = true;

    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));

    if (!this._user.value) {
      this._loading.value = false;
      throw new Error("No authenticated user");
    }

    this._loading.value = false;
    return { ...this._user.value } as IUserDetail;
  }

  async signIn(username: string, password: string): Promise<SignInResult> {
    this._loading.value = true;

    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 500));

    const mockUser = this.mockUsers[username as keyof typeof this.mockUsers];

    if (mockUser && mockUser.password === password) {
      this._user.value = mockUser.user;
      sessionStorage.setItem("mockUser", JSON.stringify(mockUser.user));
      this._loading.value = false;

      console.log("[MockAuth] Sign in successful:", username);
      return { succeeded: true };
    }

    this._loading.value = false;
    console.log("[MockAuth] Sign in failed");
    return {
      succeeded: false,
      error: "Invalid credentials. Try admin@test.com/Admin123! or vendor@test.com/Vendor123!",
    };
  }

  async signOut(): Promise<void> {
    this._loading.value = true;
    await new Promise(resolve => setTimeout(resolve, 300));

    this._user.value = undefined;
    sessionStorage.removeItem("mockUser");
    this._loading.value = false;
  }

  async validateToken(userId: string, token: string): Promise<boolean> {
    await new Promise(resolve => setTimeout(resolve, 300));
    return token === "valid_mock_token";
  }

  async validatePassword(password: string): Promise<IdentityResult> {
    if (password.length < 6) {
      return {
        succeeded: false,
        errors: [{
          code: "PasswordTooShort",
          description: "Password must be at least 6 characters"
        }],
      };
    }

    if (!/[A-Z]/.test(password)) {
      return {
        succeeded: false,
        errors: [{
          code: "PasswordRequiresUpper",
          description: "Password must contain uppercase letter"
        }],
      };
    }

    if (!/[0-9]/.test(password)) {
      return {
        succeeded: false,
        errors: [{
          code: "PasswordRequiresDigit",
          description: "Password must contain a number"
        }],
      };
    }

    return { succeeded: true };
  }

  async resetPasswordByToken(
    userId: string,
    password: string,
    token: string
  ): Promise<SecurityResult> {
    await new Promise(resolve => setTimeout(resolve, 500));

    if (token === "valid_mock_token" && password.length >= 6) {
      return { succeeded: true };
    }

    return {
      succeeded: false,
      errors: ["Invalid token or password requirements not met"]
    };
  }

  async requestPasswordReset(loginOrEmail: string): Promise<RequestPasswordResult> {
    await new Promise(resolve => setTimeout(resolve, 500));

    if (loginOrEmail.includes("@")) {
      return { succeeded: true };
    }

    return { succeeded: false, error: "Invalid email address" };
  }

  async changeUserPassword(
    oldPassword: string,
    newPassword: string
  ): Promise<SecurityResult | undefined> {
    await new Promise(resolve => setTimeout(resolve, 500));

    if (!this._user.value) {
      return { succeeded: false, errors: ["User not authenticated"] };
    }

    if (newPassword.length < 6) {
      return {
        succeeded: false,
        errors: ["New password must be at least 6 characters"]
      };
    }

    return { succeeded: true };
  }

  async getLoginType(): Promise<LoginType[]> {
    return [LoginType.Password];
  }
}
```

### Example 3: Integration with External API

A provider that communicates with a custom authentication API:

```typescript
import { computed, ref } from "vue";
import axios from "axios";
import type { IAuthProvider, IUserDetail, SignInResult } from "@vc-shell/framework";

export class CustomApiAuthProvider implements IAuthProvider {
  private _user = ref<IUserDetail | undefined>();
  private _loading = ref(false);
  private apiClient = axios.create({
    baseURL: import.meta.env.VITE_AUTH_API_URL,
  });

  user = computed(() => this._user.value);
  loading = computed(() => this._loading.value);
  isAuthenticated = computed(() => !!this._user.value);
  isAdministrator = computed(() => this._user.value?.isAdministrator);

  async loadUser(): Promise<IUserDetail> {
    this._loading.value = true;

    try {
      const token = localStorage.getItem("authToken");
      if (!token) throw new Error("No token found");

      const response = await this.apiClient.get("/api/auth/me", {
        headers: { Authorization: `Bearer ${token}` },
      });

      this._user.value = response.data;
      return this._user.value as IUserDetail;
    } catch (error) {
      console.error("Failed to load user:", error);
      throw error;
    } finally {
      this._loading.value = false;
    }
  }

  async signIn(username: string, password: string): Promise<SignInResult> {
    this._loading.value = true;

    try {
      const response = await this.apiClient.post("/api/auth/login", {
        username,
        password,
      });

      if (response.data.token) {
        localStorage.setItem("authToken", response.data.token);
        this._user.value = response.data.user;
        return { succeeded: true };
      }

      return { succeeded: false, error: "Authentication failed" };
    } catch (error: any) {
      return {
        succeeded: false,
        error: error.response?.data?.message || "Authentication failed"
      };
    } finally {
      this._loading.value = false;
    }
  }

  async signOut(): Promise<void> {
    try {
      await this.apiClient.post("/api/auth/logout");
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      this._user.value = undefined;
      localStorage.removeItem("authToken");
    }
  }

  // Implement other methods...
  async validateToken(userId: string, token: string): Promise<boolean> {
    try {
      const response = await this.apiClient.post("/api/auth/validate-token", {
        userId,
        token,
      });
      return response.data.valid;
    } catch {
      return false;
    }
  }

  async validatePassword(password: string): Promise<IdentityResult> {
    try {
      const response = await this.apiClient.post("/api/auth/validate-password", {
        password,
      });
      return response.data;
    } catch {
      return { succeeded: false };
    }
  }

  async resetPasswordByToken(
    userId: string,
    password: string,
    token: string
  ): Promise<SecurityResult> {
    try {
      await this.apiClient.post("/api/auth/reset-password", {
        userId,
        password,
        token,
      });
      return { succeeded: true };
    } catch (error: any) {
      return {
        succeeded: false,
        errors: [error.response?.data?.message]
      };
    }
  }

  async requestPasswordReset(loginOrEmail: string): Promise<RequestPasswordResult> {
    try {
      await this.apiClient.post("/api/auth/request-reset", { email: loginOrEmail });
      return { succeeded: true };
    } catch (error: any) {
      return {
        succeeded: false,
        error: error.response?.data?.message
      };
    }
  }

  async changeUserPassword(
    oldPassword: string,
    newPassword: string
  ): Promise<SecurityResult | undefined> {
    try {
      await this.apiClient.post("/api/auth/change-password", {
        oldPassword,
        newPassword,
      });
      return { succeeded: true };
    } catch (error: any) {
      return {
        succeeded: false,
        errors: [error.response?.data?.message]
      };
    }
  }

  async getLoginType(): Promise<LoginType[]> {
    try {
      const response = await this.apiClient.get("/api/auth/login-types");
      return response.data;
    } catch {
      return [];
    }
  }
}
```

## Integration with Framework

### How Authentication Pages Work

All authentication-related pages in the framework automatically work with any custom provider:

- **Login Page** (`/login`) - Uses `signIn()` and `getLoginType()`
- **Reset Password Page** (`/reset-password`) - Uses `requestPasswordReset()`
- **Change Password Page** (`/change-password`) - Uses `changeUserPassword()` and `validatePassword()`
- **Invite Page** (`/invite`) - Uses `validateToken()` and `resetPasswordByToken()`

No modifications are needed to these pages when implementing a custom provider.

### HTTP Interceptors

The framework's HTTP interceptors automatically work with custom providers:

- **401 Unauthorized** - Automatically calls `signOut()` and redirects to login
- **Missing User** - Validates authentication state using `isAuthenticated`

### Route Guards

Authentication guards use the `isAuthenticated` computed property to protect routes:

```typescript
router.beforeEach((to, from, next) => {
  const { isAuthenticated } = useUser();

  if (to.meta.requiresAuth && !isAuthenticated.value) {
    next("/login");
  } else {
    next();
  }
});
```

## Best Practices

### 1. Configure Before Using Composables

**Important:** Always call `VirtoShellFramework.configure()` before calling any composables that depend on authentication.

```typescript
// ✅ CORRECT ORDER
async function startApp() {
  // 1. Configure auth provider FIRST
  VirtoShellFramework.configure({
    authProvider: new CustomAuthProvider()
  });

  // 2. THEN use composables
  const { loadUser } = useUser();
  await loadUser();

  // 3. Initialize the application
  const app = createApp(App);
  app.use(VirtoShellFramework, { router });
  app.mount("#app");
}
```

**Why this matters:** Composables like `useUser()` and `usePermissions()` need the authentication provider to be configured before they can be used. The framework's internal modules handle this correctly by using lazy initialization.

### 2. Use Proper Error Handling

Always wrap authentication operations in try-catch blocks:

```typescript
async signIn(username: string, password: string): Promise<SignInResult> {
  this._loading.value = true;

  try {
    // Your authentication logic
    return { succeeded: true };
  } catch (error) {
    console.error("Sign in error:", error);
    return { succeeded: false, error: error.message };
  } finally {
    this._loading.value = false;
  }
}
```

### 2. Implement Loading States

Always update the `_loading` ref to provide user feedback:

```typescript
async loadUser(): Promise<IUserDetail> {
  this._loading.value = true; // Start loading

  try {
    // Load user logic
  } finally {
    this._loading.value = false; // Always clear loading
  }
}
```

### 3. Secure Token Storage

- Use `sessionStorage` for short-lived sessions
- Use `localStorage` for persistent sessions
- Never store passwords in browser storage
- Clear storage on sign out

```typescript
async signOut(): Promise<void> {
  this._user.value = undefined;
  sessionStorage.removeItem("authToken");
  localStorage.removeItem("authToken");
}
```

### 4. Validate User Input

Implement proper password validation:

```typescript
async validatePassword(password: string): Promise<IdentityResult> {
  const errors = [];

  if (password.length < 8) {
    errors.push({
      code: "PasswordTooShort",
      description: "Password must be at least 8 characters"
    });
  }

  if (!/[A-Z]/.test(password)) {
    errors.push({
      code: "PasswordRequiresUpper",
      description: "Password must contain an uppercase letter"
    });
  }

  if (!/[a-z]/.test(password)) {
    errors.push({
      code: "PasswordRequiresLower",
      description: "Password must contain a lowercase letter"
    });
  }

  if (!/[0-9]/.test(password)) {
    errors.push({
      code: "PasswordRequiresDigit",
      description: "Password must contain a number"
    });
  }

  if (!/[!@#$%^&*]/.test(password)) {
    errors.push({
      code: "PasswordRequiresSpecial",
      description: "Password must contain a special character"
    });
  }

  return {
    succeeded: errors.length === 0,
    errors: errors.length > 0 ? errors : undefined
  };
}
```

### 5. Log Authentication Events

Add logging for debugging and monitoring:

```typescript
async signIn(username: string, password: string): Promise<SignInResult> {
  console.log(`[Auth] Sign in attempt for: ${username}`);

  try {
    // Authentication logic
    console.log(`[Auth] Sign in successful for: ${username}`);
    return { succeeded: true };
  } catch (error) {
    console.error(`[Auth] Sign in failed for: ${username}`, error);
    return { succeeded: false, error: error.message };
  }
}
```

## Troubleshooting

### Platform Provider Created Despite Custom Configuration

**Problem:** You see logs showing `PlatformAuthProvider` being created even though you configured a custom provider.

**Logs:**
```
[AuthProviderManager] Lazy-initializing default PlatformAuthProvider
[PlatformAuthProvider] Constructor called - using PLATFORM authentication
[MockAuthProvider] Initialized with mock authentication
[VirtoShellFramework] Configuring with custom auth provider: MockAuthProvider
```

**Root Cause:** You're calling composables like `useUser()` or `usePermissions()` **before** calling `VirtoShellFramework.configure()`. This triggers the creation of the default `PlatformAuthProvider`.

**Solution:**
Call `VirtoShellFramework.configure()` **BEFORE** using any authentication-related composables:

```typescript
// ✅ Correct order
async function startApp() {
  // Configure FIRST
  VirtoShellFramework.configure({ authProvider: new CustomAuthProvider() });

  // THEN use composables
  const { loadUser } = useUser();
  await loadUser();

  // Initialize app
  const app = createApp(App);
  app.use(VirtoShellFramework, { router });
  app.mount("#app");
}

// ❌ Wrong order
async function startApp() {
  const { loadUser } = useUser(); // This triggers PlatformAuthProvider creation!
  VirtoShellFramework.configure({ authProvider: new CustomAuthProvider() }); // Too late
}
```

### Provider Not Found Error

**Error:**
```
Error: AuthProvider not found. Make sure VirtoShellFramework is properly installed.
```

**Solution:**
Make sure you call `VirtoShellFramework.configure()` **before** calling `useUser()`:

```typescript
// ❌ Wrong order
async function startApp() {
  const { loadUser } = useUser(); // Error!
  VirtoShellFramework.configure({ authProvider: customProvider });
}

// ✅ Correct order
async function startApp() {
  VirtoShellFramework.configure({ authProvider: customProvider });
  const { loadUser } = useUser(); // Works!
}
```

### User Not Persisting Across Refreshes

**Problem:** User is lost after page refresh.

**Solution:** Implement proper storage and restoration:

```typescript
constructor() {
  // Restore user from storage
  const storedUser = sessionStorage.getItem("user");
  if (storedUser) {
    this._user.value = JSON.parse(storedUser);
  }
}

async signIn(...): Promise<SignInResult> {
  // Save user to storage
  sessionStorage.setItem("user", JSON.stringify(this._user.value));
}
```

## Summary

The VC Shell framework's pluggable authentication system provides:

- ✅ **Flexibility** to implement any authentication strategy
- ✅ **Type safety** with TypeScript interfaces
- ✅ **Full compatibility** with all framework pages and features
- ✅ **Easy integration** with a simple configuration API
- ✅ **Backward compatibility** with existing applications
- ✅ **Clear separation** between platform and custom authentication

You can now build applications with complete control over authentication while maintaining all the benefits of the VC Shell framework.

