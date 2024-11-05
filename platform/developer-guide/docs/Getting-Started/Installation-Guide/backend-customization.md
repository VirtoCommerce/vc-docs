# Backend Customization

This guides demonstrates how to build a custom module and deploy it to a Virto Cloud environment, which was previously connected using DevOps practices.

For demonstration purposes, we are going to:

1. Create a new module which will extend current **Order** module functionality.
1. Prepare the new module for deployment.
1. Deploy new module functionalities in current project. 

## Create new test module

1. Create a new repository **vc-module-order-ex** in your personal or organization account on GitHub.
1. Download [**vc-module-order.zip**](https://github.com/VirtoCommerce/vc-module-order/) to use it as a base for further extension.
1. Unpack it, go to the **sample** folder and deploy the **VirtoCommerce.OrdersModule2.Web** folder to your **vc-module-order-ex** repository. This folder contains the files needed for order module functionality extension.


## Build and compile module

Compile the module and connect it to the platform's modules folder for real-time operation. This ensures the platform can reference the necessary artifacts from the order module

## Verify module functionality

To confirm that the module is working as intended, let's check that the modifications made to the Order module have been applied. For example, a new document type can be added in the extended module:

![Extended vs. Standard](media/extended-vs-standard.png)

## Build artifact

To deploy the module on Virto Cloud, build an artifact:

![Build](media/build-module.png)

This command compiles the entire package into a single artifact, ready for installation and deployment.

!!! note
    Our client projects include out-of-the-box functionality that automatically builds and packages artifacts whenever a commit is made.

After the build is finished, the artifact appears in the artifacts folder:

![Artifacts folder](media/artifacts-folder.png)

## Publish release

Let's manually add the compiled release to GitHub:

1. Go to your account on GitHub --> Module repository (**vc-module-order-ex** in our case) --> **Releases**.
1. Click **Create a new release**.
1. Name your release, select a tag from the dropdown list, and attach your ZIP archive:

    ![Publish release](media/publish-release.png)

1. Click **Publish release**.

The release is now published.

## Generate personal access token

1. Open your profile on GitHub, go to **Settings** --> **Developer settings** --> **Personal access tokens** --> **Tokens (classic)** ---> **Generate new token** --> **Generate new token (classic)**.  
1. Enter authentication code.
1. Describe what this token is for in the **Note** field and set token expiration date if necessary. **No expiration** option is recommended. Otherwise, set a reminder to renew the token before it expires.
1. Define the access scope for your personal token. Generally, the following access scope should be sufficient:

    ![Access scope](media/access-scope.png)

1. Click **Generate token** and copy its value.
1. Go to your deployment repository (**vc-deploy-dental** in our case) --> **Settings** --> **Secrets and variables** --> **Actions**
1. Register a new secret, paste the value of the previously generated token, and give it a name (**GITHUBTOKEN** in our case).

This token will be used for downloading the repository and uploading artifacts. 

## Register release in packages.json

1. In your current project (**vc-deploy-dental** in our case), open **deploy-backend.yml**.
1. Specify an additional parameter for the **pack** step:

    ```console
    vc-build install ... - GitHubToken ${{ secrets.GITHUBTOKEN }}
    ```

    This ensures the workflow can access and deploy the module from your private repository.

1. Open **packages.json** file in the same project. 
1. Add new source to the **Sources** node for the module you are deploying:

    ```console
    "Sources": [
                {
            "Name": "GitHunPrivateRepos",
            "Owner": "OlegoO"
            "Modules": [
                {
                    "Id": "vc-module-order-ex",
                    "Version": "1.0.0"
                }
            ]
        }
    ...
    ]
    ```

1. Commit your modifications.
1. You can monitor the process:

    === "In the Portal"
        ![Portal update](media/monitor-in-portal.png)
    
    === "In Argo"
        ![Argo update](media/monitor-in-argo.png)


## Verify result

1. Open your project's backend environment (**virtostart-dentalstoredemo.govirto.com** in our case).
1. Open platform information (click Platform version in the toolbar) to verify that the module has been installed:

    ![Installed module](media/platform-information.png)

1. Click **Orders** in the main menu. Then select any order.
1. In the next blade, click **New document** in the toolbar.
1. In the next blade, you see that the new document type can be added:

    ![New document type](media/new-document-type-added.png)

The modifications have been applied.


## Remove module

To remove your module, delete it from the **Source** node in the **packages.json**.