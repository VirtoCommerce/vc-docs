# Integration with DataTrans

The **DataTrans** module integrates the DataTrans payment gateway with your Virto Commerce Platform.

It enables secure and reliable payment processing using merchant credentials provided by DataTrans. This module is ideal for businesses that require a streamlined, PCI-compatible payment solution and want to connect their ecommerce operations with DataTrans' Swiss-based payment services.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-datatrans)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-datatrans/releases)

## Key features

* Secure payment processing using DataTrans merchant credentials.
* Authentication of payment requests using **MerchantId** and **Secret** keys.
* Seamless integration with Virto Commerce checkout flows.
* Configurable through **appsettings.json** with no code changes required.
* Supports PCI-compliant implementations depending on your DataTrans setup.

## Setup

To integrate DataTrans with Virto Commerce for secure payment processing:

1. [Configure appsettings.json](#configure-appsettingsjson)
1. [Configure Platform](#configure-platform)

### Configure appsettings.json

Configure the **appsettings.json** file as follows:

{% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--datatrans-start-->" end="<!--datatrans-end-->" %}

### Configure Platform

To setup Virto Commerce Platform:

1. Click **Stores** in the main menu. 
1. In the next blade, select a store.
1. In the **Store details** blade, click on the **Payment methods** widget.

    !!! note
        You can set the order in which payment methods appear in the web store. Drag and drop them to change the order.

1. In the **Payment methods** blade, select **Datatrans**.
1. In the **Edit payment method** blade, configure the following fields:

    ![Edit payment method 2](media/payment-method-management.png){: style="display: block; margin: 0 auto;" }

1. Click **Save** in the toolbar to save the changes.

Your modifications have been saved.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CyberSource">← CyberSource payment method </a>
    <a href="../Skyflow">Skyflow payment method →</a>
</div>
