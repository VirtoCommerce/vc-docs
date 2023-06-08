# childCategories ==~query~==

This query allows you to retrieve a list of child categories for a given parent category. You can also retrieve their names, ids, and urls. This information can be used to build custom user interfaces or to retrieve data for other purposes within your application.

<br>

<div style="display: flex;">
    <div style="flex: 0 0 50%;">
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
        <tbody>
        <tr>
            <td class="tg-0lax"><code>storeId</code> {==String==}</th>
            <td class="tg-0lax">Specifies the ID of the store to retrieve pages from.</th>
        </tr>
        <tr>
            <td class="tg-0lax"><code>userId</code> {==String==}</td>
            <td class="tg-0lax">Identifies the user.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>cultureName</code> {==String==}</td>
            <td class="tg-0lax">Specifies the language.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>currencyCode</code> {==String==}</td>
            <td class="tg-0lax">A standardized code representing a specific currency.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>categoryId</code> {==String==}</td>
            <td class="tg-0lax">Filters the child categories based on a specific category ID.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>maxLevel</code> {==Int==}</td>
            <td class="tg-0lax">Determines the maximum depth or level of child categories to retrieve.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>onlyActive</code> {==Boolean==}</td>
            <td class="tg-0lax">Indicates whether only active child categories should be included in the results.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>productFilter</code> {==String==}</td>
            <td class="tg-0lax">Specifies filtering criteria for the products within the child categories.</td>
        </tr>
        </tbody>
        </table>
    </div>
    <div style="flex: 0 0 10%;">
    </div>
    <div style="flex: 0 0 40%;">
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
    childCategories(storeId:"B2B-Store",
    cultureName:"en-US",
    currencyCode:"USD",
    maxLevel:1
    productFilter:
    "category.subtree:fc596540864a41bf8ab78734ee7353a3 
    price:(0 TO) instock_quantity:(0 TO)" ),
    {
        childCategories {
        name
        id
        code
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
        "childCategories": {
        "childCategories": [
            {
            "name": "Bolts",
            "id": "02fe37dcaeb2458a831011abe43fd335",
            "code": "cd9312"
            },
            {
            "name": "Printers",
            "id": "d6019d4d27e44854a58ebbd5428b873b",
            "code": "b76cb"
            },
            {
            "name": "Test",
            "id": "ef80faed-03b6-42ac-bfae-cfdace0981e7",
            "code": "a7dec"
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
