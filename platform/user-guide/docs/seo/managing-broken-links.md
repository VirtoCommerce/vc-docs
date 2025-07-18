# Manage Broken Links

The SEO module includes a powerful tool for detecting and managing broken URLs reported by the Frontend. When the Frontend encounters a missing slug (via an empty `slugInfo` GraphQL response), the system logs the **404 error** and makes it visible to administrators in the back office.

To view the list of broken links and manage them:

1. Click **Stores** in the main menu.
1. In the next blade, select your store.
1. In the next blade, click on the broken links widget.

    If the [broken links management feature is enabled](settings.md), the widget displays the number of active broken links, not the total number:

    ![Broken links count](media/broken-links-count.png){: style="display: block; margin: 0 auto;" }

    If disabled, the widget displays the following:

    ![Disabled broken links](media/disbaled-broken-links.png){: style="display: block; margin: 0 auto;" }

1. The next blade lists all the broken links with the following statuses:

    | Broken link status   | Description                                                                                                                                                                          |
    | ---------------------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Active**           | Broken links that require your attention. The hit count continues until the link is either resolved or accepted.                                                                     |
    | **Accepted**         | Broken links pointing to intentionally removed pages. Once accepted, the hit count stops. This status indicates that you're aware of the broken link and have approved it as intentional. |
    | **Resolved**         | Broken links that have been redirected to a valid URL. The hit count stops once the redirect is assigned. Resolved broken links can be reopened to modify redirect URLs. |

    !!! note
        The links can be sorted, for example, alphabetically, by status, or by hit count. 

1. Click any link to view the details, change its status, or set the redirect URL:

    ![Broken links details](media/broken-links-details.png){: style="display: block; margin: 0 auto;" }

1. Click **Save** in the toolbar to save the changes.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../catalog/managing-SEO">← Managing SEO</a>
    <a href="../settings">Settings →</a>
</div>