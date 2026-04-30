# How to Register New App 

Using the Reports application as an example, let's look at the application installation process.

## Prerequisites

Before adding a new web app, make sure the following prerequisites have been installed:

* [Virto Commerce Platform 3.264+](https://github.com/VirtoCommerce/vc-platform)
* [Virto Commerce CLI (VC-BUILD) 3.12+](https://github.com/VirtoCommerce/vc-build)
* [VC-Shell framework](https://github.com/VirtoCommerce/vc-shell)

## Registration process

To register a new app:

1. Add a web app in the [module.manifest](../Fundamentals/Modularity/06-module-manifest-file.md):

    1. Add the app section in the **module.manifest**.

        ```xml
        ...
        <apps>
            <app id="reports">
                <title>Reports</title>
                <description>Power BI Commerce Reports</description>
                <iconUrl>/apps/reports/power_bi_logo.svg</iconUrl>
                <permission>PowerBiReports:access</permission>
            </app>
        </apps>
        ...
        ```

        <details><summary>Attributes description</summary>

        | `id`           	| A unique identifier for the app, which distinguishes it from other apps in the system.       	|
        |----------------	|----------------------------------------------------------------------------------------------	|
        | `title`        	| The name or title of the app that is displayed to the users.                                	|
        | `description`  	| A short description of the app that gives users an overview of what the app does and its purpose.|
        | `iconUrl`      	| The URL or path to the app's icon or logo used to identify the app in the system.          	|
        | `permission`   	| The permissions or access rights required to use the app, which are used to control<br>who can access the app and its features.     	|
        | `contentPath`  	| Optional override for the path to the built app, relative to the module's install directory. When omitted, the Platform serves the app from **Content/[Id]**. 	|

        </details>
        
    1. Open Platform.
    1. Click ![Dots](media/nine-dots-icon1.png){: width="25"} in the top left corner.
    1. Find the added app.
    
        ![image](media/app-menu-2.png)

1. The app lives in two locations:

    - **Runtime (inside the deployed module package).** The Platform serves the app from **Content/[app_id]** under the module's install directory, or from the `contentPath` value declared in **module.manifest** when present. It binds this folder to the `/apps/[app_id]` URL and throws a module initialization error if the folder is missing.
    - **Source (inside the source repo).** The VC-Shell source code lives in the module's Web project. The Virto Commerce CLI (vc-build) `BuildCustomApp` target looks for the app's **package.json** under **Apps/[app_id]** first, and falls back to a legacy **App** folder when the module declares a single app. It then runs `yarn install` and `yarn build` in that folder (Vite emits to **dist** by default) and copies the **dist** contents into **Content/[app_id]** in the module package, satisfying the runtime requirement above.

    The content can be a VC-Shell app or any other HTML application. For example, **vc-module-news** ships a single app via the legacy layout:

    ```text title="Source repo"
    src/VirtoCommerce.News.Web/App/             # VC-Shell source (vc-build runs yarn build, emits dist)
    ```

    ```text title="Module package (.zip), produced by vc-build"
    Content/vc-news/                            # dist contents, served by the Platform at /apps/vc-news
    ```

    A multi-app module instead places sources under **Apps/[app_id]**, for example **vc-module-pagebuilder** has **Apps/page-builder-shell/** and **Apps/page-builder-designer/**.

    ![image](media/app-folder.png)

1. Build, compress, and deploy. Use the Virto Commerce CLI (vc-build) to create a module package.

    ![image](media/vc-build.png)

1. Invoke Rest API. Virto Commerce provides an API to returns list of available apps.

    ```ps
    curl -X GET "https://mycustomdomain.com/api/platform/apps" -H  "accept: text/plain"
    ```

    ![image](media/rest-api.png)

New app is ready to go.
