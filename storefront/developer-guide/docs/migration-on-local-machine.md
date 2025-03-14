# Migrate on Local Machine

If you are currently running a local deployment of Virto Commerce with the Platform, Storefront, and Theme files stored on the filesystem, this guide will help you migrate to the new Virto Commerce architecture:

1. Stop and disable VC Storefront. For example, if you use Docker, locate the **docker-compose.yml** file that manages your VC Solution, then remove the VC storefront service definition from it.
1. If you are using the standard, non-customized VC Theme, remove the theme files from the directory in which they are stored. Otherwise, you'll need to migrate your customization to the VC Theme version.
1. [Deploy Frontend Application on a local machine.](deployment.md#frontend-application-deployment)

You have successfully migrated to new architecture.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../migration-on-azure">← Migration on Azure Cloud</a>
    <a href="../authentication/authentication-types">Authentication types →</a>
</div>