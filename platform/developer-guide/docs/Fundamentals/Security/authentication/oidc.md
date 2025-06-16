# OpenID Connect  

[OpenID Connect](https://openid.net/developers/how-connect-works/) (OIDC) is a standardized authentication protocol built on the OAuth 2.0 framework. It enables clients to verify end-user identities through an authorization server and provides access to basic user profile information.  

OIDC serves as a bridge to identity providers, offering a unified framework to connect applications with providers like Virto Commerce, Google, or Microsoft. These providers securely authenticate users and share identity details using OIDC protocols.  

In the Virto Commerce Platform, you can:  

* Use our individual identity modules for specific providers.  
    
    ![Readmore](media/readmore.png){: width="25"} [Using Azure AD (MS Entra) as identity provider](../extensions/adding-azure-as-sso-provider.md)
    
    ![Readmore](media/readmore.png){: width="25"} [Using Google as identity provider](../extensions/adding-google-as-sso-provider.md)
    

* [Use our OIDC module](#use-oidc-module-for-identity-providers-setup) to support any or multiple providers simultaneously.

## Key features

* **Authentication**: Ensures secure user authentication and authorization.
* **Single Sign-On (SSO)**: Allows users to log in once and gain access to multiple applications.
* **User information**: Provides access to user profile information.
* **Interoperability**: Works with various identity providers like Google, Microsoft, and others.
* **Security**: Implements robust security measures to protect user data.

<br>

## Use OIDC module for identity providers setup

Our OpenID module allows using any, all, or a combination of the existing providers. To start using our OpenID module:

1. [Download](https://github.com/VirtoCommerce/vc-module-openid-connect/releases) and install it.
1. Configure the **appsettings.json** file.

The `oidc` node in the **appsettings.json** file defines the settings for OpenID Connect authentication in Virto Commerce. This configuration enables integration with OIDC providers, allowing users to authenticate via external identity systems:  

{%
   include-markdown "../../../Configuration-Reference/appsettingsjson.md"
   start="<!--OIDC-start-->"
   end="<!--OIDC-end-->"
%}

You can now use the registered identity provider.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../api-key-authentication">← API key authentication </a>
    <a href="../virto-as-identity-provider">Virto as identity provider →</a>
</div>
