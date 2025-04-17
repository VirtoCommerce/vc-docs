# System Requirements
This sections lists the basic hardware and software requirements to installing the Virto Commerce Platform.

## Minimum hardware requirements
Before installing, make sure your computer meets these minimum requirements:

| Parameter         | Value         |
|-------------------|---------------|
| RAM               | 1GB           |
| Disk space        | 1GB           |
| Processor speed   | 2GHz          |
| Number of cores   | Dual core     |
| Processor type    | x64-compatible only |

## Supported operation systems for .NET 8

The Virto Platform runs on .NET 8. [.NET 8](https://github.com/dotnet/core/blob/main/release-notes/8.0/README.md) is a [Long Term Support (LTS)](https://github.com/dotnet/core/blob/main/release-policies.md) release and is [supported](https://github.com/dotnet/core/blob/main/support.md) on multiple operating systems per their lifecycle policy.

For issues with .NET on operating systems not listed here, open a GitHub issue in the appropriate .NET repository or contact the OS maintainer community . 

![Readmore](media/readmore.png){: width="25"} [List of repositories](https://github.com/dotnet/core/blob/main/Documentation/core-repos.md)

=== "Windows"

    |OS                                                         | Version                 | Architectures   | Lifecycle                                                                                              |
    |---------------------------------------------------------- |-------------------------|-----------------|--------------------------------------------------------------------------------------------------------|
    |[Windows 10 Client](https://www.microsoft.com/windows/)    | Version 1607+           | x64, x86, Arm64 | [Windows](https://support.microsoft.com/help/13853/windows-lifecycle-fact-sheet)                       |
    |[Windows 11](https://www.microsoft.com/windows/)           | Version 22000+          | x64, x86, Arm64 | [Windows](https://support.microsoft.com/help/13853/windows-lifecycle-fact-sheet)                       |
    |[Windows Server](https://learn.microsoft.com/windows-server/) | 2012+                | x64, x86        | [Windows Server](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)   |
    |[Windows Server Core](https://learn.microsoft.com/windows-server/) | 2012+           | x64, x86        | [Windows Server](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)   |
    |[Nano Server](https://learn.microsoft.com/windows-server/get-started/getting-started-with-nano-server) | Version 1809+| x64| [Windows Server](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)|

    .NET 8 is supported in the x64 emulator on Windows 11 Arm64.

    
=== "Linux"

    |OS                                                                                                     | Version               | Architectures     | Lifecycle                     |
    |-------------------------------------------------------------------------------------------------------|-----------------------|-------------------|-------------------------------|
    |[Alpine Linux](https://alpinelinux.org/)                                                               | 3.17+                 | x64, Arm64, Arm32 | [Alpine][Alpine-lifecycle]    |
    |[Debian](https://www.debian.org/)                                                                      | 11+                   | x64, Arm64, Arm32 | [Debian][Debian-lifecycle]    |
    |[Fedora](https://getfedora.org/)                                                                       | 37+                   | x64               | [Fedora][Fedora-lifecycle]    |
    |[openSUSE](https://opensuse.org/)                                                                      | 15+                   | x64               | [OpenSUSE][OpenSUSE-lifecycle]|
    |[Oracle Linux](https://www.oracle.com/linux/)                                                          | 8+                    | x64               | [Oracle][Oracle-lifecycle]    |
    |[Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)    | 8+                    | x64, Arm64        | [Red Hat][RHEL-lifecycle]     |
    |[SUSE Enterprise Linux (SLES)](https://www.suse.com/products/server/)                                  | 12 SP5+               | x64               | [SUSE][SLES-lifecycle]        |
    |[Ubuntu](https://ubuntu.com/)                                                                          | 20.04+                | x64, Arm64, Arm32 | [Ubuntu][Ubuntu-lifecycle]    |

    Other distributions are supported at best effort, per [.NET Support and Compatibility for Linux Distributions](https://github.com/dotnet/core/blob/main/linux-support.md).

    **Libc compatibility**:

    - [glibc](https://www.gnu.org/software/libc/) 2.23 (from Ubuntu 16.04).
    - Alpine: [musl](https://musl.libc.org/) 1.2.2 (from Alpine 3.13).

=== "macOS"

    |OS                                         | Version                   | Architectures     |
    |-------------------------------------------|---------------------------|-------------------|
    |[macOS](https://support.apple.com/macos)   | 10.15+                    | x64, Arm64        |

    .NET 8 is supported in the Rosetta 2 x64 emulator.

=== "Android"

    | OS                                            | Version                 | Architectures     |
    |-----------------------------------------------|-------------------------|-------------------|
    | [Android](https://support.google.com/android) | API 21+                 | x64, Arm32, Arm64 |

=== "iOS / tvOS / MacCatalyst"

    | OS                                                    | Version                 | Architectures     |
    |-------------------------------------------------------|-------------------------|-------------------|
    | [iOS](https://support.apple.com/ios)                  | 11.0+                   | Arm64             |
    | [iOS Simulator](https://support.apple.com/ios)        | 11.0+                   | x64, Arm64        |
    | [tvOS](https://support.apple.com/apple-tv)            | 11.0+                   | Arm64             |
    | [tvOS Simulator](https://support.apple.com/apple-tv)  | 11.0+                   | x64, Arm64        |
    | [MacCatalyst](https://support.apple.com/macos)        | 10.15+, 11.0+ on Arm64  | x64, Arm64        |


!!! note
    The following versions [are no longer supported by .NET 8.0](https://github.com/dotnet/core/blob/main/os-lifecycle-policy.md).


## Supported databases

The Virto Commerce Platform supports:

* MS SQL Server 2019 and higher.
* MySql Server 5.7 and higher.
* PostgreSQL 12 and higher.

![Readmore](media/readmore.png){: width="25"} [Configuring Platform with database providers](../Fundamentals/Persistence/DB-Agnostic/overview.md)

## Supported browsers

The Virto Commerce Platform supports:

-   Microsoft Internet Explorer 9 and higher.

    !!! note
        Virto Commerce previously supported IE6 and IE7 in versions prior to 3.60, while IE8 was supported in versions prior to 4.10.
    
-   Mozilla Firefox 2.0 and higher.
    
-   Google Chrome 1.x.
    
-   Apple Safari 2.x.

