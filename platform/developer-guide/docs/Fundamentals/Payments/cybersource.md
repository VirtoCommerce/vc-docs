# Integration with CyberSource

The **CyberSource** module integrates CyberSource payment solutions with your Virto Commerce Platform.

It enables secure and seamless payment processing, using CyberSource's Flex Microform technology for enhanced user experience and PCI compliance. This module is designed for businesses seeking to integrate a robust and scalable payment gateway into the ecommerce platform.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-cyber-source)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-cyber-source/releases)

## Key features

* CyberSource-based payment methods like Card Payment, 3D Secure, Visa Click to Pay, Google Pay, eCheck, and Apple Pay.  
* Tokenization to create, update, and delete a card token.  
* Authorization and capture of a payment.  
* Refunding a payment back to the merchant.  
* *(Coming Soon)* Manual capture of a payment.  
* *(Coming Soon)* Synchronization of payments to track missing and fraudulent transactions based on merchant decisions.


## Setup

To integrate CyberSource with Virto Commerce for secure payment processing:

1. [Configure appsettings.json](#configure-appsettingsjson)
1. [Configure Platform](#configure-platform)

### Configure appsettings.json

Configure the **appsettings.json** file as follows:

{% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--cybersource-start-->" end="<!--cybersource-end-->" %}

### Configure Platform 

To setup Virto Commerce Platform:

1. Go to Virto Commerce Platform and click **Stores** in the main menu. 
1. In the next blade, select your store.
1. In the **Store details** blade, click on the **Payment methods** widget.
1. In the next blade, select **CyberSource** payment method. It automatically appears in the list after the module is installed.
1. In the next blade, enable the CyberSource payment method and configure other settings (optionally):

    ![Back office 2](media/configure-cybersource.png)

1. Click **Save** in the toolbar to save the changes.

The CyberSource payment method has been enabled for your Store.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../skyflow">← Skyflow </a>
    <a href="../../Shipments/new-shipping-method-registration">Registering new shipping method →</a>
</div>