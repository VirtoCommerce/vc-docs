# fullfillmentCenters ==~query~==

This connection allows you to search for fulfillment centers.
<br>
<br>
<div style="display: flex;">
    <div style="flex: 0 0 45%;">
    <style type="text/css">
    .tg  {border:none;border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-0pky:nth-child(1),
    .tg .tg-0lax:nth-child(1) {width: 40%;}
    .tg .tg-0pky:nth-child(2),
    .tg .tg-0lax:nth-child(2) {width: 60%;}
    </style>
    <table class="tg">
      <tr>
        <td class="tg-0lax"><code>after</code> {==String==}</th>
        <td class="tg-0lax">Defines a cursor value to paginate through the results.</th>
      </tr>
    <tbody>
      <tr>
        <td class="tg-0lax"><code>first</code> {==Int==}</td>
        <td class="tg-0lax">Indicates the number of pages in a single query.</td>
      </tr>
      <tr>
        <td class="tg-0lax"><code>storeId</code> {==String==}</td>
        <td class="tg-0lax">Specifies the ID of the store to retrieve pages from.</td>
      </tr>
      <tr>
        <td class="tg-0lax"><code>query</code> {==String==}</td>
        <td class="tg-0lax">Performs the full-text search.</td>
      </tr>
      <tr>
        <td class="tg-0lax"><code>sort</code> {==String==}</td>
        <td class="tg-0lax">Specifies the sorting order of the returned products.</td>
      </tr>
      <tr>
        <td class="tg-0lax"><code>fullfillmentCenters</code><br>{==String==}</td>
        <td class="tg-0lax">Identifies fullfillment centers.<br>This argument is exclusive! If set, it overrides all other arguments.</td>
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
    <button class="tab-button" onclick="openTab('Query 1')">Query 1</button>
    <button class="tab-button" onclick="openTab('Return 1')">Return 1</button>
    <button class="tab-button" onclick="openTab('Query 2')">Query 2</button>
    <button class="tab-button" onclick="openTab('Return 2')">Return 2</button>
</div>

<div id="Query 1" class="tab active">
    <p><pre>
    ```json
    {
      fulfillmentCenters(
        fulfillmentCenterIds: ["vendor-fulfillment", "los-angeles-fulfillment"]
      ) {
        totalCount
        items {
          id
          name
          shortDescription
          address {
            city
            countryCode
          }
        }
      }
    }
    ```
    </pre></p>
</div>

<div id="Return 1" class="tab">
    <p><pre>
    ```json
    {
      "data": {
        "fulfillmentCenters": {
          "totalCount": 1,
          "items": [
            {
              "id": "vendor-fulfillment",
              "name": "Los Angeles Branch",
              "shortDescription": null,
              "address": {
                "city": "Los Angeles",
                "countryCode": "USA"
              }
            }
          ]
        }
      }
    }    
    ```
    </pre></p>
</div>

<div id="Query 2" class="tab">
    <p><pre>
    ```json
    {
      products (storeId:"B2B-store")
      {
        items{
          name
          availabilityData
          {
            isActive
            inventories
            {
              fulfillmentCenterId
              fulfillmentCenterName
              inStockQuantity
            }
          }
        }
      }
    }
    ```
    </pre></p>
</div>

<div id="Return 2" class="tab">
    <p><pre>
    ```json
    {
      "data": {
        "products": {
          "items": [
            {
              "name": "SunBriteTV DS-3214P-BL 32\" Weatherproof LED - Portrait Mode (Black)",
              "availabilityData": {
                "isActive": true,
                "inventories": [
                  {
                    "fulfillmentCenterId": "tulsa-branch",
                    "fulfillmentCenterName": "Tennessee Branch",
                    "inStockQuantity": 760
                  },
                  {
                    "fulfillmentCenterId": "142ba5568ae4454aad553ece41b9c3b5",
                    "fulfillmentCenterName": "Chicago Branch",
                    "inStockQuantity": 10
                  },
                  {
                    "fulfillmentCenterId": "vendor-fulfillment",
                    "fulfillmentCenterName": "Los Angeles Branch",
                    "inStockQuantity": 5
                  }
                }
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
