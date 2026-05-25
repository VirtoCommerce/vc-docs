# Custom robots.txt File

You can upload a custom **robots.txt** file via the Virto Commerce Platform, which will override the system-generated one.

??? "About robots.txt file"

    The **robots.txt** file is a plain text file that tells search engine crawlers which pages they are allowed or disallowed to crawl and index. It helps prevent technical or sensitive sections of your site from appearing in search results.

    **Example**:

    ``` title="robots.txt"
    User-agent: *                               // Applies the rule to all crawlers
    Disallow: /admin/                           // Blocks indexing of the `/admin/` path 
    Disallow: /checkout/                        // Blocks indexing of the `/checkout/` path
    Allow: /                                    // Allows crawling of all other content
    Sitemap: https://example.com/sitemap.xml    // Provides the URL of your site’s sitemap to improve indexing
    ```


To upload your custom **robots.txt**:

1. Open **Stores** in the main menu.
1. In the next blade, select your store.
1. In the next blade, click on the **Assets** widget.
1. In the next blade, click **Upload** in the toolbar and upload your file.

![Upload robots.txt](media/adding-robot-txt.png)

Your file has been uploaded and overrides the system-generated one.

!!! note
    To serve different **robots.txt** files based on domain or language, we recommend creating separate stores for each domain and uploading a distinct **robots.txt** file to the **Assets** of each store. This approach allows each store to manage its own file.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuring-store">← Configuring store</a>
    <a href="../settings">Store settings →</a>
</div>
