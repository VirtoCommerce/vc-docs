# Custom Modules Templates for Dotnet New

In this guide, we will learn how to create own custom module using `dotnet new` templates for Virto Commerce modules. This feature allows you to create a Virto Commerce module with a pre-configured entity, simplifying the development and integration of new components.

| Template Name                                                                                                                 | Description |
|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| [vc-module-dba-xapi](https://github.com/VirtoCommerce/vc-cli-module-template/tree/main/templates/vc-module-dba-xapi-template) | Creates a new Virto Commerce module with DB Agnostic and xAPI support. |
| [vc-module-dba](https://github.com/VirtoCommerce/vc-cli-module-template/tree/main/templates/vc-module-dba-template)           | Creates a new Virto Commerce module with DB Agnostic support. |
| [vc-module-xapi](https://github.com/VirtoCommerce/vc-cli-module-template/tree/main/templates/vc-module-xapi-template)         | Creates a new Virto Commerce module with xAPI support. |
| [vc-crud](https://github.com/VirtoCommerce/vc-cli-module-template/tree/main/templates/vc-crud-template)                       | Creates all the classes needed for CRUD operations. |


[![video tutorial](media/video-tutorial-button.png)](https://youtu.be/C77kBhl1At4)


## Install

To install the templates, run:

```powershell
dotnet new install VirtoCommerce.Module.Template
```

## Create new module from template

To create new module:

1. Open Windows PowerShell console.
1. Navigate to your sources folder.
1. Run one of the following commands depending on the type of module you want to create:

    ```powershell 
    dotnet new vc-module-dba-xapi --ModuleName CustomerReviews --Author "Jon Doe" --CompanyName VirtoCommerce
    ```

    ```powershell
    dotnet new vc-module-dba --ModuleName CustomerReviews --Author "Jon Doe" --CompanyName VirtoCommerce
    ```

    ```powershell
    dotnet new vc-module-xapi --ModuleName CustomerReviews --Author "Jon Doe" --CompanyName VirtoCommerce
    ```

    **Parameters**

    | Options               | Description                           | Type   | Required | Default value |
    |-----------------------|---------------------------------------|--------|----------|---------------|
    | --Author (or -A)      | Your name                             | string | Optional | John Doe      |
    | --CompanyName (or -C) | Your company name                     | string | Optional | VirtoCommerce |
    | --ModuleName (or -M)  | Your module name                      | string | Optional | NewModule     |
    | --ModuleVersion       | Your module version                   | string | Optional | 3.800.0       |
    | --PlatformVersion (or -P) | Virto Commerce platform version   | string | Optional | 3.876.0       |
    | --CoreVersion         | Virto Commerce Core module version    | string | Optional | 3.800.0       |
    | --XapiVersion (or -X) | XAPI module version                   | string | Optional | 3.901.0       |



1. A **vc-module-customer-reviews** folder with module solution has been created.

!!! info
    You can pass PlatformVersion attribute to create a new module for specific version of Virto Commerce.  


## Create CRUD classes from template

To create CRUD classes from template, run the following command:

```powershell
dotnet new vc-crud --EntityName FooBar --CompanyName VirtoCommerce --ModuleName CustomerReviews
```

**Parameters**

| Options | Description | Type | Required | Default value |
|--------|-------------|------|----------|---------------|
| --CompanyName (or -C) | Your company name| string | Optional | VirtoCommerce |
| --ModuleName (or -M) | Your module name | string | Optional | NewModule |
| --EntityName (or -E) | New entity name  | string | Optional | FooBar |

It will create a folder called **vc-module-customer-reviews** with models, events, and services needed for CRUD operations. The company name and the module name are used to create the namespace for new classes.

!!! note
    You can simply copy most of these files into your module, but you will need to merge new **DbContext.cs**, **Repository.cs**, and **Module.cs** files with existing ones.

## Uninstall

To uninstall templates, run:

```powershell
dotnet new uninstall VirtoCommerce.Module.Template
```

## Contribute

To improve and extend the module creation process, contribute to the **dotnet new** templates by:

* [Installing templates locally.](#install-templates-locally)
* [Uninstalling them.](#uninstall-locally-installed-templates)

### Install templates locally

To install templates locally:

1. Open Windows PowerShell console
1. Clone repository

    ```powershell
    git clone https://github.com/VirtoCommerce/vc-cli-module-template
    ```

1. Install downloaded templates:

    ```powershell
    dotnet new install vc-cli-module-template\templates
    ```

### Uninstall locally installed templates

To uninstall locally installed templates, run:

```powershell
dotnet new uninstall <full or relative path to the templates directory>
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../creating-custom-module">← Creating custom module from template </a>
    <a href="../create-new-module-from-scratch">Create new module from scratch  →</a>
</div>