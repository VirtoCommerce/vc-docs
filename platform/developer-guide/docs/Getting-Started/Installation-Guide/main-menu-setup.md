# Main Menu Setup

Let's create the following dropdown menu:

![Dropdown menu](media/catalog-categories.png)

1. Use [this guide](https://docs.virtocommerce.org/platform/user-guide/content/managing-linklists/) to add links:

    1. Add root categories:

        ![Root categories](media/root-categories.png)

    1. Add subcategories to each root category:

        ![Link lists](media/link-lists.png)

    1. Click **Save** in the toolbar.

1. Check that the **Top level catalog linked list** is correctly specified (dental-store in our case) in your store settings (**Stores** --> **Dental Demo Store** --> **Settings** widget).
1. Check that the **catalog_menu_link_list_name** is correctly specified (dental-store in our case) in the **settings_data.json** file (**Content** --> **Dental Demo Store** --> **Themes** --> **default** -- **config** --> **settings_data.json**):

    ![Theme settings](media/theme-settings.png)

    Reboot the environment in the Cloud Portal if required.

The dropdown menu appears in the Frontend Application.