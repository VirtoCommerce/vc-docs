# Custom llms.txt File

You can upload a custom **llms.txt** file through the Virto Commerce Platform, which overrides the system-generated one.

??? "About llms.txt file"

    The **llms.txt** file is a plain text file, similar in spirit to **robots.txt**, that gives AI agents a brief about your brand, product categories, and policies. Strict UCP agents do not require it, but recommendation and discovery agents increasingly read it for context.

    The format is informal, and these section headings are a working convention rather than a fixed spec. Replace the placeholders with your own brand details, and update the file whenever your policies or product lines change.

    **Example**:

    ``` title="llms.txt"
    # llms.txt
    # Public brief for AI agents about Yourstore
    # About
    One or two sentences on what you sell, who you sell to, and any defining context.
    # Product Categories
    - Category one
    - Category two
    - Category three
    # Policies
    - Returns: 30 days, full refund.
    - Shipping: free over $30, 3-5 business days.
    - Any other policy worth surfacing, for example cruelty-free, vegan, made-to-order.
    # Agent Capabilities
    - UCP manifest: /.well-known/ucp
    - Supported flows: cart, checkout, tokenized payment.
    - Anything explicitly not supported, for example no subscription products via agent.
    # Contact
    support@yourstore.com
    ```

To upload your custom **llms.txt**:

1. Open **Stores** in the main menu.
1. In the next blade, select your store.
1. In the next blade, click the **Assets** widget.
1. In the next blade, click **Upload** in the toolbar and upload your file.

![Adding llms.txt](media/adding-llms-txt.png)

Your file has been uploaded and overrides the system-generated one.

!!! note
    To serve different **llms.txt** files based on domain or language, create separate stores for each domain and upload a distinct **llms.txt** file to the **Assets** of each store.


![Readmore](media/readmore.png){: width="25"} [Custom robots.txt file](custom-robot-txt.md)

![Readmore](media/readmore.png){: width="25"} [UCP module](/platform/developer-guide/latest/Fundamentals/UCP/overview/)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../custom-robot-txt">← Custom robots.txt file</a>
    <a href="../settings">Store settings →</a>
</div>
