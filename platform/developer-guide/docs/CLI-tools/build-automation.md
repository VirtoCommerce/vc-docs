The `vc-build` tool streamlines various build scenarios for solutions based on VirtoCommerce. Its builder-server agnostic nature and cross-platform support make it adaptable to any CI/CD pipeline or local development setup.
<br>
<br>
<br>
<br>
![vc-build CLI](media/build-automation.png)

## Compile

To compile .NET Core solution, run:

```console
vc-build compile -configuration <Debug|Release>
```

**Parameters**:

* `-configuration <Debug|Release|CONFIGURATION>`: Defines the build configuration. The default configuration for build on build server is `Release`, on the local machine is `Debug`, but you can override the build configuration settings in your project.
  

## Test

To compile the solution and execute all unit tests discovered from the projects located in the solution folder and satisfied by the mask `*.Tests|*.Testing`, run: 

```console
vc-build test (with no args)
```

This command also generates a test coverage and overall stats report.

??? Example

    ```console
    vc-build test

    Starting test execution, please wait...
    A total of 1 test files matched the specified pattern.
    Passed!  - Failed:     0, Passed:    48, Skipped:     0, Total:    48, Duration: 4 s - VirtoCommerce.CatalogCsvImportModule.Tests.dll (netcoreapp3.1)

    Calculating coverage result...
    Generating report 'c:\Projects\VirtoCommerce\V3\Modules\vc-module-catalog-csv-import\.tmp\coverage.xml'
    +-------------------------------------------+--------+--------+--------+
    | Module                                    | Line   | Branch | Method |
    +-------------------------------------------+--------+--------+--------+
    | VirtoCommerce.CatalogCsvImportModule.Core | 77,17% | 73,38% | 72,83% |
    +-------------------------------------------+--------+--------+--------+
    | VirtoCommerce.CatalogCsvImportModule.Data | 56,47% | 52,15% | 56,86% |
    +-------------------------------------------+--------+--------+--------+

    +---------+--------+--------+--------+
    |         | Line   | Branch | Method |
    +---------+--------+--------+--------+
    | Total   | 65,23% | 60,64% | 66,66% |
    +---------+--------+--------+--------+
    | Average | 66,81% | 62,76% | 64,84% |
    +---------+--------+--------+--------+


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

To build the module solution and create NuGet packages, run:

```console
vc-build pack -configuration <Debug|Release> 
```

This command generates NuGet packages for projects with `<IsPackable>` set to `True` in the **.csproj** file.

The result of this target is NuGet packages that are stored in the `artifacts` path of the module's root folder. If you execute this target for the platform solution, the version is taken from `Directory.Build.props`. If you execute this target for a module solution, the version is taken from the module manifest file.

## PublishPackages

To push discovered NuGet packages to a server and publish them, run:

```console
vc-build publishPackages -source <SOURCE> -apiKey <API_KEY>
```

It pushes the NuGet packages discovered in the `artifacts` folder to the server specified by the `-source` parameter and publishes them.

### Example

```console
vc-build publishPackages -source C:\local-nuget 
```

**Parameters**

* `-source <SOURCE>` - Specifies the server URL. NuGet identifies a UNC or local folder source and simply copies the file there instead of pushing it using HTTP. If `-source` is not set the default NuGet server `https://api.nuget.org/v3/index.json` will be used.
* `-apiKey <API_KEY>` - The API key for the server.


## Compress 

To pack build artifacts into a distribution bundle zip, ready for transfer or publication, run:

```console
vc-build compress -configuration <Debug|Release>
```

This command puts the resulting zip into the artifact folder in the module root. 


This target normally checks and excludes from the resulting zip all files which names are enumerated in these multiple sources:

* [global module.ignore](https://raw.githubusercontent.com/VirtoCommerce/vc-platform/dev/module.ignore) file that is managed by the VirtoCommerce team.
* local `module.ignore` file that is taken from the root folder of the module.
  
??? Example

    ```console
    vc-build compress -configuration Release
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