---
title: Virto Commerce documentation - Custom module development
description: Virto Commerce documentation - Custom module development
layout: docs
date: 2018-05-10
priority: 8
---
## Custom module development

### Introduction

Virto Commerce Platform is an ASP.NET MVC and [AngularJS](http://angularjs.org/) Single Page Application with VirtoCommerce's modularity feature.

A module is a subdirectory of **~/Modules** directory which contains a **module.manifest** file. Additionally, a module can contain any other content such as JavaScript, CSS, image files, .NET assemblies, etc. Some content is specialized and specifics should be outlined in the module manifest. If a module contains .NET assemblies it is called a **managed module**.

Modules can extend Virto Commerce Platform either with JavaScript or with managed code.

JavaSript allows the user to:
* add new items to main menu
* add new widgets to widget containers (on dashboard or in blades) [Working with widgets](https://virtocommerce.com/docs/vc2devguide/working-with-platform-manager/basic-functions/widgets)
* add new blades
* add custom content inside the blade or totally redefine the content using [metaform](https://virtocommerce.com/docs/vc2devguide/working-with-platform-manager/basic-functions/metaform) control
* add new buttons and other content to existing blade toolbars [Working with blade toolbar](https://virtocommerce.com/docs/vc2devguide/working-with-platform-manager/basic-functions/blade-toolbar)
* define new types of notifications and add new notification templates [Working with notifications](https://virtocommerce.com/docs/vc2devguide/working-with-platform-manager/basic-functions/push-notifications)
* define new UI for settings management

Managed code allows the user to:
* add new Web API controllers
* add new services
* override existing services
* modify database

The UI can be extended with Javascript and the backend can be extended with managed code.

In addition, new security permissions as well as new application settings are added with the module manifest, but they are still used either in JavaScript or in managed code.

You can create custom modules with and without managed code. Each module will be loaded to the main application and will have its entry in the main menu.

### Publishing

![Modules contributing process](./images/Modules_contributing_process.png)


### Packaging

Module package is a distributable piece of software that can be installed in VirtoCommerce Platform. Technically, module package is a ZIP archive containing module manifest and other module content:

![ZIP archive](./images/image2015-5-29_12-13-41.png)

Modules can be unmanaged (JavaScript only) or managed (containing .NET assemblies).

#### Create an unmanaged module package

For pure JavaScript modules you can use your favorite ZIP archiver: navigate to the folder containing *module.manifest* and archive all the necessary files / folders.

#### Create a managed module package

Managed modules should be created by using a special Powershell command in Visual Studio (VS).

#### Preparing the project

The following steps are needed only once per module. Skip this paragraph if your module has the reference to VirtoCommerce.Module library.

* Open Package Manager Console in VS having your new module project loaded (Tools -> NuGet Package Manager -> Package Manager Console);
* In the "Default project" list select the module project (the one with module.manifest file);
* Install VirtoCommerce.Module package (execute command: Install-Package VirtoCommerce.Module). More info on the package: <a href="https://www.nuget.org/packages/VirtoCommerce.Module" rel="nofollow">https://www.nuget.org/packages/VirtoCommerce.Module</a>
* readme.txt is displayed after the package installation is completed.
![Package installation completed](./images/image2016-6-1_10-21-32.png)

The module is ready to be build as a package.

#### Building the module package

Execute these steps every time when you need the module package to be created / updated:

Open and build the module project in VS;If need, update the module version (in module.manifest) and build again;Open Package Manager Console (Tools -> NuGet Package Manager -> Package Manager Console);In the "Default project" list select the module project (the one with module.manifest file);Execute command: Compress-Module

![Compress-Module](./images/image2016-6-1_10-44-13.png)

The module package is created in the project directory.

### Debugging

### Versioning
