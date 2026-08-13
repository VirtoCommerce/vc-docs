# Sales Rep

The **Sales Rep** module turns selected users into sales representatives who serve a defined set of customer organizations. It exposes a storefront GraphQL (X-API) surface that lets a B2B storefront show the reps supporting an organization, the customers a rep serves, and their orders.

The storefront queries are exposed on a dedicated scoped schema at `POST /graphql/sales-rep`, with a GraphiQL UI at `/ui/graphiql/sales-rep`. Every query requires an authenticated caller and is store- and membership-scoped, so a rep only sees the customers they serve and a buyer only sees their own reps.

!!! note "Authentication"
    Every query needs a bearer token. Rep login accounts are typically store-bound, so the password grant must include the `storeId` form parameter. See [Issue and use access token](../../Fundamentals/Security/authentication/issuing-and-using-access-token.md#resource-owner-password-credential-flow).

| Queries | Objects | Mutations |
| --- | --- | --- |
| [customerSalesReps](queries/customerSalesReps.md) <br> [salesRepCustomers](queries/salesRepCustomers.md) <br> [salesRepCustomer](queries/salesRepCustomer.md) <br> [salesRepOrders](queries/salesRepOrders.md) <br> [salesRepCustomerOrderStatistics](queries/salesRepCustomerOrderStatistics.md) <br> [salesRepCustomerCartStatistics](queries/salesRepCustomerCartStatistics.md) <br> [salesRepCustomerCounts](queries/salesRepCustomerCounts.md) <br> [salesRepTopSellers](queries/salesRepTopSellers.md) <br> [salesRepTopSellerSortRules](queries/salesRepTopSellerSortRules.md) <br> [salesRepTopSellerFilterRules](queries/salesRepTopSellerFilterRules.md) <br> [salesRepOrderFilterRules](queries/salesRepOrderFilterRules.md) <br> [salesRepCartFilterRules](queries/salesRepCartFilterRules.md) <br> [salesRepCustomerFilterRules](queries/salesRepCustomerFilterRules.md) | [SalesRepContactType](objects/SalesRepContactType.md) <br> [SalesRepCustomerType](objects/SalesRepCustomerType.md) <br> [SalesRepCustomerDetailsType](objects/SalesRepCustomerDetailsType.md) <br> [SalesRepOrderType](objects/SalesRepOrderType.md) <br> [SalesRepAddressType](objects/SalesRepAddressType.md) <br> [CustomerOrderStatisticsType](objects/CustomerOrderStatisticsType.md) <br> [CustomerOrderStatisticsPeriodType](objects/CustomerOrderStatisticsPeriodType.md) <br> [CustomerOrderStatisticsComparisonType](objects/CustomerOrderStatisticsComparisonType.md) <br> [CustomerCartStatisticsType](objects/CustomerCartStatisticsType.md) <br> [CustomerCartStatisticsPeriodType](objects/CustomerCartStatisticsPeriodType.md) <br> [SalesRepCustomerCountsType](objects/SalesRepCustomerCountsType.md) <br> [SalesRepCustomerCountsPeriodType](objects/SalesRepCustomerCountsPeriodType.md) <br> [SalesRepCustomerCountsComparisonType](objects/SalesRepCustomerCountsComparisonType.md) <br> [SalesRepTopSellerType](objects/SalesRepTopSellerType.md) <br> [SalesRepTopSellerSortRuleType](objects/SalesRepTopSellerSortRuleType.md) <br> [SalesRepTopSellerFilterRuleType](objects/SalesRepTopSellerFilterRuleType.md) <br> [SalesRepOrderFilterRuleType](objects/SalesRepOrderFilterRuleType.md) <br> [SalesRepCartFilterRuleType](objects/SalesRepCartFilterRuleType.md) <br> [SalesRepCustomerFilterRuleType](objects/SalesRepCustomerFilterRuleType.md) <br> [SalesRepCommunicationResultType](objects/SalesRepCommunicationResultType.md) | [sendCustomerCommunication](mutations/sendCustomerCommunication.md) |

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-sales-rep)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-sales-rep/releases/latest)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Quote/overview">← Quote module overview</a>
    <a href="../queries/customerSalesReps">customerSalesReps query →</a>
</div>
