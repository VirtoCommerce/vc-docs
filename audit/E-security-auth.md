# Group E — Security, Auth, Compliance

## Claim 1: OAuth2 / OIDC provider configuration is thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure OAuth2 / OIDC provider for authentication in VirtoCommerce?"):
Rich results. Dedicated OIDC module docs: `Fundamentals/Security/authentication/oidc.md` plus per-provider extensions (`adding-google-as-sso-provider.md`, `adding-azure-as-sso-provider.md`). `Configuration-Reference/appsettingsjson.md` documents single and multiple-provider configurations, callback paths, authority URLs, client id/secret, claim mapping. Platform uses OpenIddict as OIDC server.

**Grep** (scope: DOCS):
- `grep -rli "OAuth"`: 14 files
- `grep -rli "OpenID"`: 10 files
- Top hits: `PlatformDeveloperGuide/.../Fundamentals/Security/authentication/oidc.md`, `.../Security/extensions/adding-google-as-sso-provider.md`, `.../Security/extensions/adding-azure-as-sso-provider.md`, `.../Configuration-Reference/appsettingsjson.md`, `.../Fundamentals/Security/security-in-depth.md:11` — "Issue JWT tokens with OpenIddict".

**Verdict**: ✅ Well documented
**Note**: Claim rejected. VC has a dedicated OIDC module with per-provider setup guides and full appsettings reference.

---

## Claim 2: SAML / enterprise SSO is thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support SAML SSO / enterprise single sign-on for Azure AD / Okta?"):
Returns Azure AD (Entra ID) SSO via OIDC and Google SSO. No SAML results. `storefront/.../authentication-types.md` lists SSO via Entra ID and Google only.

**WebSearch**: Competitors (SFCC, commercetools, BigCommerce) commonly list SAML as an enterprise checkbox; VC competes on composable B2B but has no SAML story.

**Grep** (scope: DOCS):
- `grep -rli "SAML"`: **0 files**
- `grep -rli "SAML"` across CODE: **3 files** (source code mentions — minimal).
- `grep -rli "single sign-on"`: 7 files; `grep -rli "SSO"`: 406 files (mostly false positives for "sessions", unrelated acronyms — only a few are real SSO docs).

**Verdict**: 🟠 Implemented but undocumented / partly absent
**Note**: SSO is documented **only via OIDC** (Azure AD, Google). SAML is zero in DOCS. Enterprise buyers who assume SAML=SSO will not find it.

---

## Claim 3: JWT claim structure / validation is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "What is the JWT token claim structure and how do I validate JWT in VirtoCommerce?"):
Covers JWT bearer auth thoroughly: `authorization-using-jwt.md`, `sharing-bearer-tokens.md` (Authority, Audience, cert/key paths, signing algorithms). Sample decoded token shown in `graphiql.md`. Flows: Password, RefreshToken, ClientCredentials.

**Grep** (scope: DOCS):
- `grep -rli "JWT"`: 6 files
- Top hits: `.../Fundamentals/Security/security-in-depth.md:11-26`, `.../How-tos/authorization-using-jwt.md`, `.../How-tos/sharing-bearer-tokens.md`, `.../GraphQL-Storefront-API-Reference-xAPI/graphiql.md`, `.../authentication/access-token-and-cookie-mixed-auth.md`.

**Verdict**: 🟡 Mentioned but thin
**Note**: Validation config (Authority/Audience/cert paths) is documented. **Actual claim structure** (which claims VC issues: `sub`, `role`, `memberId`, `oi_tkn_id`, etc.) is shown only in a sample token snippet without a claim-by-claim reference table.

---

## Claim 4: WebAuthn / passkeys / MFA / TOTP is absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support WebAuthn / passkeys / MFA / TOTP?"):
Returns only a TypeScript `SignInResult` interface with a `requiresTwoFactor?: boolean` flag (vc-shell custom auth scaffolding). No TOTP/WebAuthn/passkey configuration docs.

**WebSearch**: Passkeys/WebAuthn are the 2026 default across enterprise IAM. Competitors (Okta, LoginRadius, Auth0) list them as core MFA.

**Grep** (scope: DOCS):
- `grep -rli "WebAuthn\|passkey"`: **0 files**
- `grep -rli "\<MFA\>"`: 0 files (word-boundary; earlier 19 was all "facet" matches)
- `grep -rli "two-factor\|2FA\|TOTP\|multi-factor"`: 12 files — real hits limited to 3 GraphQL object pages exposing a `twoFactorEnabled` boolean attribute on `ApplicationUser`. No configuration or setup guide.

