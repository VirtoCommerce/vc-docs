# Extend Specific Schema Type

Virto Commerce GraphQL schema types can be extended with additional fields. For example, let’s extend a field of type `InputPersonalDataType` belonging to the `InputUpdatePersonalDataType` schema type with a new `gender` field.

The `InputUpdatePersonalDataType` schema type contains a field of type `InputPersonalDataType`. By extending `InputPersonalDataType`, we indirectly extend `InputUpdatePersonalDataType` as well, as it depends on it.

```csharp title="Example from xAPI"
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