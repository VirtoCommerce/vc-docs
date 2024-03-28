# VirtoCloud

In this guide, we will explore how to interact with VirtoCloud, including logging in, initializing environments, managing environments, deploying to VirtoCloud, and additional operations, all with detailed commands and parameters.

## Log in via GitHub account  
   
This target saves a token for accessing the VirtoCloud portal, eliminating the need to use the `CloudToken` parameter with every call to targets in the Cloud group.  
   
```
vc-build CloudAuth
```

## Initialize New Environment  

This target creates a new environment. It additionally accepts the `ServicePlan` parameter to specify the service plan (default value is `F1`).  
   
```
vc-build CloudInit -EnvironmentName <EnvName>
vc-build CloudInit -EnvironmentName <EnvName> -ServicePlan F1
```

## List Environments with Statuses  

```
vc-build CloudEnvList <EnvName>
```

## Restart Environment

```
vc-build CloudEnvRestart -EnvironmentName <EnvName>
```

## Show Environment’s Logs  

```
vc-build CloudEnvLogs -EnvironmentName <EnvName>
```

## Update Environment from Manifest

```
vc-build CloudEnvUpdate -ArgoConfigFile <path to the manifest>
```

## Set Parameters for Environment  

```
vc-build CloudEnvSetParameter -EnvironmentName <EnvName> -HelmParameters <PARAMETER_NAME>=<PARAMETER_VALUE> <PARAMETER_NAME2>=<PARAMETER_VALUE2>
```

## Delete Environment
   
```
vc-build CloudDown -EnvironmentName <EnvName>
```

## Wait for Expected Status of Environment  


```
vc-build CloudEnvStatus -HealthStatus Healthy -SyncStatus Progressing
```

Additional parameter `AttemptsNumber` (default value 100) determines the number of attempts, while `Delay` (default value 10) specifies the delay between attempts.  

```
vc-build CloudEnvStatus -HealthStatus Healthy -SyncStatus Progressing -AttemptsNumber <number of attempts> -Delay <num of sec>
```

## Deploy Custom Image to Cloud

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
