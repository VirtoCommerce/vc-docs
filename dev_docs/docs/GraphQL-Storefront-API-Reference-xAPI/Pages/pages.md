# Pages ==~query~==

Page search function helps users retrieve page information from a specific shop in the Virto Commerce xAPI Module. 

<br>

<div style="display: flex;">
    <div style="flex: 0 0 50%;">
        <br>
        <br>
        <code>after</code> {==String==} <br>Defines a cursor value to paginate through the results.<br>
        <code>first</code> {==Int==} <br>Indicates the number of pages in a single query.<br>
        <code>storeId</code> {==String!==}<br>Specifies the ID of the store to retrieve pages from.<br>
        <code>keyword</code> {==String!==}<br>Filters the pages based on a specific keyword.<br>
        <code>cultureName</code> {==String==}<br>Specifies the language.
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
    <p><pre><code>
    {
      pages(storeId: "B2B-store", 
        keyword: "aliases:test", after: "0", first: 30) {
        totalCount
        items {
          relativeUrl
          name
          __typename
        }
      pageInfo {
        startCursor
        endCursor
        hasNextPage
        hasPreviousPage
      }
    }
  }
  </code></pre></p>
</div>

<div id="Return" class="tab">
    <p><pre><code>
    {
  "data": {
    "pages": {
      "totalCount": 1,
      "items": [
        {
          "relativeUrl": "/testpagefrompage",
          "name": "testpagefrompage",
          "__typename": "PageType"
        }
      ],
      "pageInfo": {
        "startCursor": "0",
        "endCursor": "1",
        "hasNextPage": false,
        "hasPreviousPage": false
      }
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
