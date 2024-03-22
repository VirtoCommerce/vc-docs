# Stable Releases

In this guide, we will explore the process of installing and updating to the latest stable release of Virto Commerce. 

## Install Stable Release

To install a stable release

1. Create a clean folder for Virto Commerce, for example, `C:\vc-platform-stable`.

1. In the command prompt, go to your **vc-platform** folder:

	```console
	cd C:\vc-platform-stable
	```

1. Install the latest stable release for the platform and modules:

	```console
	vc-build install
	```

	!!! tip
		To install a specific version of a stable release, use a `-v` parameter.<br>For example, to install version 7, run `vc-build install -v 7`

The latest stable release has been installed.

## Update to Latest Stable Release

To update to the latest stable release:
 
1. In the command prompt, go to your **vc-platform** folder:

	```console
	cd C:\vc-platform-stable
	```

1. Install the latest stable release for both platform and modules from the **vc-package.json** file:

	```console
	vc-build update
	```

The stable release has been updated.