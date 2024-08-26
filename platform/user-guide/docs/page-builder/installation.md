# Getting started

This guide will show how to set up and configure the Virto Commerce Page Builder, including content setup, and theme customization.

## Prerequisites
1. [Virto Commerce 3.800 and higher.](https://github.com/VirtoCommerce/vc-platform/releases)
1. Virto Storefront 6.7+ (`vc-storefront`).  [Deploy Storefront](https://docs.virtocommerce.org/getting-started/connect-storefront-to-platform-v3/)
1. Vue B2B Theme 1.10+ (`vc-theme-b2b-vue`). 
1. Page Builder Module 3.201+. [Download and Install](https://github.com/VirtoCommerce/vc-module-pagebuilder/releases). 

## Setup content 
Check that Virto Commerce Platform and Storefront use same Shared Content folder.

## Setup content module
Content configuration should be extended with `PathMappings` section.

```json title="appsettings.json"
"Content": {
    ...
    "PathMappings":{
        "pages": [
            "Themes",
            "_storeId",
            "_theme",
            "content/pages",
        ],
        "themes": [
            "Themes",
            "_storeId"
        ]
    }
    ...
}, 
```

Environment Variables
```yaml
      Content__PathMappings__pages__0: "Themes"
      Content__PathMappings__pages__1: "_storeId"
      Content__PathMappings__pages__2: "_theme"
      Content__PathMappings__pages__3: "content/pages"
      Content__PathMappings__themes__0: "Themes"
      Content__PathMappings__themes__1: "_storeId"
```

## Setup store

Public Store URL should be configured.

![image](https://user-images.githubusercontent.com/7639413/195312399-ec9a6c1e-e0d2-4798-8c37-1310f9c3a8ea.png)

1. Open Virto Commerce Admin UI.
1. Select `Stores`.
1. Select Current Store.
1. Setup Store URL if it's empty
1. Click Save button to apply. 

## Purge cache

You can purge static page from storefront cache by event. Otherwise, you will need to wait for cache expiration.

Virto Storefront has `/storefrontapi/content/reset-cache` end point for static page invalidation.

We recommend using Webhooks module.

1. Install `vc-module-webhooks` module.
1. Open Virto Commerce Admin UI.
1. Select Webhooks module.
1. Click `Add` button in toolbar to create a new webhook subscription.
1. Enter webhook subscription name.
1. Select `Page Builder Content Changed Event` event in Events drop-down.
1. Select `Path` and `Type` in additional fields.
1. Turn on `Activate` checkbox.
1. Enter Storefront end point in URL. Ex: https://www.mypublic-domain.com//storefrontapi/content/reset-cache
1. Save webhook subscription.


![image](docs/media/screen-webhook-settings.png)


## Page Builder theme structure
Page Builder reads meta-data from theme. Developers can extend or customize page builder behaviour by theme repository.

```text
├── client-app                    // The main folder for the application.
|   ├── shared                    // Assets needed to be precompiled during building.
|   |   └── static-content
|   |      └── components         // Vue Components for rendering Page Builder elements. 
├── config                        
|   |   └── schemas               // All Page Builder meta information are stored here.
|   |      ├── blocks             // Block definitions.
|   |      |   └──...
|   |      ├── objects            // Object definitions.
|   |      |   └──...
|   |      ├── sections           // Sections definitions.
|   |      |   └──...
|   |      ├── shared             // Global settings folder.
|   |      |   └── _blocks.json   // Global settings for blocks.
|   |      |   └── _sections.json // Global settings for sections.
|   |      └── templates          
|   |          └── page.json      // Page Builder configuration for static pages.
|   └── settings_schema.json      // Theme settings schema file. Page Builder uses it for Theme and Preset editor.
|   └── settings_data.json        // Theme config file.
```
