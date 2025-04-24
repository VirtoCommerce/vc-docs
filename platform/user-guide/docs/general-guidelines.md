# General Guidelines

Although the Platform interface is user friendly and intuitive, read this article to understand general techniques of working with the Platform. 

## Home page

The Platform's home page shows:

* **Dashboard**: Provides insights into sales performance, customer behavior, and overall business health.
* **Main menu**: Lists some of the available modules. You can adjust the number of items in the menu to suit your needs. Click **More** in the main menu to view the complete list of available modules.
* **Applications menu button**: Opens a list of tools and integrations to enhance various aspects of e-commerce operations.
* **Links to documentation**.
* **Modules Settings Button**.
* [User profile link](user-profile.md). 

![Guide](media/platform-dashboard.png)


## Blades

The Virto Commerce Platform's UI is organized and divided into multiple screens called blades. Blades are ordered left to right and share parent-child hierarchy. Any parent blade has one or more child blades, while every child has a reference to its parent. The hierarchy depth is unlimited. 

To access a module, click on it in the main menu. Its content will appear in the next blade. Manage the module's content using the buttons in the top toolbar or by clicking the three dots next to the item's name:

![Blades](media/blades.png)

## Settings

There are several options to open a module's settings in the Platform:

=== "**Settings** in the main menu"

    ![Settings in the main menu](media/settings-in-main-menu.png){: style="display: block; margin: 0 auto;" }

=== "**Settings** button in the toolbar"

    ![Settings](media/settings.png){: style="display: block; margin: 0 auto;" }

=== "**Settings** widget inside the specific module"

    ![Settings](media/settings-widget.png){: style="display: block; margin: 0 auto;" }

In the **Settings** toolbar, you can:

* Restart the application to apply new settings.
* Clear all cached data.

![Restart and reset](media/restart-reset.png){: style="display: block; margin: 0 auto;" }

## Items URLs

When you open the desired order, product, or product category, you can copy its URL and paste it into a new window to open the desired item immediately:

![Copy and paste order URL](media/order-url.gif)


## Developer tools

This section gives developers access to useful diagnostics and integration tools:

* **Health**: Shows the health status of the Virto Commerce Platform and its dependencies (e.g., database, search engine, blob storage).
* **Hangfire**: Provides a dashboard for managing and monitoring background jobs.
* **Swagger**: Interactive API documentation for the Virto Commerce Platform.
* **GraphQL**: An IDE for exploring and executing GraphQL queries against the platform.

![Developer tools](media/developer-tools.gif)


The **Developer tools** blade is available to users with the **platform:developer-tools:access** permission. Access to **Hangfire** also requires the same permission.

<br>
<br>
********

<div style="display: flex; justify-content: flex-end;">
    <a href="../user-profile">User profile →</a>
</div>

