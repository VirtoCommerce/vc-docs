# Schemas
This section describes the schema structure that powers the Page Builder in Virto Commerce. It explains how to define and organize templates, sections, blocks, shared settings, and reusable objects. These JSON-based schemas enable developers to control layout, behavior, and editable settings in the Page Builder through a structured, extensible configuration.

## Theme structure
Page Builder reads metadata from the theme. Developers can extend or customize Page Builder behavior through the theme repository.

```text
├── client-app                    // The main folder for the application.
|   ├── shared                    // Assets needed to be precompiled during building.
|   |   └── static-content
|   |      └── components         // Vue Components for rendering Page Builder elements.
├── config
|   |   └── schemas               // All Page Builder meta information are stored here.
|   |      ├── templates
|   |      |   └── page.json      // Page Builder configuration for static pages.
|   |      ├── sections           // Sections definitions.
|   |      |   └──...
|   |      ├── blocks             // Block definitions.
|   |      |   └──...
|   |      ├── shared             // Global settings folder.
|   |      |   └── _blocks.json   // Global settings for blocks.
|   |      |   └── _sections.json // Global settings for sections.
|   |      └── objects            // Object definitions.
|   |          └──...
|   └── settings_schema.json      // Theme settings schema file. Page Builder uses it for Theme and Preset editor.
|   └── settings_data.json        // Theme config file.
```

### Templates

Each file is a descriptor for a particular page, template, or group of pages. Dropdown options in the template selector are generated from these descriptors.

| Property         | Type                                                                             | Required value | Description                                                                    |
|------------------|----------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------|
| `name`           | string                                                                           | true   | Template or page name.                                                                  |
| `alias`          | string                                                                           | true   | Used for routing, must be unique.                                                       |
| `previewUrl`     | string                                                                           | true   | url for preview this page in preview area.                                              |
| `path`           | string                                                                           | false  | Path to file with page content relative to storage root.                                |
| `type`           | string                                                                           | false  | ContentType for template (`pages`, `theme`, etc.)                                      |
| `request`        | `ServerRequestDescriptor` <br> `ServerRequestDescriptor[]` <br> string <br> string[]   | false  | Descriptor for loading children elements.                                               |
| `sort`           | number                                                                           | false  | Ability to sort items in dropdown.                                                      |
| `isDefault`      | boolean                                                                          | false  | Default template.                                                                       |
| `sections`       | string[]                                                                         | false  | List of available sections for current template.<br>If array is empty, every section will be available. |
| `settings`       | `SectionPropertyDescriptor[]`                                                    | false` | Template settings.                                                                     |
| `children`       | `TemplateEntryList`                                                              | false` | Children templates.                                                                    |
| `previewMessage` | any                                                                              | false` | Additional data, that sends to preview area.                                            |

=== "Basic template example"
    ```json
    {
    "name": "Homepage",
    "alias": "homepage",
    "previewUrl": "/",
    "type": "pages",
    "sections": [ ],
    }
    ```

=== "Template with sections and settings"
    ```json
    {
    "name": "Products",
    "previewUrl": "/products/hp-laserjet-pro-mfp-m130fw",
    "type": "theme",
    "sections": [
        "call-to-action",
        "call-to-action-with-image",
        "features",
        "image",
        "products",
        "text",
        "title"
    ],
    "settings": [
        {
        "id": "header",
        "label": "Page Header / H1",
        "type": "string"
        }
    ]
    }
    ```

=== "Template with dynamic children (request descriptor)"

    ```json
    {
    "name": "Pages",
    "previewUrl": "",
    "request": [
        {
        "url": "/api/content/pages",
        "method": "get",
        "cacheable": true
        }
    ],
    "type": "pages"
    }
    ```

### Sections

Each file defines a section that can be added to a page. The section editor in the UI is based on this configuration.

| Property        | Type                          | Description                                                                                                 |
|-----------------|-------------------------------|-------------------------------------------------------------------------------------------------------------|
| `icon`          | string                        | Icon in section list.                                                                                        |
| `name`          | string                        | Section name in list of new elements.                                                                        |
| `static`        | boolean <br> string           | Indicates that block is static. These blocks cannot be added or removed. <br>Actually it is a section settings. |
| `displayField`  | string                        | Property name, that used for indicate section in section list.                                              |
| `sort`          | number                        | Order section in list of new elements.                                                                      |
| `settings`      | `SectionPropertyDescriptor[]` | List of descriptors for section properties.                                                                  |
| `default`       | `SectionModel`                | Default section model. Used for creation of new section.                                                    |
| `group`         | string                        | Sections can be grouped in add new element panel.                                                            |
| `groupIcon`     | string                        | Group icon.                                                                                                  |
| `groupSort`     | number                        | Group sort.                                                                                                  |
| `includeShared` | string[]                      | List of names to add settings from Shared.                                                                   |
| `excludeShared` | string[] <br> true            | `true` - not use shared settings, <br>`string[]` - list of settings id to exclude from result shared list.       |

<!-- blocks?: string[]; -->
<!-- inline?: boolean; // used for settings groups, when false, group displayed as a overlap panel -->


=== "Simple text section"
    ```json
    {
      "name": "Text",
      "icon": "text_snippet",
      "displayField": "title",
      "settings": [
        {
          "id": "title",
          "label": "Title",
          "type": "string"
        },
        {
        "id": "text",
        "label": "Content",
        "type": "text"
        }
      ]
    }
    ```

=== "Image section with group settings"
    ```json
    {
      "name": "Image",
      "icon": "image",
      "displayField": "name",
      "group": "Media",
      "groupIcon": "media",
      "settings": [
        {
          "id": "image",
          "type": "images",
          "multiple": false
        },
        {
          "id": "alttext",
          "label": "Alternative Text",
          "type": "string"
        }
      ]
    }
    ```

### Blocks

A section can contain a list of blocks. Block format is the same as for sections.

### Shared

Settings can be grouped in shared files. These shared settings can be reused across sections and blocks. Global settings for sections are defined in **_sections.json**, and for blocks in **_blocks.json**.

You can also organize reusable setting groups in separate files and include them via the `includeShared` property in section or block descriptors.

| Property   | Type                          | Description                |
|------------|-------------------------------|----------------------------|
| `settings` | `SectionPropertyDescriptor[]` | Property descriptors array |

### Objects

Section property can be object. In this case, it is necessary to describe the structure of this object in a separate file, that should be stored in folder `objects`.

| property   | type                          | description                |
|------------|-------------------------------|----------------------------|
| `settings` | `SectionPropertyDescriptor[]` | Property descriptors array |


=== "Button object editor (**button.json** file)"
    ```json
    {
      "settings": [
        {
        "id": "caption",
        "type": "string",
        "label": "Caption"
        },
        {
        "id": "action",
        "type": "select",
        "label": "onClick action",
        "default": "popup",
        "options": [
            { "label": "Show popup", "value": "popup" },
            { "label": "Go to link", "value": "url" }
        ]
        },
        {
        "id": "url",
        "type": "string",
        "label": "Enter link",
        "visibility": "!!this.item && this.item.action === 'url'"
        }
      ]
    }
    ```

=== "Using the button object in a section"
    ```json
    {
    "settings": [
        {
        "id": "button",
        "type": "object",
        "label": "Button",
        "elementDescriptor": "button"
        }
    ]
    }
    ```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../settings">← Settings </a>
    <a href="../component-context">Component context →</a>
</div>