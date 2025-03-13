# Get Started

To get started with the module, complete the following steps:

* [Publish Power BI report.](#publish-power-bi-report)
* [Set up the module.](#set-up-virto-commerce-module)

## Prerequisites

* Ensure that the system has Power BI Desktop installed.
* Apply SQL scripts from [Script bi-Orders-view.sql](https://github.com/VirtoCommerce/vc-module-power-bi-reports/blob/dev/src/Sql-Scripts/bi-Orders-view.sql) on Virto Commerce database to create BI Views which are used as a Data Source.
* Verify that the custom connection string is correctly configured and that the SQL Server and database are accessible from the system where the report will be deployed.

## Publish Power BI report

1. Open the [eCommerce-Sales-Report file](https://github.com/VirtoCommerce/vc-module-power-bi-reports/blob/dev/src/Power-BI-Files/ECommerce-Sales-Report.pbix) in Power BI Desktop and check that it loads the data correctly.
1. On the **Home** tab of the Power BI Desktop ribbon, click **Publish** to publish the report to Power BI Service.
1. Set up data refresh options for the report:
    1. Go to the **Datasets** page and click on the ellipsis (...) next to the dataset that corresponds to the report data source.
    1. Select **Schedule Refresh** and configure the refresh settings as needed.
1. Ensure that the you have appropriate access to the report and its underlying data sources.
1. Share the report with the System Administrator, assign them to a role with appropriate permissions, or grant them access to the SQL Server database if necessary.
1. Keep the Power BI Reports URL.

## Set up Virto Commerce module

1. In the Virto Commerce Platform, open **Setting**.
1. In the search field of the next blade, type  **Power BI Reports** to find the settings related to the module. 
1. Click **Power BI Reports URL**.
1. In the next blade, set up **Power BI Reports URL**.

    ![Set up URL](../media/power-bi-report-url.png)

1. Click **Save** in the toolbar to save the changes.

Once set up, Virto Commerce will redirect users to Power BI reports from the Apps menu:

![Redirect](../media/redirecting-to-power-bi.gif)