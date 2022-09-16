#Using Domain Events
As its name soggests, a domain event is something that happened in a particular domain, and something you want other parts of the same domain to be aware of and potentially react to (the in-process principle).

An important benefit of domain events is that any side effects of something happening in a domain can be expressed explicitly and not implicitly. Those side effects must be consistent, i.e. either all operations related to the task happen, or none. In addition, domain events enable a better separation of concerns among classes within the same domain.

## How to Define Domain Events
A domain event is just a simple POCO type that represents an interesting occurence in the domain:

```C#
public class CustomDomainEvent : DomainEvent
{
 public Customer Customer { get; set; }
}
```

## How to Define New Event Handler 
Defining a new event handler works in the following way:

```C#
public class CutomDomainEventHandler : IEventHandler<CustomDomainEvent>
{
  public async Task Handle(CustomDomainEventmessage)
  {
    //Some logic here
  }
}
```

## How to Register Event Handler and Subscribe to Domain Event
To register an event handler or subscribe to a domain event, use the following code:

```C#
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

## How to Raise Domain Events
In your domain entities, when any significant status change happens, you may want to raise your domain events like this:

```
var eventPublisher = _container.Resolve<IEventPublisher>();
eventPublisher.Publish(new CustomDomainEvent()));
```

## How to Override Existing Event Handler with New Derived Type
This option may be also of use in some cases, and it is done this way:

```C#
//Derive a new handler from an overrided handler class
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
