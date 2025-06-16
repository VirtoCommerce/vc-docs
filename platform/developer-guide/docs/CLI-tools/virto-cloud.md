# Virto Cloud

In this guide, we will explore how to interact with Virto Cloud, including logging in, initializing environments, managing environments, deploying to Virto Cloud, and additional operations, all with detailed commands and parameters.

## Log in via GitHub account  
   
This target saves a token for accessing the Virto Cloud portal, eliminating the need to use the `CloudToken` parameter with every call to targets in the Cloud group.  
   
```
vc-build CloudAuth
```

By default, authorization uses a Github account. There is an optional `-AzureAD` parameter that allows you to authorize using an Azure AD (Entra ID) account:

```
vc-build CloudAuth -AzureAD
```

You can also authenticate by directly providing a cloud token using the `-CloudToken` parameter. This eliminates the need for a Github or Azure AD account when accessing the VirtoCloud portal:

```console
vc-build CloudAuth -CloudToken <token>
```

## Initialize new environment  

This target creates a new environment. It additionally accepts the `ServicePlan` parameter to specify the service plan (the default value is **F1**).  
   
```
vc-build CloudInit -EnvironmentName <EnvName>
vc-build CloudInit -EnvironmentName <EnvName> -ServicePlan **F1**
```

## List environments with statuses  

```
vc-build CloudEnvList 
```

## Download environment manifest

```
vc-build CloudDownloadManifest -EnvironmentName <name> -Manifest <path>
```

This command downloads the manifest for the specified environment:
 
* `-EnvironmentName <name>`: Specifies the environment from which the manifest will be downloaded.
* `-Manifest <path>` (optional): Defines the path where the manifest will be saved. If not provided, the manifest will be saved in the current directory with a filename matching the environment name.


## Restart environment

```
vc-build CloudEnvRestart -EnvironmentName <EnvName>
```

## Show environment’s logs  

```
vc-build CloudEnvLogs -EnvironmentName <EnvName>
```

## Update environment

This target updates an existing environment with a new application manifest. You can update the environment configuration, application version, or other settings defined in the manifest.


```
vc-build CloudEnvUpdate -EnvironmentName <EnvName> -Manifest <path>
```

It accepts the following parameters: 

* `-EnvironmentName <EnvName>`: Specifies the name of the environment to update.
* `-CloudToken <token>`: Authentication token for the cloud environment (optional if already authenticated via `CloudAuth`).
* `-Manifest <path>`: Path to the application manifest file containing the updated configuration.
* `-RoutesFile <path>`: Path to the routes file (optional).

### Alternative syntax with CloudToken

If you haven't authenticated using `CloudAuth`, you can provide the cloud token directly:

```
vc-build CloudEnvUpdate -CloudToken <your token> -EnvironmentName <EnvName> -Manifest <path>
```


### Usage with routes file

This optional configuration allows you to include a routes file by specifying the `-RoutesFile` parameter:

```
vc-build CloudEnvUpdate -EnvironmentName <EnvName> -Manifest <path> -RoutesFile <routes-path>
```

**Example**:

```
vc-build CloudEnvUpdate -EnvironmentName myapp-prod -Manifest ./manifests/production-manifest.json -RoutesFile ./config/routes.yml
```

**Routes file example (routes.yml)**:

```
- name: my-environment
  routes:
  - host: example.com
    root: main-app
    paths:
    - path: /api
      route: backend-service
    - path: /files
      route: file-service
    redirects:
    - path: /old-path
      target: main-app
      regex: false
    - path: ^/legacy/(.*)$
      target: main-app
      regex: true
```


## Set parameters for environment  

```console
vc-build CloudEnvSetParameter -CloudToken <your token> -EnvironmentName <environment name> -HelmParameters platform.config.paramname=somevalue123
```


## Delete environment
   
```console
vc-build CloudDown -EnvironmentName <EnvName>
vc-build CloudDown -Organization <OrgName> -EnvironmentName <EnvName>
```


## Wait for expected status of environment  

```console
vc-build CloudEnvStatus -CloudToken <your token> -EnvironmentName <environment name> -HealthStatus Healthy -SyncStatus Progressing
```


Additional parameter `AttemptsNumber` (default value **100**) determines the number of attempts, while `Delay` (default value **10**) specifies the delay between attempts.  

```
vc-build CloudEnvStatus -HealthStatus Healthy -SyncStatus Progressing -AttemptsNumber <number of attempts> -Delay <num of sec>
```

## Deploy custom image to cloud

You can quickly deploy a local environment and see how it performs in the cloud.

!!! note
    To run the following targets, you must have Docker installed to build the docker image. If authorization is not performed in the Docker client, the `DockerPassword` parameter must be passed in addition to the `DockerUsername` parameter.<br>
    The `DockerfileUrl` parameter can be used to pass the url of a customized docker file.


You can build and deploy docker images to:

* Existing environment: 
    
    ```
    vc-build CloudDeploy -EnvironmentName <EnvName> -DockerUsername <username of docker hub>
    ```

* New environment:
    
    ```
    vc-build CloudUp -EnvironmentName <EnvName> -DockerUsername <username of docker hub>
    ```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../more-targets">← Managing Platform and modules</a>
    <a href="../../fundamentals/caching/01-overview">Fundamentals. Caching →</a>
</div>