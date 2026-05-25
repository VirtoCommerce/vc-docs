# Grab Migrator Utility Quickstart

This guide introduces the Grab Migrator utility, which facilitates the extraction and application of EF-migrations from the Virto Commerce Platform and its modules.

## Run

To execute the Grab Migrator utility, run the following command:

```
vc-build GrabMigrator --grab-migrator-config <configfile>
```

## Grab migrations from Platform and modules

This section outlines the process of extracting EF-migrations from both the Platform and its modules:

1. Checkout Platform/modules source codes.
1. Ensure the **dotnet-ef** tool is installed. If not, reference to the [Installation guide](https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/dotnet).
1. Prepare the grab config file as follows:

    ``` json
    {
      "MigrationDirectories": [
        "D:\\AK\\Code\\Projects\\VC3-DEV-CORE3\\modules",
        "D:\\AK\\Code\\Projects\\VC3-DEV-CORE3\\vc-platform\\src\\VirtoCommerce.Platform.Data",
        "D:\\AK\\Code\\Projects\\VC3-DEV-CORE3\\vc-platform\\src\\VirtoCommerce.Platform.Security"
      ],
      "StatementsDirectory": "Statements"
    }
    ```
    
    Where:

    | Node                      | Description                                                                                               |
    | ------------------------- | --------------------------------------------------------------------------------------------------------- |
    | `MigrationDirectories`    | Directories where tool searches for migrations. Multiple paths can be specified.                          |   
    | `StatementsDirectory`     | There the tool stores grabbed SQL statements. One file per module. Default is 'Statements'.               |
    | Mode                      | 'V2V3' or 'All'. Upgrade Platform v2 to v3 scripts or all scripts should be grabbed. Default is 'V2V3'.   |

1. Run the tool, wait for the sql files to appear in **Statements** directory.
1. Check the config file: the `ConnectionStringsRefs` node should appear.


## Apply migrations to different databases

To apply the extracted migrations to different databases:

1. Prepare the apply config file with the desired order and settings:

    ``` json
    {
      "ApplyingOrder": [
        "VirtoCommerce.Platform",
        "VirtoCommerce.Platform.Security",
        "VirtoCommerce.CoreModule",
        "VirtoCommerce.TaxModule",
        "VirtoCommerce.InventoryModule",
        "VirtoCommerce.ImageToolsModule",
        "VirtoCommerce.NotificationsModule",
        "VirtoCommerce.ContentModule",
        "VirtoCommerce.Payment",
        "VirtoCommerce.StoreModule",
        "VirtoCommerce.CustomerModule",
        "VirtoCommerce.CatalogModule",
        "VirtoCommerce.ShippingModule",
        "VirtoCommerce.SitemapsModule",
        "VirtoCommerce.PricingModule",
        "VirtoCommerce.CartModule",
        "VirtoCommerce.OrdersModule",
        "VirtoCommerce.MarketingModule",
        "VirtoCommerce.SubscriptionModule",
        "VirtoCommerce.CustomerReviews",
        "VirtoCommerce.CatalogPersonalizationModule",
        "VirtoCommerce.CatalogPublishingModule",
        "VirtoCommerce.DynamicAssociationsModule",
        "VirtoCommerce.QuoteModule"
      ],
      "PlatformConfigFile": "D:\\AK\\Code\\Projects\\VC3-DEV-CORE3\\vc-platform\\src\\VirtoCommerce.Platform.Web\\appsettings.json",
      "StatementsDirectory": "Statements",
      "CommandTimeout": 30,
      "Grab": false,
      "Apply": true
    }
    ```

    Where:

    | Node                  | Description                                                                                 |
    | --------------------- | ------------------------------------------------------------------------------------------- |
    | `ApplyingOrder`       | The order in which the scripts will be applied.                                             |
    | `PlatformConfigFile`  | Platform config location used to discover connection strings for each module.               |
    | `StatementsDirectory` | Directory containing previously grabbed SQL statements.                                     |
    | `CommandTimeout`      | Command timeout in seconds.                                                                 |
    | `Grab`                | Switches the tool to grab mode (if **true**).                                                   |
    | `Apply`               | Switches the tool to apply mode (if **true**).                                                  |

1. Copy the `ConnectionStringsRefs` node from the grab config file to apply the config file.
1. Run the tool to apply the migrations to the databases.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../package-management">← Package management</a>
    <a href="../cold-start-and-data-migration">Cold start and data migration →</a>
</div>