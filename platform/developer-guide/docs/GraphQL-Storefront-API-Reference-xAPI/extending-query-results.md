# Extend Query Results

If you need to extend the result set of a GraphQL query, for example, add `banners` field to `SearchProductResponse`, you can use one of the following options:

* **Multiple queries in one xAPI call**: Submit multiple queries in a single network request using the xAPI. This is useful when the product search and banners retrieval are logically separate but you want to reduce the number of HTTP round-trips.  

* **Extend search result with a new field**: If you prefer to keep everything under the same response schema (especially if the Frontend expects it), extend search result object by adding a new property.

While the first option is easier and quicker to implement, this guide focuses on the more advanced second option.

## Add new field to search result object

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

            AbstractTypeFactory<SearchProductResponse>.OverrideType<SearchProductResponse, SearchProductResponseExtended>(); // register extended reponse via AbstractTypeFactory
            serviceCollection.OverrideQueryType<SearchProductQuery, SearchProductQueryExtended>().WithQueryHandler<SearchProductQueryHandlerExtended>(); // extended query handler
        }
    ```

We can see that new Banners field is available in the GraphQL schema and is returned with the data from the handler:

![Extended query results](media/banners-added.png)

## Consider module dependency

In the example above, two related components (a custom type and an extended query builder) reside within the same module. If you apply this pattern in your project, the module containing the extended query builder should declare a dependency on the module that registers the custom type, both:

* In its **module.manifest** file.
* And in the project’s package (e.g., NuGet) references.

The original module first registers the custom type in the schema, and the dependent module uses this type to extend or override the connection type. If a new module needs to override both the custom type and the extended query builder with its own implementations, it should declare a dependency on the module containing these components. This ensures a proper dependency chain for GraphQL type registration and overrides, avoiding issues with type resolution or loading order.