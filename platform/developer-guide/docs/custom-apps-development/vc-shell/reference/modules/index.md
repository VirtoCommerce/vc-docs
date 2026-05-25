# Built-in Modules

Domain modules that ship inside `@vc-shell/framework` and install automatically with the shell. Applications consume them through the same APIs as any application module — composables, blades, and components are imported from `@vc-shell/framework`.

These modules cover cross-cutting concerns that every back-office app needs: asset management for Platform-stored binaries, and an assets-manager surface that wraps the asset lifecycle behind a Vue-friendly composable.

## Modules

| Module | Plugin export | What it provides |
| --- | --- | --- |
| [Assets.](assets.md) | `AssetsDetailsModule`. | The single-asset details blade and its components. Used together with the `useAssets` composable from `@vc-shell/framework`. |
| [Assets Manager.](assets-manager.md) | `AssetsManagerModule`. | The multi-asset management blades and components. Used together with the `useAssetsManager` composable and the `VcGallery` integration. |

Both modules are installed by the framework's shell during `app.use(VirtoShellFramework, ...)`. Application code never calls `app.use(AssetsDetailsModule)` directly; the blade components and matching composables are exported from `@vc-shell/framework` and ready to import where needed.

## Choosing between Assets and Assets Manager

| Scenario | Reach for |
| --- | --- |
| The blade owns a single asset, for example, a logo, a profile picture, or a document. | `useAssets`. |
| The blade owns a list of assets with reorder, upload, and remove operations, for example, a product gallery or attachments. | `useAssetsManager`. |
| The blade needs a one-off file upload without long-term storage, for example, a CSV import. | Neither. Use **VcFileUpload** with your own handler. |

## Customization surface

Both modules expose a small set of public composables and components. They do not advertise extension points; if a blade needs deeper customization, wrap the composables in an app-local composable rather than fork the modules.

```ts title="Wrap useAssetsManager with app defaults"
import { useAssetsManager } from "@vc-shell/framework";
import type { Ref } from "vue";
import type { ICommonAsset } from "@vc-shell/framework";

export function useProductGallery(images: Ref<ICommonAsset[]>) {
  return useAssetsManager(images, {
    uploadPath: () => "products",
    // App-wide defaults applied to every product blade.
  });
}
```

## Related

- [Forms recipes — file upload.](../../guides/forms/index.md#recipe-file-upload)
- [Platform recipes — asset and file upload.](../../guides/platform/index.md#recipe-asset-and-file-upload)
- [VcGallery component.](../../components/data-display/vc-gallery.md)
- [VcFileUpload component.](../../components/form/vc-file-upload.md)
- [VcImageUpload component.](../../components/media/vc-image-upload.md)
