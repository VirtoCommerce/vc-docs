# VcLoginForm

VcLoginForm is a container component designed specifically for login, password reset, and similar authentication pages. It provides a consistent, styled layout for authentication forms with support for logos, background images, and versioning information.

## Basic Usage

```vue
<template>
  <VcLoginForm
    title="Sign In"
    :logo="logoUrl"
    :background="backgroundImageUrl"
  >
    <VcForm @submit.prevent="handleLogin">
      <!-- Username input -->
      <VcInput
        v-model="username"
        label="Username"
        placeholder="Enter your username"
        required
      />
      
      <!-- Password input -->
      <VcInput
        v-model="password"
        type="password"
        label="Password"
        placeholder="Enter your password"
        required
      />
      
      <!-- Login button -->
      <div class="tw-mt-4 tw-flex tw-justify-end">
        <VcButton @click="handleLogin">
          Sign In
        </VcButton>
      </div>
    </VcForm>
  </VcLoginForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcLoginForm, VcForm, VcInput, VcButton } from '@vc-shell/framework';

const username = ref('');
const password = ref('');
const logoUrl = '/assets/logo.svg';
const backgroundImageUrl = '/assets/login-bg.jpg';

function handleLogin() {
  // Handle login logic
  console.log('Logging in with:', username.value, password.value);
}
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string` | `"Login"` | Title displayed in the header of the login form |
| `logo` | `string` | - | URL to the logo image displayed above the form |
| `background` | `string` | - | URL to the background image used for the login page |

## Slots

| Slot Name | Description |
|-----------|-------------|
| `default` | The main content of the login form - typically contains your authentication form elements |

## CSS Variables

The login form component uses CSS variables for theming, which can be customized:

```css
:root {
  --login-version-color: var(--neutrals-400);           /* Color for the version text shown at the bottom */
  --login-header-bg-color: var(--secondary-700);        /* Background color for the header section */
  --login-box-shadow-color: var(--additional-950);      /* Base color for the shadow of the login box */
  --login-box-shadow: rgb(from var(--login-box-shadow-color) r g b / 5%); /* Shadow effect for the login form box */
  --login-bg-color: var(--additional-50);               /* Background color of the login form box */
  --login-title-color: var(--additional-50);            /* Color of the title text in the header */
  --login-title-bg: var(--secondary-700);               /* Background color of the title section (often same as header) */
}
```

## Automatic Version Display

The component automatically displays the application version from the route metadata when available. The version is displayed at the bottom left of the login form.

## Examples

### Basic Login Form

```vue
<template>
  <VcLoginForm
    title="Sign In"
    :logo="logoUrl"
  >
    <VcForm @submit.prevent="handleLogin">
      <VcInput
        v-model="username"
        label="Username"
        placeholder="Enter your username"
        required
      />
      <VcInput
        v-model="password"
        type="password"
        label="Password" 
        placeholder="Enter your password"
        required
      />
      <div class="tw-mt-4 tw-flex tw-justify-between tw-items-center">
        <VcButton text @click="forgotPassword">
          Forgot Password?
        </VcButton>
        <VcButton @click="handleLogin">
          Sign In
        </VcButton>
      </div>
    </VcForm>
  </VcLoginForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcLoginForm, VcForm, VcInput, VcButton } from '@vc-shell/framework';

const username = ref('');
const password = ref('');
const logoUrl = '/assets/logo.svg';

function handleLogin() {
  // Login logic
}

function forgotPassword() {
  // Forgot password logic
}
</script>
```

### Password Reset Form

```vue
<template>
  <VcLoginForm
    title="Reset Password"
    :logo="logoUrl"
    :background="backgroundImageUrl"
  >
    <template v-if="!requestSent">
      <VcForm @submit.prevent="sendPasswordReset">
        <VcInput
          v-model="email"
          label="Email"
          type="email"
          placeholder="Enter your email address"
          required
        />
        <div class="tw-mt-4 tw-flex tw-justify-between tw-items-center">
          <VcButton text @click="goBack">
            Back to Login
          </VcButton>
          <VcButton @click="sendPasswordReset">
            Send Reset Link
          </VcButton>
        </div>
      </VcForm>
    </template>
    
    <template v-else>
      <div class="tw-text-center tw-py-4">
        <div class="tw-mb-4">Password reset link has been sent to your email address.</div>
        <VcButton @click="goBack">
          Return to Login
        </VcButton>
      </div>
    </template>
  </VcLoginForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcLoginForm, VcForm, VcInput, VcButton } from '@vc-shell/framework';
import { useRouter } from 'vue-router';

const router = useRouter();
const email = ref('');
const requestSent = ref(false);
const logoUrl = '/assets/logo.svg';
const backgroundImageUrl = '/assets/reset-bg.jpg';

function sendPasswordReset() {
  // Send password reset logic
  requestSent.value = true;
}

function goBack() {
  router.push('/login');
}
</script>
```

### Custom Styling with Social Login Options

```vue
<template>
  <VcLoginForm
    title="Sign In"
    :logo="logoUrl"
    :background="backgroundImageUrl"
  >
    <VcForm @submit.prevent="handleLogin">
      <VcInput
        v-model="username" 
        label="Username"
        placeholder="Enter your username"
        required
      />
      <VcInput
        v-model="password"
        type="password"
        label="Password"
        placeholder="Enter your password"
        required
      />
      <div class="tw-mt-4 tw-flex tw-justify-end">
        <VcButton @click="handleLogin">
          Sign In
        </VcButton>
      </div>
    </VcForm>
    
    <div class="tw-my-4 tw-relative tw-text-center">
      <div class="tw-absolute tw-inset-0 tw-flex tw-items-center">
        <div class="tw-w-full tw-border-t tw-border-gray-300"></div>
      </div>
      <div class="tw-relative tw-inline-block tw-px-4 tw-bg-white tw-text-sm tw-text-gray-500">
        Or continue with
      </div>
    </div>
    
    <div class="tw-flex tw-gap-2 tw-justify-center">
      <VcButton icon="fab fa-google" variant="outline" @click="loginWithGoogle">
        Google
      </VcButton>
      <VcButton icon="fab fa-microsoft" variant="outline" @click="loginWithMicrosoft">
        Microsoft
      </VcButton>
      <VcButton icon="fab fa-github" variant="outline" @click="loginWithGithub">
        GitHub
      </VcButton>
    </div>
  </VcLoginForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcLoginForm, VcForm, VcInput, VcButton } from '@vc-shell/framework';

const username = ref('');
const password = ref('');
const logoUrl = '/assets/logo.svg';
const backgroundImageUrl = '/assets/login-bg.jpg';

function handleLogin() {
  // Login logic
}

function loginWithGoogle() {
  // Google login logic
}

function loginWithMicrosoft() {
  // Microsoft login logic
}

function loginWithGithub() {
  // GitHub login logic
}
</script>
```
