# Manage Platform and Modules with CLI

In this guide, we are going to explore more `vc-build` commands. Each section provides an overview of the command’s purpose along with examples.

## Init

The `Init` command creates a **vc-package.json** file with initial content, including the latest version of the platform.

```console
vc-build Init
```


| **Parameter**       | **Description**                      | **Example**                                |
|---------------------|--------------------------------------|--------------------------------------------|
| `-PlatformVersion`  | Specifies a custom platform version. | `vc-build Init -PlatformVersion 3.52.0`    |

This setup file serves as the foundation for managing platform and module versions in your environment.



## InstallModules

The `InstallModules` command installs all modules listed in **vc-package.json** and resolves any dependencies required.

```console
vc-build InstallModules
```


| **Parameter**       | **Description**                                | **Example**                                               |
|---------------------|------------------------------------------------|-----------------------------------------------------------|
| `-DiscoveryPath`    | Specifies a custom path to discover modules.   | `vc-build InstallModules -DiscoveryPath ../modules`       |

This command ensures that all required modules are installed and their dependencies managed.


## InstallPlatform

The `InstallPlatform` command installs the platform as defined in **vc-package.json**, providing the necessary components for the platform’s operation.

```console
vc-build InstallPlatform
```

This command sets up the platform, readying it for module integration and configuration.


## ClearTemp

The `ClearTemp` command removes the **.tmp** directory.

```console
vc-build ClearTemp
```

This command helps keep your workspace clean by removing temporary build files.

