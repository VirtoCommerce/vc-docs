# XAPI Modules Update Guide

This guide explains how to update XAPI modules in the Virto Commerce Platform after upgrading GraphQL.NET libraries from v4 to v8. Follow these steps to update references, initialize modules, and handle breaking changes. Be sure to thoroughly test your implementations after making these updates.

## Affected libraries and modules

GraphQL.NET libraries were updated from v4 to v8. The following modules are affected:

- VirtoCommerce.Xapi
- VirtoCommerce.XCatalog
- VirtoCommerce.XCart
- VirtoCommerce.XOrder
- VirtoCommerce.XCMS
- VirtoCommerce.ProfileExperienceApi
- VirtoCommerce.FileExperienceApi
- VirtoCommerce.MarketingExperienceApi
- VirtoCommerce.QuoteModule
- VirtoCommerce.PushMessages
- VirtoCommerce.TaskManagement
- VirtoCommerce.Skyflow
- VirtoCommerce.Contracts
- VirtoCommerce.CustomerReviews
- VirtoCommerce.Recommendations
- VirtoCommerce.WhiteLabeling

Use the PowerShell script below to update references in your projects.

### PowerShell script for updating xAPI module references

This PowerShell script automates the process of updating XAPI module references in `.csproj` files to specific new versions. Run this script before applying the code-level changes described in this guide. 

The script scans all `.csproj` files in the solution directory, identifies package references for specified XAPI modules, and updates them to the desired versions as defined in a hashtable.

#### Prerequisites
* Run the script in the root directory of the solution.  
* Have the necessary permissions to modify `.csproj` files.  

#### Script

```powershell
# Define the hashtable with package partial names and new versions
$hash = @{
    'VirtoCommerce.Xapi' = '3.800.0'
    'VirtoCommerce.XCatalog' = '3.800.0'
    'VirtoCommerce.XCore' = '3.800.0'
    'VirtoCommerce.XCart' = '3.800.0'
    'VirtoCommerce.XOrder' = '3.800.0'
    'VirtoCommerce.XCMS' = '3.800.0'
    'VirtoCommerce.ProfileExperienceApi' = '3.800.0'
    'VirtoCommerce.FileExperienceApi' = '3.800.0'
    'VirtoCommerce.MarketingExperienceApi' = '3.800.0'
    'VirtoCommerce.QuoteModule' = '3.800.0'
    'VirtoCommerce.PushMessages' = '3.800.0'
    'VirtoCommerce.TaskManagement' = '3.800.0'
    'VirtoCommerce.Skyflow' = '3.800.0'
    'VirtoCommerce.Contracts' = '3.800.0'
    'VirtoCommerce.CustomerReviews' = '3.800.0'
    'VirtoCommerce.WhiteLabeling' = '3.800.0'
    'VirtoCommerce.Recommendations' = '3.800.0'
}

# Get all .csproj files in the solution root directory and subdirectories
$solutionRoot = Get-Location
$csprojFiles = Get-ChildItem -Path $solutionRoot -Recurse -Filter "*.csproj"

foreach ($csprojPath in $csprojFiles) {
    Write-Host "Processing file: $csprojPath"

    # Load the .csproj file into an XML document
    [xml]$csprojXml = Get-Content -Path $csprojPath.FullName

    # Namespace manager to handle XML namespaces (if any)
    $namespaceManager = New-Object System.Xml.XmlNamespaceManager($csprojXml.NameTable)
    $namespaceManager.AddNamespace("ns", $csprojXml.Project.NamespaceURI)

    # Iterate through each package in the hashtable
    foreach ($partialName in $hash.Keys) {
        $newVersion = $hash[$partialName]

        # Find PackageReference elements that match the partial name
        $packageReferences = $csprojXml.SelectNodes("//ns:PackageReference[contains(@Include, '$partialName')]", $namespaceManager)

        foreach ($packageReference in $packageReferences) {
            # Update the Version attribute
            $packageReference.Version = $newVersion
            Write-Host "Updated $($packageReference.Include) to version $newVersion in file $csprojPath"
        }
    }

    # Save the modified XML back to the .csproj file
    $csprojXml.Save($csprojPath.FullName)
    Write-Host "Updated .csproj file saved at $csprojPath"
}
```

#### Execution steps  

1. Copy the script to a `.ps1` file (e.g., `UpdateXapiModules.ps1`).  
1. Open PowerShell in the root directory of your solution.  
1. Execute the script:  
   ```powershell
   ./UpdateXapiModules.ps1
   ```  
1. Verify that `.csproj` files were updated successfully by checking the updated versions in `PackageReference` entries.  


Now you can proceed with the code-level updates described.

## Initialization changes

### Single xAPI project example

```c#
// old
var assemblyMarker = typeof(AssemblyMarker);
var graphQlBuilder = new CustomGraphQLBuilder(serviceCollection);
graphQlBuilder.AddGraphTypes(assemblyMarker);
serviceCollection.AddMediatR(assemblyMarker);
serviceCollection.AddAutoMapper(assemblyMarker);
serviceCollection.AddSchemaBuilders(assemblyMarker);

// new
var graphQlBuilder = new GraphQLBuilder(serviceCollection, builder =>
{
    builder.AddSchema(serviceCollection, typeof(AssemblyMarker));
});
```

### Core/Data XAPI project example

```c#
// old
var graphQlBuilder = new CustomGraphQLBuilder(serviceCollection);
graphQLBuilder.AddSchema(typeof(CoreAssemblyMarker), typeof(DataAssemblyMarker));

// new
var graphQlBuilder = new GraphQLBuilder(serviceCollection, builder =>
{
    builder.AddSchema(serviceCollection, typeof(CoreAssemblyMarker), typeof(DataAssemblyMarker));
});
```

