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

This target creates a new environment. It additionally accepts the `ServicePlan` parameter to specify the service plan (default value is `F1`).  
   
```
vc-build CloudInit -EnvironmentName <EnvName>
vc-build CloudInit -EnvironmentName <EnvName> -ServicePlan F1
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
 
`-EnvironmentName <name>`: Specifies the environment from which the manifest will be downloaded.

`-Manifest <path>` *(optional)*: Defines the path where the manifest will be saved. If not provided, the manifest will be saved in the current directory with a filename matching the environment name.


## Restart environment

```
vc-build CloudEnvRestart -EnvironmentName <EnvName>
```

## Show environment’s logs  

```
vc-build CloudEnvLogs -EnvironmentName <EnvName>
```

## Update environment

```console
vc-build CloudEnvUpdate -CloudToken <your token> -Manifest <path to application manifest>
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


Additional parameter `AttemptsNumber` (default value 100) determines the number of attempts, while `Delay` (default value 10) specifies the delay between attempts.  

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

* New environment  
    
    ```
    vc-build CloudUp -EnvironmentName <EnvName> -DockerUsername <username of docker hub>
    ```
