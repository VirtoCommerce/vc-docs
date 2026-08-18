# VcVideo Component

The `VcVideo` component is an atom used throughout the VC-Shell framework for embedding video content with an optional label and tooltip. It provides a responsive container for video playback.

## Storybook

[VcVideo Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcvideo--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcvideo--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcVideo
    label="Introduction Video" 
    source="https://www.youtube.com/embed/PeXX-V-dwpA" 
  />
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';
</script>
```

## Props

| Prop      | Type     | Default     | Description                                    |
| --------- | -------- | ----------- | ---------------------------------------------- |
| `label`   | `string` | `undefined` | Label displayed above the video                |
| `tooltip` | `string` | `undefined` | Additional information shown in a tooltip      |
| `source`  | `string` | `undefined` | URL of the video to be embedded                |

## CSS Variables

The video component uses CSS variables for theming, which can be customized:

```css
:root {
  --video-icon-color: var(--primary-400);      /* Color of the placeholder video icon when no source is provided */
}
```

## Examples

### Basic Video Embed

```vue
<template>
  <VcVideo
    label="Product Demo" 
    source="https://www.youtube.com/embed/PeXX-V-dwpA" 
  />
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';
</script>
```

### Video with Tooltip

```vue
<template>
  <VcVideo
    label="Product Overview" 
    tooltip="This video provides an overview of our product features and benefits"
    source="https://www.youtube.com/embed/PeXX-V-dwpA" 
  />
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';
</script>
```

### Video without Label

```vue
<template>
  <VcVideo source="https://www.youtube.com/embed/PeXX-V-dwpA" />
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';
</script>
```

### Placeholder When No Source is Available

```vue
<template>
  <VcVideo label="Video Coming Soon" />
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';
</script>
```

### Multiple Videos in a Grid

```vue
<template>
  <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 tw-gap-4">
    <VcVideo
      v-for="video in videos"
      :key="video.id"
      :label="video.title"
      :tooltip="video.description"
      :source="video.embedUrl"
    />
  </div>
</template>

<script lang="ts" setup>
import { VcVideo } from '@vc-shell/framework';

const videos = [
  {
    id: 1,
    title: 'Getting Started',
    description: 'Learn how to get started with our platform',
    embedUrl: 'https://www.youtube.com/embed/PeXX-V-dwpA'
  },
  {
    id: 2,
    title: 'Advanced Features',
    description: 'Explore advanced features and customization options',
    embedUrl: 'https://www.youtube.com/embed/dQw4w9WgXcQ'
  },
  {
    id: 3,
    title: 'Integration Guide',
    description: 'How to integrate our platform with your existing systems',
    embedUrl: 'https://www.youtube.com/embed/PeXX-V-dwpA'
  },
  {
    id: 4,
    title: 'Best Practices',
    description: 'Best practices for optimal usage and performance',
    embedUrl: 'https://www.youtube.com/embed/dQw4w9WgXcQ'
  }
];
</script>
```

### Conditional Video Display

```vue
<template>
  <div>
    <VcLabel>Video Content</VcLabel>
    <VcSelect 
      v-model="selectedVideo" 
      :options="videoOptions" 
      placeholder="Select a video"
    />
    
    <div class="tw-mt-4">
      <VcVideo 
        v-if="selectedVideo" 
        :label="getVideoTitle(selectedVideo)"
        :source="getVideoUrl(selectedVideo)"
      />
      <div v-else class="tw-p-4 tw-border tw-rounded-md tw-text-center tw-text-[color:var(--neutrals-500)]">
        Please select a video to view
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcVideo, VcLabel, VcSelect } from '@vc-shell/framework';

const selectedVideo = ref('');

const videoOptions = [
  { value: 'intro', label: 'Introduction' },
  { value: 'tutorial', label: 'Tutorial' },
  { value: 'demo', label: 'Product Demo' }
];

function getVideoTitle(videoId) {
  const option = videoOptions.find(opt => opt.value === videoId);
  return option ? option.label : '';
}

function getVideoUrl(videoId) {
  const urls = {
    intro: 'https://www.youtube.com/embed/PeXX-V-dwpA',
    tutorial: 'https://www.youtube.com/embed/dQw4w9WgXcQ',
    demo: 'https://www.youtube.com/embed/PeXX-V-dwpA'
  };
  
  return urls[videoId] || '';
}
</script>
```

### Video Card with Description

```vue
<template>
  <VcCard>
    <template #header>
      <h3 class="tw-font-medium tw-text-lg">Product Tutorial</h3>
    </template>
    
    <VcVideo 
      source="https://www.youtube.com/embed/PeXX-V-dwpA" 
    />
    
    <template #footer>
      <p class="tw-text-sm tw-text-[color:var(--neutrals-600)]">
        This tutorial will guide you through the basic features of our product and help you get started quickly.
        Watch the full video for step-by-step instructions.
      </p>
    </template>
  </VcCard>
</template>

<script lang="ts" setup>
import { VcVideo, VcCard } from '@vc-shell/framework';
</script>
```
