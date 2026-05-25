# Connecting custom app to platform

This article describes how to connect your custom application to the VC Platform.

## Prerequisites

* [Create custom app](../Getting-started/creating-first-custom-app.md)

## Connect app to platform

To connect your custom app to the VC Platform, add `APP_PLATFORM_URL` environment variable to your app. This variable should contain the URL of the VC Platform.

This variable is located in the `.env` file in the root of your app. If you don't have this file, you should create it as follows:

=== "Option 1"

    ```title=".env"
    APP_PLATFORM_URL=https://your_platform_url_here
    ```

=== "Option 2"

    ```bash
    $ echo "APP_PLATFORM_URL=https://your_platform_url_here" >> .env
    ```