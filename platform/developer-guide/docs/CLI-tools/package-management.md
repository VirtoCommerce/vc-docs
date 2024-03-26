# Package Management

The `vc-build` tool provides a set of targets that allow you to easily install, uninstall, update, and configure platform dependencies via simple CLI commands.

## Install

The `install` command fetches the platform or modules and installs them in the appropriate folder. Versions can be specified in command parameters or defined in **vc-package.json**. This allows `vc-build` to easily restore the platform with modules on a different machine, such as a build server, without all these packages.

If the command parameters have not been specified and **vc-package.json** is not found in the local folder, the command installs the latest stable release by default. If you need the latest available versions, use the `-edge` parameter.

By default, the `install` command installs all modules listed as dependencies in **vc-package.json**. 

The path to **vc-package.json**, discovery, and probing paths can be overridden with the `PackageManifestPath`, `DiscoveryPath`, `ProbingPath` parameters. We can also skip dependency solving with `SkipDependencySolving` parameter.

This target installs stable versions of modules by default. If you need the latest available versions, use the `-edge` parameter.

If you use a source that requires authorization, you can pass tokens using the `GithubToken`, `AzureToken`, `GitLabToken` parameters.
 
```console
vc-build install (with no args)
vc-build install -GitLabToken $GITLAB_TOKEN -githubtoken $GITHUB_TOKEN -AzureToken $AZURE_TOKEN
vc-build install -platform -version <version>
vc-build install -platform -PlatformAssetUrl https://github.com/VirtoCommerce/vc-platform/releases/download/3.216.13/VirtoCommerce.Platform.3.216.13.zip
vc-build install -module <module> -version <version>
vc-build install -module <module>:<version>
vc-build install -PackageManifestPath some_directory/vc-package.json -DiscoveryPath ../modules -ProbingPath platform_dir/app_data/modules -SkipDependencySolving
```


??? "vc-package.json file example"
    ```console
    {
      "Sources": [
        {
          "Name": "GithubReleases",
          "ModuleSources": [
            "https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json"
          ],
          "Modules": [
            {
              "Id": "VirtoCommerce.Assets",
              "Version": "3.200.0"
            }
          ]
        },
        {
          "Name": "GithubPrivateRepos",
          "Owner": "VirtoCommerce",
          "Modules":[
            {
              "Id": "vc-module-custom",
              "Version": "3.16.0"
            }
          ]
        },
        {
          "Name": "AzurePipelineArtifacts",
          "Organization": "<The name of the Azure DevOps organization.>",
          "Project": "<Project ID or project name>",
          "Modules": [
            {
              "Id": "vc-module-custom",
              "Version": "3.14.0",
              "Branch": "<Branch name>",
              "Definition": "<definition name with optional leading folder path, or the definition id>"
            }
          ]
        },
        {
          "Name": "AzureUniversalPackages",
          "Organization": "https://dev.azure.com/<YOUR_ORGANIZATION>",
          "Feed": "<FEED_NAME>",
          "Project": "<YOUR_PROJECT_NAME>",
          "Modules": [
            {
              "Id": "<PACKAGE_NAME>",
              "Version": "<PACKAGE_VERSION>"
            }
          ]
        },
        {
          "Name": "AzureBlob",
          "Modules": [
            {
              "BlobName": "CustomCompany.CustomModule1_3.200.0.zip"
            }
          ],
          "Container": "modules",
          "ServiceUri": "https://vcpsblob.blob.core.windows.net"
        },
        {
          "Name": "GitlabJobArtifacts",
          "Modules": [
            {
              "JobId": "3679907995",
              "ArtifactName": "artifacts/VirtoCommerce.Catalog_3.255.0.zip",
              "Id": "42920184"
            }
          ]
        },
        {
          "Name": "Local",
          "Modules": [
            {
              "Path": "C:/projects/vc/vc-module-saas/artifacts/VirtoCommerce.SaaS_3.214.0.zip",
              "Id": "OptionalForThisSource"
            },
            {
              "Path": "C:\\projects\\vc\\vc-module-catalog\\artifacts\\VirtoCommerce.Catalog"
            }
          ]
        }
      ],
      "ManifestVersion": "2.0",
      "PlatformVersion": "3.216.0"
    }
    ```


## Update

This command updates the platform and all modules linked to the version specified by `<version>`, respecting semver.
If `<version>` is not specified, the component will be updated to the latest version.
If no args are specified, the platform and all modules in the specified location will be updated.

This command also updates the installed dependency versions in the **vc-package.json** file.
Since the version 3.15.0 this target updates to stable bundles by default. If you want to update to the latest available versions you can add `-edge` parameter.
You can specify the bundle to update your environment to specific versions using -v <bundle name> parameter.

```console
vc-build update (with no args)
vc-build update -edge
vc-build update -v 5
vc-build update -platform
```

## Uninstall

The uninstall command removes the specified module and its dependencies. It also removes uninstalled modules from your **vc-package.json**.

```console
vc-build uninstall -module <module>
```

**Example**
```console
vc-build uninstall -module VirtoCommerce.Cart
```

## Configure

The configure command checks and updates connection strings in the **appsettings.json** file.

```console
vc-build configure -sql <sql connection string> -redis <redis connection string> -AzureBlob <container connection string> [-appsettingsPath ./appsettings.json]
```
