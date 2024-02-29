In this guide, we will explore how to start using `VirtoCommerce.GlobalTool`.

## Prerequisites

* .NET SDK 5.x
* Node.js 12.x
* Git SCM

## Install

To install `VirtoCommerce.GlobalTool` on your machine, run:

```console
dotnet tool install VirtoCommerce.GlobalTool  -g
```

## Update

To update `VirtoCommerce.GlobalTool` to the latest version, run:

```console
dotnet tool update VirtoCommerce.GlobalTool -g
```

## Use

* To use `VirtoCommerce.GlobalTool`, run:

    ```console
    `vc-build`
    ```

* To get the list of all targets, run:

    ```console
    vc-build help
    ```

    Command output

    ```console
    NUKE Execution Engine version 5.0.2 (Windows,.NETCoreApp,Version=v2.1)

    Target with name 'help' does not exist. Available targets are:
        - ChangeVersion
        - Clean
        - ClearTemp
        - Compile
        - CompleteHotfix
        - CompleteRelease
        - Compress
        - GetManifestGit
        - GrabMigrator
        - IncrementMinor
        - IncrementPatch
        - Init
        - InitPlatform
        - Install
        - InstallModules
        - InstallPlatform
        - MassPullAndBuild
        - Pack
        - Publish
        - PublishManifestGit
        - PublishModuleManifest
        - PublishPackages
        - QuickRelease
        - Release
        - Restore
        - SonarQubeEnd
        - SonarQubeStart
        - StartAnalyzer
        - StartHotfix
        - StartRelease
        - SwaggerValidation
        - Test
        - Uninstall
        - Update
        - UpdateManifest
        - ValidateSwaggerSchema
        - WebPackBuild
    ```

* To get help for the specific target, run:

    ```console
    vc-build help NameOfTheTarget
    ```

## Usage Examples

Below are the examples of using specific targets.

* **Compress**

    The target is used to create a redistributed zip archive for a module or platform. After executing, the resulting zip is placed in the `artifacts` folder.
    To execute this target, run this command in the root module folder of the cloned from GitHub repository.

    ```console
    vc-build compress
    ```

    Console output:

    ```console

    ═══════════════════════════════════════
    Target             Status      Duration
    ───────────────────────────────────────
    Clean              Executed        0:00
    Restore            Executed        0:07
    Compile            Executed        0:06
    WebPackBuild       Executed        0:00
    Test               Executed        0:05
    Publish            Executed        0:01
    Compress           Executed        0:01
    ───────────────────────────────────────
    Total                              0:23
    ═══════════════════════════════════════

    ```

* **StartRelease**, **CompleteRelease**, **QuickRelease**, **StartHotfix**, **CompleteHotfix** are used to automate routine operations with release branches.

* **StartRelease** creates and pushes the new branch release/*version* from dev.

* **CompleteRelease**:
    * Merges release/*version* into master and pushes.
    * Merges into dev branch, increments version's minor and pushes.

* **QuickRelease** triggers **StartRelease** and then **CompleteRelease**.
* **StartHotfix**:
    * increments version's patch in master.
    * creates and pushes the new branch hotfix/*version*

* **CompleteHotfix**:
    * merges hotfix branch into master.
    * adds tag and pushes.