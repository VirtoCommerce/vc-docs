# Overview

The **Background Jobs** module is the Platform's background-processing engine. It provides an engine-agnostic job API: 

1. A module defines a serializable payload and an `IBackgroundJobHandler<TPayload>`.
1. It enqueues work through the `IBackgroundJob` facade. 
1. A single active engine per Platform instance (Hangfire, RabbitMQ, or In-Memory) runs the jobs, selected by configuration.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-background-jobs)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-background-jobs/releases)

Consumer modules reference only `VirtoCommerce.Platform.Core`, so they never depend on a specific engine.

## Key features

* **Engine-agnostic API**: Define a payload and a handler, then enqueue through `IBackgroundJob`.
* **Pluggable engines**: Hangfire (SQL), RabbitMQ, and In-Memory, selected by a single configuration key.
* **Fire-and-forget with optional progress**: Stream live progress to the Admin UI over SignalR.
* **Map and Reduce**: Fan work out into parallel map tasks, then run a single reduce, with checkpoint and resume.
* **Recurring jobs**: Cron-based or setting-driven schedules with fleet-safe, exactly-once firing.
* **Retry and dead-letter**: Bounded retries with a dead-letter queue for inspection.
* **Instance modes**: Run an instance as Producer, Worker, or Both.
* **No breaking changes**: Existing Hangfire consumers keep working through legacy Hangfire mode.

## Supported engines

The Platform runs one active engine per instance:

| Engine | Use case |
| --- | --- |
| **Hangfire** | The default engine. Uses the existing SQL storage, dashboard, queues, retry, and recurring jobs. |
| **RabbitMQ** | Message-broker engine. Jobs are published to durable queues and consumed in process, with a dead-letter queue for exhausted jobs. |
| **In-Memory** | In-process and non-durable. For development and testing only. |

## Migrate without breaking changes

The module ships alongside Hangfire without breaking existing modules. The migration runs in stages:

1. **Release**: The module becomes generally available. Hangfire stays the default engine, and existing modules run untouched.
1. **Platform migration**: Virto Commerce moves its own modules onto the new interface.
1. **RabbitMQ with legacy Hangfire**: RabbitMQ becomes the primary engine while custom modules keep running on Hangfire side by side.
1. **Full migration**: Once custom modules are migrated, legacy Hangfire is disabled for a pure RabbitMQ deployment.

!!! note
    Contracts live in **VirtoCommerce.Platform.Core**. The engine is an installable module, and consumer modules take no dependency on any specific engine.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Event-Driven-Development/using-domain-events">← Event-driven development</a>
    <a href="../creating-background-jobs">Creating background jobs →</a>
</div>
