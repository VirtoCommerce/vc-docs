# Integration with Google Analytics 4 and Google Tag Manager

The Virto Commerce Frontend application has native integration with Google Analytics 4 (GA4) and Google Tag Manager (GTM).


## Direct GA4 integration 

Using GA4 is recommended for simple setups. To install it and assign Google Analytics Measurement Id for you store:

1. Create Google Analytics Account according to the [Instruction](https://support.google.com/analytics/answer/9304153):

    ![Demo](../media/demo.gif){: style="display: block; margin: 0 auto;" }
    
1. Open **Stores** from the main menu.
1. Select the required store.
1. In the **Store details** blade, click on the **Settings** widget.
1. Find the **Google Analytics** section and enable Google Analytics 4.
1. Enter your Measurement Id. 

    ![Enable Google Analytics](media/measurementId.png){: style="display: block; margin: 0 auto;" }

1. Click **OK**, then save the **Store settings** from the toolbar to activate the Google Analytics tracking.

    ![Google Analytics Tracking](../media/google-analytics-tracking.png){: style="display: block; margin: 0 auto;" }

Your modifications have been applied.


## Google Tag Manager setup for GA4

Google Tag Manager provides a centralized way to manage all your tracking tags without code changes. It is recommended for advanced tracking. Use this option if you need:

* Multiple tracking tools (GA4, Facebook Pixel, LinkedIn Insight, etc.)
* Custom event tracking and triggers.
* A/B testing tools.
* Enhanced flexibility for marketing teams. 

To start using GTM:

1. [Create a Google Tag Manager account and container](https://support.google.com/tagmanager/answer/6103696).
1. Save your Container Id (GTM-XXXXXXX).
1. In Google Tag Manager, create a new **Google Analytics: GA4 Configuration** tag.
1. Enter your GA4 Measurement Id.
1. Set the trigger to **All Pages** or **Initialization - All Pages**.
1. Configure additional parameters (user properties, custom dimensions, etc.)
1. Save and publish your container.
1. Open **Stores** from the main menu of the Platform.
1. Select the required store.
1. In the **Store details** blade, click on the **Settings** widget.
1. Find the **Google Analytics** section and enable Google Analytics 4.
1. Enter your **GTM Container Id** (GTM-XXXXXXX):

    ![Container Id](media/containerId.png){: style="display: block; margin: 0 auto;" }

1. (Optional) Enter your **Measurement Id**, if you want both GTM and direct GA4 tracking.
1. Click **OK**, then save the **Store settings** from the toolbar.

Your modifications have been applied.

!!! note
    Because the Virto Commerce Frontend integrates with Google Tag Manager (GTM) through the GA module, it can now automatically support additional third-party SaaS tools that rely on GTM - such as Product Guide.
    Product Guide can be connected to our Frontend by simply adding its script or tag to GTM. No custom Frontend development, code changes, or manual script injection into the Frontend are required:

    ![Product guide](media/product-guide.gif){: style="display: block; margin: 0 auto;" width="400"}


## GTM and GA4 integration benefits

* **Centralized management**: Update tracking configurations without code deployments.
* **Enhanced events**: Leverage `dataLayer` for rich ecommerce events.
* **Multiple tags**: Add other marketing and analytics tools easily.
* **Testing**: Preview and debug tags before publishing.
* **Load order**: GTM loads first, ensuring proper event sequencing for all tags.

## Important notes

* If both **GTM Container Id** and **Measurement Id** are provided, GTM will load first, followed by direct GA4.
* The module automatically pushes ecommerce events to `dataLayer` which GTM can capture.
* All standard ecommerce events (**add_to_cart**, **purchase**, etc.) are available in `dataLayer`.
* Virto Frontend has native integration with Google Analytics 4 module. Once you save store settings, the Google Analytics tracking will be activated.

## GTM event tracking (optional setup)

The module automatically [tracks a number of ecommerce actions](../../../../../storefront/developer-guide/integrations/google-analytics/ga-events). If you are using GTM, you can capture these events by creating GA4 Event tags in GTM:

* In GTM, create a new **Google Analytics: GA4 Event** tag.
* Set **Configuration Tag** to your GA4 Configuration tag.
* Set **Event Name** to a custom variable that reads from `dataLayer` (e.g., {{Event}}).
* Set the trigger to Custom Event matching the ecommerce events listed above.
* (Optional) Pass additional parameters using variables from `dataLayer`.
* Save and publish your container.

This allows you to:

* Customize event names before sending to GA4.
* Add conditional logic to events.
* Send events to multiple analytics platforms.
* Debug events in GTM Preview mode.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Google Analytics module overview </a>
    <a href="../settings">Settings →</a>
</div>