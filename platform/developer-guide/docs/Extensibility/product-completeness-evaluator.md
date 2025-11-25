# Extend Product Completeness Evaluation Process

The Catalog Publishing Module allows to evaluate the completeness of products for publication according to specified criteria. 

![Readmore](media/readmore.png){: width="25"} [Catalog Publishing Module](/platform/user-guide/latest/catalog-publishing/overview)

In this guide, we will show how to extend the product completeness evaluation process to allow full customization. Below are potential user scenarios along with solutions.

## Add new detail to default evaluation process

To integrate additional details into the default evaluation process:

1. Inherit your detail evaluator from `DefaultCompletenessDetailEvaluator` class.
1. Override `EvaluateCompleteness` method:

    ```csharp
    public class CustomCompletenessDetailEvaluator : DefaultCompletenessDetailEvaluator
    {
        public override CompletenessDetail[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
        {
        }
    }
    ```

1. Register this class as implementation of `DefaultCompletenessDetailEvaluator` in Unity:

    ```csharp
    _container.RegisterType<DefaultCompletenessDetailEvaluator, CustomCompletenessDetailEvaluator>(nameof(CustomCompletenessDetailEvaluator));
    ```

The default product completeness evaluator includes your detail evaluator in evaluation process.

## Define own product completeness evaluator

To create your own product completeness evaluator, you can:

=== "Implement **ICompletenessEvaluator** Interface"

    ```csharp
    public class CustomCompletenessEvaluator : ICompletenessEvaluator
    {
        public CompletenessEntry[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
        {
        }
    }
    ```

=== "Customize the default evaluation process"

    ```csharp

    public class CustomCompletenessEvaluator : DefaultCompletenessEvaluator
    {
        public override CompletenessEntry[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
        {
        }
    }
    ```

After that, register your class as implementation of `ICompletenessEvaluator` in Unity:

```csharp
_container.RegisterType<ICompletenessEvaluator, CustomCompletenessEvaluator>(nameof(CustomCompletenessEvaluator));
```

Now your product completeness evaluator is available in module's REST API and UI.


## Define own product completeness evaluator

If you want to define your own product completeness evaluation process, you can implement the same extensibility logic as ours:

```csharp
public class CustomCompletenessEvaluator : ICompletenessEvaluator
{
    protected IReadOnlyCollection<ICompletenessDetailEvaluator> DetailEvaluators { get; }
        
    public CustomCompletenessEvaluator(CustomCompletenessDetailEvaluator[] detailEvaluators, IItemService productService) :
        this(detailEvaluators as ICompletenessDetailEvaluator[], productService)
    {
    }

    protected CustomCompletenessEvaluator(ICompletenessDetailEvaluator[] detailEvaluators, IItemService productService)
    {
        _productService = productService;
        DetailEvaluators = detailEvaluators;
    }
        
    public virtual CompletenessEntry[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
    {
    }
}
```

If you prefer not to define your own product completeness evaluation process from scratch, you can simply customize the default process provided by inheriting from the DefaultCompletenessEvaluator. Here are the options for customizing your product completeness evaluator:

