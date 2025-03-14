# Create Environment via CLI and VC Build

In this guide, we explore the creation of environments via the CLI. The alternative is the [creation of environments through the Cloud Portal](deploy-on-virto-cloud.md).

To create a new environment using CLI and VC Build, complete the following steps:

1. [Install or update CLI tools.](create-environment-via-cli-and-vc-build.md#install-cli-tools)
1. [Generate API key.](create-environment-via-cli-and-vc-build.md#generate-api-key)
1. [Authenticate with Virto Commerce Cloud services.](create-environment-via-cli-and-vc-build.md#authenticate-with-virto-commerce-cloud-services)
1. [List environments (optionally).](create-environment-via-cli-and-vc-build.md#list-environemnts-optional)
1. [Create new environment.](create-environment-via-cli-and-vc-build.md#create-new-environment)

## Install CLI tools

To install Virto Commerce Global Tool, run:

```
dotnet tool install VirtoCommerce.GlobalTool  -g
```

If you have Virto Commerce Global Tool installed, update it to the latest version:

```
dotnet tool update -g VirtoCommerce.GlobalTool
```

## Generate API key

To generate API key, open the Virto Cloud Portal:

1. Click **Environments** in the main menu.
1. In the next blade, click **API key** in the toolbar.
1. In the next blade, click **Generate** in the toolbar.
1. Copy the generated API key.

![Generate API key](media/generate-api-key.png)

## Authenticate with Virto Commerce Cloud services

To access to your Virto Commerce Cloud account and perform further environment management tasks, run:

```
vc-build CloudAuth -CloudToken <your api key>
```

## List environments (optional)

To view the list of all Virto Commerce environments that are currently available for the generated token, run:

```
vc-build CloudEnvList
```

This command is useful for verifying that you have access to the appropriate environments.

## Create new environment

To create new environment, run the following command, specifying your environment name, your service plan, and the organization under which the environment is being created:

```
vc-build CloudInit -EnvironmentName DentalCMD -ServicePlan B1 -Organization virtostart
```

Your environment has been created. You can see it in the Virto Cloud Portal:

![New environment](media/created-environment.png)

You can also:

* [Wait for an expected environment status.](../../../developer-guide/CLI-tools/virto-cloud#wait-for-expected-status-of-environment) 
* [Restart the environment.](../../../developer-guide/CLI-tools/virto-cloud#restart-environment)
* [Delete the environment.](../../../developer-guide/CLI-tools/virto-cloud#delete-environment)


![Readmore](media/readmore.png){: width="25"} [Other available commands](../../../developer-guide/CLI-tools/virto-cloud)

Now you can [sign in to the created environment](deploy-on-virto-cloud.md#sign-in-to-backend).


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../deploy-on-virto-cloud">← Deploy Platform and Frontend on Virto Cloud </a>
    <a href="../catalog-creation">Create catalog →</a>
</div>
