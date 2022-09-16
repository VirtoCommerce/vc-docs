# Extending Domain Models
VirtoCommerce supports extension of managed code domain types. This article will show you how to use various techniques to extend an existing domain type without direct code modification.

To view or download our sample code, click [here](https://github.com/VirtoCommerce/vc-module-order/tree/dev/samples/VirtoCommerce.OrdersModule2.Web).

## Extending through Type Inheritance

Common domain classes have a fixed structure and are defined in modules. This means you cannot simply add any additional properties to the existing domain types without direct code modification. In order  to fix this, you can extend an entity class and add properties to the subclass.

Let’s see how the domain model extension works by extending the `CustomerOrder` type defined in the **Order Module**, with new properties.

!!! warning
	This approach does not work when a single domain entity type is to be extended from multiple modules. The extension domain model is based on class inheritance. Meanwhile, .NET does not support multiple class inheritance, so, as a result, only the last registered extension wins.

Our first step is to define a new subclass, `CustomerOrder2`, derived from the original `CustomerOrder` class.

`VirtoCommerce.OrdersModule2.Web/Model/CustomerOrder2.cs`
```C#
    public class CustomerOrder2 : CustomerOrder
    {
        public CustomerOrder2()
        {
            Invoices = new List<Invoice>();
        }
        public string NewField { get; set; }
        public ICollection<Invoice> Invoices { get; set; }
    }
```

Now, we need to register the newly defined `CustomerOrder2` type in `AbstractFactory<>` to tell the system that `CustomerOrder2` is now overriding (replacing) the original `CustomerOrder` class and will be used everywhere instead of it.

`VirtoCommerce.OrdersModule2.Web/Module.cs`
```C#
    public class Module : IModule
    {
        public void PostInitialize(IApplicationBuilder appBuilder)
        {
            ...
             AbstractTypeFactory<CustomerOrder>.OverrideType<CustomerOrder, CustomerOrder2>()
                                            .WithFactory(() => new CustomerOrder2 { OperationType = "CustomerOrder" }); //need to preserve original order  discriminator value
            ...
        }
    }
```

!!! info
	`AbstractTypeFactory<>` is the key element of Virto's **extension concept** that is responsible for activating a particular type of instance based on the internal type mapping table.

Each piece of code that should support domain type extensions must use `AbstractTypeFactory<BaseType>.TryCreateInstance()` instead of the `new BaseType()` statement.

When you need to override any base type with another derived type, you must call   `AbstractTypeFactory<BaseType>.OverrideType<BaseType, DerivedType>()`; each  call of  `AbstractTypeFactory< BaseType>.TryCreateInstance()` will return your `DerivedType` object instance instead of `BaseType`.

This is how the type extension magic works.

## Persistent Layer Extension Schema

We just extended the existing `CustomerOrder` class with a new `CustomerOrder2` class housing new  properties. The questions now is: how can you actually change the current DB schema and persist these new types into the database through Entity Framework (EF) Core? To solve this task, we can also use the inheritance techniques and define and derive new `Order2DbContext` from original `OrderDbContext`, along with `OrderRepository2` derived from `OrderRepository`.

`VirtoCommerce.OrdersModule2.Web/Repositories/Order2DbContext.cs`
```C#
    //Derive custom DB context from the OrderDbContext
    public class Order2DbContext : OrderDbContext
    {
         public Order2DbContext(DbContextOptions<Order2DbContext> builderOptions) : base(builderOptions)
        {
        }
         protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            //the method code
        }
    }
```

`VirtoCommerce.OrdersModule2.Web/Repositories/OrderRepository2.cs`
```C#
 public class OrderRepository2 : OrderRepository
    {
        public OrderRepository2(Order2DbContext dbContext, IUnitOfWork unitOfWork = null) : base(dbContext, unitOfWork)
        {
        }
    }
```

In Virto, for persistence logic we use the **[Data Mapper](https://www.martinfowler.com/eaaCatalog/dataMapper.html)** pattern, which helps to completely isolate your domain from the persistence layer. Leveraging this pattern gives one more benefits with keeping domain contracts in a more stable state. It also enables changing the persistence schema without affecting the domain used for public contracts.

Each domain type has its own representation in the database, namely dedicated `DataEntitity` classes that are defined in EF Core's `DbContext` through fluent syntax.Such classes have three methods:

+ `ToModel` and `FromModel`, which map domain type objects to persistent ones, and vice versa;
+ `Patch`, which applies changes to the specified columns only. This method is crucial for implementing partial update logic.

Now let’s define the new persistence `CustomerOrder2Entity` type that will represent the persistence schema model of the new `CustomerOrder2` class:

`VirtoCommerce.OrdersModule2.Web/Model/CustomerOrder2Entity.cs`
```C#
    public class CustomerOrder2Entity : CustomerOrderEntity
    {
        public override OrderOperation ToModel(OrderOperation operation)
        {
           //the method code
        }
        public override OperationEntity FromModel(OrderOperation operation, PrimaryKeyResolvingMap pkMap)
        {
           //the method code
        }
    }

```

At the next stage, we need to generate new DB migration for our newly extended `Order2DbContext`. We can do that by running the following command within the *Nuget* package version console in *Visual Studio*:

```Console 
Add-Migration InitialOrder2 -Context VirtoCommerce.OrdersModule2.Web.Repositories. Order2DbContext   -Verbose -OutputDir Migrations -Project VirtoCommerce.OrdersModule2.Web -StartupProject VirtoCommerce.OrdersModule2.Web -Debug
```

Running this command will yield the `Migrations/XXXXXX_InitialOrder2.cs` file containing the original (extendable) order module DB schema along with a new one. Thus, you will have to manually edit the resulting `InitialOrder2.cs` file leaving only those DB schema changes that are relevant to your extension. 

`VirtoCommerce.OrdersModule2.Web/Migrations/20200324130250_InitialOrders2.cs`
```C#
    public partial class InitialOrders2 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
           //the method code
        }
    }
```

!!! tip
	To avoid editing the resulting migration file, which may be time consuming and tricky, we recommend you first creating an empty initial migration file for the derived `DbContext` class with no changes. Then, you can just clean up the resulting  migration `.cs` file and leave the *Up* and *Down* methods empty. This will allow you to make changes to the custom 'derived' `DbContext` and generate a new migration file containing only your custom changes.

Finally, the last step is to register our derived `OrderRepository2` and `Order2DbContext` in a DI container. By registering the new `OrderRepository2` in DI, we override the base `OrderRepository` defined in `CustomerOrder.Module`:

`VirtoCommerce.OrdersModule2.Web/Module.cs`
```C#
    public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            var snapshot = serviceCollection.BuildServiceProvider();
            var configuration = snapshot.GetService<IConfiguration>();
            serviceCollection.AddDbContext<Order2DbContext>(options => options.UseSqlServer(configuration.GetConnectionString("VirtoCommerce")));
            serviceCollection.AddTransient<IOrderRepository, OrderRepository2>();

        }
    }
```

It is also important to register our new persistent schema representation, `CustomerOrder2Entity`, in `AbstractTypeFactory<>` and override the base `CustomerOrderEntity` with new type:

`VirtoCommerce.OrdersModule2.Web/Module.cs`
```C#
    public class Module : IModule
    {
        public void PostInitialize(IApplicationBuilder appBuilder)
        {
            ...

            AbstractTypeFactory<IOperation>.OverrideType<CustomerOrder, CustomerOrder2>();
            AbstractTypeFactory<CustomerOrderEntity>.OverrideType<CustomerOrderEntity, CustomerOrder2Entity>();

            ...
        }
    }
```

## How API Understands and Deserializes Derived Domain Types 

Up to now, we talked about extending domain types and persistent layers. In some cases, however, this is not enough. This is especially true when your domain types are used as DTOs (Data Transfer Objects) in public API contracts and can be leveraged as a result or parameter in the API endpoints. 

Basically, you may need to instantiate the right instance of an 'efficient' type from the incoming JSON data, which is called deserialization.

There are two ways to force ASP.NET Core API JSON serializer to understand our domain extensions:

1. Use platform-defined `PolymorphJsonConverter`, which is preferable in most cases. `PolymorphJsonConverter` transparently deserializes extended domain types with no developer effort.

2. Transfer custom JSON converter to `MvcNewtonsoftJsonOptions`. Consider using it only in case `PolymorphJsonConverter` is not suitable for your specific case.
