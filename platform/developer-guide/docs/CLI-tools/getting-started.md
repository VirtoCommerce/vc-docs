# Get Started

In this guide, we will explore how to start using **VirtoCommerce.GlobalTool**.

## Prerequisites

* .NET SDK 8.x
* Node.js 12.x
* Git SCM

## Install

To install **VirtoCommerce.GlobalTool** on your machine, run:

```console
dotnet tool install VirtoCommerce.GlobalTool  -g
```

## Update

To update **VirtoCommerce.GlobalTool** to the latest version, run:

```console
dotnet tool update VirtoCommerce.GlobalTool -g
```

## Use

* To use **VirtoCommerce.GlobalTool**, run:

    ```console
    vc-build
    ```

* To get the list of all targets, run:

    ```console
    vc-build help
    ```

    Command output

    ```console

    There is a help for targets:
    - Init
    - Install
    - Update
    - InstallModules
    - InstallPlatform
    - Uninstall
    - Clean
    - Restore
    - Compile
    - Pack
    - Test
    - PublishPackages
    - QuickRelease
    - Publish
    - WebPackBuild
    - Compress
    - PublishModuleManifest
    - SonarQubeStart
    - SonarQubeEnd
    - Release
    - ClearTemp
    - DockerLogin
    - BuildImage
    - PushImage
    - BuildAndPush
    - Configure
    - CloudEnvUpdate
    - CloudEnvSetParameter
    - CloudEnvStatus
    - CloudAuth
    - CloudInit
    - CloudEnvList
    - CloudEnvRestart
    - CloudEnvStatus
    - CloudEnvLogs
    - CloudDown
    - CloudDeploy
    - CloudUp
    ```

* To get help for the specific target, run:

    ```console
    vc-build help NameOfTheTarget
    ```


## Usage examples

Below are examples of using specific `vc-build` targets to automate development and release tasks.

### Compress

Creates a redistributable zip archive for a module or platform. The output zip file is placed in the **artifacts** folder.

To run the target, execute the following command from the root module folder of your cloned GitHub repository:

```console
vc-build Compress
```

**Example output:**

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


### Release automation targets

These targets are used to automate routine operations with **release** and **hotfix** branches:

| Target            | Description                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `StartRelease`    | Creates and pushes a new `release/version` branch from `dev`.                                                                    |
| `CompleteRelease` | - Merges `release/version` into `master` and pushes. <br> - Merges changes into `dev`, increments the minor version, and pushes. |
| `QuickRelease`    | Runs both `StartRelease` and `CompleteRelease` in sequence.                                                                      |
| `StartHotfix`     | - Increments the patch version in `master`. <br> - Creates and pushes a new `hotfix/version` branch.                             |
| `CompleteHotfix`  | - Merges the hotfix branch into `master`. <br> - Adds a tag and pushes the changes.                                              |


Each of these targets can be executed using:

```console
vc-build TargetName
```

For example:

```console
vc-build QuickRelease
```






<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← CLI tools overview</a>
    <a href="../build-automation">Build automation →</a>
</div>