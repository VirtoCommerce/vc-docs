# Properties ==~query~==

This connection allows you to search for catalog property metadata.

<br>

<div style="display: flex;">
    <div style="flex: 0 0 45%;">
        <style type="text/css">
      .tg  {border:none;border-collapse:collapse;border-spacing:0;}
      .tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
        overflow:hidden;padding:10px 5px;word-break:normal;}
      .tg th{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
        font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
        .tg .tg-0pky:nth-child(1),
        .tg .tg-0lax:nth-child(1) {width: 40%;}
        .tg .tg-0pky:nth-child(2),
        .tg .tg-0lax:nth-child(2) {width: 60%;}
        </style>
        <table class="tg">
        <thead>
          <tr>
            <th class="tg-0lax"><code>after</code> {==String==}</th>
            <th class="tg-0lax">Defines a cursor value to paginate through the results.</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="tg-0lax"><code>first</code> {==Int==}</td>
            <td class="tg-0lax">Indicates the number of pages in a single query.</td>
          </tr>
          <tr>
            <td class="tg-0lax"><code>storeId</code> {==String!==}</td>
            <td class="tg-0lax">Specifies the ID of the store to retrieve pages from.</td>
          </tr>
          <tr>
            <td class="tg-0lax"><code>types</code> {==PropertyType==}</td>
            <td class="tg-0lax">Specifies the type of property to retrieve.</td>
          </tr>
          <tr>
            <td class="tg-0lax"><code>filter</code> {==String==}</td>
            <td class="tg-0lax">Applies a filter to the query results.</td>
          </tr>
          <tr>
            <td class="tg-0lax"><code>cultureName</code> {==String==}</td>
            <td class="tg-0lax">Specifies the language.</td>
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
      properties (storeId:"Electronics", cultureName:"de-DE", 
      filter:"keyword:Brand", types:[PRODUCT, VARIATION])
      {
        items
        {
          name
          type
          id
          multivalue
          propertyDictItems
          {
            totalCount
            items
            {
              value
            }
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
        "properties": {
          "items": [
            {
              "name": "Brand",
              "type": "Product",
              "id": "43d14478-d142-4a65-956f-0a308d0c4ee8",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 21,
                "items": [
                  {
                    "value": "3DR"
                  },
                  {
                    "value": "Apple"
                  },
                  {
                    "value": "Asus"
                  },
                  {
                    "value": "Beats By Dr Dre"
                  },
                  {
                    "value": "BLU"
                  },
                  {
                    "value": "DJI"
                  }
                ]
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
      properties (storeId:"Electronics", 
      filter:"categoryId:53e239451c844442a3b2fe9aa82d95c8")
      {
        items
        {
          name
          type
          id
          multivalue
          propertyDictItems
          {
            totalCount
            items
            {
              value
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
        "properties": {
          "items": [
            {
              "name": "Camcorder_Type",
              "type": "Category",
              "id": "4af9a56f-fcf2-4a2d-b5bb-8b979ae38f9b",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 0,
                "items": []
              }
            },
            {
              "name": "Features",
              "type": "Product",
              "id": "1b91897a-19d4-41d9-97db-9b3b2bd3637b",
              "multivalue": false,
              "propertyDictItems": {
                "totalCount": 4,
                "items": [
                  {
                    "value": "3D"
                  },
                  {
                    "value": "GPS"
                  },
                  {
                    "value": "Waterproof"
                  },
                  {
                    "value": "Wi-Fi"
                  }
                ]
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
