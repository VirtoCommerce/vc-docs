# Group V — Testing & QA

Scope: user-facing docs corpus under `documentation/` plus cross-checks into `PlatformBackendSourceCode` for implementation evidence.

Key finding up front: VC publishes a **single, dedicated testing page** — [`PlatformDeveloperGuide/.../Fundamentals/Testing/testing.md`](../../documentation/PlatformDeveloperGuide/platform/developer-guide/docs/Fundamentals/Testing/testing.md) (435 lines) — describing the `vc-testing-module` (Playwright + Python, ~80 pytest tests). A short pointer in [`StorefrontDeveloperGuide/.../tests.md`](../../documentation/StorefrontDeveloperGuide/storefront/developer-guide/docs/tests.md) links to it. Almost every test-related claim is answered (or not) by what that one page covers. Backend `.NET` unit testing (xUnit + Moq) is heavily used in **source code** but barely mentioned in docs.

---

## Claim 1: Unit testing framework (xUnit, NUnit) in platform is thin.
**Context7** (`/virtocommerce/vc-docs`, query: "How do I write unit tests for a VirtoCommerce module? What testing framework is used (xUnit, NUnit, MSTest)?"):
Two hits. (a) `CLI-tools/build-automation.md` shows `vc-build test` with a coverage report for `VirtoCommerce.CatalogCsvImportModule.Tests.dll`. (b) `Tutorials/create-new-module-from-scratch.md` mentions generating an "xUnit Test Project (.NET Core)" subproject. No separate xUnit how-to, no conventions doc, no assertion-library guidance.

**WebSearch** (query: "e-commerce platform documentation testing guide ..."):
Competitor docs (commercetools, Shopify) publish dedicated testing guides. commercetools has explicit "Testing" section with `test-utils`. Shopify publishes an entire Ecommerce Testing Guide. VC does not match this depth for backend unit testing.

**Grep** (scope: DOCS):
- `grep -rli "xunit" DOCS`: 1 file (`create-new-module-from-scratch.md:15` — "xUnit Test Project (.NET Core)").
- `grep -rli "nunit\|mstest" DOCS`: 0 files.
- `grep -rli "unit test" DOCS`: 6 files, almost all tangential (`skills-required-for-VC-developers.md`, release-notes bullets, vc-build CLI reference).
- Cross-check CODE: `grep -rli "xunit" PlatformBackendSourceCode`: **603 files**. xUnit is pervasive in the codebase, ~1500 `*Tests.cs` files. The contrast — deep in code, near-silent in docs — is sharp.

**Verdict**: 🟠 Implemented but undocumented
**Note**: xUnit is the de-facto standard (603 code files, `vc-build test` wraps it), yet docs give no tutorial, no naming conventions, no assertion-style guidance, no link to a sample `*.Tests` csproj. Mentioned only as a VS project template in the "new module" tutorial.

---

## Claim 2: Integration testing is thin.
**Context7** (query: "How do I write integration tests against VirtoCommerce platform and modules?"):
Three hits. (a) `modules-architecture.md` says "Write unit and integration tests for all module functionalities" (one-line best-practice). (b) `Intent-Search/installation-and-configuration.md` tells the reader to run `IntegrationScenarios.Test_Complete_Scenario()` — with no explanation of how integration scenarios are authored. (c) `testing.md` describes the Playwright/pytest suite, which targets API+UI E2E rather than .NET integration tests.

**WebSearch**: commercetools has `load-testing` and separate integration test pages in their API docs. Shopify's testing blog pushes dedicated integration testing layers. VC has no integration-test-layer guide.

**Grep** (scope: DOCS):
- `grep -rli "integration test" DOCS`: 4 files — 3 exhortations ("add integration tests"), 1 specific reference to the Intent-Search scenario. No dedicated integration-testing tutorial (no `WebApplicationFactory`, no Testcontainers, no in-memory DB provider walkthrough).
- Cross-check CODE: Integration-style tests exist (`-TestsFilter "Category!=IntegrationTest"` in `build-automation.md:47` implies a category convention).

**Verdict**: 🟡 Mentioned but thin
**Note**: The term appears, but docs never explain the **how**: no `WebApplicationFactory<T>`, no database fixture strategy, no Testcontainers, no "IntegrationTest" category definition despite the vc-build filter hinting at the convention.

---

## Claim 3: E2E testing (Playwright, Cypress) is thin.
**Context7** (query: "Is there an end-to-end testing harness (Playwright, Cypress, Selenium) for the VirtoCommerce storefront?"):
Playwright is the answer. `testing.md` describes the vc-testing-module as Playwright+Python, ~80 tests (54 GraphQL + 25 E2E UI), cross-browser (Chromium/Firefox/WebKit), `playwright install`, `playwright codegen`, traces, retries, CI/CD integration.

**WebSearch**: Shopware's frontends framework documents Playwright + axe for accessibility; competitor depth roughly matches VC for E2E but not for adjacent topics.

**Grep** (scope: DOCS):
- `grep -rli "playwright" DOCS`: 1 file (`testing.md`), ~20 mentions.
- `grep -rli "cypress\|selenium" DOCS`: 0 files.
- `testing.md` wc: 435 lines.

