# Include Module Data in Backups

The **Backup and Restore** module exports the Platform entries (security, settings, dynamic properties, and binary data) together with the data of any installed module that opts in. Your custom module can join a backup so that its data is exported and restored alongside the rest of the Platform. Backup and Restore uses your module's export and import implementations both when creating a backup and when restoring one.

A module opts in by implementing two interfaces on its module class, `IExportSupport` and `IImportSupport`. No registration or configuration is needed.

When your module implements both interfaces, it appears in the **Choose modules to back up** and **Choose modules to restore** lists, and its data is written to its own JSON file inside the backup ZIP. The Backup and Restore module handles the manifest, optional AES-256 encryption, and progress orchestration. You only read and write your own data.

!!! note
	The Backup and Restore module does not keep a list of participating modules. When a backup or restore runs, it asks the module service for every installed module and keeps the ones whose module instance implements the export or import interface:

	```csharp
	_moduleService.GetInstalledModules()
	    .Where(x => x.ModuleInstance is IExportSupport);
	```

**For regular module data**, implement `IExportSupport` and `IImportSupport`, covered next. **For binary data**, such as images or files, additionally implement the [binary-data interfaces](#stream-binary-assets-alongside-your-data) described further down.

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

## Stream binary assets alongside your data

If your module exports binary data, such as images or files, use the interfaces described in this section instead of inlining the binaries as base64 in your own JSON.

`IExportSupport` and `IImportSupport` are unchanged, and a module that implements only those two keeps working as before. Binary streaming adds four further, optional interfaces in `VirtoCommerce.Platform.Core.ExportImport`, so a module carries binary side-cars without loading them fully into memory.

Without these interfaces, a module that needs to export binaries has to inline them as base64 inside its own JSON. That works for small assets, but memory use then scales with asset size and batch size, and base64 inflates the payload by about a third. On a module with many or large assets, this risks an out-of-memory failure during backup or restore. The **Catalog** module uses these interfaces for exactly this reason, to stream product images and file assets instead of embedding them.

| Interface | Implemented by | Purpose |
| --- | --- | --- |
| `IExportBinaryDataSupport` | Your module. | Provides the primary payload and declares references to its binary side-cars. |
| `IImportBinaryDataSupport` | Your module. | Reads binary side-car references back on import. |
| `IExportBinaryDataWriter` | The Backup and Restore module. | Streams one archive entry to the module, for writing. |
| `IImportBinaryDataReader` | The Backup and Restore module. | Streams one archive entry to the module, for reading. |

Your module never touches the raw archive stream. It asks for one entry at a time by reference, and the Backup and Restore module streams that entry directly between blob storage and the archive.

!!! note "Implementation note"
    As of this writing, the Backup and Restore module buffers only your module's JSON payload, to a temporary file deleted on close, when a seekable payload is required, and asset binaries are streamed rather than accumulated in managed memory. Treat this buffering detail as current behavior rather than a guaranteed contract; the bounded-memory outcome is what the interfaces are designed to provide.

### Binary data references

`AssetBase` gained a transient `BinaryDataReference` property. It is populated only while a backup is being written or read, is never persisted, and is omitted from JSON when null.

A reference is a relative archive path, for example `assets/catalog/products/image.jpeg`. It is validated on both write and read:

* It must start with `assets/`.
* It must not contain a backslash.
* It must have a non-empty relative part.
* No segment may be empty, `.`, `..`, or contain control characters.

Validation runs against the decoded value, so a percent-encoded traversal attempt is rejected too. The reference is also checked against the destination blob URL before any data is written.

### Compatibility on import

Import detects the shape it is given, so all of the following layouts load:

* **Current**: a readable catalog JSON plus top-level `assets/` archive entries.
* **Nested package**: the module's part is itself an archive with `package.json`, a data JSON, and `assets/`. Both readable source paths and the earlier `assets/<sha256>.bin` naming are accepted. Inner entries must be stored, not compressed.
* **Legacy JSON**: a plain JSON payload with inline base64 `binaryData`, the original format.

A backup taken before a module adopts binary streaming therefore still restores, without being re-taken.

## Verify the integration

To confirm the integration:

1. Build and install your module.
1. Click **Backup and restore** in the main menu, then click **Backup**.
1. Confirm your module appears in the module list, run a backup, and restore it into a clean environment.

The module is now included in the Platform backup and restore workflow.

![Readmore](media/readmore.png){: width="25"} [Export folder and file name settings for Backup and Restore](../Configuration-Reference/appsettingsjson.md#virtocommerce)

![Readmore](media/readmore.png){: width="25"} [Backup and Restore administrator workflow](/platform/user-guide/latest/backup-and-restore/overview/)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-application-user">← Extending application user</a>
    <a href="../opentelemetry">Open Telemetry →</a>
</div>