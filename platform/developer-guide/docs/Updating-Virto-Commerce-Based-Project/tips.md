
# Tips

Follow these tips when installing and updating our releases:

* On a local machine, we recommend creating a new clean folder for each stable update. This helps to avoid unexpected behavior in the cloud when CI rebuilds a platform image from scratch.
* Keep **vc-package.json** under source control, such as in GitHub, Azure DevOps, etc. It helps to have a history of changes.
* Create a **vc-package.json** boilerplate with the latest version number of the platform by running `vc-build init`.
* You can customize the location of the **vc-package.json** file by using the `-PackageManifestPath ./somedir/somename.json' command argument`, e.g.: `vc-build install -PackageManifestPath /path/package.json`.
* Virto Commerce CLI prevents **appsettings.json** from being modified during upgrade.
* You can find the preview version of the modules in our pull requests and [modules_v3.json on github](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json).
* Check out all the [Virto Commerce CLI Features](https://github.com/VirtoCommerce/vc-build).