**Verdict**: ✅ Well documented
**Note**: This is the strongest corner of Group V. Single long page, Playwright codegen, trace viewer, fixture scopes, pytest markers (`@pytest.mark.e2e`), Allure reporting, retry config. Cypress/Selenium deliberately absent — VC standardised on Playwright.

---

## Claim 4: Load / performance testing (k6, JMeter) is absent.
**Context7** (query: "How do I load test VirtoCommerce using k6, JMeter or Gatling?"):
No testing-tool hit — results were unrelated (platform run commands). `testing.md` never mentions k6, JMeter, Gatling, Locust, NBomber, or Artillery.

**WebSearch**: Industry-standard for e-commerce: k6 for API-first stacks, JMeter for traditional loads, commercetools has a dedicated `docs.commercetools.com/api/load-testing` page. k6 and JMeter are expected references in competitor docs.

**Grep** (scope: DOCS):
- `grep -rli "k6\|jmeter\|gatling\|locust\|nbomber\|artillery" DOCS`: 0 files.
- `grep -rli "load test\|load-test\|performance test\|stress test" DOCS`: 4 files — all prose assertions ("releases undergo load/performance testing before stable"), no tooling, no scripts, no results, no SLOs (`release-strategy-overview.md:24`, `upgrading-to-dot-net-10.md:14`, `upgrading-to-net8.md:5`, `elastic-app-search-overview.md:31`).
- `testing.md`'s "Load and seed datasets" section is about seeding payloads, not load testing — keyword collision only.

**Verdict**: 🔴 Absent
**Note**: VC claims "full regression, E2E and load testing" gates stable releases but provides zero public load-test tooling, harness, or reference scripts. A customer wanting to run their own load test has nothing to follow.

---

## Claim 5: Contract testing (Pact) is absent.
**Context7** (query: "Does VirtoCommerce publish a Pact contract? Is there consumer-driven contract testing?"):
No hits — results were about *user contracts* in the B2B module (Contract Name, Contract Code, Create Contract). "Contract" in VC docs means B2B legal contracts, never API contracts.

**WebSearch**: Pact is the industry standard for consumer-driven contract testing in microservice-ish commerce architectures. Headless / MACH stacks (commercetools, Saleor) are natural Pact candidates.

**Grep** (scope: DOCS):
- `grep -rli "\bpact\b\|consumer-driven\|consumer driven\|contract test" DOCS`: 0 files.
- OpenAPI/Swagger is documented (separate claim), but no contract-testing layer bridges producer↔consumer verification.

**Verdict**: 🔴 Absent
**Note**: No Pact, PactFlow, Spring Cloud Contract, or any consumer-driven contract testing mention. Given VC's xAPI / GraphQL façade pattern, this would be a natural fit — zero docs.

---

## Claim 6: Mocking / test doubles is thin.
**Context7** (query: "How do I mock dependencies and use test doubles for VirtoCommerce?"):
Only hit is a TypeScript `MockAuthProvider` example inside vc-shell (custom-apps-development). It's a mock **at the application-provider level** (for swapping out the Platform auth provider during vc-shell app dev), not a test-double / mocking library tutorial. No Moq, NSubstitute, FakeItEasy guidance.

**WebSearch**: .NET commerce platforms typically standardise on Moq or NSubstitute; Magento uses PHPUnit mocks; Shopify docs cover test mode and fake payment providers.

**Grep** (scope: DOCS):
- `grep -rli "moq\|nsubstitute\|fakeiteasy" DOCS`: 0 files (single "MOQ" hit in B2BExperts is "minimum order quantity", not the library).
- `grep -rli "\bmock\b" DOCS`: 4 files, all vc-shell auth-provider or UI-related (`vc-table.md`, `usebreadcrumbs.md`, etc.) — none about unit-test mocking.
- `grep -rli "test double" DOCS`: 0 files.
- Cross-check CODE: `grep -rli "using Moq" PlatformBackendSourceCode`: **253 files**. Moq is pervasive in the actual codebase.

**Verdict**: 🟠 Implemented but undocumented
**Note**: 253 files `using Moq` in backend source, zero docs on "how to mock an `ICatalogService`". The `MockAuthProvider` guide exists but serves a different purpose (vc-shell app-level dependency injection swap).

---

## Claim 7: Test data / fixtures is thin.
**Context7** (query: "How do I seed test data or create fixtures for a VirtoCommerce test environment?"):
Four hits, all inside `testing.md`. `dataset/dataset_seeder` script, `dataset/dataset_config.py`, `dataset/dataset.json`, selective seeding via `--seed currencies languages fulfillment_centers`. Payload JSON schema (endpoint, payload_type, priority, data) fully documented with a table.

**WebSearch**: commercetools' `test-utils` package, Shopify's test mode with sample data. VC's dataset-manager approach is competitive.

**Grep** (scope: DOCS):
- `grep -rli "fixture\|seed data\|seeder\|test data" DOCS`: 3 files (`testing.md` + 2 B2B articles unrelated).
- `testing.md` has a full "Load and seed datasets" section with payload placeholders (`{PAYLOAD_ITEM:productId}`).
- Backend unit-test fixtures (`*.Tests` bootstrap, `DbContextFactory`, `AutoFixture`, `Bogus`) are not documented.

