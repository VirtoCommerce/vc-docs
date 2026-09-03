# Local install with start-local

`start-local` is a turnkey script that runs the full Virto Commerce stack in Docker containers on your local machine. It starts the Platform backend, Frontend, database, Redis, Elasticsearch, and Kibana with a single PowerShell command. Use it as the fastest way to try Virto Commerce or to set up an isolated local development environment.

!!! warning
    This setup is intended for local development and testing only. It is not suitable for production. Elasticsearch and Kibana run with security features disabled. Do not expose any of the listed ports beyond your local machine.

## Prerequisites

Before you begin, make sure you have:

* Around 5 GB of free disk space.
* .NET SDK installed.
* `vc-build` tool installed (run `dotnet tool install VirtoCommerce.GlobalTool -g`).
* Docker installed and running.
* PowerShell 7 (required on every supported OS, including Windows).
* On Linux and macOS, Docker configured to run without `sudo`.

## Install and run

Open a PowerShell 7 terminal in an empty working directory and run:

```powershell
$installSCript = Invoke-WebRequest -Uri "https://raw.githubusercontent.com/VirtoCommerce/start-local/dev/VirtoLocal_create_local_files.ps1" -UseBasicParsing; Set-Content -Path ".\VirtoLocal_create_local_files.ps1" -Value $installSCript.Content; .\VirtoLocal_create_local_files.ps1
```

The script downloads the helper files, pulls the required Docker images, and starts the stack. The first run takes several minutes while images download.


## Select database provider

During initial setup, you'll be prompted to choose a database provider:

| Provider | Default version | Default port |
|---|---|---|
| PostgreSQL (default ) | 18.3 | 5432 |
| MySQL  | 9.3 | 3306 |
| SQL Server  | 2022 - latest| 1433 |

You can also pass the provider via the `-dbProvider` parameter:

```powershell
.\VirtoLocal_create_local_files.ps1 -dbProvider mysql
```

### Switch database provider

To switch providers after initial setup:

1. Edit **.env** and change `DB_PROVIDER` to `postgres`, `mysql`, or `sqlserver`.
1. Run `stop-VC-solution.ps1` (if currently running).
1. Run `start-VC-solution.ps1`.

The solution now runs with the selected database provider.

Each provider stores its data in a separate Docker volume. Switching providers does not remove the previous provider's data. When you switch back, your data is still there. Only `remove-VC-solution.ps1` removes all volumes.

## Install sample data

After the build completes and the solution starts, you'll be prompted to install sample data (catalogs, products, etc.). Installation is enabled by default. Press **Enter** or **Y** to install, or **N** to skip.

You can also control sample data installation via parameter when running scripts directly:

* `.\build-VC-solution.ps1 -skipSampleData $true`: Build and start without installing sample data (default: $false, sample data is installed)
* `.\start-VC-solution.ps1 -skipSampleData $false`: Rerun the start step and install sample data. Direct start-VC-solution.ps1 invocations default to skipping sample data, since start is most commonly used to restart an existing install that already has data.


## Created files and folders

The following files and folders will be created:

* **docker-compose.yml**: Docker Compose configuration for Virto Commerce solution.
* **backend** folder: Dockerfile and script(s) for the backend.
* **frontend** folder: Dockerfile and config file(s) for the frontend.
* **scripts** folder: Scripts in the build solution process.
* **build-VC-solution.ps1**: Script to build docker images for backend and frontend.
* **start-VC-solution.ps1**: Script to start a solution using built by build-VC-solution.ps1 script.
* **stop-VC-solution.ps1**: Script stops VC solution but does NOT remove the volumes associated with the docker containers.
* **remove-VC-solution.ps1**: Script removes docker volumes associated with the containers, removes backend and frontend docker images from local docker storage.

By default **build-VC-solution** script is executed automatically after the files are created and **start-VC-solution** script is executed automatically after the build is complete. However, the execution can be skipped.

You have two options for installing Virto Commerce: 

* Using the [latest stable release](../../Updating-Virto-Commerce-Based-Project/stable-releases.md).
* Using [edge release](../../Updating-Virto-Commerce-Based-Project/edge-releases.md). 

## Endpoints

After running the script:

* Virto Commerce Frontend will be running at http://localhost:80
* Virto Commerce Backend will be running at http://localhost:8090

## Initial configuration

For initial configuration:

1. Open the Virto Commerce Backend and sign in using the default credentials:

    Username: admin
    Password: store

1. You will be prompted to change the password upon first login.
1. Review or install the sample data set to populate the system with example products and catalogs.
1. Navigate to the Search Index section and ensure that all indexes are built successfully.
1. Open the Virto Commerce Frontend to view and explore the sample data.

