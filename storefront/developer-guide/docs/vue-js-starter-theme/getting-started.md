# Getting Started

In this guide, we will explore the necessary steps to get started with the Virto Commerce platform.

## Prerequisites

- Install latest version of vc-platform 3.x. 
    
    - [On Windows](/platform/developer-guide/latest/Getting-Started/Installation-Guide/windows)
    - [On macOS](/platform/developer-guide/latest/Getting-Started/Installation-Guide/macOS)
    - [On Linux](/platform/developer-guide/latest/Getting-Started/Installation-Guide/linux)

- Install the [xAPI module.](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/getting-started)
- Install the [Profile xAPI module](https://github.com/VirtoCommerce/vc-module-profile-experience-api) module.
- Install [Node](https://nodejs.org/en/download/) v.16.X
- Install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable) package manager.
  
  ```
  npm install --global yarn
  ```

!!! warning
    Node.js and Yarn have been recently updated. If you wish to upgrade:

    1. Install [Node.js v20](https://nodejs.org/en/download/).
    1. Enable [corepack](https://yarnpkg.com/corepack) (run from administrator on Windows):

        ```bash
        corepack enable
        ```

    If you have installed `yarn` globally, uninstall it:

    1. Using npm:

        ```bash
        npm uninstall --global yarn
        ```

    1. Or using your native Operation System installation tools.


## Install vc-storefront

To install **vc-storefront**:

1. Clone [vc-storefront](https://github.com/VirtoCommerce/vc-storefront) to a local folder.
1. Open the **appsettings.json** file in a text editor.
1. In the **Endpoint** section, replace **Url**, **UserName**, **Password** with correct path and credentials for Virto Commerce Platform:

    ```
    ...
        "Endpoint": {
            "Url": "https://localhost:5001",
            "UserName": "admin",
            "Password": "store",
    ...
    ```

## Run vc-storefront

To run the **vc-storefront** application, execute the following commands:

```bash
# change the current directory
cd C:\vc-storefront\VirtoCommerce.Storefront
# build and run storefront application
dotnet run
# In future, if you don't need to rebuild you can use that
dotnet run --no-build
```

## Setup Сurrent Theme

To set up the current theme for your storefront, execute the following commands:

```bash
# Clone repo into the folder where storefront is installed
# `store-code` can be found in the platform running locally. More -> Shops -> Shop Name -> Code
git clone https://github.com/VirtoCommerce/vc-theme-b2b-vue.git "C:\vc-storefront\VirtoCommerce.Storefront\wwwroot\cms-content\themes\{store-code}\default"
# Change the current directory
cd C:\vc-storefront\VirtoCommerce.Storefront\VirtoCommerce.Storefront\wwwroot\cms-content\themes\{store-code}\default
# install dependencies
yarn install
```

### For Visual Studio Code Users

If you're using Visual Studio Code:

1. Setup recommended extensions.
1. Configure [Volar Takeover mode](https://vuejs.org/guide/typescript/overview#volar-takeover-mode).

### Development Workflow

Let's explore the development workflow and various commands you can use during development.

#### Compile and Hot-Reload for Development

1. Open the **.env** file in a text editor.
1. Change **APP_BACKEND_URL** to the correct endpoint to `vc-storefront`:

    ```dotenv
    # .env file
    APP_BACKEND_URL=https://localhost:2083
    ```

1. Run command: `yarn dev` or `yarn dev-expose`.
1. Follow the link in the terminal

#### Type-Check, Compile, and Minify for Production

```bash
yarn build
```

#### Compile and Minify in Development mode

```bash
yarn build:dev
```

#### Compile and Minify in Development mode with change tracking

```bash
yarn build:watch
```

#### Compile to get the artifact to install

```bash
yarn compress
```