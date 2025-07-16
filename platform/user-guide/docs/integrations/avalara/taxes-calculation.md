# Taxes Calculation

AvaTax automatically calculates sales and use tax for transactions, invoices, and other activity powered by Virto Commerce. Virto Commerce sends transaction data to AvaTax, and AvaTax sends back the tax total. Customers, salespeople, and others can see the tax owed in real time.

## Send orders automatically
To calculate taxes and send them to AvaTax automatically :

1. In the main menu, click **Stores** to open the **Stores** blade.
1. Select the required store.
1. In the **Store details** blade, click the **Tax providers** widget.
1. Click **Avalara Tax Provider**. Make sure the **Is active** option is checked.
1. In the **Edit tax provider** blade, click **Settings**.

    ![path](../media/avalara-path.png)

1. Enter the desired [settings](settings.md). Enable scheduled synchronization of VC Platform orders with AvaTax to send orders to AvaTax automatically.

    ![Enabled Synchronization](../media/send-orders-automatically.png)

1. Verify your connection by clicking the **Test connection with AvaTax** button.
    * If the button gets green, the connection was set successfully.
        
        ![Successful connection](../media/connection-test.png)
    
    * If the button gets red, correct the listed mistakes.
    
        ![Connection errors](../media/connection-errors.png) 

## Send orders manually
In some cases, you may need the option to manually send transaction data to AvaTax. For example, if an error occured during the automatic data transfer. 

To send the data to AvaTax manually:

1. In the main menu, click **Orders** to open the **Orders** blade.
1. Select the required order.
1. Click the red button to send the order to AvaTax.

![Send data manually](../media/send-orders-manually.png){: width="700"}

Your data has been successfully sent.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../orders-synchronization">← Orders synchronization </a>
    <a href="../tax-type-configuration">Tax type configuration →</a>
</div>