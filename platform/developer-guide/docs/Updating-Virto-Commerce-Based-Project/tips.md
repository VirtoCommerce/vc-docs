
# Tips

Explore this list of useful hints and tips to follow when installing and updating our releases:

1.  On a local machine, we recommend creating a new clean folder for each stable update. This helps to avoid unexpected behaviour in the cloud when CI is rebuilding a platform image from scratch.
    
2.  Keep `vc-package.json` under source control, e.g. in GitHub, Azure DevOps, etc. It helps to have a history of changes.
    
3.  Create a `vc-package.json` boilerplate with the latest version number of the platform by running `vc-build init`.
    
4.  You can customise the location of the `vc-package.json' file by using the `-PackageManifestPath ./somedir/somename.json' command argument, e.g: `vc-build install -PackageManifestPath /path/package.json'.
    
5.  Virto Commerce CLI prevents **appsettings.json** from being modified during the upgrade.
    
6.  You can find the preview version of the modules in our pull requests and [modules_v3.json on github](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json).
    
7.  Check out all the [Virto Commerce CLI Features](https://github.com/VirtoCommerce/vc-build).