# VcSwitch Component

The `VcSwitch` component is a toggle switch that allows users to change settings between two states: on and off. It provides a visual representation of a binary choice using a sliding toggle mechanism.

## Storybook

[VcSwitch Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcswitch--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcswitch--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcSwitch v-model="isEnabled" label="Enable feature" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const isEnabled = ref(false);
</script>
```

## Props

| Prop           | Type                  | Default     | Description                                      |
| -------------- | --------------------- | ----------- | ------------------------------------------------ |
| `modelValue`   | `boolean \| undefined`| -           | The value bound to the switch                    |
| `disabled`     | `boolean`             | `false`     | Whether the switch is disabled                   |
| `tooltip`      | `string`              | -           | Tooltip text to show below the switch            |
| `required`     | `boolean`             | `false`     | Whether the switch is required                   |
| `label`        | `string`              | -           | Label to display above the switch                |
| `trueValue`    | `boolean`             | `true`      | Value when switch is in the on state             |
| `falseValue`   | `boolean`             | `false`     | Value when switch is in the off state            |

## Events

| Event                | Parameters                 | Description                                     |
| -------------------- | -------------------------- | ----------------------------------------------- |
| `update:modelValue`  | `(value: boolean \| undefined) => void` | Emitted when the switch value changes  |

## CSS Variables

The switch component uses CSS variables for theming, which can be customized:

```css
:root {
  --switch-width: 36px;                       /* Width of the switch component */
  --switch-height: 22px;                      /* Height of the switch component */
  --switch-thumb-size: 16px;                  /* Size of the switch thumb/knob */
  --switch-translate: 14px;                   /* Distance the thumb moves when toggled */

  --switch-main-color: var(--accent-500);     /* Background color when switch is on */
  --switch-secondary-color: var(--neutrals-300); /* Background color when switch is off */
  --switch-icon-background: var(--additional-50); /* Background color of the thumb */
  --switch-icon-color: var(--neutrals-400);   /* Color of any icon in the switch */
  --switch-transition: all 0.2s ease-in-out;  /* Transition effect for the switch */
}
```

## Examples

### Basic Switch

```vue
<template>
  <VcSwitch v-model="enabled" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const enabled = ref(false);
</script>
```

### Switch with Label

```vue
<template>
  <VcSwitch 
    v-model="darkMode" 
    label="Dark Mode" 
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const darkMode = ref(false);
</script>
```

### Disabled Switch

```vue
<template>
  <VcSwitch 
    v-model="featureFlag" 
    label="Experimental Feature" 
    disabled 
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const featureFlag = ref(true);
</script>
```

### Switch with Tooltip

```vue
<template>
  <VcSwitch 
    v-model="notifications" 
    label="Notifications" 
    tooltip="Enable to receive real-time notifications" 
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const notifications = ref(false);
</script>
```

### Required Switch

```vue
<template>
  <VcSwitch 
    v-model="termsAccepted" 
    label="Accept Terms and Conditions" 
    required 
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const termsAccepted = ref(false);
</script>
```

### Multiple Switches in a Form

```vue
<template>
  <div class="tw-space-y-4">
    <VcSwitch 
      v-model="settings.emailNotifications" 
      label="Email Notifications" 
    />
    
    <VcSwitch 
      v-model="settings.pushNotifications" 
      label="Push Notifications" 
    />
    
    <VcSwitch 
      v-model="settings.soundAlerts" 
      label="Sound Alerts"
      tooltip="Play a sound when a notification is received" 
    />
    
    <VcSwitch 
      v-model="settings.darkTheme" 
      label="Dark Theme" 
    />
  </div>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { VcSwitch } from '@vc-shell/framework';

const settings = reactive({
  emailNotifications: true,
  pushNotifications: false,
  soundAlerts: true,
  darkTheme: false
});
</script>
```
