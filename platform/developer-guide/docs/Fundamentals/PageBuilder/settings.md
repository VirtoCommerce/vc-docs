# Settings Configuration

This guide describes how to configure the settings file for the Virto Commerce Page Builder. These settings define how the builder loads templates, fetches data, saves changes, and interacts with the frontend and backend APIs.

Each setting can be either a static string or a dynamic request (or list of requests) that returns the desired value. The structure is highly flexible and supports templating, scripting, and conditional logic.

## Key settings properties

| Property                  | Description                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `templatesListUrl`      | URL or server request returning the list of available templates. Templates are managed <br>as described in the [schemas documentation](./schemas.md). |
| `sectionsListUrl`       | URL or request that returns the list of available sections (blocks).<br>Response format is documented [here](./schemas.md).                          |
| `templateUrl`           | URL or request used to fetch a selected template by path and type.                                                                                |
| `saveTemplates`         | Request for saving templates. Usually a POST request with a `files` array in the body,<br> each containing: `path`, `pageId`, `type`, and `content`.  |
| `settingsDataRequest`   | Request to retrieve the theme's **settings_data.json** file.                                                                                        |
| `settingsSchemaRequest` | Request to retrieve the theme’s **settings_schema.json** used to render the settings form and presets.                                              |
| `saveSettings`          | URL or request for saving theme settings.<br> The request format matches `saveTemplates`.                                                             |
| `uploadAssetsRequest`   | Request for uploading assets (e.g., images or media).<br>Can be defined directly or referenced as a setting.                                         |
| `fullPreviewUrl`        | URL template used as the source of the preview iframe.<br>**Example**:<br> `{{settings.storefrontUrl}}{{settings.previewPath}}?ep={{location.origin}}` <br>resolves to <https://localhost:3000/designer-preview?ep=https://localhost:5001> |
| `skipTheme`         | Boolean flag or a request resolving to a flag. If **true**, the theme settings panel is hidden. |
| `skipTemplates`     | Boolean flag or a request resolving to a flag. If **true**, template switching is disabled.     |
| `assetsUrlTemplate` | Template for forming asset upload URLs.                                                       |
| `publish`           | An object containing configuration for publishing content. Includes: <br> - `status`: URL to check publication status. <br> - `publish`: request to publish. <br> - `unpublish`: request to unpublish. <br> If not defined, the publish functionality is disabled. |
| `publishPages` | Same structure as `publish`, but used for **VirtoPages**-based pages. |
| `externalPreview` | Object with a `url` property that defines how the preview page is formed in the live environment. <br>Triggered via the preview button in the toolbar. |


## Execution context

When resolving templates or executing scripts (e.g., in `url`, `body`, or `selector`), the following context is available:

- **location**: Describes the current URL and its components. Includes: **url**, **params**, **path**, **host**, **protocol**, **hash**, **origin**.
- **settings**: Contains resolved values from other settings. This object is not evaluated dynamically.
- **config**: Configuration settings, such as theme name. Evaluated during execution.

These values can be combined to form URLs, populate request bodies, or define conditional behavior.


