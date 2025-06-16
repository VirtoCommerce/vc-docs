# Build Automation

The **vc-build** tool streamlines various build scenarios for solutions based on VirtoCommerce. Its builder-server agnostic nature and cross-platform support make it adaptable to any CI/CD pipeline or local development setup.

![vc-build CLI](media/CLI.png){: style="display: block; margin: 0 auto;" }

!!! note
    You can adjust the verbosity (level of details) of the output with the `-verbosity` parameter, which can be applied to any target. It accepts one of four values:

    - `Verbose`: Shows all messages.  
    - `Normal`: Shows information (INF) and above.  
    - `Minimal`: Shows warnings (WRN) and above.  
    - `Quiet`: Shows only errors (ERR).  

    **Example**  
    ```console
    vc-build compress -verbosity <Verbose|Normal|Minimal|Quiet>
    ```

---

## Clean

To clean your bin, objects, and artifacts directories, run:

```console
vc-build clean
```

This command helps prepare your project by clearing previous build data.


## Restore

To restore NuGet dependencies, run:

```console
vc-build restore
```

| Parameter     | Description                                        | Example| 
|------------------|--------------------------------------------------------| ---|
| `-NugetConfig`    | Specifies the path to the NuGet configuration file.   | `vc-build restore -NugetConfig <path to NuGet config>` |

This ensures all required packages are restored before compiling.


## Compile

To compile .NET Core solution, run:

```console
vc-build compile -configuration <Debug|Release>
```

| Parameter     | Description                                                                 |
|------------------|---------------------------------------------------------------------------------|
| `-configuration`  | Defines the build configuration. Default is `Release` on CI/CD, `Debug` locally. |

Use this to control the optimization level of the compiled output.


## Test

To compile the solution and execute all unit tests discovered from the projects located in the solution folder and satisfied by the mask `*.Tests|*.Testing`, run:

```console
vc-build test
```

| Parameter  | Description                                        | Example                                                  |
|----------------|--------------------------------------------------------|----------------------------------------------------------|
| `-TestsFilter` | (Optional) Filter tests by category or other criteria. | `vc-build Test -TestsFilter "Category!=IntegrationTest"` |

This command also generates a test coverage and overall stats report.

??? Example

    ```console
    vc-build test

    Starting test execution, please wait...
    A total of 1 test files matched the specified pattern.
    Passed!  - Failed:     0, Passed:    48, Skipped:     0, Total:    48, Duration: 4 s - VirtoCommerce.CatalogCsvImportModule.Tests.dll (netcoreapp3.1)

    Calculating coverage result...
    Generating report 'c:\Projects\VirtoCommerce\V3\Modules\vc-module-catalog-csv-import\.tmp\coverage.xml'
    ++++
    | Module                                    | Line   | Branch | Method |
    ++++
    | VirtoCommerce.CatalogCsvImportModule.Core | 77,17% | 73,38% | 72,83% |
    ++++
    | VirtoCommerce.CatalogCsvImportModule.Data | 56,47% | 52,15% | 56,86% |
    ++++

    ++++
    |         | Line   | Branch | Method |
    ++++
    | Total   | 65,23% | 60,64% | 66,66% |
    ++++
    | Average | 66,81% | 62,76% | 64,84% |
    ++++


    ═══════════════════════════════════════
    Target             Status      Duration
    ───────────────────────────────────────
    Restore            Executed        0:04
    Compile            Executed        0:08
    Test               Executed        1:09
    ───────────────────────────────────────
    Total                              1:22
    ═══════════════════════════════════════
    ```


## Pack

The `pack` command compiles the solution and creates NuGet packages from the projects located in the solution folder.

```console
vc-build pack
```

| Parameter        | Description                                                       | Example                                        |
|------------------|-------------------------------------------------------------------|------------------------------------------------|
| `-configuration` | (Optional) Specifies build config: `Release` (default) or `Debug` | `vc-build pack -configuration <Debug|Release>` |

It generates NuGet packages from packable projects and stores them in the **artifacts** folder.



## PublishPackages

To push discovered NuGet packages to a server and publish them, run:

```console
vc-build publishPackages -source <SOURCE> -apiKey <API_KEY>
```

| Parameter    | Description                                                                                                                                                            | Example |
|------------------|---------------------------------------------------------------------------------| -------------------------------------------------------------------------------------------|
| `-source`         | Server URL or path where the NuGet package will be published. If no source is set, the default NuGet server **https://api.nuget.org/v3/index.json** will be used. | `vc-build publishPackages -source C:\local-nuget `|
| `-apiKey`         | API key for authentication.                                                    | |



