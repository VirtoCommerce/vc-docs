# Useful Tips

Follow these tips when installing and updating our releases:

* On a local machine, we recommend creating a new clean folder for each stable update. This helps to avoid unexpected behavior in the cloud when CI rebuilds a platform image from scratch.
* Keep **vc-package.json** under source control, such as in GitHub, Azure DevOps, etc. It helps to have a history of changes.
* You can customize the location of the **vc-package.json** file by using the `-PackageManifestPath ./somedir/somename.json` parameter:

    ```console 
    vc-build install -PackageManifestPath /path/package.json
    ```

* To customize `DiscoveryPath` and `ProbingPath`, run: 

    ```console
    vc-build install -PackageManifestPath some_directory/vc-package.json -DiscoveryPath ../modules -ProbingPath platform_dir/app_data/modules
    ```

* **Appsettings.json** is backed up during a platform update.

* You can find the preview version of the modules in our pull requests and [modules_v3.json on github](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json).
* If you notice any problem, please report it [here](https://github.com/VirtoCommerce/vc-build/issues/new).