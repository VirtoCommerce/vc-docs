# StorePluginType ==~object~==

This type represents a Module Federation plugin that a frontend host app can discover and load as a remote at store startup.

## Fields

| Field          | Description                                                                       |
|----------------|------------------------------------------------------------------------------------|
| `id` ==String!==            | Plugin ID.                                                            |
| `version` ==String==         | Plugin version.                                                       |
| `permission` ==String==      | Permission the consuming SPA evaluates before loading the plugin.     |
| `entry` [==StorePluginFileType==](StorePluginFileType.md) | The plugin's entry asset (its `remoteEntry.js`).    |
| `contentFiles` [==[StorePluginFileType!]!==](StorePluginFileType.md) | Additional assets the plugin ships.      |
| `remote` [==StorePluginRemoteType==](StorePluginRemoteType.md) | Module Federation remote coordinates.              |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../StoreResponseType">← StoreResponseType</a>
    <a href="../StorePluginFileType">StorePluginFileType →</a>
</div>
