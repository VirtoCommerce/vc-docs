# ProductType ==~object~==

The `productType` field represents the type or category of the product. It is used to classify products into different categories or types, allowing for easier organization and filtering within the catalog.

<div style="display: flex;">
    <div style="flex: 0 0 45%;">
    <style type="text/css">
    .tg  {border:none;border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:white;border-style:solid;border-width:1px;font-family:'Circular Std', sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:'Circular Std', sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-0pky:nth-child(1),
    .tg .tg-0lax:nth-child(1) {width: 30%;}
    .tg .tg-0pky:nth-child(2),
    .tg .tg-0lax:nth-child(2) {width: 70%;}
    </style>
    <table class="tg" style="undefined;table-layout: fixed; width: 717px">
    <tbody>
      <tr>
        <td class="tg-0pky"><code>id</code> {==String!==}</td>
        <td class="tg-0pky">A unique identifier for the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>code</code> {==String!==}</td>
        <td class="tg-0pky">The SKU of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>catalogId</code> {==String==}</td>
        <td class="tg-0pky">The unique ID of the catalog.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>productType</code> {==String==}</td>
        <td class="tg-0pky">The type of product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>minQuantity</code> {==Int==}</td>
        <td class="tg-0pky">The minimum quantity that can be ordered for the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>maxQuantity</code> {==Int==}</td>
        <td class="tg-0pky">The maximum quantity that can be ordered for the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>outline</code> {==String==}</td>
        <td class="tg-0pky">All parent category IDs relative to the requested catalog, concatenated together.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>slug</code> {==String==}</td>
        <td class="tg-0pky">The URL slug for the product, related to the request.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>name</code> {==String!==}</td>
        <td class="tg-0pky">The name of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>seoInfo</code> {==<a href="../SeoInfo">SeoInfo</a>==}</td>
        <td class="tg-0pky">A list of SEO information associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>descriptions(...)</code> {==<a href="../DescriptionType">DescriptionType</a>==}</td>
        <td class="tg-0pky">A list of descriptions or reviews associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>description(...)`</code> {==<a href="../DescriptionType">DescriptionType</a>==}</td>
        <td class="tg-0pky">A description or review associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>category</code> {==<a href="../category/CategoryType">Category</a>==}</td>
        <td class="tg-0pky">The category to which the product is associated.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>imgSrc</code> {==String==}</td>
        <td class="tg-0pky">The URL or path to the main image of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>outerId</code> {==String==}</td>
        <td class="tg-0pky">The outer identifier of the category to which the product belongs.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>brandName</code> {==String==}</td>
        <td class="tg-0pky">The brand name associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>masterVariation</code> {==<a href="../VariationType">VariationType</a>==}</td>
        <td class="tg-0pky">The main variation of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>variations</code>{==<a href="../VariationType">VariationType</a>==}</td>
        <td class="tg-0pky">A list of variations available for the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>hasVariations</code> {==Boolean==}</td>
        <td class="tg-0pky">Indicates whether the product has variations or not.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>availabilityData</code> {==<a href="../AvailabilityData">AvailabilityData</a>==}</td>
        <td class="tg-0pky">Information about the availability of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>images</code> {==<a href="../ImageType">ImageType</a>==}</td>
        <td class="tg-0pky">A list of images associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>price</code> {==<a href="../Price/PriceType">PriceType</a>==}</td>
        <td class="tg-0pky">The price of the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>prices</code> {==<a href="../Price/PriceType">PriceType</a>==}</td>
        <td class="tg-0pky">A list of prices associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>properties(...)</code> {==<a href="../Property/Property">Property</a>==}</td>
        <td class="tg-0pky">A list of properties or attributes associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>keyProperties</code> {==<a href="../Property/Property">Property</a>==}</td>
        <td class="tg-0pky">A list of key properties associated with the product. The <code>keyProperties</code> field can be limited by the <code>take</code> argument.<details><summary>Configuring <code>keyProperties</code></summary>
        <br>To make a catalog property appear in the keyProperties list:
          <ul>
          <li>Open the platform and go to the <strong>Catalog</strong> module.</li>
          <li>Click the three dots next the name of the required catalog and select <strong>Manage</strong> from the dropdown menu.</li>
          <li>Selects the <strong>Properties</strong> widget.
          <li>In the new blade, select the <strong>Product property</strong> from a list.
          <li>In the <strong>Manage property</strong> blade select <strong>Attributes</strong>.
          <li> Add the KeyProperty attribute to <strong>Current attributes</strong>.<code>KeyProperties</code> are automatically sorted in ascending order based on the attribute value.</li>
        </ul>
        <br>
        <img src="../media/KeyPropertiesAttr.png" alt="Image description">
        </details> </td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>assets</code> {==<a href="../Asset">Asset</a>==}</td>
        <td class="tg-0pky">A list of assets associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>outlines</code> {==<a href="../OutlineType/OutlineType">OutlineType</a>==}</td>
        <td class="tg-0pky">A list of category outlines for the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>breadcrumbs</code> {==<a href="../Breadcrumb">Breadcrumb</a>==}</td>
        <td class="tg-0pky">Product navigation information in the form of breadcrumbs.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>vendor</code> {==<a href="../Commonvendor">CommonVendor</a>==}</td>
        <td class="tg-0pky">The vendor associated with the product.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>inWishlist</code> {==Boolean!==}</td>
        <td class="tg-0pky">Indicates whether the product is in the user's wishlist or not.</td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>associations(...)</code> {==<a href="../ProductAssociation/ProductAssociationConnection">ProductAssociationConnection</a>==}</td>
        <td class="tg-0pky">The associations or relationships of the product with other products. This field is resolved using the object. </td>
      </tr>
      <tr>
        <td class="tg-0pky"><code>videos(...)</code> {==<a href="../VideoConnection">VideoConnection</a>==}</td>
        <td class="tg-0pky">The videos associated with the product.</td>
      </tr>
    </tbody>
    </table>
    </div>
    <div style="flex: 0 0 5%;">
    </div>
    <div style="flex: 0 0 50%;">
        <style>
    .tab {
        display: none;
    }

    .tab.active {
        display: block;
    }

    .tab-button {
        background-color: #f2f2f2;
        border: none;
        color: #000;
        padding: 8px 16px;
        cursor: pointer;
    }

    .tab-button.active {
        background-color: #ccc;
    }
</style>

<div>
    <button class="tab-button" onclick="openTab('Query')">Query</button>
    <button class="tab-button" onclick="openTab('Return')">Return</button>
</div>

<div id="Query" class="tab active">
    <p><pre>
    ```json
    query {
      products(
        storeId: "B2B-store"
        cultureName: "en-US"
      ) {
        items 
        {
          keyProperties (take:3) {
            name
            value
            label
            displayOrder
            propertyDictItems
            {
              pageInfo
              {
                endCursor
                hasNextPage
                hasPreviousPage
              }
              totalCount
              items
              {
                sortOrder
                __typename
                value
              }
            }
            id
            type
          }
        }
      }
    }
    ```
    </pre></p>
</div>

<div id="Return" class="tab">
    <p><pre>
    ```json
    {
      "data": {
        "products": {
          "items": [
            {
              "keyProperties": []
            },
            {
              "keyProperties": []
            },
            {
              "keyProperties": []
            },
            {
              "keyProperties": []
            }
          ]
        }
      }
    }
    ```
    </pre></p>
</div>

<script>
    function openTab(tabName) {
        var tabs = document.getElementsByClassName("tab");
        for (var i = 0; i < tabs.length; i++) {
            tabs[i].classList.remove("active");
        }
        document.getElementById(tabName).classList.add("active");

        var tabButtons = document.getElementsByClassName("tab-button");
        for (var j = 0; j < tabButtons.length; j++) {
            tabButtons[j].classList.remove("active");
        }
        document.querySelector('[onclick="openTab(\'' + tabName + '\')"]').classList.add("active");
    }
</script>

    </div>
</div>
