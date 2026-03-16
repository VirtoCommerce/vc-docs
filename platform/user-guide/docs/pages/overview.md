# Overview

The **Pages** module is a solution designed to connect different CMSs seamlessly within Virto Commerce. It offers a CMS-agnostic architecture, enabling users to manage public, private, and personalized pages effectively. Once pages are published, they are stored within Virto Pages, making the CMS optional after the design phase. This approach allows for flexibility in detaching, replacing, or using multiple CMS platforms simultaneously for scenarios like landing pages, blogs, and more.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-pages/)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-pages/releases/)

## Key features

* **CMS-agnostic architecture**: CMS is required only during the design phase. Once published, content is stored in Virto Pages for use without real-time CMS dependency.
* **Hosted content pages**: Save pages retrieved from a CMS into the Virto platform for efficient management.
* **Content scenarios**:
    * **Public pages**: Allow access to all users.
    * **Private pages**: Restrict access to unauthorized users.
    * **Personalized pages**: Tailor content for specific user groups.
    * **Scheduled publishing**: Define start and end dates for content visibility.
    * **Pages returned by permalink**: Access pages easily using unique identifiers or user-friendly URLs.
    * **Pages returned by ID**: Access pages easily using unique identifiers or user-friendly URLs.
* **Full-text search capabilities**: Quickly search and retrieve pages by keyword.

## Supported CMS platforms

* [Builder.io](../integrations/builder-io/overview.md): Fully supported for integration.
* [Sanity](../sanity/overview.md)
* [Virto Page Builder.](../page-builder/overview.md)
* **Contentful**: Coming soon.
* **Optimizely**: Coming soon.




<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../page-builder/overview">← Page Builder module overview</a>
    <a href="../enabling-pages">Enabling Pages →</a>
</div>