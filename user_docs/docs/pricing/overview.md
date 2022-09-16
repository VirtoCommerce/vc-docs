# Overview

Virto Commerce ***Pricing*** module is designed for storing, managing, and calculating product prices.

The Pricing module comprises three core entities:

+ Price
+ Price list
+ Price list assignment

We will cover them one by one below.

## Price

The price entity stores the item price supports static discounts and tier prices. It's key properties are:

+ ***Product*** (required): Item the current price refers to.
+ ***List price*** (required): Base product price in the appropriate currency, without any promotions or offers applied.  
+ ***Sale price*** (optional): Discount price, i.e. with all relevant offers or promotions applied.
+ ***Mininum quantity*** (the minimum value is 1): The lowest number of items possible, with which the price is valid.

## Price List

A price list is, technically, a container that stores prices in a single currency. Its key properties are:

+ ***Currency*** (required): Single currency for all prices included into the price list.  
+ ***Prices***: List of prices included into the price list.

## Price List Assignment

Price list assignments enable associating  specific price lists with catalogs based on the relevant rules and conditions.  

Any price list assignment has the following key properties:

+ ***Price list*** (required) - relation to selected pricelist.  
+ ***Catalog*** (required) - relation to selected catalog.
+ ***Enable*** (start) and ***Expiration dates*** – the specified Enabled and Expiration dates determine the validation period of the pricelist assignment.  
+ ***Priority***  defines the priority of the Pricelist. The system will apply the pricelist that has the highest priority.  
+ ***Dynamic Assignment*** of applicability.

## Key Features 

1. The system supports multiple **Pricelists**, i.e. the same product item may have different price in different price lists.
1. Each **Catalog** can have its own list of **Pricelists**.
1. Every **Pricelists** should have a unique Name-ID, and single currency.
1. Each **Pricelists** contains a list of product prices with single currency.
1. The system supports **Tier Pricing** and it is a way to encourage shoppers to buy larger quantities of a product by applying discounts based on the quantity ordered.
1. The system supports static discounts on products and allows the user to specify the discount on each item on the list.
1. In order to make the **Pricelists** active, it should be assigned to a specific **Catalog** in the system. The system allows the user to specify specific rules and conditions that can also be assigned to the **Pricelists**. These specific rules and conditions will influence the price calculation and define to which user categories or Organizations the pricelist will be displayed. This is a so-called **Dynamic Assignment**.
1. The system allows expanding the **Dynamic Assignment** tree and it completely depends on the organization business needs. Any condition or rule can be added without changing the Module logic.
1. The system allows assigning one **Pricelists** to several different **Catalogs**. The **Pricelists** is integrated into the **Catalog**.
1. The system allows specify the **Pricelists** priority and therefore display on **Storefront** the **Pricelists** with higher priority.

## Scenarios  

1. [Create a New Price list](create-new-price-list.md)
    1. [Add Products to the New Price List](add-products-to-the-new-price-list.md)
    1. [Add Prices to products](add-prices-to-products.md)
        1. [Add List Price](add-prices-to-products.md#add-list-price)
        1. [Add Sale Price](add-prices-to-products.md#add-sale-price)
        1. [Specify Tier Price](add-prices-to-products.md#specify-tier-price)
1. [View Price list via Catalog Module](view-price-list-via-catalog-module.md)
1. [Add New Assignment](add-new-assignment.md)
    1. [Simple Assignment without rules and conditions](add-new-assignment.md#simple-assignment-without-rules-and-conditions)
    1. [Assignment with Rules and Conditions](add-new-assignment.md#assignment-with-rules-and-conditions)
1. [Managing Pricing module settings](managing-pricing-module-settings.md)
1. [Export Prices and Pricelist Assignments](export-functionality.md)
1. [Troubleshooting incorrect prices in Storefront](troubleshooting-guide.md)