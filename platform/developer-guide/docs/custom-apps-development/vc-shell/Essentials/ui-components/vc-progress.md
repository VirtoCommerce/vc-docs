# VcProgress Component

The `VcProgress` component is an atom used throughout the VC-Shell framework for visualizing the completion progress of a task or process. It provides a clean and customizable progress bar with support for different visual styles.

## Storybook

[VcProgress Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcprogress--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcprogress--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcProgress :value="30" />
</template>

<script lang="ts" setup>
import { VcProgress } from '@vc-shell/framework';
</script>
```

## Props

| Prop      | Type                    | Default     | Description                                 |
| --------- | ----------------------- | ----------- | ------------------------------------------- |
| `value`   | `number`                | `0`         | Current progress value (0-100)              |
| `variant` | `'default' \| 'striped'`| `'default'` | Visual style of the progress bar            |

## CSS Variables

The progress component uses CSS variables for theming, which can be customized:

```css
:root {
  --progressbar-height: 16px;                     /* Height of the progress bar */
  --progressbar-border-radius: 2px;               /* Border radius of the progress bar */
  --progressbar-background-color: var(--additional-50); /* Background color of the empty part */
  --progressbar-foreground-color: var(--accent-200); /* Color of the filled progress part */
  --progressbar-border-width: 1px;                /* Width of the border around the progress bar */
  --progressbar-border-color: var(--neutrals-200); /* Color of the border around the progress bar */
  
  /* Striped variant */
  --progressbar-striped-bg: linear-gradient(      /* Background pattern for striped variant */
        45deg,
        transparent 50%,
        var(--accent-200) 50%,
        var(--accent-200) 75%,
        transparent 75%
      )
      left/30px 30px repeat-x,
    var(--accent-50);
  --progressbar-striped-color: var(--accent-200); /* Color of the stripes in striped variant */
}
```

## Examples

### Default Progress Bar

```vue
<template>
  <VcProgress :value="30" />
</template>

<script lang="ts" setup>
import { VcProgress } from '@vc-shell/framework';
</script>
```

### Striped Animated Progress Bar

```vue
<template>
  <VcProgress :value="50" variant="striped" />
</template>

<script lang="ts" setup>
import { VcProgress } from '@vc-shell/framework';
</script>
```

### Progress Stages Example

```vue
<template>
  <div class="tw-w-full tw-space-y-6">
    <div v-for="(stage, index) in stages" :key="index" class="tw-space-y-1">
      <div class="tw-flex tw-justify-between tw-items-center">
        <span class="tw-text-sm tw-font-medium">{{ stage.label }}</span>
        <span class="tw-text-sm tw-text-[color:var(--neutrals-500)]">{{ stage.value }}%</span>
      </div>
      <VcProgress 
        :value="stage.value" 
        :variant="stage.value === 100 ? 'striped' : 'default'" 
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcProgress } from '@vc-shell/framework';

const stages = [
  { value: 0, label: "Not started" },
  { value: 25, label: "Initial phase" },
  { value: 50, label: "Halfway there" },
  { value: 75, label: "Almost complete" },
  { value: 100, label: "Complete" },
];
</script>
```

### Interactive Progress with Controls

```vue
<template>
  <div class="tw-w-full tw-space-y-4">
    <div class="tw-flex tw-justify-between tw-items-center">
      <span class="tw-text-sm tw-font-medium">Progress: {{ progress }}%</span>
      <div class="tw-space-x-2">
        <VcButton
          @click="decrement"
          size="small"
          variant="secondary"
          :disabled="progress <= 0"
        >
          -10%
        </VcButton>
        <VcButton
          @click="increment"
          size="small"
          variant="primary"
          :disabled="progress >= 100"
        >
          +10%
        </VcButton>
        <VcButton
          @click="reset"
          size="small"
          variant="outline"
        >
          Reset
        </VcButton>
      </div>
    </div>
    <VcProgress 
      :value="progress" 
      :variant="progress === 100 ? 'striped' : 'default'" 
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcProgress, VcButton } from '@vc-shell/framework';

const progress = ref(30);

function increment() {
  if (progress.value < 100) {
    progress.value += 10;
  }
}

function decrement() {
  if (progress.value > 0) {
    progress.value -= 10;
  }
}

function reset() {
  progress.value = 0;
}
</script>
```

### File Upload Progress Indicator

```vue
<template>
  <div class="tw-w-full tw-space-y-2">
    <div class="tw-flex tw-justify-between">
      <span class="tw-text-sm">Uploading: product-image.jpg</span>
      <span class="tw-text-sm">{{ uploadProgress }}%</span>
    </div>
    <VcProgress :value="uploadProgress" :variant="uploadProgress < 100 ? 'default' : 'striped'" />
    <p class="tw-text-xs tw-text-[color:var(--neutrals-500)]" v-if="uploadProgress === 100">
      Upload complete!
    </p>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { VcProgress } from '@vc-shell/framework';

const uploadProgress = ref(0);

// Simulate file upload progress
onMounted(() => {
  const interval = setInterval(() => {
    if (uploadProgress.value < 100) {
      uploadProgress.value += 5;
    } else {
      clearInterval(interval);
    }
  }, 300);
});
</script>
```

### Multiple Progress Indicators

```vue
<template>
  <div class="tw-space-y-4">
    <div class="tw-space-y-1">
      <div class="tw-flex tw-justify-between">
        <span class="tw-text-sm tw-font-medium">Tasks completed</span>
        <span class="tw-text-sm">{{ tasksProgress }}%</span>
      </div>
      <VcProgress :value="tasksProgress" />
    </div>
    
    <div class="tw-space-y-1">
      <div class="tw-flex tw-justify-between">
        <span class="tw-text-sm tw-font-medium">Storage used</span>
        <span class="tw-text-sm">{{ storageProgress }}%</span>
      </div>
      <VcProgress :value="storageProgress" variant="striped" />
    </div>
    
    <div class="tw-space-y-1">
      <div class="tw-flex tw-justify-between">
        <span class="tw-text-sm tw-font-medium">Process completion</span>
        <span class="tw-text-sm">{{ processProgress }}%</span>
      </div>
      <VcProgress :value="processProgress" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcProgress } from '@vc-shell/framework';

const tasksProgress = 75;
const storageProgress = 40;
const processProgress = 90;
</script>
```

