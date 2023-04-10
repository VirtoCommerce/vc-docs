# Using Azure SQL Elastic Pool and Several Satabases Instead of the Big One

Azure SQL pools are well suited for Virto Commerce solutions. Virto Commerce allows you to create a unique connection string for each module. The more databases you can add to a Pool, the more you're going to save. Depending on your application usage patterns, it's possible to see savings with as few as two S3 databases.

To set own connection string for every module, use Module Id as a name of a connection string. You can find Module Id in the [module.manifest](https://docs.virtocommerce.org/new/dev_docs/Fundamentals/Modularity/06-module-manifest-file/) file. For example, Module Id for the Order module is as follows:
```
<?xml version="1.0" encoding="utf-8" ?>
<module>
    <id>VirtoCommerce.Orders</id>
    <version>2.17.30</version>
    <platformVersion>2.13.42</platformVersion>
    <dependencies>
        <dependency id="VirtoCommerce.Core" version="2.25.24" />
        <dependency id="VirtoCommerce.Catalog" version="2.12.0" />
        <dependency id="VirtoCommerce.Pricing" version="2.11.0" />
        <dependency id="VirtoCommerce.Customer" version="2.11.0" />
        <dependency id="VirtoCommerce.Store" version="2.11.0" />
    </dependencies>
```

Set your own connection strings for:

* VirtoCommerce.Cart.
* VirtoCommerce.Catalog.
* VirtoCommerce.Customer.
* VirtoCommerce.Orders.
* VirtoCommerce.Pricing.
* VirtoCommerce - Default database for other modules.

It decreases database size and cost, increases performance and simplifies maintenance tasks.