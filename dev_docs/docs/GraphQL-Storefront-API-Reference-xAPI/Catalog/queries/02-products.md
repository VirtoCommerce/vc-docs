# Products ==~query~==

This connection allows you to search for products.

<br>

<div style="display: flex;">
    <div style="flex: 0 0 50%;">
        <style type="text/css">
        .tg  {border:none;border-collapse:collapse;border-spacing:0;}
        .tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
          overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
          font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-0pky{border-color:#ffffff;text-align:left;vertical-align:top}
        .tg .tg-0lax{text-align:left;vertical-align:top}
        .tg .tg-0pky:nth-child(1),
        .tg .tg-0lax:nth-child(1) {width: 45%;}
        .tg .tg-0pky:nth-child(2),
        .tg .tg-0lax:nth-child(2) {width: 55%;}
        </style>
        <table class="tg">
        <tbody>
        <tr>
            <td class="tg-0pky"><code>after</code> {==String==}</th>
            <td class="tg-0pky">Defines a cursor value to paginate through the results.</th>
        </tr>
        <tr>
            <td class="tg-0pky"><code>first</code> {==Int==}</td>
            <td class="tg-0pky">Indicates the number of pages in a single query.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>storeId</code> {==String!==}</td>
            <td class="tg-0pky">Specifies the ID of the store to retrieve pages from.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>userId</code> {==String==}</td>
            <td class="tg-0pky">Identifies the user.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>currencyCode</code> {==String==}</td>
            <td class="tg-0pky">A standardized code representing a specific currency.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>query</code> {==String==}</td>
            <td class="tg-0pky">Performs the full-text search.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>cultureName</code> {==String==}</td>
            <td class="tg-0pky">Specifies the language.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>filter</code> {==String==}</td>
            <td class="tg-0pky">Applies a filter to the query results.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>fuzzy</code> {==Boolean==}</td>
            <td class="tg-0pky">If true, includes slight variations of the search text in the returned products.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>fuzzyLevel</code> {==Int==}</td>
            <td class="tg-0pky">The fuzziness level is measured by the Damerau-Levenshtein distance.It calculates the number of operations required to transform one word into another.</td>
        </tr>
        <tr>
            <td class="tg-0pky"><code>facet</code> {==String==}</td>
            <td class="tg-0pky">Calculates statistical counts to aid in faceted navigation.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>sort</code> {==String==}</td>
            <td class="tg-0lax">Specifies the sorting order of the returned products.</td>
        </tr>
        <tr>
            <td class="tg-0lax"><code>productIds</code> {==String==}</td>
            <td class="tg-0lax">Identifies specific products within a given store.</td>
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
        products(
            storeId: "Electronics"
            userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
            cultureName: "en-Us"
            currencyCode: "USD"
  	        first: 10
  	        after: "10")
        {
            items
            {
                id
                code
            }
            pageInfo
            {
                hasNextPage
                startCursor
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
              "id": "7c835a9b1c8e4445aa118dae659231c3",
              "code": "SAG920F32GBB"
            },
            {
              "id": "8db64bd60a354c4c96e25e61d7361565",
              "code": "LG65EG9600"
            },
            {
              "id": "8e3a763a3cff407b97e2a2f6390b4048",
              "code": "SAHTJ5500W"
            },
            {
              "id": "92e671024a8648de97dedcd488f58455",
              "code": "SUDS3214PSL"
            },
            {
              "id": "be4ab6701f84440ea84ccd09210cbe0a",
              "code": "VIM70C3"
            }
        ],
        "pageInfo": {
            "hasNextPage": true,
            "startCursor": "10"
        }
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
