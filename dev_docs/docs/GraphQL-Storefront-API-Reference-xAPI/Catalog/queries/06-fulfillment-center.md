# fulfillmentCenter ==~query~==

This query allows you to get a fulfillment center by its Id.
<br>
<br>
<br>

<div style="display: flex;">
    <div style="flex: 0 0 40%;">
    <style type="text/css">
    .tg  {border:none;border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-0pky:nth-child(1),
    .tg .tg-0lax:nth-child(1) {width: 30%;}
    .tg .tg-0pky:nth-child(2),
    .tg .tg-0lax:nth-child(2) {width: 70%;}
    </style>
    <table class="tg">
    <thead>
      <tr>
        <td class="tg-0lax"><code>id</code> {==String!==}</td>
        <td class="tg-0lax">Identifies the fullfillment center.</td>
      </tr>
    </thead>
    </table>
    </div>
    <div style="flex: 0 0 60%;">
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
    {
      fulfillmentCenter(
        id: "vendor-fulfillment"
      ) {
        id
        name
        description
        shortDescription
        outerId
        geoLocation
        address {
          city
        }
        nearest (take: 3) {
          name
          id
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
          "fulfillmentCenter": {
            "id": "vendor-fulfillment",
            "name": "Los Angeles Branch",
            "description": "<h3>Open 24/7</h3>,
            "shortDescription": null,
            "outerId": null,
            "geoLocation": null,
            "address": {
              "city": "Los Angeles"
            },
            "nearest": [
              {
                "name": "Chicago Branch",
                "id": "142ba5568ae4454aad553ece41b9c3b5"
              },
              {
                "name": "New York Branch",
                "id": "c20d27cdb09c4c7abd5d78a71510ab83"
              },
              {
                "name": "Tennessee Branch",
                "id": "tulsa-branch"
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
