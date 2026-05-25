# Create Custom xAPI Module

This guide describes how to create a **custom xAPI module** in Virto Commerce. xAPI modules extend the GraphQL-based Storefront API by introducing new types, queries, and mutations while following the platform’s modular architecture and conventions.

The guide focuses on a **basic but production-aligned setup** and assumes familiarity with:

* .NET SDK
* C# and ASP.NET Core
* GraphQL concepts
* Virto Commerce Platform fundamentals

## Install module template

Virto Commerce provides official .NET templates that scaffold modules with the recommended structure.

1. Open a command-line interface and navigate to your source directory.
1. Install (or update) the module templates:

    ```
    dotnet new install VirtoCommerce.Module.Template
    ```

Now, you can use one of the following templates:

{%
   include-markdown "../Tutorials-and-How-tos/Tutorials/module-templates-for-dotnet-new.md"
   start="<!--templates-start-->"
   end="<!--templates-end-->"
%}


## Generate module structure

Create a new xAPI module using the provided template.

```
dotnet new vc-module-xapi --ModuleName XYourModule --Author "Your Name" --CompanyName YourCompany
```

This command generates a solution with the following structure:

```
XYourModule/
├── src/
│   └── XYourModule.Web/
│       ├── Module.cs
│       ├── Schemas/
│       ├── Queries/
│       ├── Commands/
│       ├── Types/
│       └── Services/
├── tests/
└── module.manifest
```

Open the solution in Visual Studio and ensure it builds successfully.


## Register GraphQL schema

In Virto Commerce modules, GraphQL schemas and components are registered during the module lifecycle. Each module defines its lifecycle in **module.cs**:

* **Initialize**: Register services, repositories, and dependencies.
* **PostInitialize**: Register GraphQL schemas and extend xAPI components. This ensures your types, queries, and mutations participate in the platform’s modular schema composition.

```csharp title="module.cs"
public class Module : IModule
{
    public void Initialize(IServiceCollection services)
    {
        // Register application services
        services.AddTransient<IYourService, YourService>();

        // Register CQRS handlers using MediatR
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(typeof(Module).Assembly));
    }

    public void PostInitialize(IApplicationBuilder appBuilder)
    {
        // Register GraphQL schema builder for this module
        _ = new GraphQLBuilder(appBuilder.ApplicationServices, builder =>
        {
            builder.AddSchema(appBuilder.ApplicationServices, typeof(YourModuleAssemblyMarker));
        });
    }
}
```

## Define and register GraphQL types

GraphQL types map your domain models to the GraphQL schema. Follow these steps:

1. Create a GraphQL type class for your domain model:

    ```csharp
    public class YourCustomType : ExtendableGraphType<YourModel>
    {
        public YourCustomType(IMediator mediator)
        {
            Name = "YourCustomType";
            Description = "Represents a custom domain object.";

            Field(x => x.Id).Description("Unique identifier.");
            Field(x => x.Name, nullable: true).Description("Display name.");
            Field(x => x.CreatedDate, nullable: true)
                .Description("Creation date.");
        }
    }
    ```

1. Register the GraphQL type in the DI container, typically in `Module.Initialize`:

    ```csharp
    services.AddSchemaType<YourCustomType>();
    ```

1. Verify your type is included in your module’s schema by running the GraphQL playground and checking that `YourCustomType` is available for queries or mutations.


## Implement queries and mutations

Virto Commerce xAPI modules follow the **CQRS pattern** using MediatR. Follow these steps to implement your own queries and mutations:


1. Create a query:
    1. In your module project, create a new file in the `Queries/` folder, e.g., `GetYourModelQuery.cs`.
    1. Define the query class that represents the request:

        ```csharp
        public class GetYourModelQuery : IRequest<YourModel>
        {
            public string Id { get; set; }
        }
        ```

1. Create a query handler:
    1. In the same `Queries/` folder, create a handler class, e.g., `GetYourModelQueryHandler.cs`.
    1. Implement `IRequestHandler<TRequest, TResponse>` to handle the query:

        ```csharp
        public class GetYourModelQueryHandler
            : IRequestHandler<GetYourModelQuery, YourModel>
        {
            private readonly IYourService _service;

            public GetYourModelQueryHandler(IYourService service)
            {
                _service = service;
            }

            public async Task<YourModel> Handle(
                GetYourModelQuery request,
                CancellationToken cancellationToken)
            {
                return await _service.GetByIdAsync(request.Id);
            }
        }
        ```

1. Create a mutation (command):
    1. In the `Commands/` folder, create a file `UpdateYourModelCommand.cs`.
    1. Define the command class:

        ```csharp
        public class UpdateYourModelCommand : IRequest<YourModel>
        {
            public string Id { get; set; }
            public string Name { get; set; }
        }
        ```

1. Define the GraphQL input type:
    1. In the `Types/` folder, create a new file `UpdateYourModelInputType.cs`.
    1. Map the command properties to a GraphQL input type:

        ```csharp
        public class UpdateYourModelInputType
            : InputObjectGraphType<UpdateYourModelCommand>
        {
            public UpdateYourModelInputType()
            {
                Name = "UpdateYourModelInput";
                Field(x => x.Id);
                Field(x => x.Name, nullable: true);
            }
        }
        ```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../getting-started">← Setting up environment </a>
    <a href="../x-api-extensions">Extending xAPI module  →</a>
</div>