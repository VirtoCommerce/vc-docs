# Customize Cart Validation Policies

When it comes to adapting cart validation policies, flexibility is key. In this article, we explore two ways to tailor these policies to your specific needs:

* [Allowing addition of products with zero prices.](customizing-cart-validation-policies.md#allow-adding-products-with-zero-price)
* [Allowing addition of products with custom prices.](customizing-cart-validation-policies.md#allow-adding-products-with-custom-price)

## Allow adding products with zero price

To customize the cart validation policies and enable the addition of products with zero prices in Virto Commerce, follow these steps:

1. Create Virto Commerce Extensions Module for VirtoCommerce.ExperienceApi:
1. Set up a new Virto Commerce extensions module specifically for VirtoCommerce.ExperienceApi.

1. Create a new class `CustomCatalogProductIsBuyableSpecification` inherited from `CatalogProductIsBuyableSpecification`:
    ```csharp
    public class CustomCatalogProductIsBuyableSpecification : CatalogProductIsBuyableSpecification
    {
        public override bool IsSatisfiedBy(ExpProduct product)
        {
            if (product == null)
                throw new ArgumentNullException(nameof(product));

            // Customize buyability conditions as needed
            return product.IndexedProduct.IsActive.GetValueOrDefault(false)
                && product.IndexedProduct.IsBuyable.GetValueOrDefault(false);
        }
    }
    ```

1. Override `IsSatisfiedBy` method in `CustomCatalogProductIsBuyableSpecification` to include additional conditions for buyability.

1. Create a new class `CustomProductIsBuyableSpecification` inherited from `ProductIsBuyableSpecification`:
    ```csharp
    public class CustomProductIsBuyableSpecification : ProductIsBuyableSpecification
    {
        public override bool IsSatisfiedBy(CartProduct product)
        {
            return base.IsSatisfiedBy(product);
        }

        protected override bool CheckPricePolicy(CartProduct product)
        {
            // Allow buying products with zero price
            return true;
        }
    }
    ```

1. Override `IsSatisfiedBy` Method in `CustomProductIsBuyableSpecification`.

1. Implement `CheckPricePolicy` to allow buying products with zero price.

1. Override specs in `Module.Initialize` for both `ProductIsBuyableSpecification` and `CatalogProductIsBuyableSpecification``:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        // Override models
        AbstractTypeFactory<ProductIsBuyableSpecification>.OverrideType<ProductIsBuyableSpecification, CustomProductIsBuyableSpecification>();
        AbstractTypeFactory<CatalogProductIsBuyableSpecification>.OverrideType<CatalogProductIsBuyableSpecification, CustomCatalogProductIsBuyableSpecification>();
    }
    ```

This implementation creates two custom specification classes, `CustomCatalogProductIsBuyableSpecification` and `CustomProductIsBuyableSpecification`, inheriting from their respective base classes. The specifications are then overridden in the `Module.Initialize` method to enable the desired customizations, allowing the addition of products with zero prices in the cart.


## Allow Adding Products with Custom Price

To allow the addition of products with custom prices:

1. Create a new class `CustomNewCartItemValidator` inherited from `NewCartItemValidator`:

    ```csharp
    public class CustomNewCartItemValidator : NewCartItemValidator
    {
        // Override the ValidateTierPrice virtual method to customize tier price validation
        protected override ValidationResult ValidateTierPrice(CartAggregate cart, CartProduct product)
        {
            // Implement custom logic for tier price validation as needed
            // ...

            // Return the validation result
            return base.ValidateTierPrice(cart, product);
        }
    }
    ```

2. Override the `ValidateTierPrice` virtual method in `CustomNewCartItemValidator` to customize tier price validation.

3. Create a new class `CustomCartAggregate` inherited from `CartAggregate`:

    ```csharp
    public class CustomCartAggregate : CartAggregate
    {
        // Override the SetLineItemTierPrice method to handle custom tier price logic
        protected override void SetLineItemTierPrice(CartProduct cartProduct, TierPrice tierPrice)
        {
            // Implement custom logic for setting line item tier price
            // ...

            // Call the base method to ensure proper functionality
            base.SetLineItemTierPrice(cartProduct, tierPrice);
        }
    }
    ```

4. Override the `SetLineItemTierPrice` in `CustomCartAggregate` to handle custom tier price logic.

5. Override `NewCartItemValidator` in `Module.Initialize` to use `CustomNewCartItemValidator`:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        // Override models
        AbstractTypeFactory<NewCartItemValidator>.OverrideType<NewCartItemValidator, CustomNewCartItemValidator>();

        // Override the registration of CartAggregate to use CustomCartAggregate
        serviceCollection.AddTransient<CartAggregate, CustomCartAggregate>();

        // Override the registration of CartAggregate to use CustomCartAggregate with proper scoping
        services.AddTransient<Func<CartAggregate>>(provider => () => provider.CreateScope().ServiceProvider.GetRequiredService<CustomCartAggregate>());
    }
    ```

6. Override `CartAggregate` in `Module.Initialize` to use `CustomCartAggregate`.

These steps enable the customization of cart validation policies to accommodate products with custom prices. The provided code snippets demonstrate the creation of custom classes (`CustomNewCartItemValidator` and `CustomCartAggregate`) that inherit from the respective base classes and override relevant methods to implement the desired custom logic. The `Module.Initialize` method is then configured to use these custom classes, ensuring the application follows the updated cart validation policies.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-cart-query-with-custom-parameter">← Extending Cart query with custom parameter </a>
    <a href="../upgrading-to-net8">Upgrading to .NET 8  →</a>
</div>