**Verdict**: 🟡 Mentioned but thin
**Note**: Well documented **for the Playwright/pytest vc-testing-module dataset seeder**. Zero docs on .NET test fixtures, `IClassFixture<>`, `AutoFixture`, `Bogus` / `Faker`, or database fixture patterns for backend unit/integration tests.

---

## Claim 8: Visual regression testing is absent.
**Context7** (query: "Does VirtoCommerce support visual regression testing (Percy, Chromatic, Playwright screenshots)?"):
Yes — `testing.md` key-features row explicitly lists "Visual regression testing using pixelmatch" via the `pytest-image-snapshot` plugin. Built-in to the vc-testing-module.

**WebSearch**: Industry options are pixelmatch (what VC uses), Percy, Chromatic, Applitools. VC's choice is legitimate and open-source-friendly.

**Grep** (scope: DOCS):
- `grep -rli "visual regression\|pixelmatch\|image snapshot\|chromatic\|\bpercy\b" DOCS`: 1 file (`testing.md`).
- No worked example, no baseline-management workflow, no "how to update a golden snapshot" guide — just the capability declaration and a `pytest-image-snapshot` dependency row.

**Verdict**: 🟡 Mentioned but thin
**Note**: Capability exists and is declared, but docs don't walk through authoring a visual-regression test, storing baselines, or handling drift across browsers. Competitors (Shopware, Chromatic-using shops) go deeper.

---

## Claim 9: Accessibility testing is absent.
**Context7** (query: "Does VirtoCommerce include accessibility testing (axe-core, pa11y, WCAG validation) in its test framework?"):
No tooling hit. Closest match is `platform/user-guide/docs/ada-compliance.md` — a short page saying the platform doesn't disable zoom/scale on login, cart, and catalog. That's a compliance *claim*, not an automated accessibility *test*.

**WebSearch**: The industry baseline is **axe-core + Playwright** — Shopware Frontends documents it explicitly, Magento/Salesforce shops use it, the NPM `@axe-core/playwright` package is pervasive.

**Grep** (scope: DOCS):
- `grep -rli "axe-core\|axe core\|pa11y\|accessibility test\|wcag test\|ada test" DOCS`: 0 files.
- `testing.md` never mentions `@axe-core/playwright` or `axe-playwright-python` despite being Playwright-based (trivial to add).

**Verdict**: 🔴 Absent
**Note**: VC uses Playwright — adding `axe-playwright-python` or `@axe-core/playwright` would be a one-line dependency. No mention, no guidance, no baseline ruleset, no WCAG assertion pattern. Given the ADA-compliance page already exists, the gap between claim and verification is striking.

---

## Claim 10: Security testing (OWASP ZAP, Burp) is absent.
**Context7** (query: "Does VirtoCommerce document security testing, penetration testing, OWASP ZAP, Burp Suite or SAST/DAST?"):
No hits. Results were unit-test CLI references and `IAuthorizationService` scope-based permissions — unrelated.

**WebSearch**: Enterprise commerce platforms typically document SAST (SonarQube, CodeQL, Snyk), DAST (OWASP ZAP, Burp), and dependency scanning. Even Shopify mentions third-party DAST partners.

**Grep** (scope: DOCS):
- `grep -rli "owasp zap\|burp\|\bsast\b\|\bdast\b\|pentest\|penetration test" DOCS`: 1 file (`B2BExperts/Six-cybersecurity...md:86`) — generic McKinsey DevSecOps prose ("integrate security testing at every stage"), not VC-specific tooling or guidance.
- No dependency-scan guide (Dependabot, Snyk, Trivy), no CI security-gate template, no SBOM docs, no threat-model walkthrough.

**Verdict**: 🔴 Absent
**Note**: Zero VC-specific security-testing tooling or workflow. One generic third-party article mentions DevSecOps in passing. For an enterprise platform handling payments and customer data, the absence is notable.

---

## Overall shape of Group V

- **One strong page, one pointer.** `Fundamentals/Testing/testing.md` (435 lines) + `storefront/.../tests.md` (24 lines pointing at the first). That is effectively *all* of VC's test documentation. It's focused on one asset — the Playwright+Python `vc-testing-module` with ~80 tests (54 GraphQL + 25 E2E UI + WebAPI coverage).
- **The .NET backend testing story is invisible in docs.** 603 xUnit files and 253 Moq-using files in source, but docs only mention xUnit once (as a VS project template in the "new module" tutorial) and Moq/NSubstitute zero times. No `*.Tests` conventions, no `WebApplicationFactory` integration-test walkthrough, no unit-test coverage target, no "how to test a custom module" guide. Classic implemented-but-undocumented pattern.
- **Entire layers are missing:** load testing, contract testing, accessibility testing, security testing — all zero. "Load testing" is claimed as a stable-release gate but no artifacts or harness are published. Given VC runs on Playwright already, `axe-core` accessibility testing is a one-line dependency away and still absent.
