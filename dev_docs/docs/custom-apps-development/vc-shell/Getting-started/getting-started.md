# Start using VC shell

To start using VC shell:

1. Install and relocate root and packages dependencies. This will also install and configure package dependencies and git hooks
    ```bash
    yarn
    ```
2. Clone Vendor Portal from github
   ```bash
   yarn vendor-portal-app-init
   ```
3. Build packages:

    === "All at once"
        ```bash
        yarn build
        ```

    === "One by one"
        ```bash
        yarn build-framework
        yarn build:import-module
        yarn build-cli:config
        yarn build-cli:api-client
        yarn build-cli:create-vc-app
        ```

4. Generate api client (require .NET Core 6 on Mac OS or Linux):
    ```bash
    yarn generate-api-client:api-client
    ```

5. Start Vendor Portal with hot reload at localhost:8080
    ```bash
    cd apps/vendor-portal && yarn serve
    ```

6. Interactive documentation:

    === "Run"
        ```bash
        yarn storybook-serve
        ```
    === "Build"
        ```bash
        yarn storybook-build
        ```
