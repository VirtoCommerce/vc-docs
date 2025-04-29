# Getting Started

This guide helps you set up the Page Builder for Virto Commerce Platform and Frontend, ensuring content creation works smoothly.

## Prerequisites

Before you begin, ensure that the following components are installed:

* [Virto Commerce 3.253.0+](https://github.com/VirtoCommerce/vc-platform/releases/)  
    ![Readmore](media/readmore.png){: width="25"} [Platform deployment guide](../../Getting-Started/Installation-Guide/windows.md)

* [Virto Frontend 2.2.0+](https://github.com/VirtoCommerce/vc-frontend/releases/)  
    ![Readmore](media/readmore.png){: width="25"} [Frontend deployment guide](../../../../../storefront/developer-guide/deployment)

* [Page Builder module 3.201+](https://github.com/VirtoCommerce/vc-module-pagebuilder/releases)

## Setup content

Verify that the Virto Commerce Platform and Frontend are using the same **Shared content** folder for proper page synchronization.

## Setup Content module

Extend your content configuration by adding a `PathMappings` section to your **appsettings.json** file.

```json title="appsettings.json"
"Content": {
  "PathMappings": {
    "pages": [
      "Themes",
      "_storeId",
      "_theme",
      "content/pages"
    ],
    "themes": [
      "Themes",
      "_storeId"
    ]
  }
}
```

If you manage settings via environment variables, use the following:

```yaml title="environments.yml"
Content__PathMappings__pages__0: "Themes"
Content__PathMappings__pages__1: "_storeId"
Content__PathMappings__pages__2: "_theme"
Content__PathMappings__pages__3: "content/pages"
Content__PathMappings__themes__0: "Themes"
Content__PathMappings__themes__1: "_storeId"
```

## Setup store

Configure the public store URL to ensure pages are accessible correctly.

1. Open Platform.
1. In the main menu, select **Stores**.
1. In the next blade, select your store.
1. In the next blade, set up the public store URL, if it is empty.
1. Click **Save** in the toolbar to save the changes.

You store URL has been set.

## Purge cache

To see updates immediately, configure automatic cache clearing after content changes. We recommend setting up the Webhooks module to trigger cache reset automatically.

1. [Install](../../../../user-guide/modules-installation) the [Webhooks module](https://github.com/VirtoCommerce/vc-module-webhooks/).
1. Open Platform.
1. In the main menu, select **Webhooks**.
1. In the next blade, click **Add** in the toolbar to create a new subscription.
1. Fill in the following fields:

    1. Enter a subscription name.
    1. In the **Events** dropdown list, select **Page Builder Content Changed Event**.
    1. Add **Path** and **Type** fields.
    1. Switch the webhook toggle to on.
    1. Set the URL to your frontend endpoint.
    1. Click **Save** in the toolbar to save the changes.

![Webhook settings](media/webhook-settings.png){: style="display: block; margin: 0 auto;" }

New webhook has been added.

## Run

Now you are ready to create and manage content pages:

=== "via the Content module"

    1. Click **Content** in the main menu.
    1. In the next blade, find the required store and click on the **Pages** widget.
    1. In the next blade, click **Add** in the toolbar. 
    1. In the next blade, select **Design page**.

        ![New page](media/new-page.png){: style="display: block; margin: 0 auto;" }

    1. In the next blade, fill in the following fields:

        ![Fill in the fields](media/create-page-fields.png){: style="display: block; margin: 0 auto;" width="600"}

    1. Click **Create**. The Page Builder opens the newly created page in a new window. It contains uneditable header and footer by default.  

        ![New page in Page Builder](media/new-page-opens.png){: style="display: block; margin: 0 auto;" }

    1. Click **Save** in the top right corner. 

    The page appears in the list of pages with the **.page-draft** extension. After you [publish](#publish-or-unpublish-pages) your page, it will receive the **.page** extension. 

    You can open it in the browser using the specified permalink.


=== "via the Page Builder Office"

    1. Click **Stores** in the main menu.
    1. In the next blade, select the required store.
    1. In the next blade, click on the **Page Builder** widget to open the Page Builder Office:

        ![Office](media/page-builder-office.png){: style="display: block; margin: 0 auto;" }

    1. Click **Add** in the toolbar.
    1. In the next blade, fill in the following fields:

        ![Fill in the fields](media/new-page-office.png){: style="display: block; margin: 0 auto;" }

    1. Click **Save** in the toolbar. 

    Your new page appears in the list of pages with the **Draft** status.

