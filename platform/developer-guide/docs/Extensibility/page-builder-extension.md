# Add Blocks to Page Builder

Frontend developers can now add or edit Page Builder blocks in Virto Commerce Frontend to simplify the customization process. 
<br>
<br>
![Readmore](media/readmore.png){: width="25"} [Page Builder user guide](/platform/user-guide/latest/page-builder/overview)
<br>

As of [Page Builder 3.818.0](https://github.com/VirtoCommerce/vc-module-pagebuilder/releases/tag/3.818.0), the Virto Commerce Frontend includes a **PageBuilderPreview** plugin, which enhances how preview mode works. Here is what this update changes:

* The plugin runs automatically when the system enters preview mode in Page Builder.
* The plugin collects all configuration files into a single object for streamlined data management.
* The collected data is sent to the Page Builder using **postMessage**, ensuring smooth communication.
* The previous approach (using a shared folder or blob storage) is still supported for backward compatibility.
* If a section with the same name already exists in the Page Builder, it will now be overwritten.

As an example, let's add two blocks to the configuration:

* **Image**: A modified version of the existing **Image** block.
* **Image2**: A new block.

To add these blocks:

1. Go to **Content** --> **Theme**.
1. Create the following folder structure: **config**--> **schemas** --> **sections**.
1. Upload **Image.json** and **Image2.json** files to this folder.

The existing **Image** block is replaced with the new one. The new **Image2** block is added to the list of blocks:

![New blocks](media/new-blocks.png){: style="display: block; margin: 0 auto;" }


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-application-user">← Extending application user </a>
    <a href="../../Operations/maintenance-tasks-for-sql">Maintenance tasks for SQL  →</a>
</div>