# Using Thumbnails

After successfully generating thumbnails for your images, you can access them simply by adding the desired resolution suffix (defined by the options suffix) to the original image URL.

For instance:

* If the original image is accessible via this URL:

    ```url
    https://localhost/assets/catalog/my-cool-image.jpg
    ```

* And you've generated thumbnails with suffixes `64x64` and `small`, the resulting thumbnail URLs will be:
    1. 
        ```url
        https://localhost/assets/catalog/my-cool-image_64x64.jpg
        ```

    2. 

        ```url
        https://localhost/assets/catalog/my-cool-image_small.jpg
        ```

This makes it easy to retrieve the specific thumbnail you need.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../thumbnail-options">← Managing thumbnail settings</a>
    <a href="../settings">Settings →</a>
</div>