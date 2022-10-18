
## Installing Stable Release
To install a stable release:

+ Create a clean folder for Virto Commerce, e.g., `C:\vc-platform-stable`

+ Open the [vc-modules/bundles](https://github.com/VirtoCommerce/vc-modules/tree/master/bundles) repository and select the stable release folder (currently, it is v3)

+ Download the `package.json` file

+ Rename the `vc-package.json` file and copy it to your `C:\vc-platform-stable` folder

!!! note
	The `vc-package.json` file is used to maintain the list of installed modules with their versions. This allows `vc-build` to easily restore the platform with the modules when on a different machine, such as a build server, without all those packages.
	
	When you install `vc-build`, it creates the default `vc-package.json` file in the folder automatically. You can customize the `vc-package.json` file with your set of modules, both by Virto Commerce or third party ones.

+ In the command prompt, navigate to your `vc-platform` folder:

```console
1cd C:\vc-platform-stable
```

+ Install the latest stable release for the platform and modules:

```console
1vc-build install
```

## Updating to Latest Stable Release
To update to the latest stable release:
 
+ Open the [vc-modules/bundles](https://github.com/VirtoCommerce/vc-modules/tree/master/bundles) repository and select the appropriate stable release folder

+ Download the `package.json` file.

+ Open `C:\vc-platform-stable\vc-package.json` in any text editor and update Virto Commerce based on versions listed in `package.json`

+ Save the `vc-package.json` file


+ In the command prompt, navigate to your `vc-platform` folder:

```console
1cd C:\vc-platform-stable
```

Install the latest stable release for both platform and modules from the `vc-package.json` file:

```console
1vc-build install
```
