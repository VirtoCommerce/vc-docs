# pageDocument ==~query~==  

This query retrieves information about a specific page document using its unique Id.  

## Arguments  

| Argument        | Description                         |  
|-----------------|-------------------------------------|  
| `id` ==String!== | The unique Id of the page document. |  

## Possible returns  

| Possible return                                                        | Description                                                                        |  
|------------------------------------------------------------------------|------------------------------------------------------------------------------------|  
| [`PageDocumentType`](../Objects/PageDocumentType.md)                   | Information about the page document, including its source, permalink, and content. |  

## Examples  

=== "Query"  
    ```json linenums="1"  
    {  
      pageDocument(id: "24caa0d5a05145f3a3433a2930fbfb0f") {  
        id  
        source  
        permalink  
        content  
      }  
    }  
    ```  

=== "Return"  
    ```json linenums="1"  
    {  
      "data": {  
        "pageDocument": {  
          "id": "24caa0d5a05145f3a3433a2930fbfb0f",  
          "source": "builder.io",  
          "permalink": "/test-2",  
          "content": "..."  
        }  
      }  
    }  
    ```  