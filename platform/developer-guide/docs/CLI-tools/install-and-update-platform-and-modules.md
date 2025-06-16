# Install and Update Platform and Modules 

In this guide, you'll learn how to install and update the Virto Commerce Platform and its modules using the vc-build command-line tool. Whether you're starting from scratch, working with a manifest, targeting specific versions, or dealing with custom modules, the steps below will guide you through each scenario.

The available options include:

* [Platform and modules installation.](#install-platform-and-modules)
* [Platform installation.](#install-platform)
* [Modules installation.](#install-modules-on-existing-platform)
* [Platform and modules update.](#update-platform-and-modules)
* [Custom modules installation.](#install-custom-modules)

## Install Platform and modules

Below you will find various ways to install both the Platform and its modules.

### Install from scratch

Use the `vc-build install` command to install the latest stable version of the Platform and modules:

1. Create and enter a new directory:

    ```bash
    mkdir platform && cd platform
    ```

1. Install the Platform and modules:

    ```bash
    vc-build install
    ```

You can use this command to:

* Initialize a new Platform in an empty directory.
* Install according to the existing **vc-package.json** manifest.


### Install from manifest

If a current directory already contains a **vc-package.json** manifest, `vc-build` will install the platform and modules as defined there. If the manifest is located elsewhere, specify its path as follows:

```bash
vc-build install -PackageManifestPath <path to vc-package.json>
```


### Install specific bundle version

To install the Platform and modules from a specific bundle version (version 9 in our example), run:

```bash
vc-build install -v 9
```

### Install latest (edge) versions

To install the latest available versions of the Platform and modules, run:

```bash
vc-build install -edge
```

## Install Platform

To install the latest stable Platform version, run:

```bash
vc-build install -platform
```


To install a specific version of the Platform (3.854.7 in our example), run:

```bash
vc-build install -platform -version 3.854.7
```


## Install modules on existing Platform

To install individual modules on top of the already installed Platform, run:

```bash
vc-build install -module VirtoCommerce.WhiteLabeling
```


## Update Platform and modules

To update **vc-package.json** with the latest Platform and module versions or install the updated versions, run:

```bash
vc-build update
```

Run the same command to update to the latest stable bundle:

```bash
vc-build update
```

To update Platform and modules to the latest available (edge) versions, run:

```bash
vc-build update -edge
```

## Install custom modules

Custom modules are defined in the **vc-package.json** manifest. Virto Commerce supports multiple module sources — both public and private. When working with private or authenticated sources, you may need to provide access tokens or credentials using specific command-line parameters.

| Source                          | Description                                                | Authentication parameter       |
| ------------------------------- | ---------------------------------------------------------- | ------------------------------ |
| GitHub releases / Private repos | Modules hosted on GitHub (public or private repositories). | `-GithubToken`                 |
| Azure pipeline artifacts        | Modules from Azure DevOps CI/CD pipeline artifacts.        | `-AzureToken`                  |
| Azure universal packages        | Universal Packages from Azure Artifacts feed.              | `-AzureUniversalPackagesPat`   |
| Azure blob storage              | Modules stored as blobs in Azure Storage.                  | `-AzureSasToken`               |
| GitLab job artifacts            | Modules built and stored as artifacts in GitLab pipelines. | `-GitLabToken`                 |
| Local files                     | Modules from the local file system.                        | No authentication required     |



To install custom modules defined in a manifest, providing tokens for GitHub and Azure as needed, run:

```bash
vc-build install -PackageManifestPath ./vc-package.json -GithubToken ghp_XXXXXXXXXXXXXXXXXXX -AzureToken azp_YYYYYYYYYYYYYYY
```


??? Example "vc-package.json example"

    ```json
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
          "Modules": [
            {
              "Id": "vc-module-custom",
              "Version": "3.16.0"
            }
          ]
        },
        {
          "Name": "AzurePipelineArtifacts",
          "Organization": "<Azure DevOps Organization>",
          "Project": "<Project name>",
          "Modules": [
            {
              "Id": "vc-module-custom",
              "Version": "3.14.0",
              "Branch": "<Branch name>",
              "Definition": "<Pipeline definition name or ID>"
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
              "Path": "C:\projects\vc\vc-module-catalog\artifacts\VirtoCommerce.Catalog"
            }
          ]
        }
      ],
      "ManifestVersion": "2.0",
      "PlatformVersion": "3.216.0"
    }
    ```

## Backup procedure

If `vc-build install` or `vc-build update` is executed in a directory that already contains Platform files, a backup will be created automatically. To skip the backup step, use:

```bash
vc-build install -skip backup
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../cold-start-and-data-migration">← Cold start and data migration</a>
    <a href="../more-targets">Managing Platform and modules →</a>
</div>