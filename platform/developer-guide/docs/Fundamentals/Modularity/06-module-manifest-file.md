# Module.manifest

**Module.manifest** is an XML file containing a top-level `<module>` node with a number of section elements.

The **module.manifest** file is always included into a module package to:

* Provide information to the platform runtime when a module is loading.
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

* `<platformVersion>`: The minimum platform version the current module is compatible with.

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

* `<dependencies>`: Any number of `<dependency>` elements that identify other modules this module depends on. 

    ```xml 
    <dependencies>
      <dependency id="VirtoCommerce.Core"` `version="3.22.0" />
    </dependencies>
    ```

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
  <dependencies>
      <dependency id="VirtoCommerce.Core" version="3.22.0" />  
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
