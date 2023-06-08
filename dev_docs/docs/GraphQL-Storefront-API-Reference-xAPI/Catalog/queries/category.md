# Category ==~query~==

This connection allows you to search for a specific category.

<br>

<div style="display: flex;">
    <div style="flex: 0 0 50%;">
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
            <th class="tg-0lax"><code>id</code> {==String!==}</th>
            <th class="tg-0lax">Identifies the category.</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td class="tg-0lax"><code>storeId</code> {==String!==}</td>
            <td class="tg-0lax">Specifies the ID of the store to retrieve pages from.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>userId</code> {==String==}</td>
            <td class="tg-0lax">Identifies the user.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>currencyCode</code> {==String!==}</td>
            <td class="tg-0lax">A standardized code representing a specific currency.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>cultureName</code> {==String!==}</td>
            <td class="tg-0lax">Specifies the language.</td>
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
        category (storeId:"B2B-store",
        id:"02fe37dcaeb2458a831011abe43fd335", 
        cultureName:"en-US", currencyCode:"USD")  
        {    
            name    
            code    
            id    
            level    
            path    
            parent    
            {      
                name    
            }  
        }
    }
    ```
    </pre></p>
</div>

<div id="Return" class="tab">
    <p><pre><code>
    {
        "data": {
            "category": {
            "name": "Bolts",
            "code": "cd9312",
            "id": "02fe37dcaeb2458a831011abe43fd335",
            "level": 1,
            "path": "Bolts",
            "parent": null
            }
        }
    }
    </code></pre></p>
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
