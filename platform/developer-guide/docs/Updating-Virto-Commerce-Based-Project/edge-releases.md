# Edge Releases

In this guide, we will explore how to automate the installation and update processes for the latest edge release of Virto Commerce using Virto Commerce CLI (**vc-build**).

![Readmore](media/readmore.png){: width="25"} [Install and use Virto Commerce CLI](../Getting-Started/Installation-Guide/windows.md)

## Install Platform latest edge release

To install the latest edge release:

1. Create a clean folder for Virto Commerce, e.g., `C:\vc-platform-edge`
1. In the command prompt, navigate to your **vc-platform** folder:

    ```console
    cd C:\vc-platform-edge
    ```

1. Install the latest edge release for the platform and modules:

    ```console
    vc-build install -edge
    ```

    !!! note
        Running `vc-build install` installs latest stable release.

The latest edge release has been installed.

## Install module latest edge release

To install the module latest edge release, run:

```
vc-build install -module <moduleId> -edge
```

## Update to latest edge release

To update to the latest edge release:

1. In the command line, go to the **vc-platform** folder:

    ```console
    cd C:\vc-platform-edge
    ```

1. Install the latest edge release for the platform and modules from the commerce bundle:

    ```console
    vc-build update -edge
    ```

The edge release has been updated.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../stable-releases">← Stable releases </a>
    <a href="../installing-specific-version">Installing specific version  →</a>
</div>