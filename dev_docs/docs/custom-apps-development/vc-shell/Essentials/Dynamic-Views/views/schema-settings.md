# Schema Settings API

Every newly created view must have settings that describe its behavior and appearance. Depending on the type of view used, the settings may vary slightly. The settings are represented by an object built using the following SettingsBase interface:

```typescript
interface SettingsBase {
    url?: string;
    localizationPrefix: string;
    id: string;
    titleTemplate: string;
    composable: string;
    toolbar: {
        id: string;
        title: string;
        icon: string;
        method: string;
    }[];
    component: "DynamicBladeForm" | "DynamicBladeList";
    permissions?: string | string[];
    pushNotificationType?: string | string[];
    isWorkspace?: boolean;
}
```

| Property | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the view. This option is required if you want to add the view to the navigation menu or want to access it directly by URL. If you do not specify a URL, the view will be available only as a child view of another view. |
| `id` | `string` | The unique ID of the view. This option is required. The ID is used to identify the view in the navigation system and provides scheme overriding capabilities. |
| `localizationPrefix` | `string` | The prefix used for localization keys. This option is required. The prefix is used to provide localized content for the view. For example, if you specify the prefix `MyList`, the localization key for the title of the view will be `MyList.Title`. Under the hood, [vue-i18n](https://kazupon.github.io/vue-i18n/) is used. |
| `titleTemplate` | `string` | The title of the view that is shown in the blade header by default. This option is required. |
| `component` | `"DynamicBladeForm" | "DynamicBladeList"` | The name of the Vue component used by the view. This option is required. It could be one of the following values: <br> - `DynamicBladeList` <br> - `DynamicBladeForm` |
| `composable` | `string` | The name of the composable used by the view. This option is required. |
| `isWorkspace` | `boolean` | Indicates whether the view is a workspace. This option is used to determine which view should be the default view. Default: `false` |
| `toolbar` | `object[]` | An array of objects representing the toolbar buttons. This option is optional. If you do not specify any buttons, the toolbar will not be displayed. Each object in the array must have the following properties: id, title, icon, and method. More info about toolbar creation can be found in the [Toolbar](./toolbar.md) section. |
| `permissions` | `string | string[]` | The permissions required to access the view. This option is optional. If you do not specify any permissions, the view will be available to all users. |
| `pushNotificationType` | `string | string[]` | The push notification types associated with the view. This option is optional. If you do not specify any push notification types, the view will not receive any push notifications. |
