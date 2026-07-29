# Map and Reduce

Map and Reduce splits a large batch into many independent map tasks that run in parallel, then runs a single reduce once all items complete. Use it for work such as reindexing a catalog, recalculating prices, or bulk export, where a single serial job would be slow and lose all progress on a crash.

## Build Map and Reduce job

1. Implement the map handler, which runs per item in parallel:

    ```csharp
    public class IndexPageHandler(IIndexingManager indexer)
        : IMapJobHandler<IndexPage, IndexPageResult>
    {
        public async Task<IndexPageResult> Map(IndexPage page,
            IJobExecutionContext ctx, CancellationToken ct)
        {
            var failed = await indexer.IndexDocuments(page.DocumentType, page.DocumentIds, ct);
            return new IndexPageResult(page.DocumentIds.Length - failed.Length, failed);
        }
    }
    ```

1. Implement the reduce handler, which runs once after all items finish:

    ```csharp
    public class IndexSummaryReducer
        : IReduceJobHandler<IndexSummary, IndexPageResult>
    {
        public Task Reduce(IndexSummary state,
            IReadOnlyCollection<MapResult<IndexPageResult>> results,
            IJobExecutionContext ctx, CancellationToken ct)
        {
            var indexed = results.Where(r => r.Succeeded).Sum(r => r.Value!.Indexed);
            return Task.CompletedTask;
        }
    }
    ```

1. Register the handlers:

    ```csharp
    services.AddMapReduceJob<IndexPageHandler, IndexSummaryReducer>();
    ```

1. Enqueue a batch, partitioned into pages rather than individual items:

    ```csharp
    var pages = allProductIds.Chunk(50).Select(ids => new IndexPage("Product", ids));

    await _mapReduce.Enqueue<IndexPageHandler, IndexSummaryReducer>(
        items: pages,
        state: new IndexSummary("Product", DateTime.UtcNow.Ticks),
        options: new MapReduceOptions
        {
            Queue = "indexing",
            FailurePolicy = FailurePolicy.ContinueOnError,
            ReportProgress = true
        });
    ```

## Failure policies

| Policy | Behavior |
| --- | --- |
| FailFast | The default. Any item failure faults the batch and skips the reduce. |
| ContinueOnError | Failures are recorded, and the reduce runs with the full result set. Each `MapResult<T>` carries its success state and error. |

## Storage

Map and Reduce state is checkpointed so a retried or crashed worker resumes without repeating work:

* **Redis**: Fleet-safe. Results are kept with a 7-day time to live.
* **In-memory**: Single instance only.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../recurring-jobs">← Recurring jobs</a>
    <a href="../extensibility">Extensibility →</a>
</div>
