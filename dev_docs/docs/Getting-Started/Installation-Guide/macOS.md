# Deploy on macOS

Use this guide to deploy and configure precompiled Virto Commerce Platform V3.

## Prerequisites

* [.NET6 SDK on Mac OS.](https://docs.microsoft.com/en-us/dotnet/core/install/macos)

    1. [Download .NET Core SDK](https://dotnet.microsoft.com/download/dotnet-core).
    1. Install the LTS version, it will include components for build and launch runtime application.

* [Microsoft SQL Server.](https://www.microsoft.com/en-us/sql-server)

## Install LibSass

To install LibSass:

1. Download the nuget package [LibSass Host Native for for OS X (x64)](https://www.nuget.org/packages/LibSassHost.Native.osx-x64).
1. Unzip the package.

    ```console
    unzip libsasshost.native.osx-x64.1.x.x.nupkg -d libsass
    ```

1. Move the library to dotnet location path. You can find the location of dotnet using CLI **dotnet --info**  

    ```console
    sudo cp libsass/runtimes/osx-x64/native/libsass.dylib /usr/local/share/dotnet/shared/Microsoft.NETCore.App/6.x.x/
    ```

## Download precomplied binaries

1. Open the [Releases section of the Virto Commerce Platform](https://github.com/VirtoCommerce/vc-platform/releases) in GitHub.

1. Find **VirtoCommerce.Platform.3.x.x.zip** file. This file contains the prebuilt site and can be executed without additional compilation. The source code is not included. 

1. Download the binaries using the following command:

    ```console
    wget "https://github.com/VirtoCommerce/vc-platform/releases/download/3.x.x/VirtoCommerce.Platform.3.x.x.zip"
    ```

1. Unpack the downloaded file to the local directory **/vc-platform-3** using the following command: 

    ```console
    unzip VirtoCommerce.Platform.3.x.x.zip -d vc-platform-3
    ```

Now you have the directory with the precompiled files of the Virto Commerce Platform.

## Setup Platform

To set up the Platform:

1. [Configure application strings.](linux.md#configure-application-strings)
2. [Run the Platform by CLI "dotnet".](linux.md#run-the-platform-by-cli-dotnet)
3. [Perform initial sign in.](linux.md#perform-initial-sign-in)

### Configure application strings

To configure application strings:

1. Open the **appsettings.json** file in a text editor.
1. In the **ConnectionStrings** section, modify the **VirtoCommerce** node as follows:

    ```json
        "ConnectionStrings": {
            "VirtoCommerce" : "Data Source={SQL Server URL};Initial Catalog={Database name};Persist Security Info=True;User ID={User name};Password={User password};MultipleActiveResultSets=True;Connect Timeout=30"
        },

    ```

    !!! note
        Make sure the user has permission to create new databases.


1.  To display images, specify the public url for assets by updating `Assets:FileSystem:PublicUrl` in the **Assets** section:

    ```json
    "Assets": {
            "Provider": "FileSystem",
            "FileSystem": {
                "RootPath": "~/assets",
                "PublicUrl": "https://localhost:5001/assets/" <-- Set your platform application url with port localhost:5001
            },
        },
    ```

1. To configure CMS content storage, specify the public url for content for content by updating `Content:FileSystem:PublicUrl` in the Content section: 

    ```json
    "Content*": {
            "Provider": "FileSystem",
            "FileSystem": {
                "RootPath": "~/cms-content",
                "PublicUrl": "https://localhost:5001/cms-content/" <-- Set your platform application url with port localhost:5001
            },
        },
    ```

1. Save the **appsettings.json** file to apply the configurations.

### Run the Platform by CLI "dotnet"

To run the Platform by CLI:

1. Install and trust HTTPS certificate. Run steps described in [this article](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-3.0&tabs=visual-studio%2Clinux-ubuntu#trust-the-aspnet-core-https-development-certificate-on-windows-and-macos-1) to trust the .NET Core SDK HTTPS development certificate on Linux.

    Read more about [enforcing HTTPS in ASP.NET Core.](https://docs.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-3.0&tabs=visual-studio#trust)

1. Run the Platform using the following command:

    ```console
    export ASPNETCORE_URLS="http://+:5000;https://+:5001"
    cd vc-platform-3
    dotnet VirtoCommerce.Platform.Web.dll
    ```

1. The output in the console will say something like:

    ```console
    Now listening on: http://[::]:5000
    Now listening on: https://[::]:5001
    ```

### Perform initial sign-in

To access the Platform and perform initial sign-in:

1. Open your browser and type `https://localhost:5001`.
1. If you encounter the **Your connection is not private** error, click **Advanced --> Proceed to...**. This option allows you to proceed to the website even though the browser has detected an issue with the SSL certificate.
   
    !!! note
        For additional details on addressing this error and using a self-signed certificate, refer to [Trust the ASP.NET Core HTTPS development certificate](link-to-guide).

1. Upon the first request, the application will create and initialize the database.
1. Once completed, you will be redirected to the sign-in page. Use the following credentials to sign in:

    * Login: `admin`
    * Password: `store`

Your Platform is ready to go.