The Platform is now configured and ready to use.

## Install manually

The manual installation steps are as follows:

1. Run build-VC-solution.ps1 with these parameters:

    * **vcSolutionVersion**:
        * `latest-stable`: Installs the latest stable backend bundle with compatible frontend.
        * `edge`: Installs the newest backend and frontend releases.
    * `skipSampleData` (optional, default `$false`): Pass `$true` to skip sample data installation when the start step is invoked automatically.

1. Run start-VC-solution.ps1 to launch:

    * Virto Commerce backend/frontend.
    * Database (PostgreSQL, MySQL, or SQL Server configured in .env).
    * Redis.
    * Elasticsearch.
    * Kibana.

`start-VC-solution.ps1` accepts a `skipSampleData` parameter. When invoked directly (not via `build-VC-solution.ps1`), it defaults to `$true`, sample data is not installed on a bare start run. Pass `-skipSampleData $false` if you want to install sample data on a direct start.

Use `stop-VC-solution.ps1` to pause containers while preserving your data.

The solution is now installed and running.

## Version configuration

Customize versions and ports in the **.env** file. Default settings:

``` title=".env"
DB_PROVIDER=postgres

# PostgreSQL
PGSQL_VERSION=18.3
PGSQL_PORT=5432

# MySQL
MYSQL_VERSION=9.3
MYSQL_PORT=3306

# SQL Server
MSSQL_VERSION=2022-latest
MSSQL_PORT=1433

# Shared
DB_PASSWORD=$(New-RandomPassword)   # auto-generated at setup; do not edit manually unless you also reset the DB volume
STACK_VERSION=8.18.0
PLATFORM_PORT=8090
ES_PORT=9200
KIBANA_PORT=5601
REDIS_PASSWORD=$(New-RandomPassword)
ELASTIC_PASSWORD=$(New-RandomPassword)
KIBANA_PASSWORD=$(New-RandomPassword)
REDIS_PORT=6379
FRONTEND_PORT=80
ES_CLUSTER_NAME=elasticsearch
ES_LICENSE=basic
ES_MEM_LIMIT=1g
```

!!! note
    After changing the **.env** file, restart the services using `stop-VC-solution.ps1` and start-VC-solution.ps1


## Upgrade from an earlier install

!!! warning
    The multi-database release renames all Docker volumes with a `virto_` prefix (`virto_cms-content-data`, `virto_modules-data`, `virto_postgres_data`, `virto_esdata01`, `virto_redisdata`). If you already have a working install from an earlier version, running `start-VC-solution.ps1` after upgrading will create **new, empty** volumes. The old ones remain on disk but are no longer attached.

Recommended upgrade path:

1. Start the old version and export anything you need (catalog data, modules, etc.).
1. Run `remove-VC-solution.ps1` on the old version to clean up orphan volumes.
1. Rerun the initial setup with the new version.

The solution is now running the new version.

If you prefer to keep the old data in place and start fresh, the old volumes can be identified with `docker volume ls` and removed manually when you are sure they are no longer needed.


## Troubleshooting

In some cases, a failed or interrupted build can leave stale layers in the Docker builder cache, causing subsequent `build-VC-solution.ps1` runs to fail or produce unexpected results (e.g., missing files, outdated dependencies, or errors that disappear after a fresh pull). If you suspect this, inspect and clear the cache, then rebuild.

* Check overall Docker disk usage (images, containers, volumes, build cache): `docker system df`
* For a detailed breakdown of individual build cache entries and their sizes: `docker system df -v`
* Or list builder cache records directly: `docker builder du`
* Remove all build cache: `docker builder prune -af`
* To reclaim space from unused images, containers, networks, and build cache in one go: `docker system prune -af`

!!! warning
    These commands remove cache/data on the host globally, not just for this solution. Subsequent builds of other projects will be slower until their caches are repopulated, and `docker system prune` will also delete any stopped containers and dangling images from unrelated projects.

## Uninstall

To fully uninstall and erase all data, run `/VirtoLocal/remove-VC-solution.ps1`. It stops containers, deletes persistent volumes, and removes vc-platform:local-latest and vc-frontend:local-latest images.

!!! warning
    This permanently destroys all data.

!!! warning
    Database (PostgreSQL, MySQL, or SQL Server), Redis, Elasticsearch, and Kibana base images remain installed.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../macOS">← Installation on MacOS</a>
    <a href="../../post-installation-steps/01-setting-up-self-signed-ssl-cert">Setting up self-signed SSL certificate →</a>
</div>

