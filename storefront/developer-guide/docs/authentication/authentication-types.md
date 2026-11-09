# Authentication Types

At the heart of Virto Commerce Frontend’s security is token-based authentication. This approach offers a streamlined way to verify users while maintaining a high level of security. There are two primary methods for obtaining these tokens in Virto Commerce Frontend:

* **Username and password authentication**: The most common form of authentication involves users logging in with their username and password. Upon successful authentication, a token is generated and sent to the user. This token is then used for subsequent requests, ensuring that the user remains authenticated without the need to re-enter their credentials.

    ![Login-password authentication](media/login-password-authentication.png){: style="display: block; margin: 0 auto;" }

    !!! note
        A store can require a second factor on top of the password: a one-time code emailed to the user after a correct password, from the [MFA module](/platform/user-guide/latest/mfa/overview). The password grant then answers `two_factor_required` instead of issuing tokens, until the client exchanges the code with the `mfa` grant.

* **Single Sign-On (SSO) via Providers like Entra ID (Azure AD) or Google**: For businesses that use Single Sign-On (SSO), Virto Commerce Frontend supports integration with SSO providers such as Azure Active Directory (Azure AD or Entra ID) or Google. This method allows users to authenticate using their existing credentials from another trusted provider. Once authenticated through SSO provider, the platform issues a token that the user can use to access Virto Commerce’s features without needing to log in separately.

    ![SSO](media/sso-flow-illustration.png){: style="display: block; margin: 0 auto;" }

* **Passkey authentication**: Instead of a password, the user can sign in with a passkey (a fingerprint, face, screen lock, or security key) through the browser's WebAuthn API.

    Fetch sign-in options with the `passkeyRequestOptions` query, pass the result to `navigator.credentials.get`, then exchange the assertion for a token with `grant_type=passkey` on the token endpoint. A signed-in user registers a passkey the same way, with `passkeyCreationOptions` and the `createPasskey` mutation. A passkey sign-in satisfies [MFA](/platform/user-guide/latest/mfa/overview) on its own, so no code follows it.

![Readmore](media/readmore.png){: width="25"} [Adding Entra ID [Azure AD] as SSO provider](adding-sso-provider.md)

![Readmore](media/readmore.png){: width="25"} [Adding Google as SSO provider](adding-google-as-sso-provider.md)

![Readmore](media/readmore.png){: width="25"} [Passkeys module](/platform/user-guide/latest/passkeys/overview)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../migration">← Migration to Storefrontless architecture</a>
    <a href="../anonymous-authentication">Anonymous authentication →</a>
</div>