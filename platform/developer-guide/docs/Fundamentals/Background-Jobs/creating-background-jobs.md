# Create Background Jobs

A background job is a serializable payload plus a handler that processes it. This page shows how to define, register, enqueue, and report progress from a job.

## Define and enqueue job

To create a fire-and-forget job:

1. Define the payload, a serializable class extendable through `AbstractTypeFactory`:

    ```csharp
    public class SendOrderEmailPayload : ValueObject
    {
        public string OrderId { get; set; }
        public string CustomerEmail { get; set; }
    }
    ```

1. Implement the handler:

    ```csharp
    public class SendOrderEmailJob(IEmailSender sender)
        : IBackgroundJobHandler<SendOrderEmailPayload>
    {
        public async Task Execute(SendOrderEmailPayload payload,
            IJobExecutionContext context, CancellationToken cancellationToken = default)
        {
            await sender.Send(payload.CustomerEmail, payload.OrderId, cancellationToken);
        }
    }
    ```

1. Register the handler in the module's `Initialize` method:

    ```csharp
    services.AddBackgroundJob<SendOrderEmailJob>();
    ```

1. Enqueue the job from your code:

    ```csharp
    var payload = AbstractTypeFactory<SendOrderEmailPayload>.TryCreateInstance();
    payload.OrderId = order.Id;
    payload.CustomerEmail = order.Email;

    await jobs.Enqueue<SendOrderEmailJob>(payload);
    ```

The `Enqueue` call returns immediately. The job runs on a worker instance.

## Report progress

Long-running jobs can stream progress to the Admin UI over SignalR. Enable it at enqueue time, then report from the handler through `context.Progress`:

```csharp
await jobs.Enqueue<SendOrderEmailJob>(payload, new EnqueueOptions { ReportProgress = true });
```

```csharp
await context.Progress.Report(new()
{
    Message = "Processing item 50 of 100",
    TotalCount = 100,
    ProcessedCount = 50
}, cancellationToken);
```

The Platform turns each progress report into a live notification with a message and count. Fire-and-forget jobs skip this.

## Enqueue options

`EnqueueOptions` controls how a job is queued:

| Option | Description |
| --- | --- |
| Queue | Routes the job to a dedicated queue and worker pool. |
| ReportProgress | Streams progress to the Admin UI. |
| ProgressNotificationId | Reports into an existing notification instead of creating a new one. |
| UniqueKey | Deduplication hint, honored by engines that support it. |

Retries are configured globally through `VirtoCommerce:BackgroundJobs:MaxRetryAttempts`.

## Static enqueue

For migrating off direct Hangfire calls, a static helper mirrors the Hangfire API:

```csharp
using VirtoCommerce.Platform.Core.Jobs;

await BackgroundJob.Enqueue<SendOrderEmailJob>(payload);
```

The static call opens a dependency injection scope and delegates to `IBackgroundJob`. New code should inject `IBackgroundJob` instead.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Overview</a>
    <a href="../recurring-jobs">Recurring jobs →</a>
</div>
