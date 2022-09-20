# Overview

Virto Commerce ***Pricing*** module is designed for storing, managing, and calculating product prices.

## Related Components

To view the source code of Virto Commerce Marketing module, check out our GitHub repository.

To download the latest Marketing module release, click here.

## Core Entities

The Pricing module comprises three core entities:

+ Price
+ Price list
+ Price list assignment

We will cover them one by one below.

### Price

The price entity stores the item price supports static discounts and tier prices. It's key properties are:

+ ***Product*** (required): Item the current price refers to.
+ ***List price*** (required): Base product price in the appropriate currency, without any promotions or offers applied.  
+ ***Sale price*** (optional): Discount price, i.e. with all relevant offers or promotions applied.
+ ***Mininum quantity*** (the minimum value is 1): The lowest number of items possible, with which the price is valid.

### Price List

A price list is, technically, a container that stores prices in a single currency. Its key properties are:

+ ***Currency*** (required): Single currency for all prices included into the price list.  
+ ***Prices***: List of prices included into the price list.

### Price List Assignment

Price list assignments enable associating  specific price lists with catalogs based on the relevant rules and conditions.  

Any price list assignment has the following key properties:

+ ***Price list*** (required): Refers to a specific price list.  
+ ***Catalog*** (required): Refers to a specific catalog.
+ ***Enable date*** , ***Expiration date***: Start and end dates that determine the period, during which the pricelist assignment is valid.  
+ ***Priority***: Price list priority. The price list having the highest priority will be used first.

## Key Features 

With the Pricing module, you can count on the following key features and user scenarios:

+ [Creating New Price list](creating-new-price-list.md)
    + [Adding Products to New Price List](adding-products-to-new-price-list.md)
    + [Adding Prices to Products](adding-prices-to-products.md)      
+ [View Price list via Catalog Module](viewing-price-list-in-catalog.md)
+ [Adding New Assignment](adding-new-assignment.md)
+ [Managing Pricing Module Settings](managing-pricing-module-settings.md)
+ [Exporting Prices and Price List Assignments](export-functionality.md)
+ [Troubleshooting Incorrect Prices in Storefront](troubleshooting-guide.md)