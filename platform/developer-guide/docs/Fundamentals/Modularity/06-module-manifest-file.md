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



## Apps section

Apps are entries that show up in the Platform's **Apps** menu. Each app declares its identity, icon, and permission inside the `<apps>` section of **module.manifest**. The Platform serves the app's static content from the deployed module and binds it to the `/apps/[id]` URL.

```xml title="module.manifest"
<apps>
    <app id="reports">
        <title>Reports</title>
        <description>Power BI Commerce Reports</description>
        <iconUrl>/apps/reports/power_bi_logo.svg</iconUrl>
        <permission>PowerBiReports:access</permission>
    </app>
</apps>
```

### App attributes

| Attribute | Description |
| --- | --- |
| `id` | A unique app identifier within the Platform. Becomes part of the runtime URL `/apps/[id]`. |
| `title` | The name shown to users in the Apps menu. |
| `description` | A short description shown next to the title. |
| `iconUrl` | The URL or path to the app's icon. Typically `/apps/[id]/<file>` for assets shipped with the app, or `Modules/$(ModuleId)/Content/<file>` for module-level icons. |
| `permission` | The permission a user must have to see and open the app. |
| `contentPath` | Optional override for the path to the app's content, relative to the module's install directory. When omitted, the Platform serves the app from **Content/[id]** and throws a module initialization error if the folder is missing. |
| `supportEmbeddedMode` | Optional. When `true`, allows the app to be opened inside the AngularJS-based back office in embedded mode. See [Enabling Embedded Mode for VC-Shell Instances](../../Tutorials-and-How-tos/How-tos/enable-embedded-mode-for-vc-shell.md). |

### Registration procedures

Two registration paths exist depending on what kind of app you ship:

* [Register your own app](../../custom-apps-development/register-your-own-app.md): For custom back-office apps you build yourself, packaged into a module via the Virto Commerce CLI (vc-build). VC-Shell is the recommended framework, but other frontend toolchains, such as Vue, React, or Angular, are also supported.
* [Register a third-party app](../../custom-apps-development/register-third-party-app.md): For Apps menu entries that hand the user off to an external service via a static redirect, for example, the [Power BI Reports module](https://github.com/VirtoCommerce/vc-module-power-bi-reports).



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../IPlatformStartup">← IPlatformStartup </a>
    <a href="../05-best-practices"> Best practices →</a>
</div>
