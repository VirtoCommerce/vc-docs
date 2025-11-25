# Set Up New Testing Environment in Virto Cloud Portal

In this guide, we'll explore how to create new environments on the Virto Cloud Portal for different purposes — for example, QA or development. These environments are typically created to test new features in isolation, preventing any impact on other ongoing work. Once testing is complete, the environments and their corresponding branches should be deleted.

## Create new account

1. [Enter the Virto Cloud portal](https://portal.virtocommerce.cloud/#!/login) with Azure AD.
1. Click **Environments** in the main menu.
1. In the next blade, click **Add** in the toolbar. 
1. The following blade opens:

    ![Add new environment](media/qa-new-environment.png)

    Set the following parameters:

    * App project (**vcptcore** project).
    * Environment name (**testenv** in our example).
    * Service plan.
    * Database technology.

1. Click **Create**. 

The system will check for available resources and, if necessary, allocate additional virtual machines to run your application. This process may take up to 5 minutes. Once you see the **Healthy** and **Synced** statuses, you have a fully functional environment.


## Sign in to backend

Once setup is complete, your environment appears in the list. Click on it to get a link to your application:

![Link to backend](media/qa-environment-url.png)

To sign in for the first time:

1. Click on the link highlighted above. The login page opens.

1. Log in using the default credentials: **admin** as the username and **store** as the password.

    ![Default credentials](media/default-credentials.png)

You will be offered to use sample data (B2B Sample Store), or create your store from scratch (Empty). For the purpose of this guide, we are going to use sample data:

![Sample Store](media/sample-data-type.png)


## Set own credentials

Next you will be forced to set your own credentials:

![New credentials](media/change-credentials.png)

!!! warning
    Make sure to save your credentials. Without them, you won’t be able to sign in again.

!!! note
    You can configure additional authentication methods, such as signing in via [Google](/storefront/developer-guide/latest/authentication/adding-google-as-sso-provider#manage-platform-settings) or [Entra ID (formerly Azure AD)](/storefront/developer-guide/latest/authentication/adding-sso-provider).

## Copy API key

1. Login to your new environment using new credentials.
1. In the main menu, click **Security**.
1. Go to **Users** --> **admin** --> **API key**.
1. In the next blade, click **Generate** in the toolbar, then copy the generated API key to clipboard. 

You will need this API key later.


## Enable GitOps

1. Open the Virto Cloud Portal and select **Environments** in the main menu.
1. Select your environment.
1. In the next blade, switch the **GitOps** option to on.
1. Click **Save** in the toolbar.
1. Click **Download manifest** in the toolbar. 


## Connect new environment to GitHub

1. Go to [vc-deploy-dev](https://github.com/VirtoCommerce/vc-deploy-dev).
1. Use the existing **vcptcore-qa** branch as a source to create your new branch. Its name should contain the name of your new environment (**vcptcore-testenv** in our example).
1. Click **Create new branch**. Your new branch appears in the list of branches.

    ![Create new branch](media/new-qa-env.gif)

1. Open this branch, select the **Infra** folder, then open the **environments.yml** file.
1. Now, you need to replace the settings in the environments.yml file with the settings from the downloaded manifest file and the copied API key:

    ![Settings replacement](media/settings-replacememt.png)

1. Click **Commit changes**.

