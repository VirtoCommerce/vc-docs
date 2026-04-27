# Group O — Payments

> Findings returned inline by resumed subagent (Write permission denied to the agent); persisted here by the parent session. Raw Context7/WebSearch/grep trails live in the prior-work digest at `_resume/O-prior-work.txt`.

## Verdicts

### Claim 1 — Stripe integration thin
- **grep** (DOCS): `stripe` → 6 files, all incidental (CSS class name, demo CSV, blog posts). No first-party Stripe module or how-to.
- **Context7** returned only Skyflow / CyberSource / DataTrans / Authorize.Net when asked about payment gateways.
- **Verdict**: 🔴 Absent. Zero first-party Stripe integration docs.

### Claim 2 — Adyen integration thin
- **grep** (DOCS): `adyen` → 5 hits, **all "McFadyen" false positives**. Word-boundary grep = 0 files.
- **Verdict**: 🔴 Absent.

### Claim 3 — PayPal / Braintree thin
- **grep** (DOCS): PayPal appears only as an illustrative example in `new-payment-method-registration.md` + a UI demo; Braintree = 0 files.
- **Verdict**: 🔴 Absent.

### Claim 4 — Klarna / Afterpay / BNPL absent
- **grep** (DOCS): Klarna named once as a `PreparedForm` example in `new-payment-method-registration.md:66`; "buy now pay later" only in a B2B blog post.
- **Verdict**: 🔴 Absent.

### Claim 5 — SCA / 3DS2 thin
- **grep** (DOCS): "3D Secure" appears once in `cybersource.md:13` (single bullet). `\bsca\b|strong customer authentication` = 0 hits.
- **Verdict**: 🔴 Absent.

### Claim 6 — Tokenization / vaulting thin
- **grep** (DOCS): Covered only inside `skyflow.md` + `cybersource.md` + `appsettingsjson.md` Skyflow section. No vendor-neutral tokenization / PCI-scope-reduction guidance.
- **Verdict**: 🟠 Implemented-but-undocumented-as-concept.

### Claim 7 — Saved cards / recurring billing thin
- **grep** (DOCS): `StorefrontUserGuide/.../saved-credit-cards.md` is **17 lines total** — user can view/delete cards, nothing else. No card-on-file, MIT/CIT, or recurring-charge architecture.
- **Verdict**: 🟡 Mentioned but thin.

### Claim 8 — Apple Pay / Google Pay thin
- **grep** (DOCS): One bullet in `cybersource.md:13`. Backend modules `vc-module-cyber-source` / `vc-module-payment` / `vc-module-datatrans` support wallets but docs say nothing about Express Checkout, Apple merchant ID, domain verification, or Google Pay wiring.
- **Verdict**: 🟠 Implemented but undocumented.

### Claim 9 — Payment orchestration absent
- **grep** (DOCS): 0 hits for `payment orchestration|payment router|payfac|orchestrator`.
- **WebSearch** confirms standard 2025 vocabulary at Stripe / Checkout.com / Airwallex. VC model is "one `PaymentMethod` per gateway; merchant picks one."
- **Verdict**: 🔴 Absent.

### Claim 10 — Refunds / partial refunds / void thin
- **grep** (DOCS): Refund UI (`managing-documents.md` → Create refund documents) + developer hooks (`RefundProcessPayment`, `VoidProcessPayment`) + CSV refund path documented across 12 files. Partial-refund semantics implied (enter amount) but not formalized. Chargeback / dispute handling = 0 hits.
- **Verdict**: 🟡 Mentioned but thin.

## Group shape

VC's documented payments surface is a closed set of vendor integrations — Authorize.Net, CyberSource, DataTrans, Skyflow, Native (manual) + a CSV "simplified integration" + the `PaymentMethod` abstract-class extensibility pattern. The stack's strength is **extensibility** (custom-module registration is well-described). The vocabulary is **vendor-first, not concept-first**: the biggest-name processors (Stripe, PayPal, Adyen, Braintree) have zero first-party coverage; BNPL (Klarna / Afterpay / Affirm) is missing; wallet support is locked to CyberSource; tokenization is per-vendor only; SCA / PSD2 / 3DS2, payment orchestration, chargeback / dispute handling, and card-on-file / MIT are not part of the VC vocabulary at all. A merchant manager asking "does VC do Stripe + 3DS2 + saved-card subscriptions?" finds the answer nowhere.

## Citation paths

- `documentation/PlatformDeveloperGuide/platform/developer-guide/docs/Fundamentals/Payments/{cybersource,skyflow,datatrans,authorize-net,new-payment-method-registration,simplified-integration}.md`
- `documentation/PlatformUserGuide/platform/user-guide/docs/{authorize-net,cybersource,native-payment-methods,payment,order-management,return}/`
- `documentation/StorefrontUserGuide/storefront/user-guide/docs/account/saved-credit-cards.md` (17 lines)
- `documentation/PlatformDeveloperGuide/platform/developer-guide/docs/Configuration-Reference/appsettingsjson.md` — Skyflow config ~line 1511-1530
- Backend modules (code-side): `vc-module-payment`, `vc-module-cyber-source`, `vc-module-datatrans`, `vc-module-skyflow`, `vc-module-authorize-net`, `vc-module-NativePaymentMethods`
