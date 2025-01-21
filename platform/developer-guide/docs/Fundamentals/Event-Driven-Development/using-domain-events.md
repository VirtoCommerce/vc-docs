# Using Domain Events

A domain event is something that happened in a particular domain, and something you want other parts of the same domain to be aware of and potentially react to (the in-process principle).

An important benefit of domain events is that any side effects of something happening in a domain can be expressed explicitly and not implicitly. Those side effects must be consistent, i.e. either all operations related to the task happen, or none. In addition, domain events enable a better separation of concerns among classes within the same domain.

## Define domain events

A domain event is just a simple POCO type that represents an interesting occurrence in the domain:

```csharp
public class CustomDomainEvent : DomainEvent
{
 public Customer Customer { get; set; }
}
```

## Define new event handler 

Define a new event handler as follows:

```csharp
public class CutomDomainEventHandler : IEventHandler<CustomDomainEvent>
{
  public async Task Handle(CustomDomainEventmessage)
  {
    //Some logic here
  }
}
```

## Register event handler and subscribe to domain event

Register an event handler or subscribe to a domain event as follows:

```csharp
void  Initialize(IServiceCollection serviceCollection)
{
  ...
   serviceCollection.AddTransient<CustomDomainEventHandler>();
  ...
}

void PostInitialize(IApplicationBuilder appBuilder)
{
  ...
var eventHandlerRegistrar = appBuilder.ApplicationServices.GetService<IHandlerRegistrar>();
eventHandlerRegistrar.RegisterHandler<CustomDomainEvent>((message, token) => appBuilder.ApplicationServices.GetService<CustomDomainEventHandler>().Handle(message));
  ...
}
```

## Raise domain events

In your domain entities, when any significant status change happens, you can raise your domain events as follows:

```
var eventPublisher = _container.Resolve<IEventPublisher>();
eventPublisher.Publish(new CustomDomainEvent()));
```

## Override existing event handler with new derived type

This might be a useful option in some cases:

```csharp
//Derive a new handler from an overridden handler class
public class CustomDomainEventHandler2 : CustomDomainEventHandler
{ .... }
//Override in DI container
void Initialize(IServiceCollection serviceCollection)
{
  ...
   serviceCollection.AddTransient<CustomDomainEventHandler, CustomDomainEventHandler2>();
  ...
}
```
