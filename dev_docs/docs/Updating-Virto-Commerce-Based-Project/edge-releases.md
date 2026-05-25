## Installing Latest Edge Release

You can use Virto Commerce CLI (***vc-build***) to automate all installation and update processes.

!!! tip
	To learn how to install and use Virto Commerce CLI, refer to [this guide](../Getting-Started/Installation-Guide/Installing-on-Windows/03-installation-windows-on-premises-CLI.md).

To install the latest edge release:

+ Create a clean folder for Virto Commerce, e.g., `C:\vc-platform-edge`

+ In the command prompt, navigate to your vc-platform folder:

```console
cd C:\vc-platform-edge
```

+ Install the latest edge release for the platform and modules:

```console
vc-build install
```

## Updating to Latest Edge Release

In the command line go to the vc-platform folder

`cd C:\vc-platform-edge`

Install latest edge release for platform and modules from commerce bundle

`vc-build update`
