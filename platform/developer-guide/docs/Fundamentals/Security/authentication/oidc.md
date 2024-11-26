# OpenID Connect 

OpenID Connect (OIDC) is an identity module on top of the OAuth 2.0 protocol, allowing clients to verify the identity of end-users based on the authentication performed by an authorization server. It also provides basic user profile information.

OIDC is closely tied to identity providers, as it acts as a standardized framework for connecting applications to identity providers like Virto Commerce, Google, or Microsoft. These identity providers authenticate users and share identity details securely using OIDC protocols.

## Key features

* **Authentication**: Ensures secure user authentication and authorization.
* **Single Sign-On (SSO)**: Allows users to log in once and gain access to multiple applications.
* **User information**: Provides access to user profile information.
* **Interoperability**: Works with various identity providers like Google, Microsoft, and others.
* **Security**: Implements robust security measures to protect user data.

<br>
To start using an identity provider via the OpenID module:

1. [Register your identity provider in the Platform.](#register-your-identity-provider-in-the-platform)
1. [Configure the appsettings.json file.](#configuration-appsettingsjson)

## Register your identity provider in the Platform

To register new identity provider in the Platform:

1. In the main menu, click **Security**.
1. In the next blade, click **OAuth applications**. 
1. In the next blade, click **Add** in the toolbar.
1. Configure the following fields:

    ![Adding OAuth application](media/OAuth-settings.png)

1. Click **OK** to save the changes.

Your new app appears in the OAuth applications list.

## Configuration appsettings.json  

The `oidc` node in the **appsettings.json** file defines the settings for OpenID Connect authentication in Virto Commerce. This configuration enables integration with OIDC providers, allowing users to authenticate via external identity systems:  

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--OIDC-start-->"
   end="<!--OIDC-end-->"
%}

You can now use the registered identity provider.

## First-time login with Virto

To log in using the Virto authentication provider for the first time:

1. Click **Virto** on the login page.

    ![Virto login](media/click-virto.png)

1. Consent to providing access to the following information:

    * **OpenID**: A unique identifier associated with your identity, used to confirm who you are.
    * **Profile**: Basic personal information such as your name and username, used to personalize your experience.
    * **Email**: Your email address, often used for communication and account recovery.

1. You will see an **Access denied** notification:

    ![Access denied](media/access-denied.png){: width="600"}

This message means that you will not be able to log in until an administrator assigns you the required roles. Once the required roles are assigned, you will be able to successfully log in to the Platform.