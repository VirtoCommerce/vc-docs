# Extending cart query with custom parameter


To extend cart queries and incorporate a custom parameter, such as a contract ID:



1. Override the existing cart query type with the extended version and specify a custom query handler:

    ```csharp
    services.OverrideQueryType<GetCartQuery, GetCartQueryExtended>().WithQueryHandler<CustomGetCartQueryHandler>();
    ```

1. Override the `ShoppingCartSearchCriteria` type to include the extended version:

    ```csharp
    AbstractTypeFactory<ShoppingCartSearchCriteria>.OverrideType<ShoppingCartSearchCriteria, ShoppingCartSearchCriteriaExtended>();
    ```

1. Create an extended version of the `GetCartQuery`, introducing the `ContractId` parameter:

    ```csharp
    public class GetCartQueryExtended : GetCartQuery
    {
        public string ContractId { get; set; }

        public override IEnumerable<QueryArgument> GetArguments()
        {
            foreach (var argument in base.GetArguments())
            {
                yield return argument;
            }

            yield return Argument<StringGraphType>(nameof(ContractId));
        }

        public override void Map(IResolveFieldContext context)
        {
            base.Map(context);

            ContractId = context.GetArgument<string>(nameof(ContractId));
        }
    }
    ```


1. Implement a custom query handler to handle the extended `GetCartQuery`:

    ```csharp
    public class CustomGetCartQueryHandler : GetCartQueryHandler
    {
        public CustomGetCartQueryHandler(ICartAggregateRepository cartAggregateRepository,
            ICartResponseGroupParser cartResponseGroupParser)
            : base(cartAggregateRepository, cartResponseGroupParser)
        {
        }

        // Override the method to include the custom ContractId parameter in the search criteria.
        protected override ShoppingCartSearchCriteria GetCartSearchCriteria(GetCartQuery request)
        {
            var requestExtended = (GetCartQueryExtended)request;
            var criteriaExtended = (ShoppingCartSearchCriteriaExtended)base.GetCartSearchCriteria(request);

            criteriaExtended.ContractId = requestExtended.ContractId;

            return criteriaExtended;
        }
    }
    ```

This implementation extends the original `GetCartQuery` by introducing a `GetCartQueryExtended` class that includes the additional `ContractId` parameter. The custom query handler, `CustomGetCartQueryHandler`, is responsible for handling this extended query and updating the search criteria accordingly.