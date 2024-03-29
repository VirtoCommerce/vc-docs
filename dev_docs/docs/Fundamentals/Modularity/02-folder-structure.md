﻿# Module Solution Folder Structure

Typically, any Virto module solution is organized as shown below:

```
├── Module.Core
|	├── Events
|	|	└──...
|	├── Services
|	|	└──...
|	├── Model
|	|	└──...
|	└── ModuleConstants.cs
|
├── Module.Data
|	├── Caching
|	|	└──...
|	├── Handlers
|	|	└──...
|	├── Migrations
|	|	└──...
|	├── Model
|	|	└──...
|	├── Repositories
|	|	└──...
|	└── Services
|	|	└──...
|
├── Module.Web
|	├── Content
|	|	└──...
|	├── Scripts
|	|	└──...
|	├── dist
|	|	└──...
|	├── Controllers
|	|	└──...
|	├── Localizations
|	|	└──...
|	├── Module.cs
|	└── module.manifest
```

The sections below break down the core folder structure and clarify which folder or file stands for what.

## Module.Core
This project contains all abstractions and domain model definitions and serves as an API to access all module functionality and enable interaction between other modules. This project has a class library project type and can be packaged and distributed as a **NuGet** package.

The `Module.Core` project consists of the followng folders and files:

```
├── Module.Core
|
|	├── Events
|	├── Services
|	├── Model
|	└── ModuleConstants.cs
```

***Notes:***

+ **Events**: A folder containing all domain and integration events the module in question can trigger within the application.

+ **Services:** Contains all abstractions and interfaces of all services that represent a programming API to the entire functionality of the module domain.

+ **Model:** Contains domain model classes.

+ **ModuleConstants.cs:** Houses all module constants, such as permissions, settings, and string literals.

## Module.Data
This project is comprised of business layers and may include repositories and domain service implementations. It is also of the class library type and can be packaged and distributed as a **NuGet** package and used as a reference from other modules.

The `Module.Data` project consists of the followng folders:

```
├── Module.Data
|
|	├── Caching
|	├── Handlers
|	├── Migrations
|	├── Model
|	├── Repositories
|	└── Services
```

***Notes:***

+ **Caching**: Contains strongly typed cache regions used in the module.
    
+ **Handlers**: Houses domain and integration event handlers.
    
+ **Migrations**: Contains database migrations.
    
+ **Model**: Virto uses the **Data Mapping** pattern to isolate the domain model from the persistence specific one (**Persistence Ignorance** principle). This folder contains classes that get directly mapped to database tables with using EF fluent API.
    
+ **Repositories**: An implementation of repositories that provides a set of methods to access the database. These methods hide the code needed to implement various database features you need.
    
+ **Services**: Contains the domain CRUD services and other business logic implementations.

## Module.Web

The [**Module.Web**](http://module.web/) project represents an application level of module domain. This project uses all services and domain types in order to implement business scenarios. Initialization, public API, and user interface are also implemented on this level. This project cannot be used directly from other modules and is not distributed as a **NuGet** package.

The `Module.Core` project consists of the followng folders and files:

```
├── Module.Web
|
|	├── Content
|	├── Scripts
|	├── dist
|	├── Controllers
|	├── Localizations
|	├── Module.cs
|	└── module.manifest
```

***Notes:***

+ **Content**: Has **CSS** styles for the module user interface.
    
+ **Scripts**: Contains Angular.js JavaScript files and templates used for module presentation in Platform Manager.
    
+ **dist**: Contains the resulting JavaScript and style bundles as the output of the WebPack bundling process.
    
+ **Controllers**: Has all [ASP.NET](http://asp.net/) MVC Core REST API controllers.
    
+ **Localizations**: Contains resource files that are used for UI localization.
    
+ **Module.cs**: Core module entry point.
    
 + **module.manifest**: A required file that contains meta information describing your module with its dependencies and versions.
