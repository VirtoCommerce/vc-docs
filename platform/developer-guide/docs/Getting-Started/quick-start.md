# Quick Start

This guide gets you from a fresh machine to a running Virto Commerce solution in three stages:

* [Install and explore locally.](#install-and-try-locally)
* [Configure your own customizations.](#configure-your-custom-solution)
* [(Optionally) contribute back.](#contribute-optionally) 

![Quick start](media/quick-start.png){: style="display: block; margin: 0 auto;" }

## Install and try locally

Use **[start-local](https://github.com/VirtoCommerce/start-local)** to bring up the full stack (Platform, Frontend, database, Redis, Elasticsearch, Kibana) on your machine in one command.

```powershell
$installSCript = Invoke-WebRequest -Uri "https://raw.githubusercontent.com/VirtoCommerce/start-local/dev/VirtoLocal_create_local_files.ps1" -UseBasicParsing; Set-Content -Path ".\VirtoLocal_create_local_files.ps1" -Value $installSCript.Content; .\VirtoLocal_create_local_files.ps1
```

## Configure your custom solution

A Virto Commerce solution is **composed**, not forked. Customize three layers independently.

1. Configure the Platform:

    !!! warning
        Do not fork the Platform source!

    1. Define which modules to install via a [package.json](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json).
    1. Configure runtime behavior via [appsettings.json](../Configuration-Reference/appsettingsjson.md). 

1. Fork the [Frontend](https://github.com/VirtoCommerce/vc-frontend) for branding and customization. Track upstream to receive releases.

1. Create a custom module:

    1. Scaffold the module:

        ```powershell
        dotnet new install VirtoCommerce.Module.Template
        dotnet new vc-module --ModuleName MyModule --Author "Me" --CompanyName MyCompany
        ```

    1. Build the package:

        ```powershell
        vc-build compress
        ```

    1. Install the resulting **ZIP** via **Modules → Advanced → Install from file**, then iterate.

    1. Use the [Extensibility Framework](../Extensibility/overview.md) to add entities, override services, extend APIs, and add admin UI without forking.

![Read more](media/readmore.png){: width="20"} [Custom module guide](../Tutorials-and-How-tos/Tutorials/creating-custom-module.md)

![Read more](media/readmore.png){: width="20"} [vc-build](../CLI-tools/overview.md)

![Read more](media/readmore.png){: width="20"} [Deploying on Virto Cloud](/platform/deployment-on-cloud/latest/deploy-on-virto-cloud/)

## Contribute (optionally)

Virto Commerce welcomes contributions: code, docs, bug reports, and feature ideas. Follow this path to submit your first pull request.

1. Fork the relevant repo:
    * [vc-platform](https://github.com/VirtoCommerce/vc-platform)
    * [vc-module-catalog](https://github.com/VirtoCommerce/vc-module-catalog)
    * [vc-frontend](https://github.com/VirtoCommerce/vc-frontend), or another.
1. Branch from **dev** (not **master**): `git checkout -b feature/short-description`.
1. Push to your fork and open a PR against upstream **dev**.
1. **Sign the CLA** when prompted on your first PR.
1. Each PR builds an [Alpha release](../Updating-Virto-Commerce-Based-Project/release-strategy-overview.md) so you can test before merge.


You now have the foundation to explore, extend, and contribute to the Virto Commerce Platform.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../..">← Overview </a>
    <a href="../ai-quick-start">AI assistance →</a>
</div>

