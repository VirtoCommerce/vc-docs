# Overview

The **Environments Compare** (**Environments Comparison**) module enables backend administrators to compare platform settings, environment configurations, and system information across multiple Virto Commerce environments (development, staging, production, etc.). This module helps identify configuration discrepancies, troubleshoot environment-specific issues, and ensure consistency across deployments.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-environments-compare/)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-environments-compare/releases)


## Key features

* **Multi-environment comparison**: Comparison of settings across multiple environments, including local and remote.
* **Comprehensive settings coverage**:
    * Platform settings (grouped by settings groups).
    * Environment variables (system and process variables).
    * .NET runtime information (framework version, OS description, architecture).
    * Server features and hosting configuration.
* **Environment settings view**: Dedicated view for inspecting all settings of a single environment in a structured, filterable layout.
* **Base environment comparison**: Comparison of all environments against a selected base environment.
* **Difference filtering**: Toggle for displaying all settings or only differing values.
* **Search**: Keyword-based filtering of settings.
* **Settings export**: Export of selected environment settings for reference.
* **Security features**:
    * API key-based authentication for secure communication with remote environments.
    * Automatic masking of secret/sensitive settings (passwords, secure strings) using SHA1 hashes.
    * Clear visual feedback showing which settings differ from the base environment and which environments have errors.
    * Error handling with descriptive messages.
    * External API endpoint for secure remote settings exposure.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../dynamic-associations/overview">← Dynamic Associations module overview</a>
    <a href="../compare-environments">Comparing environments →</a>
</div>