!!! note
    The new `AddSchema` method will register GraphTypes, MediatR, AutoMapper, and Schema Builders.

## Breaking changes

* `GraphTypeExtenstionHelper` was changed to `GraphTypeExtensionHelper`. 
* The namespace `VirtoCommerce.XDigitalCatalog.Queries` was changed to `VirtoCommerce.XCatalog.Core.Queries`.
* The async resolver `AsyncFieldResolver` was replaced with `FuncFieldResolver`. Example:

    ```c#
    // old
    Resolver = new AsyncFieldResolver<object>(async context =>
    {
        var result = await _mediator.Send(new GetCountriesQuery());
        return result.Countries;
    })

    // new
    Resolver = new FuncFieldResolver<object>(async context =>
    {
        var result = await _mediator.Send(new GetCountriesQuery());
        return result.Countries;
    })
    ```

* The method `GraphTypeExtensionHelper.CreateConnection` now takes the name as the first parameter. `ConnectionType.Name` extension method is obsolete. Example:

    ```c#
    // old
    var listConnectionBuilder = GraphTypeExtenstionHelper.CreateConnection<WishlistType, object>()
        .Name("wishlists");

    // new
    var listConnectionBuilder = GraphTypeExtensionHelper.CreateConnection<WishlistType, object>("wishlists");
    ```

* The `FieldBuilder.Create` method now takes the name as the first parameter. `FieldType.Name` extension method is obsolete. Example:

    ```c#
    // old
    FieldBuilder.Create<CartAggregate, CartAggregate>(GraphTypeExtenstionHelper.GetActualType<CartType>())
        .Name("addItem");

    // new
    FieldBuilder<CartAggregate, CartAggregate>.Create("addItem", GraphTypeExtensionHelper.GetActualType<CartType>());
    ```

* The `EventStreamFieldType` was replaced with `FieldType`, and `IResolveEventStreamContext` was removed. Example:

    ```c#
    // old
    _ = new EventStreamFieldType
    {
        Name = "ping",
        Type = typeof(StringGraphType),
        Resolver = new FuncFieldResolver<string>(Resolve),
        AsyncSubscriber = new AsyncEventStreamResolver<string>(Subscribe),
    };

    private async Task<IObservable<string>> Subscribe(IResolveEventStreamContext context) { //...

    // new
    _ = new FieldType
    {
        Name = "ping",
        Type = typeof(StringGraphType),
        Resolver = new FuncFieldResolver<string>(Resolve),
        StreamResolver = new SourceStreamResolver<string>(Subscribe),
    };

    private async ValueTask<IObservable<string>> Subscribe(IResolveFieldContext context) { //...
    ```

## Obsolete warnings

* `Field` methods that take a resolver or description as parameters are now marked as obsolete. Use extension methods instead. Example:

    ```c#
    // old
    Field<IntGraphType>("addressType",
        description: "Address type",
        resolve: context => (int)context.Source.AddressType);

    // new
    Field<IntGraphType>("addressType")
        .Description("Address type")
        .Resolve(context => (int)context.Source.AddressType);
    ```

* The `FieldAsync` method was removed. Use the `ResolveAsync` extension method. Example:

    ```c#
    // old
    FieldAsync<StringGraphType>("outline", resolve: async context =>
    {
        var response = await mediator.Send(loadRelatedCatalogOutlineQuery);
        return response.Outline;
    });

    // new
    Field<StringGraphType>("outline")
        .ResolveAsync(async context =>
        {
            var response = await mediator.Send(loadRelatedCatalogOutlineQuery);
            return response.Outline;
        });
    ```

* Make sure `ExtendableField` methods do not accidentally call async functions without async/await. Example:

    ```c#
    // compiles but will raise an exception at runtime
    ExtendableField<NonNullGraphType<ListGraphType<NonNullGraphType<DynamicPropertyValueType>>>>(
        "dynamicProperties",
        context => dynamicPropertyResolverService.LoadDynamicPropertyValues(context.Source, context.GetCultureName()));

    // correct declaration
    ExtendableFieldAsync<NonNullGraphType<ListGraphType<NonNullGraphType<DynamicPropertyValueType>>>>(
        "dynamicProperties",
        async context => await dynamicPropertyResolverService.LoadDynamicPropertyValues(context.Source, context.GetCultureName()));
    ```

## Settings updates

Some settings were moved to their corresponding X-modules and made public:

* `VirtoCommerce.Xapi.Core.ModuleConstants.Settings.General.IsSelectedForCheckout` —> `VirtoCommerce.XCart.Core.ModuleConstants.Settings.General.IsSelectedForCheckout`
* `VirtoCommerce.Xapi.Core.ModuleConstants.Settings.General.CreateAnonymousOrder` —> `VirtoCommerce.XOrder.Core.ModuleConstants.Settings.General.CreateAnonymousOrder`

## Deprecated fields and mutations

Deprecated fields and mutations were removed to reduce redundancy and ensure schema clarity. Use the suggested alternatives:

### Fields:

- `DynamicPropertyType.valueType` —> Use `dynamicPropertyValueType` instead
- `InputDynamicPropertyValueType.locale` —> Use `cultureName` field
- `QuoteAttachmentType.mimeType` —> Use `contentType` field
- `PriceType.validFrom` —> Use `startDate` field
- `PriceType.validUntil` —> Use `endDate` field
- `PropertyType.type` —> Use `propertyType` field
- `PropertyType.valueType` —> Use `propertyValueType` field
- `PropertyType.propertyDictItems` —> Use `propertyDictionaryItems` field

### Mutations:

- `renameWishlist` —> Use `changeWishlist` mutation
- `processOrderPayment` —> Use `initializePayment` mutation
