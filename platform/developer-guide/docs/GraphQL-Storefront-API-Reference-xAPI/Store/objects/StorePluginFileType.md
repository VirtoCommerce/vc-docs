# StorePluginFileType ==~object~==

This type represents a single asset shipped by a store plugin, such as its entry file or an additional content file.

## Fields

| Field          | Description                                           |
|----------------|--------------------------------------------------------|
| `type` ==String==  | Asset kind, e.g. `script` or `style`.               |
| `path` ==String==  | Public URL of the asset.                            |
| `hash` ==String==  | Cache-busting hash derived from the file's last-write time. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../StorePluginType">← StorePluginType</a>
    <a href="../StorePluginRemoteType">StorePluginRemoteType →</a>
</div>
