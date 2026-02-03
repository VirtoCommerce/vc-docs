# General Guidelines

Although the Platform interface is user friendly and intuitive, read this article to understand general techniques of working with the Platform. 

## Home page

The Platform's home page shows:

* **Dashboard**: Provides insights into sales performance, customer behavior, and overall business health.
* **Main menu**: Lists some of the available modules. You can adjust the number of items in the menu to suit your needs. Click **More** in the main menu to view the complete list of available modules.
* **Applications menu button**: Opens a list of tools and integrations to enhance various aspects of ecommerce operations.
* **Links to documentation**.
* **Modules Settings Button**.
* [User profile link](user-profile.md). 

![Guide](media/platform-dashboard.png)

## Multilingual SEO URLs

This feature allows each localized page in the Virto Commerce Frontend to have a language-specific URL that improves both search engine optimization and user experience.

When a customer visits a multilingual Frontend, URLs automatically adapt to the selected language or region, ensuring that:

* Search engines index the correct localized version of each page.
* Customers land on the appropriate language version when browsing or sharing links.
* Switching languages in the Frontend does not disrupt navigation or cause broken links.

The feature is available only for multi-language Frontend configurations.

| Configuration type    | Example URL     | Description                                                                          |
| --------------------- | ----------------| ------------------------------------------------------------------------------------ |
| Default language  | `/about-us`         | Used for the default Frontend language when no language code is specified.           |
| Language-specific | `/{xx}/about-us`    | Includes a two-letter language code, e.g., `/en/about-us`.                           |
| Region-specific   | `/{xx-XX}/about-us` | Includes both language and region codes, e.g., `/en-US/about-us`, `/en-GB/about-us`. |


When a customer changes the language in the Frontend, the permalink is updated in the browser to include the selected culture code (for example, **/en/about-us** --> **/de/über-uns**). The selected language is saved in local storage and automatically applied as the default language for future visits.

### Items URLs

When you open the desired order, product, or product category, you can copy its URL and paste it into a new window to open the desired item immediately:

![Copy and paste order URL](media/order-url.gif)


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

### Platform settings

The **Platform settings** section contains global configuration options that define how the Virto Commerce Platform behaves at the system level.
These settings are organized into logical categories:

* [General](#general).
* [Security](#security).
* [Setup](#setup).
* [User interface](#user-interface).
* [User profile](#user-profile).

#### General

The **General** group defines basic Platform-level parameters such as language configuration and environment identification.

| Setting              | Description                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Languages**        | Lists the available languages supported by the Platform. These can be used for the admin interface or content localization. |
| **Environment name** | Identifies the current Platform environment (for example, **Demo**, **QA**). This name will help distinguish environments.  |


#### Security

The **Security** group manages user account policies, token behavior, and access control lists.

| Setting                             | Description                                                                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Account statuses**                | Defines possible account states (e.g., **Approved**, **Deleted**, **New**, **Rejected**).                                          |
| **Account types**                   | Lists available account categories, such as **Administrator**, **Customer**, **Manager**.                                          |
| **Cron for the tokens prune job**   | Specifies the schedule (CRON expression) for automatic cleanup of expired tokens.                                                  |
| **Default account status**          | Sets the initial status assigned to newly created accounts.                                                                        |
| **Default account type**            | Defines the default type for new user accounts.                                                                                    |
| **Default external account status** | Sets the default status for accounts created via external identity providers.                                                      |
| **Prune expired tokens**            | Enables automatic deletion of expired tokens to maintain security and database hygiene.                                            |
| **Black list**                      | Lists file extensions prohibited from upload by the Platform (additionally to **FileExtensionsBlackList** in **appsettings.json**) |
| **White list**                      | Lists fle extensions permitted for upload by the Platform (additionally to **FileExtensionsWhiteList** in **appsettings.json**)    |


#### Setup

The **Setup** group controls technical parameters related to the Platform installation, module management, and telemetry.

| Setting                       | Description                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------|
| **Modules installed**         | Indicates that the modules are automatically installed .                                        |
| **Modules autoinstall state** | Indicates the current state of autoinstall modules wizard.                                      |
| **Sample data state**         | Shows the current state of sample data wizard.                                                  |
| **Send diagnostic data**      | Allows the Platform to send diagnostic information to improve system stability and performance. |
| **Current setup step**        | Displays the current step in setup wizard.                                                      |


#### User interface

The **User interface** settings store a JSON file with manager UI personalization data. The file can be automatically formatted, and detailed error messages appear if issues are detected.

![User interface JSON](media/user-interface-settings.gif){: style="display: block; margin: 0 auto;" }

#### User profile

The **User profile** group allows users to personalize their experience in the admin interface.

| Setting                               | Description                                                                                                    |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Full date threshold**               | Defines how long ago a date can be shown in the **time ago** format before switching to the full date display. |
| **Full date threshold unit**          | Defines the unit for the date threshold (**days**, **hours**).                                                 |
| **Language**                          | Specifies the default language for the user interface.                                                         |
| **Persisted state of the main menu**  | Determines whether the left navigation menu is collapsed or expanded.                                          |
| **Regional format**                   | Determines date, time, and number formatting according to locale conventions.                                  |
| **Show time meridian**                | Enables display of AM/PM time format.                                                                          |
| **Time zone**                         | Sets the user’s preferred time zone for displaying time-sensitive data.                                        |
| **Use time ago format when possible** | Enables relative time formatting (“5 minutes ago”) for improved readability.                                   |


### Frontend settings

The Frontend settings define how the storefront behaves and how customer-facing elements such as navigation, page titles, and display options are configured:

![Frontend settings](media/frontend-settings.png){: style="display: block; margin: 0 auto;" }

## Developer tools

This section gives developers access to useful diagnostics and integration tools:

* **Health**: Shows the health status of the Virto Commerce Platform and its dependencies (e.g., database, search engine, blob storage).
* **Hangfire**: Provides a dashboard for managing and monitoring background jobs.
* **Swagger**: Interactive API documentation for the Virto Commerce Platform.
* **GraphQL**: An IDE for exploring and executing GraphQL queries against the platform.

![Developer tools](media/developer-tools.gif)


The **Developer tools** blade is available to users with the **platform:developer-tools:access** permission. Access to **Hangfire** also requires the same permission.

## Glossary

All terms used throughout the Platform user documentation are listed in the [Glossary](glossary.md), where you can find clear definitions and explanations for each concept.
Some key terms also include tooltips that appear the first time they are mentioned in the documentation, helping you quickly understand their meaning without leaving the page.


<br>
<br>
********

<div style="display: flex; justify-content: flex-end;">
    <a href="../virto-oz">Virto OZ AI assistant →</a>
</div>

