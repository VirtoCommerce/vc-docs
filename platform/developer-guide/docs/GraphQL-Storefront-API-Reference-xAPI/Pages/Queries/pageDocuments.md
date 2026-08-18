# pageDocuments ==~query~==  

This query retrieves a list of page documents that match specified search criteria, such as store Id, keyword, or culture name.  

## Arguments  

| Argument                | Description                                     |  
|-------------------------|-------------------------------------------------|  
| `after` ==String==      | A cursor value to paginate through the results. |  
| `first` ==Int==         | The number of pages in a single query.          |  
| `storeId` ==String!==    | The Id of the store to retrieve pages from.    |  
| `keyword` ==String!==    | The keyword for searching page content.        |  
| `cultureName` ==String== | A language to retrieve data in.                |  

## Possible returns  

| Possible return                                                        | Description                                                                        |  
|------------------------------------------------------------------------|------------------------------------------------------------------------------------|  
| [`PageDocumentConnection`](../Objects/PageDocumentConnection.md)       | A list of page documents, including their ID, source, permalink, and content.      |  

## Example

<div class="grid" markdown>

```json title="Query"
{  
  pageDocuments(after: "0", first: 10, storeId: "B2B-store", keyword: "tv", cultureName: "en-US") {  
    totalCount  
    items {  
      id  
      source  
      permalink  
      content  
    }  
  }  
}  
```

```json title="Return"
{  
  "data": {  
    "pageDocuments": {  
      "totalCount": 16,  
      "items": [  
        {  
          "id": "9911349254704e3596ddbe9136fc8273",  
          "source": "builder.io",  
          "permalink": "/televisions-d",  
          "content": "..."  
        }  
        // Additional pages...  
      ]  
    }  
  }  
}  
```

</div>