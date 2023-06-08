# Product ==~query~==

This query allows you to get a product by its Id and calculate all fields based on the parameters being sent. 

<div style="display: flex;">
    <div style="flex: 0 0 45%;">
        <style type="text/css">
        .tg  {border:none;border-collapse:collapse;border-spacing:0;}
        .tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
          overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
          font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
        .tg .tg-zv4m:nth-child(odd) {width: 40%;}
        .tg .tg-zv4m:nth-child(even) {width: 60%;}
        </style>
        <table class="tg">
        <tbody>
        <tr>
            <td class="tg-zv4m"><code>id</code> {==String!==} </td>
            <td class="tg-zv4m">Product Id.</td>
        </tr>
        <tr>
            <td class="tg-zv4m"><code>storeId</code> {==String!==} </td>
            <td class="tg-zv4m">Store Id.</td>
        </tr>
        <tr>
            <td class="tg-zv4m"><code>userId</code> {==String==}</td>
            <td class="tg-zv4m">Current user Id.</td>
        </tr>
        <tr>
            <td class="tg-zv4m"><code>currencyCode</code> {==String==}</td>
            <td class="tg-zv4m">A code of a specific currency.</td>
        </tr>
        <tr>
            <td class="tg-zv4m"><code>cultureName</code> {==String==}</td>
            <td class="tg-zv4m">A language to retrieve data in.</td>
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
      product(
          id: "8b7b07c165924a879392f4f51a6f7ce0"
          storeId: "Electronics"
          userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
          cultureName: "en-us"
          currencyCode: "USD")
      {
        id
        name
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
        "product": {
          "id": "8b7b07c165924a879392f4f51a6f7ce0",
          "name": "ASUS ZenFone 2 ZE551ML 16GB Smartphone"
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
        product(
                id:"9cbd8f316e254a679ba34a900fccb076" 
                storeId:"Electronics"
                currencyCode:"USD")
        {
            prices
            {
            minQuantity
            tierPrices
            {
                quantity
                price
            {
                amount
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
            "product": {
            "prices": [
                {
                "minQuantity": 1,
                "tierPrices": [
                    {
                    "quantity": 1,
                    "price": {
                        "amount": 995.99
                    }
                    }
                ]
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