**Verdict**: 🔴 Absent
**Note**: The platform exposes a `twoFactorEnabled` flag in the GraphQL schema but no user-facing MFA/TOTP/WebAuthn setup, enrollment, or recovery docs exist. Passkeys (the 2026 industry default) are entirely missing.

---

## Claim 5: RBAC vs ABAC vs policy-based authorization — naming unclear

**Context7** (`/virtocommerce/vc-docs`, query: "RBAC vs ABAC / policy-based authorization"):
`Fundamentals/Security/authorization/overview.md` and `scope-based-permissions.md` describe **Permission-based** and **Role-based** authorization, and **scope-based permissions** (per-store scopes). Notes ASP.NET Core `IAuthorizationService` + custom handlers. vc-shell has `usePermissions` composable for RBAC.

**Grep** (scope: DOCS):
- `grep -rli "RBAC\|role-based access"`: 21 files (many are vc-shell docs)
- `grep -rli "ABAC\|attribute-based"`: 1 file
- `grep -rli "policy-based\|permission-based"`: 6 files
- Key file: `.../Fundamentals/Security/authorization/overview.md` (Permission + Role strategies), `.../custom-apps-development/vc-shell/Essentials/Usage-Guides/implementing-role-based-access-control-with-usepermissions.md`.

**Verdict**: 🟡 Mentioned but thin / naming inconsistent
**Note**: RBAC and permission-based are well covered, scope-based is covered. ABAC appears only once — the term is effectively absent. A reader looking up ABAC/policy-based vs RBAC will not get a clear comparison; VC mixes "permission / role / scope / policy" without cross-referencing industry terminology.

---

## Claim 6: GDPR / CCPA / data residency statements are thin

**Context7** (`/virtocommerce/vc-docs`, query: "GDPR CCPA data residency right to be forgotten"):
Dedicated `platform/user-guide/docs/gdpr/overview.md` + `manage-personal-data.md` describe a GDPR module for anonymization/deletion. GDPR/CCPA also mentioned incidentally in vc-shell telemetry best-practices. No dedicated CCPA or data-residency page.

**Grep** (scope: DOCS):
- `grep -rli "GDPR"`: 24 files
- `grep -rli "CCPA"`: 2 files
- `grep -rli "data residency\|right to be forgotten\|right to erasure"`: **0 files**
- Top hits: `.../user-guide/docs/gdpr/overview.md`, `.../user-guide/docs/gdpr/manage-personal-data.md`, multiple `versions/v3-*.md` release notes.

**Verdict**: 🟡 Mentioned but thin
**Note**: GDPR has a real module and a user-guide page (anonymization). CCPA is only name-dropped (2 files). "Right to be forgotten", "right to erasure", and "data residency" (EU vs US storage) are **not** in the docs by name — buyer-facing compliance language is missing.

---

## Claim 7: PCI DSS scope / tokenization is thin

**Context7** (`/virtocommerce/vc-docs`, query: "PCI DSS compliance scope tokenization VirtoCommerce"):
Skyflow integration is the main PCI story: `Fundamentals/Payments/skyflow.md` + `user-guide/docs/skyflow/overview.md` + `GraphQL-Storefront-API-Reference-xAPI/Skyflow/overview.md`. CyberSource and Authorize.Net also listed with fraud-detection / PCI language. All describe "offload to provider for PCI compliance".

**WebSearch**: Shopify and BigCommerce publish an Attestation of Compliance and PCI Level 1 certification; VC sidesteps the question by delegating to Skyflow/CyberSource.

**Grep** (scope: DOCS):
- `grep -rli "PCI DSS\|PCI-DSS\|PCI compliance"`: 6 files
- `grep -rli "tokenization\|tokenized"`: 5 files
- Top hits: `.../Payments/skyflow.md`, `.../user-guide/docs/skyflow/overview.md`, `.../Payments/cybersource.md`, `.../user-guide/docs/authorize-net/overview.md`, `.../user-guide/docs/cybersource/overview.md`, `.../GraphQL-Storefront-API-Reference-xAPI/Skyflow/overview.md`.

