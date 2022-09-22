# Troubleshooting Incorrect Prices in Storefront

Since the Pricing module enables adding multiple prices of the same currency to a single product, situations may occur where prices displayed in the Storefront catalog are not the ones expected. 
For example, say, you may add a new price to your product but Storefront will display it incorrectly:

![Incorrect price](media/troubleshooting/incorrect-price.png)

Here are some steps you can follow to find out why the correct price does not appear:

1. Open the product with the incorrect price in Catalog and navigate to the ***Price*** widget, as explained [here](viewing-price-list-in-catalog.md).
2. Make sure the new price is included into the Price list.
3. Open the assignment list and make sure the price has the assignment that meets the following conditions:
    + The assignment ***Priority*** is the highest among other price list assignments. Price with the highest priority assignment is used first.  
    + The ***Catalog*** assignment references the correct catalog. For example, if the store your Storefront is configured to work with uses a virtual catalog and the assignment points to a physical one (where the product actually is), the price will not be displayed. Alternatively, you can set the ***Store*** assignment instead of ***Catalog*** to avoid confusion.
    + If the assignment has any special conditions, make sure they are applicable. For instance, if the assignment has the ***User group containss*** condition enables, a customer should be added to the correct user group.   
    + Build the product index and check the Storefront price once again.