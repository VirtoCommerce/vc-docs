# Overview

This guide provides a comprehensive overview of the process of replacing APIs in custom VC-Shell applications using TypeScript strongly typed API clients. It specifically addresses situations where you need to access new fields or functionalities when extending the Virtocommerce REST API used by another application. The primary objective is to enable the incorporation of additional features without the need to modify the source code of the external application. To demonstrate this process, we will focus on the `vc-app-extend` project, an extension of the `vc-app` project located in the `sample` folder.

[![View the source code of the sample project](../../media/source_code.png)](https://github.com/VirtoCommerce/vc-shell/tree/main/sample/vc-app-extend)

## Replacing APIs in Custom Modules of Other Applications

When developing custom applications, there may be situations where you need to use modules from other applications while ensuring compatibility with your own API. With dynamic views, you have the capability to substitute external APIs with your own without the need to modify the source code of the external application. The fundamental steps to achieve this are as follows:

1. **Generating an API**
2. **Using the Generated API**
3. **Replacing APIs Used in External Applications**

### Generating an API

The process of generating the API is explained in detail in another one of our articles. Before proceeding with this guide, it is advisable to follow the link provided to gain a comprehensive understanding of the process. [How To Generate API client](./../../How-tos/generate-api-client.md)

### Using the Generated API

After generating the API, you need to integrate it into your application. Since you will eventually need to replace these APIs with external ones, it is advisable to create an npm package from the generated API. To accomplish this, follow these steps:

1. Ensure you are in the root folder of your project and confirm the path to your generated API. By default, this path is `src/api_client`. In the command line, execute the following command:
2.
   ```bash
   cd src/api_client && yarn init
   ```

   This command will generate a `package.json` file with the following content:

   ```json title="vc-app-extend/src/api_client/package.json" linenums="1"
   {
       "name": "api_client"
   }
   ```

3. In the generated file, lets change package name to `@vc-app-extend/api`, and include the `version`, `type`, and `exports` keys as illustrated below:

   ```json title="vc-app-extend/src/api_client/package.json" linenums="1"
   {
       "name": "@vc-app-extend/api",
       "version": "1.0.113",
       "type": "module",
       "exports": {
           ".": "./marketplacevendor.ts"
       }
   }
   ```

   Please note that `marketplacevendor.ts` serves as an example of a generated API; in your project, the file name may differ.

4. Also you need to add `types` key and script to generate API client declaration files:

    ```json title="vc-app-extend/src/api_client/package.json" linenums="1"
    {
       "name": "@vc-app-extend/api",
       "version": "1.0.113",
       "type": "module",
       "types": "./marketplacevendor.d.ts",
       "exports": {
           ".": "./marketplacevendor.ts"
       },
       "scripts": {
            "generate-types": "tsc --emitDeclarationOnly --declaration"
       },
       "devDependencies": {
            "typescript": "^5.3.2"
       },
    }
   ```

5. Also you need to create `tsconfig.json` file for your API client, that is extended from `@vc-shell/ts-config` package with following content:

    ```json title="vc-app-extend/src/api_client/tsconfig.json" linenums="1"
    {
        "extends": "@vc-shell/ts-config/tsconfig.json",
        "compilerOptions": {
            "baseUrl": ".",
            "declarationDir": ".",
            "rootDir": "."
        },
        "files": [
            "package.json",
        ],
        "include": [
            "*.ts",
        ]
    }
   ```

   This `tsconfig.json` will generate declaration files for the API client in its folder, the path to which we specified in the `types` field of the `package.json` file.

6. Run the `generate-types` script from `package.json` to generate API client declaration files.

7. Locate the primary `package.json` file of your project and append the path to your API within the `workspaces` section:

   ```json title="vc-app-extend/package.json" linenums="1"
   {
      ...
      "workspaces": [
          "./src/api_client"
      ],
      ...
   }
   ```

   Subsequently, include the newly added dependency from the previous step into your project using the following command:
   ```bash
   yarn add @vc-app-extend/api
   ```

8. Finally, install the dependencies by executing the following command:
   ```bash
   yarn install
   ```

With these steps completed, your generated API is now ready for use within your project.

### Replacing APIs Used in External Applications

This step guides you on how to replace the API utilized by external applications with the generated API named `@vc-app-extend/api`.

!!! note
    Before replacing the original API types used by `@vc-app` with the updated ones, it is recommended to gain an understanding of how Vite aliases function. Vite aliases provide a mechanism to substitute the original API types used by `@vc-app` with updated versions. For further information about aliases in Vite, refer to the [Vite documentation](https://vitejs.dev/config/shared-options.html#resolve-alias).

To customize your applications to specific requirements, you can customize the command processing logic. This involves overriding default behaviors. The modules underlying your application rely on API client packages as peerDependencies. To replace the API they use, add an alias to your main application's Vite configuration file, `vite.config.ts`:

```json title="vc-app-extend/vite.config.ts" linenums="1"
export default getApplicationConfiguration({
  resolve: {
    alias: {
      "@vc-app/api": "@vc-app-extend/api"
    },
  },
  ...
});
```
