# Builder.io Integration

The Builder.io integration allows to resolve and render published pages by slug from offline storage (index). This ensures that customers can access published content by permalink without a direct connection to Builder.io CMS.

## Configuration

To make Builder.io pages visible inside Virto Pages, you need to configure:  

1. [Webhooks.](#webhook-сonfiguration)
1. [Access and visibility.](#page-visibility-and-access-control) 

### Webhook configuration

To send requests to a specific URL (https://[URL]/api/pages/builder-io) with custom headers for authentication and localization, the webhook in Builder.io should be configured under **Settings → Integrations → Global Webhooks** as follows:

* **storeId**: Specifies the ID of the target store.
* **cultureName**: Specifies the culture (language/region) of the store, e.g., "en-US".
* **api_key**: API key for admin authentication.

![Builder.io webhooks](media/builder-io-webhooks.png){: style="display: block; margin: 0 auto;" width="500"}

These headers ensure that the necessary parameters for the store's context, language, and authentication are included in the request sent from Builder.io.

### Page visibility and access control

To test page visibility and user access, the following settings need to be configured in Builder.io:

* **Time-based visibility**: If a page has defined **start** and **end** dates, it will only be visible during that period. The page will appear in the Store blade and on the site only within this timeframe.
* **Authentication-based visibility**: If **isAuthenticated** is set to false, the page will be accessible only to registered users, for other users - 404. 
* **Group-based visibility**: If a **groupName** is set for the page, access will be restricted to users belonging to that specific group, for other users - 404. Ensure that **groupName** is correctly mapped to user groups or roles within the platform.

![Visibility and access control](media/access-visibility.png){: style="display: block; margin: 0 auto;" width="500"}

## Behavior in Platform

* Published pages appear in the **Stores** --> Your store --> **Virto Pages** widget.
* Pages with start/end dates automatically hide when out of range.
* Unpublished pages are not shown.
* Deleted pages are hidden.

![Virto Pages](media/builder-io-in-virto-pages.png){: style="display: block; margin: 0 auto;" }


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../enabling-pages">← Enabling pages</a>
    <a href="../../payment/overview">Payment module overview →</a>
</div>