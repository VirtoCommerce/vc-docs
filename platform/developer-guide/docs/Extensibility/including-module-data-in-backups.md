# Including Module Data in Backups

The **Backup and Restore** module exports the Platform entries (security, settings, dynamic properties, and binary data) together with the data of any installed module that opts in. Your custom module can join a backup so that its data is exported and restored alongside the rest of the Platform.

A module opts in by implementing two interfaces on its module class. No registration or configuration is needed.

The Backup and Restore module does not keep a list of participating modules. When a backup or restore runs, it asks the module service for every installed module and keeps the ones whose module instance implements the export or import interface:

```csharp
_moduleService.GetInstalledModules()
    .Where(x => x.ModuleInstance is IExportSupport);
```

As soon as your module class implements the interface, your module appears in the **Choose modules to back up** and **Choose modules to restore** lists, and its data is written to its own JSON file inside the backup ZIP. The Backup and Restore module handles the manifest, optional AES-256 encryption, and progress orchestration. You only read and write your own data.

## Implement export and import interfaces

Both interfaces live in the `VirtoCommerce.Platform.Core.ExportImport` namespace:

```csharp title="ISupportExportImport.cs"
Task ExportAsync(Stream outStream, ExportImportOptions options, Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken);

Task ImportAsync(Stream inputStream, ExportImportOptions options, Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken);
```

Add the interfaces to your module class and delegate to a dedicated service. The example below follows the **Inventory** module:

```csharp title="Module.cs"
public class Module : IModule, IExportSupport, IImportSupport, IHasConfiguration
{
    public async Task ExportAsync(Stream outStream, ExportImportOptions options,
        Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken)
    {
        await _appBuilder.ApplicationServices.GetRequiredService<InventoryExportImport>()
            .DoExportAsync(outStream, progressCallback, cancellationToken);
    }

    public async Task ImportAsync(Stream inputStream, ExportImportOptions options,
        Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken)
    {
        await _appBuilder.ApplicationServices.GetRequiredService<InventoryExportImport>()
            .DoImportAsync(inputStream, progressCallback, cancellationToken);
    }
}
```

Notes:

* `ICancellationToken` is the Virto Commerce token from `VirtoCommerce.Platform.Core.Common`, not the .NET `CancellationToken`.
* The `options` parameter carries the export and import settings. Most modules accept it but do not use it.
* Implementing the export and import services in a separate class keeps the module class small and is the established convention across Virto Commerce modules.

## Write export and import logic

Your service serializes your data to the provided stream and reads it back during restore. Page the data so a large dataset is never loaded into memory at once, and report progress through the callback. The snippets below are condensed from the Inventory module:

```csharp title="InventoryExportImport.cs"
public async Task DoExportAsync(Stream outStream,
    Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken)
{
    var progressInfo = new ExportImportProgressInfo();

    await using var streamWriter = new StreamWriter(outStream);
    await using var writer = new JsonTextWriter(streamWriter);
    await writer.WriteStartObjectAsync();

    await writer.WritePropertyNameAsync("Inventories");
    await writer.SerializeArrayWithPagingAsync(_jsonSerializer, _batchSize, async (skip, take) =>
    {
        var searchResult = await _inventorySearchService.SearchAsync(new InventorySearchCriteria { Skip = skip, Take = take });
        return (GenericSearchResult<InventoryInfo>)searchResult;
    }, (processedCount, totalCount) =>
    {
        progressInfo.Description = $"{processedCount} of {totalCount} inventories have been exported.";
        progressCallback(progressInfo);
    }, cancellationToken);

    await writer.WriteEndObjectAsync();
    await writer.FlushAsync();
}
```

The import side reads the same stream and saves the data in batches:

```csharp title="InventoryExportImport.cs"
public async Task DoImportAsync(Stream inputStream,
    Action<ExportImportProgressInfo> progressCallback, ICancellationToken cancellationToken)
{
    var progressInfo = new ExportImportProgressInfo();

    using var streamReader = new StreamReader(inputStream);
    await using var reader = new JsonTextReader(streamReader);

    while (await reader.ReadAsync())
    {
        if (reader.TokenType == JsonToken.PropertyName && (string)reader.Value == "Inventories")
        {
            await reader.DeserializeArrayWithPagingAsync<InventoryInfo>(_jsonSerializer, _batchSize,
                items => _inventoryService.SaveChangesAsync(items),
                processedCount =>
                {
                    progressInfo.Description = $"{processedCount} inventories have been imported.";
                    progressCallback(progressInfo);
                }, cancellationToken);
        }
    }
}
```

The `ExportImportProgressInfo.Description` you set is shown in the per-module progress timeline of the backup and restore screens, so write a message an administrator can read.

## Verify your module participates

To confirm the integration:

1. Build and install your module.
1. Click **Backup and restore** in the main menu, then click **Backup**.
1. Confirm your module appears in the module list, run a backup, and restore it into a clean environment.

For the export folder and file name settings the Backup and Restore module relies on, see [Appsettings.json](../Configuration-Reference/appsettingsjson.md#virtocommerce). 

For the administrator workflow, see [Backup and Restore](/platform/user-guide/latest/backup-and-restore/overview/).

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-application-user">← Extending application user</a>
    <a href="../opentelemetry">Open Telemetry →</a>
</div>