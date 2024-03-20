# Edge Releases

In this guide, we will explore how to automate the installation and update processes for the latest edge release of Virto Commerce using Virto Commerce CLI (**vc-build**).

!!! note
    By default, the stable release is installed. To install edge, **-edge** must be passed.

![Readmore](media/readmore.png){: width="25"} [Install and use Virto Commerce CLI](../Getting-Started/Installation-Guide/windows.md)

## Install Latest Edge Release

To install the latest edge release:

1. Create a clean folder for Virto Commerce, e.g., `C:\vc-platform-edge`
1. In the command prompt, navigate to your vc-platform folder:

    ```console
    cd C:\vc-platform-edge
    ```

1. Install the latest edge release for the platform and modules:

    ```console
    vc-build install
    ```

The latest edge release has been installed.

## Update to Latest Edge Release

To update to the latest edge release:

1. In the command line, go to the `vc-platform` folder:

    `cd C:\vc-platform-edge`

1. Install the latest edge release for the platform and modules from the commerce bundle:

    `vc-build update`

The edge release has been updated.