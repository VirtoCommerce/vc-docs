# Debug SEO Links

The SEO module allows you to analyze and debug permalink resolutions. The **Debug SEO Links** widget helps you understand how SEO slugs are processed across different stores and languages, making it easier to identify and resolve configuration or routing issues.

To analyze a slug:

1. Click **Stores** in the main menu.
1. In the next blade, select your store.
1. In the store blade, click the **Debug SEO Links** widget.
1. In the next blade, select a language, enter a slug to analyze, and click **Debug**.
1. The following blade displays a list of debug stages:

    | **Stage** | **Name**          | **Description**                                                                                           |
    | --------- | ----------------- | --------------------------------------------------------------------------------------------------------- |
    | 1         | **Original**      | SEO items found by the resolver. Displays all items from the database, not filtered by store or language. |
    | 2         | **Filtered**      | SEO items matching the selected store and language rules.                                                 |
    | 3         | **Scored**        | The system calculates numeric scores and object type priorities.                                          |
    | 4         | **FilteredScore** | Only SEO items with a positive score are kept.                                                            |
    | 5         | **Ordered**       | SEO items are ordered by score and object type priority.                                                  |
    | 6         | **Final**         | The first item with the highest priority is selected as the resolved SEO result.                          |

Click on any stage to view detailed information.

Try our interactive demo to explore key features in action:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/cufsuttr2ptz?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../managing-broken-links">← Managing broken links</a>
    <a href="../settings">Settings →</a>
</div>