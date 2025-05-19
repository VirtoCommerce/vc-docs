# Using responseGroup in Virto Commerce REST APIs

The `responseGroup` parameter in Virto Commerce REST APIs is a powerful way to optimize responses by specifying what level of detail should be returned. This is especially useful for clients that don't need the entire object graph and want to minimize payload size and improve performance.

Each module that supports `responseGroup` has its own enum definition representing available levels of detail. You can pass one or more values (in accordance with the enum's `Flags` attribute) to tailor the response.

Use `responseGroup` in:

=== "REST API calls"

    ```
    GET /api/catalog/products?responseGroup=WithProperties
    ```

=== "Code (C#) when calling services or repositories"

    ```csharp
    var criteria = new ProductSearchCriteria
    {
        ResponseGroup = "WithProperties,WithPrices"
    };
    ```


Generally, modules define an enum like this:

```csharp
[Flags]
public enum CatalogResponseGroup
{
    None = 0,
    Info = 1,
    WithProperties = 2,
    WithPrices = 4,
    Full = Info | WithProperties | WithPrices
}
```

File names often follow this pattern:

  * `CatalogResponseGroup`
  * `MemberResponseGroup`
  * `CartAggregateResponseGroup`


These flags define which parts of the object graph will be included in the response. Choose based on what you need:

| Example need                    | Add this flag                      |
| ------------------------------- | ---------------------------------- |
| I want product prices.          | `WithPrices`                       |
| I need customer addresses.      | `WithAddresses`                    |
| I want cart with payments info. | `WithPayments`                     |
| I want full object.             | `Full` or combine multiple flags   |

You can use bitwise-style combinations:

```csharp
ResponseGroup = "WithPrices,WithInventory"
```

Or the named shortcut, if available:

```csharp
ResponseGroup = "Full"
```


## Sample patterns

=== "Catalog: Load product with prices"

    ```csharp
    var criteria = new ProductSearchCriteria
    {
        Keyword = "hat",
        ResponseGroup = "WithPrices"
    };
    ```

=== "Customer: Load user with addresses"

    ```csharp
    var member = await _memberService.GetByIdAsync(userId, MemberResponseGroup.WithAddresses.ToString());
    ```

=== "Cart: Load cart with payments and shipments"

    ```csharp
    var cart = await _cartAggregateRepository.GetCartByIdAsync(
        cartId,
        CartAggregateResponseGroup.WithPayments | CartAggregateResponseGroup.WithShipments
    );
    ```

[View the list of ResponseGroup setting](https://github.com/search?q=org%3AVirtoCommerce+ResponseGroup&type=code&p=1)