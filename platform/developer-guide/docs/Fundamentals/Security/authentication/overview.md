# Overview

The Virto Commerce Platform supports the following authentication methods:  

* [Username and password](issuing-and-using-access-token.md): Users can authenticate using their credentials to obtain access tokens. This approach is straightforward and suitable for simple scenarios where no external identity provider is required.  

    ![Credentials](media/default-credentials.png)

* [OpenID connect](oidc.md): Clients can authenticate end-users via an authorization server. It adheres to the OpenID Connect standard, enabling integration with external identity providers like Entra ID (formerly Azure AD) for more robust identity management.  

    ![Oidc](media/oidc-based-authentication.png){: width="600"}

These options provide flexibility, catering to both standalone authentication setups and modern, federated identity solutions.



