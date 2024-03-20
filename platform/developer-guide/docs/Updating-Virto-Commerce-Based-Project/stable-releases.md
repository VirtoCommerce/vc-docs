# Stable Releases

In this guide, we will explore the process of installing and updating to the latest stable release of Virto Commerce. 

## Install Stable Release

To install a stable release

1. Create a clean folder for Virto Commerce, for example, `C:\vc-platform-stable`.

1. Open the [vc-modules/bundles](https://github.com/VirtoCommerce/vc-modules/tree/master/bundles) repository and select the stable release folder (currently it is v3).

1. Download the **package.json** file

1. Rename the **vc-package.json** file and copy it to your `C:\vc-platform-stable` folder.

	!!! note
		The **vc-package.json** file is used to maintain the list of installed modules and their versions. This allows `vc-build` to easily restore the platform with the modules when it is on a different machine, such as a build server, without all these packages.
		
		When you install `vc-build`, it automatically creates the default **vc-package.json** file in the folder. You can customize the **vc-package.json** file with your set of modules, both Virto Commerce and third party.

1. In the command prompt, navigate to your `vc-platform' folder:

	```console
	cd C:\vc-platform-stable
	```

1. Install the latest stable release for the platform and modules:

	```console
	vc-build install
	```

The latest stable release has been installed.

## Update to Latest Stable Release

To update to the latest stable release:
 
1. Open the [vc-modules/bundles](https://github.com/VirtoCommerce/vc-modules/tree/master/bundles) repository and select the appropriate stable release folder.

1. Download the **package.json** file.

1. Open `C:\vc-platform-stable\vc-package.json` in any text editor and update Virto Commerce based on the versions listed in **package.json**.

1. Save the **vc-package.json** file.

1. In the command prompt, navigate to your `vc-platform' folder:

	```console
	cd C:\vc-platform-stable
	```

1. Install the latest stable release for both platform and modules from the **vc-package.json** file:

	```console
	vc-build install
	```

The stable release has been updated.