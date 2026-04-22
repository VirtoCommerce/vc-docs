# Preview Pages as User

Page Builder supports previewing pages as a specific Frontend user type (anonymous, admin, agent, employee, etc.). 

Use preview as user when:

* Your store requires login because anonymous access is disabled.
* Preview shows **Anonymous access denied** errors for product blocks.
* You want to see how a page looks for a specific user type.

## Configure preview users

Let's preview the Frontend with the eyes of an reseller:

1. Copy  their IDs:

    1. Open **Security** from the main menu.
    1. In the next blade, select **Users**.
    1. In the next blade, find the user you want to preview as, a reseller in our case.
    1. Right-click the user and select **Copy ID** from the popup menu.
    1. Repeat for each user you want available in preview.

1. Add user IDs to the store settings:

    1. Open **Stores** from the main menu.
    1. In the next blade, select your store.
    1. In the next blade, click on the **Settings** widget.
    1. Open **CMS Content** --> **Page Builder** --> **Preview user IDs**:
    1. Paste the copied user IDs, one per line.
    1. Click **OK**, then **Save** in the toolbar.

Your modifications have been applied.

## Preview page as user

To preview a page as a specific user:

1. Open the page in Page Builder Designer.
1. In the toolbar, select your user from the dropdown. By default, it shows **Anonymous**.

The preview reloads with the selected user's authentication context. Product blocks, personalized content, and other authenticated data now display correctly.

To switch users, click the dropdown again and select another user. To return to the unauthenticated preview, select **Anonymous**.

!!! note
    * The preview users list is configured per store. Each store has its own list.
    * If the **Preview user Ids** setting is empty, the user icon does not appear in the toolbar.
    * Impersonation affects preview only. It does not change any data or affect the actual storefront.

Try our interactive demo to explore the flow in action:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.57% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/i78fuff5lhjv?embed=popup" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../manage-pages">← Managing pages via Page Builder office </a>
    <a href="../../pages/overview">Pages module overview →</a>
</div>