# Sales Rep

The **Sales Rep** module turns selected users into sales representatives who serve a defined set of customer organizations. It exposes a storefront GraphQL (X-API) surface that lets a B2B storefront show the reps supporting an organization, the customers a rep serves, and their orders.

The storefront queries are exposed on a dedicated scoped schema at `POST /graphql/sales-rep`, with a GraphiQL UI at `/ui/graphiql/sales-rep`. Every query requires an authenticated caller and is store- and membership-scoped, so a rep only sees the customers they serve and a buyer only sees their own reps.

!!! note "Authentication"
    Every query needs a bearer token. Rep login accounts are typically store-bound, so the password grant must include the `storeId` form parameter. See [Issue and use access token](../../Fundamentals/Security/authentication/issuing-and-using-access-token.md#resource-owner-password-credential-flow).

| Queries | Mutations |
| --- | --- |
| [customerSalesReps](queries/customerSalesReps.md) <br> [salesRepCustomers](queries/salesRepCustomers.md) <br> [salesRepCustomer](queries/salesRepCustomer.md) <br> [salesRepOrders](queries/salesRepOrders.md) | [sendCustomerCommunication](mutations/sendCustomerCommunication.md) |

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-sales-rep)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-sales-rep/releases/latest)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../Quote/overview">← Quote module overview</a>
    <a href="queries/customerSalesReps">customerSalesReps query →</a>
</div>
