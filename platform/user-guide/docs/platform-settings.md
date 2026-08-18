# Platform Settings

The **Platform settings** section contains global configuration options that define how the Virto Commerce Platform behaves at the system level.
These settings are organized into logical categories:

* [General](#general).
* [Security](#security).
* [Setup](#setup).
* [User interface](#user-interface).
* [User profile](#user-profile).

## General

The **General** group defines basic Platform-level parameters such as language configuration and environment identification.

| Setting              | Description                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Languages**        | Lists the available languages supported by the Platform. These can be used for the admin interface or content localization. |
| **Environment name** | Identifies the current Platform environment (for example, **Demo**, **QA**). This name will help distinguish environments.  |


## Security

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


## Setup

The **Setup** group controls technical parameters related to the Platform installation, module management, and telemetry.

| Setting                       | Description                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------|
| **Modules installed**         | Indicates that the modules are automatically installed .                                        |
| **Modules autoinstall state** | Indicates the current state of autoinstall modules wizard.                                      |
| **Sample data state**         | Shows the current state of sample data wizard.                                                  |
| **Send diagnostic data**      | Allows the Platform to send diagnostic information to improve system stability and performance. |
| **Current setup step**        | Displays the current step in setup wizard.                                                      |


## User interface

The **User interface** settings store a JSON file with manager UI personalization data. The file can be automatically formatted, and detailed error messages appear if issues are detected.

![User interface JSON](media/user-interface-settings.gif){: style="display: block; margin: 0 auto;" }

## User profile

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

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../backup-and-restore">← Backup and restore </a>
    <a href="../ada-compliance">ADA compliance →</a>
</div>