* [Default detail evaluators](product-completeness-evaluator.md#default-detail-evaluators): Use the default detail evaluators provided.
* [Custom detail evaluators](product-completeness-evaluator.md#custom-detail-evaluators): Implement your own custom detail evaluators.
* [Combining default and custom detail evaluators](product-completeness-evaluator.md#combining-default-and-custom-detail-evaluators): Mix default and custom detail evaluators to suit your needs.
* [Mixing default and all custom detail evaluators](product-completeness-evaluator.md#mixing-default-and-all-custom-detail-evaluators): Utilize some default evaluators alongside entirely custom ones.

### Default detail evaluators

To use the default detail evaluators provided:

1. Inject `DefaultCompletenessDetailEvaluator` array to your constructor.
1. Pass it to the protected constructor of the `DefaultCompletenessEvaluator` base class:
    ```csharp
    public class CustomCompletenessEvaluator : DefaultCompletenessEvaluator
    {
        private readonly IItemService _productService;

        public CustomCompletenessEvaluator(DefaultCompletenessDetailEvaluator[] detailEvaluators, IItemService productService) :
            base(detailEvaluators as ICompletenessDetailEvaluator[], productService)
        {
        }
    }
    ```

### Custom detail evaluators

To implement your own custom detail evaluators:

1. Create your own (possible, abstract) base class for detail evaluators.
1. Inherit all your detail evaluators from it:
    ```csharp
    public abstract class CustomCompletenessDetailEvaluator : ICompletenessDetailEvaluator
    {
        public abstract CompletenessDetail[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products);
    }


    public class CustomCompletenessDetailEvaluator1 : CustomCompletenessDetailEvaluator
    {
        public override CompletenessDetail[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
        {
        }
    }


    public class CustomCompletenessDetailEvaluator2 : CustomCompletenessDetailEvaluator
    {
        public override CompletenessDetail[] EvaluateCompleteness(CompletenessChannel channel, CatalogProduct[] products)
        {
        }
    }
    ```
1. Inject `CustomCompletenessDetailEvaluator` array into the constructor of your product completeness evaluator and pass this array to the protected constructor of the `DefaultCompletenessEvaluator` base class:
    ```csharp
    public class CustomCompletenessEvaluator : DefaultCompletenessEvaluator
    {
        private readonly IItemService _productService;

        public CustomCompletenessEvaluator(CustomCompletenessDetailEvaluator[] detailEvaluators, IItemService productService) :
            base(detailEvaluators as ICompletenessDetailEvaluator[], productService)
        {
        }
    }
    ```

1. Register your detail evaluators as implementation of `CustomCompletenessEvaluator` class in Unity:
    ```
    _container.RegisterType<CustomCompletenessEvaluator, CustomCompletenessEvaluator1>(nameof(CustomCompletenessEvaluator1));
    _container.RegisterType<CustomCompletenessEvaluator, CustomCompletenessEvaluator2>(nameof(CustomCompletenessEvaluator2));
    ```

### Combine default and custom detail evaluators

To combine both default and custom detail evaluators:

1. Inject both `DefaultCompletenessDetailEvaluator` and `CustomCompletenessDetailEvaluator` arrays (see code above). Then concatenate them. 
1. Pass this array to the protected constructor of the `DefaultCompletenessEvaluator` base class:

    ```csharp
    public class CustomCompletenessEvaluator : DefaultCompletenessEvaluator
    {
        private readonly IItemService _productService;

        public CustomCompletenessEvaluator(DefaultCompletenessDetailEvaluator[] defaultDetailEvaluators, CustomCompletenessDetailEvaluator[] customDetailEvaluators, IItemService productService) :
            base(defaultDetailEvaluators.Concat<ICompletenessDetailEvaluator>(customDetailEvaluators).ToArray(), productService)
        {
        }
    }
    ```

### Mix default and all custom detail evaluators

To mix default and all custom detail evaluators:

1. Create an array of instances of default detail evaluators.
1. Inject `CustomCompletenessDetailEvaluator` arrays (see code above). Then concatenate them.
1. Pass this array to the protected constructor of the `DefaultCompletenessEvaluator` base class:

    ```csharp
    public class CustomCompletenessEvaluator : DefaultCompletenessEvaluator
    {
        private readonly IItemService _productService;
        private readonly IPricingSearchService _pricingSearchService;

        public CustomCompletenessEvaluator(CustomCompletenessDetailEvaluator[] detailEvaluators, IItemService productService, IPricingSearchService pricingSearchService) :
            base(new[] { new PropertiesCompletenessDetailEvaluator(), new PricesCompletenessDetailEvaluator(pricingSearchService) }.Concat<ICompletenessDetailEvaluator>(customDetailEvaluators).ToArray(), productService)
        {
        }
    }
    ```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-dynamic-expression-tree">← Extending dynamic expression tree </a>
    <a href="../extending-application-user">Extending application user  →</a>
</div>