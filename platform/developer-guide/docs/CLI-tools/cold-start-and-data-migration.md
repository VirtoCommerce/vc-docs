# Cold Start Optimization and Data Migration

In the context of the Virto Commerce Platform, during startup, a significant amount of work is traditionally performed, including tasks such as verifying module versions, inspecting files in the probing path, and copying module files to the probing path if they are either missing or possess incompatible versions. All this takes time, especially on slower computers, and can sometimes lead to a startup error called **HTTP Error 500.30 - ANCM In-Process Start Failure**.

This can be resolved with a new setting introduced in Virto Commerce Platform version 3.27.0, called **VirtoCommerce:RefreshProbingFolderOnStart**. Enabling this option can significantly reduce the startup time by up to a third. When this option is set to false and the probing path is present, the Platform initializes using the existing content of the probing path without any modifications. It is crucial to note that this assumes the presence of consistent module files within the probing path. However, if the probing path is not found, the Platform will initiate the startup process as usual, including module discovery and copying operations, regardless of the configured option value.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../grab-migrator">← Grab migrator utility quickstart</a>
    <a href="../install-and-update-platform-and-modules">Install and update Platform and modules →</a>
</div>