
# Tips
here is a list of useful hints and tips you might want to follow when installing and updating our releases:

1.  On a local machine, we recommend creating a new clean folder for every stable update. It helps to prevent unexpected behavior in the cloud where CI creates a platform image from scratch.
    
2.  Keep `vc-package.json` under source control, e.g., in GitHub, Azure DevOps, etc. It helps you have a history of modifications.
    
3.  Create a `vc-package.json` boilerplate with the latest version number of the platform by running `vc-build init`.
    
4.  You can customize the `vc-package.json` file location by using  the `-PackageManifestPath ./somedir/somename.json` command argument, e.g.: `vc-build install -PackageManifestPath /path/package.json`.
    
5.  Virto Commerce CLI prevents `appsettings.json` from modifications during the update.
    
6.  You can find the preview version of modules in our pull requests and [modules_v3.json at github](https://github.com/VirtoCommerce/vc-modules/blob/master/modules_v3.json).
    
7.  You can review all features of Virto Commerce CLI [here](https://github.com/VirtoCommerce/vc-build).
