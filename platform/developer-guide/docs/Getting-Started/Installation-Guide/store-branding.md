# Store Branding

Once your store is created, you can customize its branding by:

* Replacing the default Virto Commerce logo and favicon with your own.
* Updating the native theme colors to reflect your corporate brand.
* Changing the default Virto Commerce sliders to your company sliders.
* Adding a custom background (banner) to enhance the store’s visual appeal.

To brand your store, complete the following steps:

1. [Upload your logos and background.](store-branding.md#upload-logos-and-homepage-background)
1. [Specify the paths to the images.](store-branding.md#specify-paths-to-images)
1. [Upload favicons.](store-branding.md#upload-favicons)
1. [Add theme presets.](store-branding.md#add-presets)
1. [Reboot your environment to apply the changes.](store-branding.md#reboot-environment)

Prepare the following images in advance:

![Images in advance](media/images-explanation.png)

## Upload logos and homepage background

!!! note
    Acceptable image formats are SVG and PNG. 

To add your company's branded images:

1. Click **Content** in the main menu.
1. In the next blade, select your store, then click **Themes**.
1. Choose **default** in the next blade.
1. Go to **static** → **images**.
1. In the **images** blade, click **Add** in the toolbar to create a folder for your company images, enter a folder name, and click **Create**:

    ![Create folder](media/create-images-folder.png)

1. Select the newly created folder. For better organization, create two subfolders: **home** for banners and sliders, and **logos** for logos:

    ![Subfolders](media/home-logos-folders.png)

1. In the **Logos** folder, click **Upload** to upload your company logos.
1. Copy and save the links to your logos to use in the next step:

    ![Copy link](media/copy-link-to-favicon.png)

1. Similarly, upload background and sliders to the **home** folder. Copy and save the links to your slider and banner to use in the next step.

Your branded images are now uploaded.


## Specify paths to images

To specify the paths for the uploaded images:

1. Go to **Content** → **Your store** → **Theme** → **default** → **config** → **settings_data.json**.
1. In the settings file, add the links to your logo and homepage background from the previous step:

    ![Add data to settings](media/add-data-to-settings.png)

1. Click **Save** in the toolbar to apply the changes.

The paths to your images have been saved.

## Upload favicons

1. Go to **Content** → **Your store** → **Theme** → **default** → **static** → **icons**.
1. In the **icons** blade, click **Add** to create a folder for your company icons, name the folder, and click **Create**.
1. Select the new folder, and click **Upload** to add your company icons/favicons.
1. Copy the favicon link and paste it into **Content** → **Your store** → **Theme** → **default** → **config** → **settings_data.json** as you did before with the logos and the background. 
1. Paste the favicon link into **Content** → **Your store** → **Theme** → **default** → **static** → **manifest.json** and specify the favicon size.

    ![Manifest](media/add-favicons-to-manifest.png)

1. Click **Save** in the toolbar to confirm your changes.

Your favicons are now set up for use in your store.

## Add presets

Below is the breakdown of the main colors in the color scheme:

![Color scheme](media/colors-explanation.png)

To configure a custom color scheme:

1. Go to **Content** → **Your store** → **Theme** → **default** → **config** → **presets**.
1. Click **Add** in the toolbar to create a new color scheme.
1. In the next blade, enter your color scheme name.
1. Paste your custom color scheme.

    !!! note
        You can [create your own color scheme using ChatGPT](../../../../user-guide/content/managing-themes#create-theme-colors-via-chatgpt).

1. Click **Create** to add the color scheme to the list.
1. Copy the filename of your color scheme and paste it into the config file to set it as the default:

    ![Paste link to scheme](media/add-scheme-name-to-config.png)

1. Click **Save** in the toolbar to save the changes. 

Your new color scheme has been added.



## Reboot environment

!!! tip
    If you need assistance at this or any other step, feel free to [contact our support](https://help.virtocommerce.com/support/home).

To apply all branding modifications, reboot your environment:

1. In the Virto Cloud Portal, click **Environments** in the main menu.
1. Select the environment to be branded.
1. In the next blade, click on the **Applications** widget.
1. In the next blade, click ![Paper sheet](media/paper-sheet.png){: width="20"} next to **Platform**.
1. Specify the number of reboot attempts:

    ![Reboot attempts](media/reboot-attempts.png)

1. Click **Save** in the current blade, and then again in the previous blade.

    !!! note
        If the changes are not applied after the first reboot, change the number of reboot attempts and save the changes again. You may need multiple reboots for your modifications to take effect.

1. In the **Environments** blade, click **Refresh**.

Wait for the environment to update: The **Progressing** status changes to **Synced**. Your store's branding changes will now be applied:

![Branded store](media/branded-shop.png)
