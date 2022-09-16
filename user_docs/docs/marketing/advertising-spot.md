# Adding Advertising Spot

Adding an advertising spot to your website or online store is your last step to bringing your marketing content online. This involves adding a specific piece of HTML code (see below) that will actually publish your content and make it visible for your customers. 

Logically, prior to creating your advertising spot, you will first need to:  

1. [Create a content item](managing-content-items.md)
2. [Create a content placeholder](managing-content-placeholders.md)
3. [Create published content](managing-published-content.md)

Once these prerequisites are complete, you will be able to add the dynamic content to your website:  

1. Open your web page HTML file.
1. Insert the following code into the file, the ID being the name of the relevant placeholder:

```html
<vc-content-place id="Right banner 240x400" class="col-sm-4 col-md-4 rightblock">
</vc-content-place>
```