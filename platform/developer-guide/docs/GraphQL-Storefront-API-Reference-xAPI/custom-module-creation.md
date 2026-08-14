# Create Custom xAPI Module

An **xAPI module** extends the GraphQL Storefront API with new types, queries, and mutations. This page covers only the parts that are specific to xAPI. For everything generic to a Virto Commerce module, the project layout, dependency injection, the module manifest, building, and installing, start with the general guides:

![Readmore](media/readmore.png){: width="25"} [Creating a custom module from a template](../Tutorials-and-How-tos/Tutorials/creating-custom-module.md)

![Readmore](media/readmore.png){: width="25"} [Module templates for dotnet new](../Tutorials-and-How-tos/Tutorials/module-templates-for-dotnet-new.md)

![Readmore](media/readmore.png){: width="25"} [Creating a module from scratch](../Tutorials-and-How-tos/Tutorials/create-new-module-from-scratch.md)

## Scaffold xAPI module

Scaffold with the **vc-module-xapi** template, or **vc-module-dba-xapi** if the module also needs its own database. Install the templates and run `dotnet new` as described in [Module templates for dotnet new](../Tutorials-and-How-tos/Tutorials/module-templates-for-dotnet-new.md). The xAPI command is:

```powershell
dotnet new vc-module-xapi --ModuleName XYourModule --Author "Your Name" --CompanyName YourCompany
```

The template generates a module whose xAPI code lives in the **{Module}.Data** project. The relevant folders, empty and ready for you to fill in, are `Queries`, `Commands`, `Schemas`, `Aggregates`, and `Services`, alongside `XapiAssemblyMarker.cs`. The schema is wired up in the **{Module}.Web** project's **Module.cs**.

## Register schema

The template already wires the module's schema in **Module.cs**, keyed off the module's `XapiAssemblyMarker`. You rarely change this, but it explains how your components are discovered.

```csharp title="Module.cs"
public void Initialize(IServiceCollection serviceCollection)
{
    // ... register your services ...

    _ = new GraphQLBuilder(serviceCollection, builder =>
    {
        builder.AddSchema(serviceCollection, typeof(XapiAssemblyMarker));
    });
    serviceCollection.AddSingleton<ScopedSchemaFactory<XapiAssemblyMarker>>();
}

public void PostInitialize(IApplicationBuilder appBuilder)
{
    appBuilder.UseScopedSchema<XapiAssemblyMarker>("XYourModule");
}
```

Every query, mutation, and GraphQL type in the module is discovered through `XapiAssemblyMarker`, so you do not register them one by one. `GraphQLBuilder` comes from `GraphQL.MicrosoftDI`; `ScopedSchemaFactory` and `UseScopedSchema` come from `VirtoCommerce.Xapi.Core`.

## Add query

A query is made of four pieces, all placed in the **{Module}.Data** project.

1. The **request** derives from `Query<TResponse>` and declares its GraphQL arguments:

    ```csharp title="Queries/GetYourModelQuery.cs"
    public class GetYourModelQuery : Query<YourModelResponse>
    {
        public string Id { get; private set; }

        public override IEnumerable<QueryArgument> GetArguments()
        {
            yield return new QueryArgument<NonNullGraphType<StringGraphType>> { Name = "id" };
        }

        public override void Map(IResolveFieldContext context)
        {
            Id = context.GetArgument<string>("id");
        }
    }
    ```

1. The **handler** implements `IQueryHandler<TQuery, TResponse>`:

    ```csharp title="Queries/GetYourModelQueryHandler.cs"
    public class GetYourModelQueryHandler : IQueryHandler<GetYourModelQuery, YourModelResponse>
    {
        private readonly IYourService _service;

        public GetYourModelQueryHandler(IYourService service) => _service = service;

        public async Task<YourModelResponse> Handle(GetYourModelQuery request, CancellationToken cancellationToken)
        {
            var model = await _service.GetByIdAsync(request.Id);
            return new YourModelResponse { Model = model };
        }
    }
    ```

1. The **GraphQL type** derives from `ExtendableGraphType<TResponse>`:

    ```csharp title="Schemas/YourModelType.cs"
    public class YourModelType : ExtendableGraphType<YourModelResponse>
    {
        public YourModelType()
        {
            Field<NonNullGraphType<StringGraphType>>("id").Resolve(context => context.Source.Model.Id);
            Field<StringGraphType>("name").Resolve(context => context.Source.Model.Name);
        }
    }
    ```

1. The **builder** derives from `QueryBuilder<TQuery, TResponse, TResponseType>` and names the GraphQL field. The base builder dispatches the request through MediatR and runs authorization:

    ```csharp title="Queries/GetYourModelQueryBuilder.cs"
    public class GetYourModelQueryBuilder : QueryBuilder<GetYourModelQuery, YourModelResponse, YourModelType>
    {
        public GetYourModelQueryBuilder(IMediator mediator, IAuthorizationService authorizationService)
            : base(mediator, authorizationService)
        {
        }

        protected override string Name => "yourModel";
    }
    ```

## Add mutation

A mutation follows the same shape, using the command base types:

* The **command** implements `ICommand<TResult>` and carries the input fields.
* The **input type** derives from `InputObjectGraphType<TCommand>`.
* The **handler** implements `IRequestHandler<TCommand, TResult>` (MediatR).
* The **builder** derives from `CommandBuilder<TCommand, TResult, TInputType, TResultGraphType>` and overrides `Name` with the mutation field name.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../x-api-extensions">← Extending xAPI module </a>
    <a href="../update-xapi-modules">Updating xAPI modules →</a>
</div>