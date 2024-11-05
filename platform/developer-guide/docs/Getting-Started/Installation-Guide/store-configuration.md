# Configure Store

After you have assigned a price list and a catalog to your store, configure:

1. [Tax providers.](configure-store.md#set-up-tax-providers)
1. [Payment methods.](configure-store.md#set-up-payment-methods)
1. [Shipping methods.](configure-store.md#set-up-shipping-methods)

For the remainder of this guide, all the settings are configured via the Store module (Stores--> Your store (Dental Demo Store in our case)).

## Set up tax providers

The default tax providers in the Virto Commerce Platform are:

* **Avalara**: It automatically calculates sales and use tax for transactions, invoices, and other activity powered by Virto Commerce. Virto Commerce sends transaction data to AvaTax, and AvaTax sends back the tax total. Customers, salespeople, and others can see the tax owed in real time.
* **Fixed rate tax provider**: It calculates taxes based on fixed rates.

### Avalara tax provider

To start using AvaTax:

1. [Register in Avalara.](https://www.avalara.com/us/en/index.html)

    You will further need:

    * Link to Avalara API service.
    * Link to Avalara admin page.
    * Avalara account number.
    * Avalara license key.

    ![License key](media/license-key-number.png)

1. Set up Virto Cloud portal:

    1. Go to **Virto Cloud Portal** --> **Your environment** (Dentalstoredemo in our case) --> **Applications** widget --> Platform **Application settings**.
    1. Add Avalara account number and Avalara license key:

        ![Avalara account number](media/avalara-account-number.png)

    1. Click **Save** in the toolbar to apply the changes.

1. Set up Platform according to [this guide](https://docs.virtocommerce.org/platform/user-guide/integrations/avalara/taxes-calculation/#send-orders-automatically).


### Fixed rate provider

As an example, let't set the fixed tax rate to 20%:

1. Click on the **Tax providers** widget.
1. In the next blade, check **Fixed percent tax rate**, then click on it.
1. In the next blade, click on the **Settings** widget.
1. In the next blade, enter 20 to the **Fixed tax rate** field.
1. Click **OK** to save the changes.

The fixed tax rate has been saved.

## Set up payment methods

You can configure payment methods as described in [this guide](https://docs.virtocommerce.org/platform/user-guide/payment/managing-payment-methods/#edit-payment-methods).

!!! note
    You can specify the payment method logo URL (**Payment methods widget** --> The required payment method) in the following format **/static/icons/payment-methods/credit-card.svg**.

## Set up shipping methods

As an example, let't set the ground fixed shipping rate to 20% and air shipping rate to 50%:

1. Click on the **Shipping methods** widget.
1. In the next blade, select **Fixed shipping rate**.

    !!! note
        At this step, you can specify the shipping method logo URL in the following format **/static/images/checkout/fedex.svg**.

1. In the next blade, click on the **Settings** widget.
1. In the next blade, enter 20 to the **Ground shipping rate** field and 50 to the **Air shipping rate** field.
1. Click **OK** to save the changes.

The shipping rates have been saved.

