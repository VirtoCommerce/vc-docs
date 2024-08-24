# Deploy on Windows

Use this guide to deploy and configure precompiled Virto Commerce Platform V3.

## Prerequisites

=== "Required software components"

    * [ASP.NET Core Runtime 8.0.0.](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
    * [Virto Commerce CLI](https://github.com/VirtoCommerce/vc-build), our proprietary command line interface that enables automating the installation process and updating the dependencies.
    * [MS SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) / [MySQL](https://dev.mysql.com/downloads/installer/) / [PostgreSQL.](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

    !!! note
        After installing MS SQL server, switch its authentication to mixed mode, as described [here](https://www.top-password.com/knowledge/sql-server-authentication-mode.html).
        ![Selecting server authentication mode](media/01-selecting-server-authentication.png)


=== "Optional software components"

    * For VirtoCommerce 3.800 or higher, install MS Visual Studio 2022 (version 17.8 or higher). 
    * To edit the source code, install [.NET 8 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0 "Installing .NET 6 SDK").
    * For better search capabilities, install [Elastic search 8.12](https://www.elastic.co/downloads/past-releases/elasticsearch-7-15-0). 

        !!! note
            By default, VirtoCommerce uses [Lucene .NET](https://lucenenet.apache.org/). However, it cannot be used in production due to its limited functionality.


## Install Platform 

The platform can be installed:

* [Manually by downloading the precompiled binaries](windows.md#download-precompiled-binaries).
* [Using Virto Commerce CLI (vc-build)](windows.md#use-virto-commerce-cli).

### Download precomplied binaries

1. Open the [Releases section of the Virto Commerce Platform](https://github.com/VirtoCommerce/vc-platform/releases) in GitHub.

1. Find **VirtoCommerce.Platform.3.x.x.zip** file. This file contains the prebuilt site and can be executed without additional compilation. The source code is not included. 

1. Unpack the downloaded file to the local directory **/vc-platform-3**. After that you will have the directory with Platform precompiled files. 

Now you have the directory with the precompiled files of the Virto Commerce Platform.

### Use Virto Commerce CLI

To use Virto Commerce CLI (vc-build):

1. Install vc-build using the command:

    ```console
    dotnet tool install -g VirtoCommerce.GlobalTool
    ```

1. Install the Platform and the modules using the command:

    ```console
    vc-build install
    ```

1. Specify the platform version (if required) using the command:

    ```console
    vc-build install -version 3.800.0
    ```

![Readmore](media/readmore.png){: width="25"} [Vc-build for packages management](https://github.com/VirtoCommerce/vc-build/blob/main/docs/CLI-tools/package-management.md)

## Setup Platform

To set up the Platform:

1. [Configure application strings.](windows.md#configure-application-strings)
2. [Run the Platform.](windows.md#run-platform)
3. [Perform initial sign in.](windows.md#perform-initial-sign-in)

### Configure application strings

To configure application strings:

1. Open the **appsettings.json** file in a text editor.
1. In the **ConnectionStrings** section, modify the **VirtoCommerce** node as follows:

    ```json
        "ConnectionStrings": {
            "VirtoCommerce" : "Data Source={SQL Server URL};Initial Catalog={Database name};Persist Security Info=True;User ID={User name};Password={User password};MultipleActiveResultSets=True;Connect Timeout=30"
        },

    ```

    !!! info
        You can either replace the username and password with your own in the **ConnectionStrings**, or add **virto** as the username and **virto** as the password in the database ([SQL](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-login?view=sql-server-ver16), [PostgreSQL](https://www.postgresql.org/docs/8.0/sql-createuser.html), [MySQL](https://dev.mysql.com/doc/refman/8.4/en/create-user.html)).

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

### Run Platform

You can run the Platform:

* On HTTPS schema (Preferred).
* On HTTP schema.

=== "Run on HTTPS schema (Prefered)"

    1. Install and trust HTTPS certificate. [Trust the .NET Core SDK HTTPS development certificate on Windows](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-3.0&tabs=visual-studio%2Clinux-ubuntu#trust-the-aspnet-core-https-development-certificate-on-windows-and-macos-1).


        ![Readmore](media/readmore.png){: width="25"} [Enforcing HTTPS in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-3.0&tabs=visual-studio#trust)

    1. Run the Platform using the following command:

        ```console
        cd C:\vc-platform-3\
        dotnet.exe VirtoCommerce.Platform.Web.dll
        ```

    1. When the process is complete, you will see an output in the console similar to this:

        ```console
        Now listening on: http://localhost:5000
        Now listening on: https://localhost:5001
        ```

=== "Run on HTTP schema"
 
    To run the Platform only at HTTP schema in production mode,  it is sufficient to specify only HTTP URLs in `--urls` argument of the `dotnet` command.

    ```console
    dotnet VirtoCommerce.Platform.Web.dll --urls=http://localhost:5000
    ```

### Perform initial sign-in

To access the Platform and perform initial sign-in:

1. Open your browser and type `https://localhost:5001`.
1. If you encounter the **Your connection is not private** error, click **Advanced --> Proceed to...**. This option allows you to proceed to the website even though the browser has detected an issue with the SSL certificate.
   
    !!! note
        For additional details on addressing this error and using a self-signed certificate, refer to [Trust the ASP.NET Core HTTPS development certificate](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-8.0&tabs=visual-studio%2Clinux-ubuntu#trust-the-aspnet-core-https-development-certificate-on-windows-and-macos).

1. Upon the first request, the application will create and initialize the database.
1. Once completed, you will be redirected to the sign-in page. Use the following credentials to sign in:

    * Login: admin
    * Password: store

1. The installation wizard starts downloading default modules and sample data:

	![Installation wizard screen](media/02-module-auto-installation-screen.png)
	
1. After installation, reset default credentials:

	![Resetting default credentials](media/03-resetting-default-credentials.png)

Your platform is ready to go.