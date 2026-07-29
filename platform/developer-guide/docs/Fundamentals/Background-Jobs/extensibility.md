# Extensibility

Jobs are defined against `VirtoCommerce.Platform.Core` contracts and resolved from dependency injection, so a partner extends them from their own module without forking the Platform.

## Extend payload

Subclass the platform payload and register the override through `AbstractTypeFactory`. The enqueue call carries the extended instance through unchanged:

```csharp
public class CustomSendOrderEmailPayload : SendOrderEmailPayload
{
    public string Locale { get; set; }
}

AbstractTypeFactory<SendOrderEmailPayload>
    .OverrideType<SendOrderEmailPayload, CustomSendOrderEmailPayload>();
```

## Replace handler

Register your own `IBackgroundJobHandler<TPayload>` for the same payload. The last registration wins, so your handler overrides the platform default.

## Multiple handlers for one payload

Register several handlers for the same payload and enqueue the one you need:

```csharp
services.AddBackgroundJob<SendOrderEmailJob>();
services.AddBackgroundJob<ArchiveOrderJob>();

await jobs.Enqueue<SendOrderEmailJob>(payload);
await jobs.Enqueue<ArchiveOrderJob>(payload);
```

## Custom engine

A custom engine ships as its own module that depends on Background Jobs and implements `IJobEngine` plus a consumer that calls the shared `IJobDispatcher`. Reuse the provided dispatch, serialization, progress, and recurring-job services rather than reimplementing them. Run the `VirtoCommerce.BackgroundJobs.Conformance` test base against your engine to certify it.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../map-reduce">← Map and Reduce</a>
    <a href="../configuration">Configuration →</a>
</div>
