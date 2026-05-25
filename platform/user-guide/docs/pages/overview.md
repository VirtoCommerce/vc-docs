# Overview

The **Pages** module is a solution designed to connect different CMSs seamlessly within Virto Commerce. It offers a CMS-agnostic architecture, enabling users to manage public, private, and personalized pages effectively. Once pages are published, they are stored within Virto Pages, making the CMS optional after the design phase. This approach allows for flexibility in detaching, replacing, or using multiple CMS platforms simultaneously for scenarios like landing pages, blogs, and more.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-pages/)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-pages/releases/)

## Key features

With the Pages module, you can:

* **Connect any CMS**: A CMS is required only during the design phase. Once published, content is stored in Virto Pages for use without real-time CMS dependency.
* **Host content pages**: Save pages retrieved from a CMS in the Virto Commerce Platform for efficient management.
* **Manage page access scenarios**:
    * **Publish public pages**: Allow access to all users.
    * **Restrict private pages**: Hide content from unauthorized users.
    * **Personalize content**: Tailor pages to specific user groups.
    * **Schedule publishing**: Define start and end dates for content visibility.
    * **Resolve pages by permalink**: Access pages via user-friendly URLs.
    * **Resolve pages by ID**: Access pages via unique identifiers.
* **Search pages by keyword**: Quickly find and retrieve pages using full-text search.
* **Back up and restore pages**: [Save a copy of your pages and restore them](../backup-and-restore.md) when needed.

## Supported CMS platforms

* [Builder.io](../integrations/builder-io/overview.md): Fully supported for integration.
* [Sanity](../sanity/overview.md)
* [Virto Page Builder.](../page-builder/overview.md)
* [Contentful.](../contentful/overview.md)
* **Optimizely**: Coming soon.




<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../page-builder/overview">← Page Builder module overview</a>
    <a href="../enabling-pages">Enabling Pages →</a>
</div>