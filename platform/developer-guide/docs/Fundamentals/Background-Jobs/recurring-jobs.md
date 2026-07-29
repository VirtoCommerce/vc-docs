# Recurring Jobs

A recurring job is a handler plus a schedule. Schedules can be a fixed cron expression, carry a payload, or be driven by module settings so administrators can change them without a redeploy. Recurring jobs are engine-agnostic and fire exactly once across a fleet through a distributed lock.

## Schedule recurring job

Register recurring jobs in the module's `Initialize` method:

```csharp
// Fixed cron
services.AddRecurringJob<SendDigestJob>(schedule => schedule
    .WithId("SendDigest")
    .WithCron("0 7 * * *")
    .WithQueue("maintenance"));

// With a fixed payload
services.AddRecurringJob<SendDigestJob, SendDigestPayload>(
    new SendDigestPayload { Top = 10, Period = "daily" },
    schedule => schedule.WithId("SendDigest").WithCron("0 7 * * *"));

// With a payload built fresh on each run
services.AddRecurringJob<SendDigestJob, SendDigestPayload>(
    () => new SendDigestPayload { Top = 10, RunAtTicks = DateTime.UtcNow.Ticks },
    schedule => schedule.WithId("SendDigest").WithCron("0 7 * * *"));

// Setting-driven: the enabler and cron come from module settings
services.AddRecurringJob<PruneHandler, PrunePayload>(schedule => schedule
    .WithId("Prune")
    .FromSettings(EnablePruneSetting, CronPruneSetting));
```

!!! note
    Cron expressions accept 5 or 6 fields. On Hangfire, recurring jobs use the native Hangfire scheduler and dashboard.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../creating-background-jobs">← Creating background jobs</a>
    <a href="../map-reduce">Map and Reduce →</a>
</div>
