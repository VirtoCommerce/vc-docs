# Module.manifest

**Module.manifest** is an XML file containing a top-level `<module>` node with a number of section elements.

The **module.manifest** file is always included into a module package to:

* Provide information to the Platform runtime when a module is loading.
* Build the module package. 

## File settings

The **module.manifest** file can be configured using a number of required and optional settings.

### Required settings

* `<id>`: A case-insensitive module identifier. It must be unique across the set of modules in which the module 6 resides. IDs cannot contain spaces or characters that are not valid for a URL. In general, they follow the .NET namespace rules.

    ``` xml
    <id>VirtoCommerce.Cart</id>
    ```

* `<version>`: The version of the package following the major.minor.patch pattern.
  
    ``` xml
    <version>3.27.0</version>
    ```

* `<platformVersion>`: The minimum Platform version the current module is compatible with.

    ``` xml  
    <platformVersion>3.62.0</platformVersion>
    ```

* `<assemblyFile>`: The value specifying the name of the assembly, which the module type is loaded from. 

    ``` xml  
    <assemblyFile>VirtoCommerce.CartModule.Web.dll</assemblyFile>
    ```

* `<moduleType>`: A fully qualified name of the type. It includes its namespace with a class that implements the IModule interface. The module loader creates an instance of the module class, and then it calls the Initialize method. 
    
    ``` xml  
    <moduleType>VirtoCommerce.CartModule.Web.Module, VirtoCommerce.CartModule.Web</moduleType>
    ```

### Optional settings

* `<version-tag>`: A pre-release suffix of the version. 
    
    ``` xml      
    <version-tag>beta001</version-tag>
    ```

* `<title>`, `<description>`,`<authors>`, `<owners>`: A human-friendly title and description of the module, which may be used in the Platform Manager UI. 
    
    ``` xml
    <title>Shopping cart module</title>
    <description>Shopping cart / checkout functionality</description>
    <authors>
      <author>Virto Commerce</author>
    </authors>
    <owners>
      <owner>Virto Commerce</owner>
    </owners>
    ```

* `<projectUrl>`: A URL for the package home page displayed by the Platform Manager UI.

    ``` xml
    <projectUrl>https://virtocommerce.com/apps/extensions/virto-shoppingcart-module</projectUrl>
    ```

* `<iconUrl>`: A path to an image file shown in the Platform Manager UI as a module icon. This can be either a path to an image file within the module, located in the Content folder, or a URL to an external image.

    ``` xml 
    <iconUrl>Modules/$(VirtoCommerce.Cart)/Content/logo.png</iconUrl>
    ```

* `<startupType>`: A fully qualified name of a class that implements the `IPlatformStartup` interface. When declared, the Platform discovers and invokes this class during startup phases that occur before the standard `IModule` lifecycle, for example, to add configuration sources or register host-level services.

    ``` xml
    <startupType>VirtoCommerce.CartModule.Web.CartModuleStartup, VirtoCommerce.CartModule.Web</startupType>
    ```

    <br>
    ![Readmore](media/readmore.png){: width="25"} [IPlatformStartup](IPlatformStartup.md)

    ![Readmore](media/readmore.png){: width="25"} [Loading modules into application process](04-loading-modules-into-app-process.md)
    <br>

* `<dependencies>`: Any number of `<dependency>` elements that identify other modules this module depends on. Each `<dependency>` requires an `id` and a `version` attribute. To mark a dependency as optional  add the `optional="True"` attribute.

    ```xml
    <dependencies>
      <dependency id="VirtoCommerce.Core" version="3.22.0" />
      <dependency id="VirtoCommerce.Export" version="3.800.0" optional="True" />
    </dependencies>
    ```

    ![Readmore](media/readmore.png){: width="25"} [Optional dependency between modules](optional-dependency.md)