## Compress

The `compress` command creates an archive of the artifacts, including only necessary files and filtering out excess.

```console
vc-build compress
```

| Parameter     | Description                                           | Example|
|------------------|-----------------------------------------------------------| ---|
| `-configuration`  | (Optional) Build config to use for compressing artifacts.<br>`Release` (default) or `Debug`| `vc-build compress -configuration <Release|Debug>` |
| `-NugetConfig`    | (Optional) Path to NuGet configuration file.              | `vc-build compress -NugetConfig <path to NuGet config>`|



## DockerLogin

The `dockerlogin` command logs you into Docker. You can specify registry URL, username, and password as parameters.

```console
vc-build dockerlogin -DockerRegistryUrl https://myregistry.com -DockerUsername user -DockerPassword 12345
```


## BuildImage

To build docker image, run:


```console
vc-build BuildImage -DockerfilePath ./dockerfile -DockerImageFullName myimage:tag
```



## PushImage

To push docker image to the remote registry, run:


```console
vc-build PushImage -DockerImageFullName myimage:tag
```



## BuildAndPush

To build and push docker image, run:

```console
vc-build BuildAndPush -DockerRegistryUrl <registry url> -DockerUsername <username> -DockerPassword <password> -DockerfilePath ./dockerfile -DockerImageName myimage -DockerImageTag tag1 tag2 tagN
```

| Parameter        | Description                                       | 
|----------------------|-------------------------------------------------------|
| `-DockerImageTag`     | Receives an array of tags to apply to the image.     |

!!! note
    If already signed in to Docker CLI, you can skip the `DockerPassword` parameter.



## QuickRelease

The `QuickRelease` command automates the release process by creating a release branch from dev, merging it into master, incrementing the version in dev, and then deleting the release branch.

```console
vc-build QuickRelease
```

| Parameter | Description                                                             | Example                        |
|-----------|-------------------------------------------------------------------------|--------------------------------|
| `-Force`  | (Optional) Forces release even if conflicts or validation issues occur. | `vc-build QuickRelease -Force` |



## Publish

The `publish` command prepares the application for deployment by running `dotnet publish`, packaging the application and its dependencies into a publishable format.

```console
vc-build publish
```


## WebPackBuild

The `WebPackBuild` command builds the frontend assets by first installing npm dependencies and then running Webpack to compile JavaScript and other static resources.

```console
vc-build WebPackBuild
```


## PublishModuleManifest

The `PublishModuleManifest` command updates the **modules_v3.json** file with the current artifact’s **module.manifest** information, ensuring module metadata is accurate and up-to-date.

```console
vc-build PublishModuleManifest
```


## SonarQubeStart

The `SonarQubeStart` command initiates a SonarQube analysis session with `dotnet sonarscanner begin`, accepting various parameters to configure the scanning environment.

```console
vc-build SonarQubeStart -SonarBranchName dev -SonarAuthToken *** -RepoName vc-module-marketing
```

| Parameter       | Description                                |
|---------------------|------------------------------------------------|
| `SonarBranchName`    | Branch name to associate with the scan.       |
| `SonarAuthToken`     | Token used for authenticating to SonarQube.   |
| `RepoName`           | Name of the repository being scanned.         |



## SonarQubeEnd

The `SonarQubeEnd` command finalizes the SonarQube analysis session with `dotnet sonarscanner end`, completing the scanning process.

```console
vc-build SonarQubeEnd -SonarAuthToken %SonarToken%
```

| Parameter        | Description                        |
|------------------|------------------------------------|
| `SonarAuthToken` | Token used to submit scan results. |



## Release

The `release` command facilitates the creation of a GitHub release, with parameters such as `GitHubUser`, `GitHubToken`, and `ReleaseBranch` to specify the release details.

```console
vc-build release -GitHubUser VirtoCommerce -GitHubToken %token%
```

| Parameter       | Description                                                        |
|---------------------|------------------------------------------------------------------------|
| `GitHubUser`         | GitHub username/organization for publishing release.                  |
| `GitHubToken`        | Personal access token for GitHub authentication.                      |
| `ReleaseBranch`      | (Optional) Branch to release from. Default is the current branch.     |



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../getting-started">← Getting started</a>
    <a href="../package-management">Package management →</a>
</div>