**Verdict**: 🟡 Mentioned but thin
**Note**: "PCI compliance" is invoked as a Skyflow/CyberSource selling point. There is **no** VC-side statement of scope (SAQ-A vs SAQ-D), no tokenization architecture diagram explaining where the cardholder data boundary lies, no AOC reference for the platform itself.

---

## Claim 8: OWASP Top 10 mitigations are not called out

**Context7** (`/virtocommerce/vc-docs`, query: "OWASP Top 10 security mitigations XSS SQL injection CSRF"):
No OWASP-branded content. Security headers (X-Frame-Options, CSP frame-ancestors) covered, `AllowInsecureHttp: false` mentioned, storefront lists generic "firewall and DDoS". No Top-10 mapping.

**WebSearch**: OWASP Top 10:2025 is the industry standard reference; competitor docs cross-reference mitigations explicitly. VC does not.

**Grep** (scope: DOCS):
- `grep -rli "OWASP"`: **0 files**
- `grep -rli "XSS\|cross-site scripting\|SQL injection"`: **0 files**
- `grep -rli "injection"` hits exist but for "dependency injection" / "injection point" contexts, not attack mitigations.

**Verdict**: 🔴 Absent
**Note**: Zero OWASP references in docs. XSS, SQLi, IDOR, SSRF — none explicitly addressed. Security posture relies on framework defaults (ASP.NET Core / EF) without calling them out.

---

## Claim 9: Content Security Policy (CSP) / anti-CSRF is thin

**Context7** (`/virtocommerce/vc-docs`, query: "CSP anti-CSRF configuration headers"):
`appsettingsjson.md` documents a `SecurityHeaders` block — `FrameOptions` (default `Deny`) and `FrameAncestors` (default `None`, writing a `Content-Security-Policy` header). Page Builder setup page shows `Content-Security-Policy: frame-ancestors 'self' ...` + `Cross-Origin-Resource-Policy` / `Cross-Origin-Embedder-Policy`. CSRF mentioned only as "JWT means no CSRF".

**Grep** (scope: DOCS):
- `grep -rli "Content Security Policy\|Content-Security-Policy\|CSP"`: 8 files (the "CSP" string also matches Customer Service Platform / other acronyms — real CSP hits ~2).
- `grep -rli "CSRF\|XSRF\|cross-site request"`: 1 file — `security-in-depth.md:19` "JWT Security: No cookies means you have no need to protect against cross-site request forgery attacks (CSRF)".
- Real CSP config refs: `.../Configuration-Reference/appsettingsjson.md:2295`, `.../Extensibility/cms-integrations/PageBuilder/page-builder-setup.md:94`.

**Verdict**: 🟡 Mentioned but thin
**Note**: Only `frame-ancestors` / `X-Frame-Options` configurable. `script-src`, `default-src`, `connect-src`, `report-uri`, nonces, strict-dynamic — all absent. CSRF is dismissed (argument: "JWT in header"), but the cookie-based manager auth path (`access-token-and-cookie-mixed-auth.md`) reintroduces CSRF risk and does not discuss anti-forgery tokens.

---

## Claim 10: Secret management (Key Vault, AWS Secrets Manager, Vault) is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "Secret management Azure Key Vault AWS Secrets Manager HashiCorp Vault"):
Azure Key Vault referenced as a configuration provider detail: hierarchic key separator (`--` → `:`) in `appsettingsjson.md`. Firebase/Google SSO how-tos tell users to "place value in Key Vault" — no setup guide. Azure App Configuration has its own module page. No HashiCorp Vault, no AWS Secrets Manager.

**Grep** (scope: DOCS):
- `grep -rli "Key Vault"`: 4 files — `push-messages/firebase-cloud-messaging.md:52`, `Configuration-Reference/appsettingsjson.md:2461`, `Fundamentals/Security/extensions/adding-google-as-sso-provider.md`.
- `grep -rli "Secrets Manager\|HashiCorp\|Vault"`: 6 files (mostly Key Vault matches; HashiCorp and AWS Secrets Manager both zero).

**Verdict**: 🟠 Implemented but undocumented
**Note**: Platform supports Azure Key Vault via the ASP.NET Core config provider (implied by separator note) but there is no "how to wire VC to Key Vault" tutorial. AWS Secrets Manager and HashiCorp Vault are never mentioned. pydantic-file-secrets-style `/run/secrets` convention not discussed.