<details><summary>Module.manifest example</summary>

  ``` xml title="module.manifest"
  <module xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <id>VirtoCommerce.Cart</id>
    <version>3.27.0</version>
    <version-tag>beta001</version-tag>
    <platformVersion>3.62.0</platformVersion>
    <title>Shopping cart module</title>
    <description>Shopping cart / checkout functionality</description>
    <authors>
      <author>Virto Commerce</author>
    </authors>
    <owners>
      <owner>Virto Commerce</owner>
    </owners>
    <projectUrl>https://virtocommerce.com/apps/extensions/virto-shoppingcart-module</projectUrl>
    <iconUrl>Modules/$(VirtoCommerce.Cart)/Content/logo.png</iconUrl>
    <assemblyFile>VirtoCommerce.CartModule.Web.dll</assemblyFile>
    <moduleType>VirtoCommerce.CartModule.Web.Module, VirtoCommerce.CartModule.Web</moduleType>
    <startupType>VirtoCommerce.CartModule.Web.CartModuleStartup, VirtoCommerce.CartModule.Web</startupType>
    <dependencies>
      <dependency id="VirtoCommerce.Core" version="3.22.0" />
      <dependency id="VirtoCommerce.Export" version="3.800.0" optional="True" />
    </dependencies>
  </module>
  ```
</details>



## Adding new app

To add a new web, add the app section into the **module.manifest** file:

```xml
...
<apps>
    <app id="reports">
        <title>Reports</title>
        <description>Power BI Commerce Reports</description>
        <iconUrl>/apps/reports/power_bi_logo.svg</iconUrl>
        <permission>PowerBiReports:access</permission>
    </app>
</apps>
...
```

You can use the following attributes:

* `id`: A unique identifier for the app, which distinguishes it from other apps in the system.
* `title`: The name or title of the app that is displayed to the users.
* `description`: A short description of the app that gives users an overview of what the app does and its purpose.
* `iconUrl`: The URL or path to the app's icon or logo used to identify the app in the system.
* `permission`: The permissions or access rights required to use the app, which are used to control who can access the app and its features.
*  `contentPath`: The default path to the app's content  specifying where the app's files are stored. If the ContentPath is set to `[VcModuleWeb]/Content/[Id]`, the app's content is stored in the **Content** folder of the **VcModuleWeb** module, with the app's Id appended to the end of the path.



## Declaring settings

A module can declare its settings directly in **module.manifest** instead of registering them in code. The platform parses the `<settings>` element at startup and registers each descriptor, so the settings surface through the existing settings API with no extra code. This also lets frontend-only modules, which ship no assembly, declare settings.

Add a `<settings>` element with one `<setting>` per descriptor:

```xml title="module.manifest"
<settings>
  <setting>
    <name>VirtoCommerce.MyModule.MaxRetries</name>
    <groupName>MyModule|Reliability</groupName>
    <valueType>PositiveInteger</valueType>
    <defaultValue>3</defaultValue>
  </setting>
</settings>
```

A `<setting>` supports the following elements:

* `name`: The unique setting key. Required.
* `groupName`: The group path shown in the settings UI, for example MyModule|Reliability. Required.
* `valueType`: The value type, for example ShortText, Boolean, PositiveInteger, or Integer. Required.
* `defaultValue`: The value used when nothing is stored.
* `displayName`: A human-friendly label for the settings UI.
* `allowedValues`: A fixed list of `<value>` entries when the setting is a dictionary.

By default every setting is global, with one value shared across all administrators. Read global settings through `/api/platform/settings/v2/global/*`.

### Per-user settings

To store a value per administrator rather than globally, add the `tenant="UserProfile"` attribute. The value then follows the user across devices, for example a theme preference or layout density.

```xml title="module.manifest"
<settings>
  <setting tenant="UserProfile">
    <name>VirtoCommerce.SystemOperations.DefaultTheme</name>
    <groupName>System Operations|UI</groupName>
    <displayName>Theme preference</displayName>
    <valueType>ShortText</valueType>
    <defaultValue>system</defaultValue>
    <allowedValues>
      <value>system</value>
      <value>light</value>
      <value>dark</value>
    </allowedValues>
  </setting>
</settings>
```

Per-user values are read and written through the `/api/platform/settings/v2/me/*` endpoints, which resolve the current user from the auth token. No `platform:setting:*` permission is required to manage your own profile settings. On the frontend, the `useModuleSettings` composable reads both the global and per-user scopes in a single round trip.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../IPlatformStartup">← IPlatformStartup </a>
    <a href="../07-backoffice-app-modularity"> Back-Office UI Modularity →</a>
</div>
