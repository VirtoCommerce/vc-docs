# xAPI Extension Points

The xAPI offers default GraphQL schemas for objects, queries, and mutations. However, as every project has unique requirements, it's impossible to anticipate and include them all in the base schema. Fortunately, the xAPI provides extension points that allow you to modify the baseline behavior and data structures. In this article, we explore the key extension points and techniques available for customizing your projects.

In addition to the extension points that Platform provides, the xAPI project has the following main [extensions points](https://virtocommerce.com/docs/latest/fundamentals/extensibility/overview/). However, there is no opportunity to extend AutoMapper's profiles using `AbstractTypeFactory<>` type.

[![Sample code](media/sample_code.png)](https://github.com/VirtoCommerce/vc-module-experience-api/tree/dev/samples/VirtoCommerce.Exp.ExtensionSamples)

## Extend root GraphQL schema

Within the xAPI, we have the flexibility to choose between the: 

* Schema-first approach.
* Graphtype-first approach. 

We've opted to focus exclusively on the graphtype-first approach, for it:

* Aligns more naturally with .NET development practices.
* Provides access to all the properties of your GraphTypes and Schema. 
* Is better suited for extending the model through type overrides.

To register a new query or mutation:

1. Derive a custom schema type from `ISchemaBuilder`. The `ISchemaBuilder` interface is designed to dynamically add new queries to the root GraphQL schema. Multiple `ISchemaBuilder` instances are used to add the queries to the root schema when the application starts. The example below shows how to define schema types for existing domain types. Here, we create a new GraphQL schema object type, `InventoryType`, for the underlying domain type, `Inventory`, from the inventory module.

2. Define a new type that implements this interface 

    ```csharp title="CustomSchema.cs" linenums="1"
    public class CustomSchema : ISchemaBuilder
        {
            public void Build(ISchema schema)
            {
                var inventoryQueryField = new FieldType
                {
                    Name = "inventory",
                    Arguments = new QueryArguments(
                        new QueryArgument<NonNullGraphType<StringGraphType>> { Name = "id" },
                    ),
                    Type = typeof(InventoryType),
                    Resolver = new  FieldResolver<Inventory>(context =>
                    {
                        return new Inventory { ProductId = "1", FulfillmentCenterId = "center1" };
                    })
                };
                schema.Query.AddField(inventoryQueryField);
            }
        }
    ```

3. Register your custom schema type in the Dependency Injection (DI) container. In your `module.cs` file, initialize and register the custom schema using the `services.AddSchemaBuilder<CustomSchema>()` method:

    ```csharp title="module.cs" linenums="1"
    public class Module : IModule
    {
        public void Initialize(IServiceCollection services)
        {
            //Register custom schema
            services.AddSchemaBuilder<CustomSchema>();
        }
    }
    ```

## Extend existing schema type with new properties

To extend the existing GraphQL type:

1. Create a new schema type that derives from the existing type you want to extend. This allows you to build upon the existing structure:

    ```csharp title="CartType2.cs" linenums="1"
    public class CartType2 : CartType
        {
            public CartType2(ICartAvailMethodsService cartAvailMethods) : base(cartAvailMethods)
            {
                Field<StringGraphType>("myCoolScalarProperty", resolve: context => "my cool value" );
            }
        }
    ```

1. Register your type override using the appropriate syntax in the `module.cs` file. This step is crucial to ensure that your extension is recognized and integrated into the GraphQL schema:

    ```csharp title="module.cs" linenums="1"
    public class Module : IModule
    {
        public void Initialize(IServiceCollection services)
        {
            //GraphQL schema overrides
            services.AddSchemaType<CartType2>().OverrideType<CartType, CartType2>();
        }
    }
    ```

## Extend schema type that contains another complex type

Let’s extend a field of type `InputPersonalDataType` belonging to the `InputUpdatePersonalDataType` schema type with a new `gender` field.

The `InputUpdatePersonalDataType` schema type contains a field of type `InputPersonalDataType`. By extending `InputPersonalDataType`, we indirectly extend `InputUpdatePersonalDataType` as well, as it depends on it.

```csharp
public class InputUpdatePersonalDataType : InputObjectGraphType
{
    public InputUpdatePersonalDataType()
    {
        Name = "InputUpdatePersonalDataType";

        Field<InputPersonalDataType>("personalData");
    }
}

public class InputPersonalDataType : InputObjectGraphType
{
    public InputPersonalDataType()
    {
        Name = "InputPersonalDataType";
        Field<StringGraphType>("firstName");
        Field<StringGraphType>("lastName");
        // ...
    }
}
```

To extend a field of type `InputPersonalDataType`:

1. Create a module using the Virto Commerce template as the base for your extension.

1. Add the new properties or relationships you need to the `Contact` model and `ContactEntity`.

1. Extend the input type in xAPI: Create a new class, for example `InputExtendedPersonalDataType`, that inherits from the existing `InputPersonalDataType` and adds the `gender` field:

    ```csharp
    using GraphQL.Types;

    public class InputExtendedPersonalDataType : InputPersonalDataType
    {
        public InputExtendedPersonalDataType()
        {
            Field<StringGraphType>("gender");
        }
    }
    ```


1. Override the type in **module.cs**: In your module initialization code, replace the original type mapping with your new extended type:


    ```csharp title="module.cs"
    using VirtoCommerce.XapiModule.Core.Infrastructure;
    using GraphQL.Types;

    public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            // Register the extended GraphQL input type
            serviceCollection.AddSchemaType<InputExtendedPersonalDataType>()
                            .OverrideType<InputPersonalDataType, InputExtendedPersonalDataType>();
        }
    }
    ```

The `personalData` field (of type `InputPersonalDataType`) will now include the new `gender` field.


















## Extend query results

If you need to extend the result set of a GraphQL query, for example, add `banners` field to `SearchProductResponse`, you can use one of the following options:

* **Multiple queries in one xAPI call**: Submit multiple queries in a single network request using the xAPI. This is useful when the product search and banners retrieval are logically separate but you want to reduce the number of HTTP round-trips.  

* **Extend search result with a new field**: If you prefer to keep everything under the same response schema (especially if the Frontend expects it), extend search result object by adding a new property.

While the first option is easier and quicker to implement, this guide focuses on the more advanced second option.

### Add new field to search result object

Let’s suppose that our object is mapped to a connection type schema which gives us an opportunity to explore a more complex overriding scenario.

1. Create:
    1. `ProductConnection` extension to use new `banners` field in the schema.
    1. Extended `SearchProductResponse` that contains `banners` property.
    1. `BannersType` and class (as an example of the new business logic class that we need to add in the response):

    ```csharp
    // Extended ConnectionType to use custom field
    public class ProductsConnectionTypeExtended : ProductsConnectionType<ProductType>
    {
        public ProductsConnectionTypeExtended()
        {
            Field<ListGraphType<BannersType>>("banners")
            .Resolve(context =>
            {
                return ((ProductsConnectionExtended)context.Source).Banners;
            });
        }
    }

    // Extended connection class to pass banners to the connection
    public class ProductsConnectionExtended : ProductsConnection<ExpProduct>
    {
        public ProductsConnectionExtended(IEnumerable<ExpProduct> superset, int skip, int take, int totalCount)
            : base(superset, skip, take, totalCount)
        {
        }

        public IList<Banner> Banners { get; set; }
    }

    // Extended SearchProductResponse to include Banners
    public class SearchProductResponseExtended : SearchProductResponse
    {
        public IList<Banner> Banners { get; set; }
    }

    // new business logic class with just one property for brevity 
    public class Banner
    {
        public string Type { get; set; }
    }


    public class BannersType : ObjectGraphType<Banner>
    {
        public BannersType()
        {
            Field(x => x.Type);
        }
    }
    ```

1. Create extended `SearchProductQueryBuilder` to force our new connection to work:

    ```csharp
    // Extend builder class to override connection type 
    public class SearchProductQueryBuilderExtended : SearchProductQueryBuilder
    {
        public SearchProductQueryBuilderExtended(IMediator mediator, IAuthorizationService authorizationService, IStoreService storeService, ICurrencyService currencyService)
            : base(mediator, authorizationService, storeService, currencyService)
        {
        }

        protected override FieldType GetFieldType()
        {
            var builder = ConnectionBuilder.Create<ProductType, EdgeType<ProductType>, ProductsConnectionTypeExtended, object>(Name)
                .PageSize(DefaultPageSize);

            ConfigureArguments(builder.FieldType);

            builder.ResolveAsync(async context =>
            {
                var (query, response) = await Resolve(context);
                return new ProductsConnectionExtended(response.Results, query.Skip, query.Take, response.TotalCount)
                {
                    Facets = response.Facets,
                    Banners = ((SearchProductResponseExtended)response).Banners
                };
            });

            return builder.FieldType;
        }
    }
    ```

    ??? Example "Extended `SearchProductHandler` to populate `Banners` property in the response"

        ```csharp
        // Mock extendable for SearchProductQuery
        public class SearchProductQueryExtended : SearchProductQuery
        {
        }

        public class SearchProductQueryHandlerExtended : SearchProductQueryHandler
        {
            // Override methods if needed to handle extended query logic
            public SearchProductQueryHandlerExtended(ISearchProvider searchProvider, IMapper mapper, IStoreCurrencyResolver storeCurrencyResolver, IStoreService storeService, IGenericPipelineLauncher pipeline, IAggregationConverter aggregationConverter, ISearchPhraseParser phraseParser) : base(searchProvider, mapper, storeCurrencyResolver, storeService, pipeline, aggregationConverter, phraseParser)
            {
            }

            public override async Task<SearchProductResponse> Handle(SearchProductQuery request, CancellationToken cancellationToken)
            {
                var result = await base.Handle(request, cancellationToken);

                // result is of type SearchProductResponseExtended
                if (result is SearchProductResponseExtended extendedResult)
                {
                    // Add banners to the response
                    extendedResult.Banners = new List<Banner>
                    {
                        new Banner { Type = "Sale" },
                        new Banner { Type = "New Arrival" },
                        new Banner { Type = "Limited Edition" },
                    };
                }

                return result;
            }
        }
        ```

1. Register all the overrides in **Module.Initialize**:

    ```csharp
        public void Initialize(IServiceCollection serviceCollection)
        {
            //// Register GraphQL schema
            _ = new GraphQLBuilder(serviceCollection, builder =>
            {
                // extremely important to override connection builder BEFORE registering schemas if using AddSchema to register GraphQL types
                serviceCollection.OverrideSchemaBuilder<SearchProductQueryBuilder, SearchProductQueryBuilderExtended>();
                builder.AddSchema(serviceCollection, typeof(AssemblyMarker));
            });

            AbstractTypeFactory<SearchProductResponse>.OverrideType<SearchProductResponse, SearchProductResponseExtended>(); // register extended response via AbstractTypeFactory
            serviceCollection.OverrideQueryType<SearchProductQuery, SearchProductQueryExtended>().WithQueryHandler<SearchProductQueryHandlerExtended>(); // extended query handler
        }
    ```

We can see that new Banners field is available in the GraphQL schema and is returned with the data from the handler:

![Extended query results](media/banners-added.png)

### Consider module dependency

In the example above, two related components (a custom type and an extended query builder) reside within the same module. If you apply this pattern in your project, the module containing the extended query builder should declare a dependency on the module that registers the custom type, both:

* In its **module.manifest** file.
* And in the project’s package (e.g., NuGet) references.

The original module first registers the custom type in the schema, and the dependent module uses this type to extend or override the connection type. If a new module needs to override both the custom type and the extended query builder with its own implementations, it should declare a dependency on the module containing these components. This ensures a proper dependency chain for GraphQL type registration and overrides, avoiding issues with type resolution or loading order.


## Extend validation logic/ replace validators

In the system, the Platform's abstract type factory is employed to create instances of validators. Consequently, the approach for extending validation logic is similar to other cases, such as extending domain models:

1. Create your custom validator by deriving it from the original one. This allows you to build upon the existing validation logic:

    ```csharp title="CartValidator2.cs" linenums="1"
        public class CartValidator2 : CartValidator
        {
            public CartValidator2()
            {
                // Some additional rules (to the basic) can be provided there
                RuleFor(x => x.CartAggregate.Cart.Id).NotEmpty(); // Just example
            }
        }
    ```

1. Override the original validator type with your custom validator. This step is crucial to inform the factory that CartValidator2 should replace the original validator, ensuring that your custom logic is used:

    ```csharp title="module.cs" linenums="1"
        public class Module : IModule
        {
            public void PostInitialize(IApplicationBuilder appBuilder)
            {
                ...
                // Example: replace cart validator
                AbstractTypeFactory<CartValidator>.OverrideType<CartValidator, CartValidator2>();
                ...
            }
        }
    ```

## Extend generic behavior pipelines

xAPI extension points extend beyond data structure modifications. You can also modify behavior and business logic without altering the original source code.

**Generic behavior pipelines** are primarily designed to break down complex logic into loosely coupled stages (middleware). These middleware stages can be defined in various locations and combined into a single logical pipeline that can be executed in response to specific system events or requests.

![image](media/x-api-extensions-1.png){: width="900"}

You can extend the existing generic pipelines with you custom middlewares or even replace the existing middleware with your custom version.

In the example below, you will replace the existing generic pipeline responsible for enriching the `ProductSearchResult` with pricing and availability data from different sources.

```csharp linenums="1"
 //the generic pipeline that is used  for on-the-fly additional data evaluation (prices, inventories, discounts and taxes) for resulting products
services.AddPipeline<SearchProductResponse>(builder =>
{
    builder.AddMiddleware(typeof(EvalProductsPricesMiddleware));
    builder.AddMiddleware(typeof(EvalProductsDiscountsMiddleware));
    builder.AddMiddleware(typeof(EvalProductsTaxMiddleware));
    builder.AddMiddleware(typeof(EvalProductsInventoryMiddleware));
});
```

1. Define the new middleware:

    ```csharp title="MyCoolMiddleware.cs" linenums="1"
    public class MyCoolMiddleware : IAsyncMiddleware<SearchProductResponse>
    {
        //code skipped for better clarity
    }
    ```

1. Register it for the generic behavior pipeline:

    ```csharp title="module.cs" linenums="1"
    public class Module : IModule
    {
        public void Initialize(IServiceCollection services)
        {
            services.AddPipeline<SearchProductResponse>(builder =>
            {
                    builder.AddMiddleware(typeof(MyCoolMiddleware));
            });
        }
    }
    ```

1. To replace the existing middleware with the new one, use the following syntax:

    ```csharp linenums="1"
    services.AddPipeline<SearchProductResponse>(builder =>
                {
                    builder.ReplaceMiddleware(typeof(EvalProductsTaxMiddleware), typeof(MyCoolMiddleware));
                    //this line replaced the EvalProductsTaxMiddleware with the MyCoolMiddleware for GenericPipeline<SearchProductResponse>
                });
    ```

## Replace command/ query handlers

xAPI is built using the clean architecture based on CQRS and DDD principles, where each command and query has its own handler responsible for processing incoming actions. You can easily override and substitute any existing handler with your implementation, thereby changing the default behavior.

It is just enough to replace the required handler in the DI container with your own implementation:

```csharp linenums="1"
public class Module : IModule
{
    public void Initialize(IServiceCollection services)
    {
        //use such lines to override exists query or command handler
        services.AddTransient<IRequestHandler<GetCartQuery, CartAggregate>, CustomGetCartQueryHandler>();
    }
}
```

To replace an existing command with your implementation:

1. Register and override your input type:

    ```csharp title="module.cs" linenums="1"
    services.AddSchemaType<InputRemoveCartType2>().OverrideType<InputRemoveCartType, InputRemoveCartType2>();
    ```

1. Register your implementations of the command and handler:

    ```csharp title="module.cs" linenums="1"
    services.OverrideCommandType<RemoveCartCommand, RemoveCartCommandExtended>().WithCommandHandler<RemoveCartCommandHandlerExtended>();
    ```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../custom-module-creation">← Creating xAPI module </a>
    <a href="../update-xapi-modules">Updating xAPI modules  →</a>
</div>