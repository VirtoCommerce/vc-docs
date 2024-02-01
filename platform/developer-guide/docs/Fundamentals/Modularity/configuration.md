# Configuration

This node of the [appsettings.json file](../../Configuration-Reference/appsettingsjson.md#modularity) configures the modularity logic.

| Node                      | Default or sample value                         | Description                                                                                                   |
| ------------------------- | ----------------------------------------------  | ------------------------------------------------------------------------------------------------------------- |
| IncludePrerelease         | `true`<br>`false`                               | Shows module versions marked<br>as **Prerelease** if value is `true`.                                         |
| DiscoveryPath             | `"./Modules"`                                   | Relative or absolute folder location where the platform will discover the installed modules from.             |
| ModulesManifestUrl        | `"https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json"` | Url to the **.json file** that contains module manifests.           |
| AuthorizationToken        |                                                 | The authorization token to access `ModulesManifestUrl`, added to the `Authorization` header, if specified.    |
| AutoInstallModuleBundles  | `"commerce"`                                  | Group(s) of modules to install automatically during the initial Platform setup.<br>If you do not need to install anything here, provide an empty array. |

**Example**

```json title="appsettings.json"
  "ExternalModules": {
    "IncludePrerelease": false,
    "ModulesManifestUrl": "https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json",
    "AuthorizationToken": "",
    "AutoInstallModuleBundles": [
      "commerce"
    ]
  }
```
