# Getting Started

To start using VC shell:

1. Install and relocate root and packages dependencies. This will also install and configure package dependencies and git hooks
    ```bash
    yarn
    ```
1. Reinstall or refresh packages dependencies.
    ```bash
    yarn bootstrap
    ```
1. Build packages:

    <hr />
    === "All at once"
        ```bash
        yarn build
        ```

    === "One by one"
        ```bash
        yarn build-framework:ui
        yarn build-framework:core
        yarn build-framework:api-client
        yarn build-apps:vendor-portal
        ```

1. Generate api clients (require .NET Core 6 on Mac OS or Linux):

    <hr />
    === "All at once"
        ```bash
        yarn generate-api-client
        ```

    === "One by one"
        ```bash
        yarn generate-api-client:api-client
        yarn generate-api-client:vendor-portal
        ```

1. Start Vendor Portal with hot reload at localhost:8080
    ```bash
    yarn serve-apps:vendor-portal
    ```

1. Interactive documentation can be:

    <hr />
    === "Run"
        ```bash
        yarn storybook-serve
        ```
    === "Built"
        ```bash
        yarn storybook-build
        ```
