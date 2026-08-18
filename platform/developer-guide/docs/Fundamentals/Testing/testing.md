# Tests

For testing purposes, use the [Virto Commerce Testing module](https://github.com/VirtoCommerce/vc-testing-module). It is a comprehensive, enterprise-grade test automation framework designed to ensure the quality, reliability, and performance of Virto Commerce components. Built on Playwright and Python, this framework provides robust end-to-end testing capabilities for both API and UI layers of the Virto Commerce ecosystem.

This testing module serves as the quality assurance backbone for Virto Commerce, enabling continuous validation of critical business workflows, API functionality, and user experiences across the platform. It supports both pre-deployment verification and continuous monitoring of production-like environments.

This repository contains 80 automated tests covering GraphQL APIs, end-to-end user workflows, and platform integration scenarios. The framework is production-ready and actively maintained, with CI/CD integration for continuous quality assurance:

* 54 GraphQL functional tests.
* 25 E2E UI tests.
* 1 Web API test.
* Configurable test scenarios for different Platform configurations.

## Key features

| Feature | Description |
|----------|-------------|
| Multi-layer testing strategy | <ul><li><strong>GraphQL API testing</strong>: 54 functional tests covering cart operations, catalog search, order management, organization workflows, and payment processing. </li><li><strong>End-to-End UI testing</strong>: 25 visual tests validating complete user journeys from product browsing to order completion. </li><li><strong>Web API testing</strong>: Platform-level API validation for administrative and integration scenarios. </li></ul> |
| Framework capabilities | <ul><li><strong>Flexible test configuration</strong>: Custom pytest options for different checkout flows (single-page/multi-step) and UI controls. </li><li><strong>Cross-browser support</strong>: Execution on Chromium, Firefox, and WebKit. </li><li><strong>Parallel execution</strong>: High-performance execution with built-in retry mechanisms. </li><li><strong>Visual regression testing</strong>: Automated screenshot comparison using pixelmatch. </li><li><strong>Test data management</strong>: Automated dataset seeding with configurable scenarios. </li></ul> |
| Developer experience | <ul><li><strong>Type-safe GraphQL client</strong>: Auto-generated Python types from GraphQL schema. </li><li><strong>Rich reporting</strong>: Allure integration for comprehensive reporting and analytics. </li><li><strong>Pre-commit hooks</strong>: Automated formatting (Black) and quality checks. </li><li><strong>Interactive debugging</strong>: Playwright Inspector and trace viewer. </li><li><strong>Environment flexibility</strong>: Configuration via **.env** files. </li></ul> |
| Test coverage areas | <ul><li><strong>Cart and checkout operations</strong>: Add to cart, cart merging, payment processing, shipping calculations. </li><li><strong>Catalog and search</strong>: Product discovery, filtering, SEO validation, category navigation. </li><li><strong>Order management</strong>: Order creation, tracking, history, and quote management. </li><li><strong>User management</strong>: Authentication, authorization, organization switching, contact management. </li><li><strong>Localization</strong>: Multi-language support, currency handling, regional settings. </li><li><strong>Address management</strong>: Shipping addresses, billing addresses, address favorites. </li></ul> |
| Quality assurance features | <ul><li><strong>Automated retry logic</strong>: Built-in retry mechanisms for flaky test scenarios. </li><li><strong>Request tracking</strong>: Network request monitoring and validation. </li><li><strong>Authentication management</strong>: Secure token handling and session management. </li><li><strong>CI/CD integration</strong>: GitHub Actions workflows for automated test execution. </li><li><strong>Code quality enforcement</strong>: Pre-commit hooks with Black formatter and linting. </li></ul> |


## Technology stack

| Technology stack | Description |
|------------------|-------------|
| Core framework | <ul><li><strong>Playwright</strong>: Modern browser automation with multi-browser support. </li><li><strong>Python 3.7+</strong>: Primary programming language. </li><li><strong>Pytest</strong>: Advanced testing framework with powerful fixtures and plugins. </li></ul> |
| Testing libraries | <ul><li><strong>pytest-playwright</strong>: Playwright integration for pytest. </li><li><strong>pytest-base-url</strong>: Base URL management for test environments. </li><li><strong>pytest-retry</strong>: Automatic retry logic for flaky tests. </li><li><strong>pytest-image-snapshot</strong>: Visual regression testing capabilities. </li><li><strong>Allure</strong>: Comprehensive test reporting and analytics. </li></ul> |
| API testing | <ul><li><strong>gql</strong>: GraphQL client library. </li><li><strong>graphql-core</strong>: GraphQL implementation for Python. </li><li><strong>requests</strong>: HTTP library for REST API testing. </li></ul> |
| Code quality | <ul><li><strong>Black</strong>: Opinionated code formatter. </li><li><strong>pre-commit</strong>: Git hooks for automated quality checks. </li><li><strong>isort</strong>: Import statement organization. </li></ul> |
| Utilities | <ul><li><strong>python-dotenv</strong>: Environment variable management. </li><li><strong>Faker</strong>: Test data generation. </li><li><strong>Pandas</strong>: Data manipulation and analysis. </li><li><strong>Rich</strong>: Terminal output formatting. </li></ul> |


## Prerequisites

* Recommended IDE: Cursor AI or PyCharm.
* Required software:
    * Python (version 3.7 or later).
    * pip (Python package manager).
    * Git.

## Install

To install the Testing module:

1. Clone the repository:
    ```csharp
    git clone https://github.com/VirtoCommerce/vc-testing-module
    cd vc-testing-module
    ```

1. Create and activate a virtual environment:
    ```csharp
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate     # On Windows
    ```

1. Install dependencies:
    ```csharp
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

1. Install pre-commit hooks:
    ```csharp
    pre-commit install
    ```

    !!!note
        This step needs to be done manually after installing requirements. Pre-commit hooks (including Black formatter) cannot be installed automatically through requirements.txt as this is a Git security feature.

1. Install Playwright browsers:
    ```csharp
    playwright install
    ```

1. Configure environment variables by creating an **.env** file in the project root with your environment-specific settings:

    ```ini
    FRONTEND_BASE_URL=your_frontend_url
    BACKEND_BASE_URL=your_backend_url
    STORE_ID=your_store_id
    ADMIN_USERNAME=your_admin_username
    ADMIN_PASSWORD=your_admin_password
    USERS_PASSWORD=your_users_password
    ```

1. Verify installation:
    ```csharp
    python -c "import playwright; print(playwright.__version__)"
    pytest --collect-only  # Should discover 80+ tests
    ```

## Project architecture

```
vc-testing-module/
├── tests_graphql/          # GraphQL API functional tests (54 tests)
│   ├── tests/              # Test cases for cart, catalog, orders, etc.
│   └── ...
├── tests_e2e/              # End-to-end UI tests (25 tests)
│   ├── tests/              # User journey and workflow tests
│   └── ...
├── tests_webapi/           # Web API platform tests
├── graphql_client/         # Type-safe GraphQL operations with automatic schema synchronization
│   ├── mutations/          # GraphQL mutation operations
│   ├── queries/            # GraphQL query operations
│   └── types/              # Type-safe GraphQL schema
├── dataset/                # Test data seeding and management
│   ├── dataset_seeder.py   # Automated test data generation for reproducible test environments
│   └── data/               # Test data configurations
├── fixtures/               # Reusable test components for authentication, page objects, and configuration
├── utils/                  # Helper utilities and common functions
├── conftest.py             # Flexible test configuration for different platform scenarios
├── pytest.ini              # Pytest settings and markers
└── requirements.txt        # Python dependencies
```

## Run tests

Use the following commands to execute frontend test suites locally and validate GraphQL operations, UI workflows, and cross-browser behavior.

### Quick start commands

* Run all GraphQL functional tests:
    ```sh
    pytest -v -s tests_graphql/tests/
    ```

* Run all E2E UI tests (headless):
    ```csharp
    pytest tests_e2e/tests/ -v -s
    ```

* Run E2E tests with visible browser:
    ```csharp
    pytest tests_e2e/tests/ -v -s --show-browser
    ```

* Run specific test by name:
    ```csharp
    pytest tests_graphql/tests/test_graphql_add_variation_to_cart.py -k test_add_variation_to_cart
    ```

* Run with detailed output
    ```csharp
    pytest tests_graphql/tests/test_graphql_add_variation_to_cart.py::test_add_variation_to_cart -v -s
    ```

### Select browser

Tests support multiple browsers for cross-browser validation:

```csharp
pytest --browser=chromium  # Google Chrome/Edge (default)
pytest --browser=firefox   # Mozilla Firefox
pytest --browser=webkit    # Safari
```

## Custom pytest options

This project includes custom pytest options that can be used to configure test behavior:

<table>
  <thead>
    <tr>
      <th>Pytest Option</th>
      <th>Description</th>
      <th>Values</th>
      <th>Example</th>
      <th>Example Description</th>
    </tr>
  </thead>
  <tbody>
    <!-- checkout-mode -->
    <tr>
      <td rowspan="3"><code>--checkout-mode</code></td>
      <td rowspan="3">Select checkout flow to test</td>
      <td rowspan="3"><code>single-page</code> (default)<br><br><code>multi-step</code></td>
      <td><code>pytest tests_e2e/tests/</code></td>
      <td>Runs tests with default checkout mode (<code>single-page</code>).</td>
    </tr>
    <tr>
      <td><code>pytest tests_e2e/tests/ --checkout-mode single-page</code></td>
      <td>Explicitly runs tests using single-page checkout flow.</td>
    </tr>
    <tr>
      <td><code>pytest tests_e2e/tests/ --checkout-mode multi-step</code></td>
      <td>Runs tests using multi-step checkout flow.</td>
    </tr>

    <!-- product-quantity-control -->
    <tr>
      <td rowspan="2"><code>--product-quantity-control</code></td>
      <td rowspan="2">Choose quantity selector type</td>
      <td rowspan="2"><code>stepper</code> (default)<br><code>button</code></td>
      <td><code>pytest tests_e2e/tests/ --product-quantity-control stepper</code></td>
      <td>Runs tests using stepper quantity selector.</td>
    </tr>
    <tr>
      <td><code>pytest tests_e2e/tests/ --product-quantity-control button</code></td>
      <td>Runs tests using button-based quantity selector.</td>
    </tr>

    <!-- show-browser -->
    <tr>
      <td><code>--show-browser</code></td>
      <td>Run browser in headed mode (shows browser UI)</td>
      <td>Boolean flag (no value required)</td>
      <td><code>pytest tests_e2e/tests/ --show-browser</code></td>
      <td>Runs tests with visible browser window for debugging.</td>
    </tr>
  </tbody>
</table>


!!! note
    You can combine multiple options:
    ```
    pytest tests_e2e/tests/ --checkout-mode single-page --product-quantity-control stepper --show-browser
    ```

### Access options in tests

You can access these options in your test files using the `pytestconfig` fixture:

```python
def test_example(pytestconfig):
    checkout_mode = pytestconfig.getoption("--checkout-mode")
    product_quantity_control = pytestconfig.getoption("--product-quantity-control")
    show_browser = pytestconfig.getoption("--show-browser")
    
    print(f"Checkout mode: {checkout_mode}")
    print(f"Product quantity control: {product_quantity_control}")
    print(f"Show browser: {show_browser}")
```

## Utility commands

Use the following utility commands to maintain test infrastructure, synchronize GraphQL schema types, and manage structured test datasets for Frontend testing scenarios.

### Generate GraphQL types

Generate GraphQL types as follows:

```csharp
python graphql_client/python_graphql_codegen.py -s -v
```

### Load and seed datasets

Dataset manager allows to fetch payloads from **data** directory to use them as **dataset** fixture in tests and to seed a test data to a backend endpoint.

Payload requests are located in **data** directory in JSON files. Each file should include:

| Field          | Required / <br> Optional | Description                                                       | Possible values                            |
| -------------- | ------------------- | ------------------------------------------------------------------| -------------------------------------------|
| `method`       | Required            | HTTP method used to send a request<br>to the target endpoint.        | `GET`, `POST`, `PUT`, `DELETE`, `PATCH`    |
| `endpoint`     | Required            | URL of the backend endpoint <br>where the payload will be sent.       | Any valid endpoint URL                     |
| `payload_type` | Required            | Defines how payload data is sent in requests.                     | `single` (one item per request),<br>`array` (multiple items per request) |
| `priority`     | Optional            | Determines execution order of <br>payloads to prevent dependency issues.<br>Lower values are processed first. <br>Default value is `99999`. | Any integer (default: `99999`) |
| `data`         | Required            | Array of objects representing items <br>to be seeded to the endpoint.  | JSON array of payload objects             |


To prevent security issues and simplify variables management in payload files by using placeholders:

* If a placeholder starts with **ENV** (for example, **{ENV:STORE_ID}**) it means that a value will be taken from a corresponding **.env** variable. It is a good approach to pass a sensitive values such as API keys as some of backend settings values. 
* If placeholder starts with **PAYLOAD_ITEM** (for example, **{PAYLOAD_ITEM:productId}**), it means that a value will be taken from **data** array item of a current payload file with corresponding property name. If the endpoint URL varies by some of the payload item parameters, use this approach.

After defining placeholders, use the commands below:

* Fetch payloads to a single dataset without seeding:

    ```csharp
    python -m dataset.dataset_manager
    ```

* Fetch payloads and to seed all of them to an endpoint:
    ```csharp
    python -m dataset.dataset_manager --seed
    ```

* Fetch payloads and seed only necessary entities to an endpoint (an entity name should be equal to JSON filename without extension):

    ```csharp
    python -m dataset.dataset_manager --seed currencies languages fulfillment_centers
    ```

## Advanced configuration

Advanced configuration includes:

* [Setting up environment-specific parameters](#set-up-environment-specific-parameters).
* [Integrating frontend tests into automated CI/CD workflows](#integrate-cicd-workflows).

### Set up environment-specific parameters

Environment variables are loaded automatically from the **.env** file. Access them in your tests:

```python
import os
from dotenv import load_dotenv

load_dotenv()
backend_url = os.getenv("BACKEND_BASE_URL")
frontend_url = os.getenv("FRONTEND_BASE_URL")
```

### Integrate CI/CD workflows

The project includes GitHub Actions workflows for automated testing:

- **GraphQL Tests Workflow** (`.github/workflows/graphql-tests.yml`)
- **E2E Tests Workflow** (`.github/workflows/e2e-tests.yml`)

Tests run automatically on pull requests and can be triggered manually for any branch.

## Development workflow

Below are the recommended practices for developing, debugging, and maintaining frontend automated tests to ensure consistency, reliability, and long-term maintainability.

### Apply test development best practices

* Use type-safe GraphQL operations:
    * Regenerate types after schema changes: `python graphql_client/python_graphql_codegen.py -s -v`
    * Leverage auto-completion and type checking in your IDE.

* Follow naming conventions:
    * Test files: `test_<suite>_<feature>.py`
    * Test functions: `test_<action>_<expected_outcome>`
    * Use descriptive names that explain the test purpose.

* Leverage fixtures:
    - Reuse existing fixtures from `conftest.py` and `fixtures/`
    - Create new fixtures for reusable test components.
    - Use appropriate fixture scopes (session, module, function).

* Write independent tests:
    - Tests should not depend on execution order.
    - Each test should set up its own data.
    - Use the dataset seeder for consistent test data.

* Handle flaky tests:
    - The framework includes automatic retry logic (configured in `pytest.ini`).
    - Add appropriate waits for async operations.
    - Use Playwright's auto-waiting features.

### Debug tests

| Command                        | Description                                                                                                                |
| -------------------------------| ---------------------------------------------------------------------------------------------------------------------------|
| <code>pytest tests_e2e/tests/ --headed --slowmo=500</code>  | <ul><li>Runs tests in headed mode (visible browser). </li><li>Adds slow motion (500 ms delay between actions) <br> for visual step-by-step debugging. </li></ul>|
| <code>pytest tests_e2e/tests/ --show-browser</code>         | <ul><li>Runs tests with a visible browser window. </li><li>Useful for observing UI behavior during execution. </li></ul>                           |
| <code>pytest tests_e2e/tests/ -v -s</code>                                     | <ul><li>Enables verbose output (<code>-v</code>). </li><li>Shows real-time console logs (<code>-s</code>). </li></ul>           |
| <code>pytest tests_graphql/tests/test_graphql_add_item_to_cart.py -v -s</code> | <ul><li>Runs a specific test file. </li><li>Provides detailed execution output for targeted debugging. </li></ul>               |


### Generate tests with Playwright

Generate test code by recording browser interactions:

```sh
playwright codegen https://your-frontend-url.com
```

This opens a browser and code generator that creates Playwright commands as you interact with the page.

### Enforce code quality standards

Pre-commit hooks automatically enforce code quality:

- **Black** - Code formatting (PEP 8 compliant).
- **isort** - Import statement organization.
- All checks run before each commit.

Manual code quality check:
```sh
pre-commit run --all-files
```

## Contribute

Follow the contribution guidelines below to ensure new frontend tests are consistent, maintainable, and aligned with the existing automation architecture.

### Add new tests

1. Choose the appropriate test suite:
   - `tests_graphql/` - For API functional tests.
   - `tests_e2e/` - For UI and user journey tests.
   - `tests_webapi/` - For platform API tests.

1. Create a new test file following naming conventions.

1. Use existing fixtures and patterns from similar tests.

1. Add appropriate pytest markers:
   ```python
   @pytest.mark.graphql  # For GraphQL tests
   @pytest.mark.e2e      # For E2E tests
   @pytest.mark.webapi   # For WebAPI tests
   ```

1. Ensure tests pass locally before submitting.

1. Pre-commit hooks will validate code quality.

### Test data management

Seed test data using the dataset seeder:
```sh
python -m dataset.dataset_seeder
```

Configure test data in **dataset/dataset_config.py** and **dataset/dataset.json**.

## Troubleshooting

| Issue                                    | Troubleshooting steps                                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Tests failing with authentication errors | <ul><li>Verify **.env** file contains correct credentials. </li><li>Check token expiration and refresh if needed. </li></ul>            |
| Browser not launching  | <ul><li>Reinstall browsers: <code>playwright install --force</code>. </li><li>Check system dependencies: <code>playwright install-deps</code>. </li></ul> |
| Import errors          | <ul><li>Ensure virtual environment is activated. </li><li>Reinstall dependencies: <code>pip install -r requirements.txt</code>. </li></ul>                |
| Pre-commit hooks not running             | <ul><li>Reinstall hooks: <code>pre-commit install</code>. </li><li>Check Git configuration. </li></ul>                                  |


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Event-Driven-Development/using-domain-events">← Event-driven development </a>
    <a href="../../PageBuilder/overview">Page Builder →</a>
</div>