??? "Sample settings"
    ```json
    {
        "storefrontUrl": {
            "init": "requests",
            "requests": [
                {
                    "url": "/api/stores/{{location.params.storeId}}",
                    "method": "GET",
                    "response": {
                        "result": "$.url",
                        "isArray": false
                    }
                },
                {
                    "url": "/api/platform/settings/VirtoCommerce.PageBuilderModule.General.StoreUrl",
                    "method": "GET",
                    "response": {
                        "result": "$.value",
                        "isArray": false
                    }
                }
            ]
        },
        "previewPath": {
            "init": "requests",
            "requests": [
                {
                    "url": "/api/platform/settings/VirtoCommerce.PageBuilderModule.General.StorePreviewPath",
                    "method": "GET",
                    "cacheable": true,
                    "response": {
                        "result": "$.value",
                        "isArray": false
                    }
                },
                {
                    "url": "/api/platform/settings/VirtoCommerce.PageBuilderModule.General.StorePreviewPath",
                    "method": "GET",
                    "cacheable": true,
                    "response": {
                        "result": "$.defaultValue",
                        "isArray": false
                    }
                }
            ]
        },
        "fullPreviewUrl": "{{settings.storefrontUrl}}{{settings.previewPath}}?ep={{location.origin}}",
        "themeName": {
            "init": true,
            "url": "/api/stores/{{location.params.storeId}}",
            "method": "GET",
            "response": {
                "result": "$.dynamicProperties..values[?(@.propertyName=='DefaultThemeName')].value",
                "isArray": false
            },
            "fallbackValue": "default"
        },
        "templatesListUrl": "/api/pagebuilder/templates?storeId={{location.params.storeId}}&theme={{config.themeName}}",
        "sectionsListUrl": "/api/pagebuilder/sections?storeId={{location.params.storeId}}&theme={{config.themeName}}",
        "templateUrl": {
            "__templates": "/api/pagebuilder/template?storeId={{location.params.storeId}}&theme={{config.themeName}}&path={{path}}&type={{type}}&draft=true",
            "pages": "/api/pagebuilder/template?storeId={{location.params.storeId}}&theme={{config.themeName}}&path={{path}}&type=pages&draft=true&pageId={{pageId}}",
            "blogs": "/api/pagebuilder/template?storeId={{location.params.storeId}}&theme={{config.themeName}}&path={{path}}&type=blogs&draft=true"
        },
        "saveTemplates": {
            "url": "/api/pagebuilder/save?storeId={{location.params.storeId}}&theme={{config.themeName}}&draft=true",
            "method": "POST",
            "body": {
                "files": "{{=JSON.stringify(this.templatesToSave.map(x => ({ path: x.entry.path, pageId: x.entry.pageId, type: x.entry.type, content: x.content })))}}"
            }
        },
        "publish": {
            "status": "/api/content/{{type}}/{{location.params.storeId}}/publish-status?relativeUrl={{path}}",
            "publish": {
                "url": "/api/content/{{type}}/{{location.params.storeId}}/publishing?relativeUrl={{path}}&publish=true",
                "method": "POST"
            },
            "unpublish": {
                "url": "/api/content/{{type}}/{{location.params.storeId}}/publishing?relativeUrl={{path}}&publish=false",
                "method": "POST"
            }
        },
        "publishPages": {
            "status": "/api/page-builder-pages/grouped/publish-status/?id={{pageId}}",
            "publish": {
                "url": "/api/page-builder-pages/grouped/publishing/?id={{pageId}}&publish=true",
                "method": "POST"
            },
            "unpublish": {
                "url": "/api/page-builder-pages/grouped/publishing/?id={{pageId}}&publish=false",
                "method": "POST"
            }
        },
        "externalPreview": {
            "url": "{{settings.storefrontUrl}}/pages?path={{path}}"
        },
        "settingsDataRequest": "/api/pagebuilder/template?storeId={{location.params.storeId}}&path={{settings.settingsPath}}&type=themes",
        "settingsSchemaRequest": "/api/pagebuilder/template?storeId={{location.params.storeId}}&path={{config.themeName}}/config/settings_schema.json&type=themes",
        "saveSettings": {
            "url": "/api/pagebuilder/save?storeId={{location.params.storeId}}&theme={{config.themeName}}",
            "method": "POST",
            "body": {
                "files": "[{\"path\": \"{{settings.settingsPath}}\", \"type\": \"themes\", \"content\": {{item}}}]"
            }
        },
        "settingsPath": "{{config.themeName}}/config/settings_data.json",
        "defaultPreviewUrl": "/",
        "uploadAssetsRequest": {
            "url": "/api/content/pages/{{location.params.storeId}}?folderUrl=/assets/pages&name={{file.assetName}}",
            "method": "POST",
            "form": {
                "name": "uploadedFile",
                "fileName": "{{file.assetName}}"
            },
            "response": {
                "result": "$[0].url",
                "isArray": false
            }
        },
        "skipTheme": {
            "init": true,
            "url": "/api/platform/security/currentuser",
            "method": "GET",
            "cacheable": true,
            "response": {
                "selector": "this.response.permissions.indexOf('builder:theme') === -1",
                "isArray": false
            }
        },
        "skipTemplates": {
            "init": true,
            "url": "/api/platform/security/currentuser",
            "method": "GET",
            "cacheable": true,
            "response": {
                "selector": "this.response.permissions.indexOf('builder:templates') === -1",
                "isArray": false
            }
        }
    }
    ```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../server-descriptors">← Server descriptors </a>
    <a href="../schemas">Schemas →</a>
</div>