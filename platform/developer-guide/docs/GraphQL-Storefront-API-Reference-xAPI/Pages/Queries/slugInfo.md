# slugInfo ==~query~==  

This query retrieves information about an entity associated with a specific permalink, such as its status, language, and type.  

## Arguments  

| Argument                  | Description                                                                  |  
|---------------------------|-----------------------------------------------------------------------------------|
| `slug` ==String==         | The URL slug, related to the request.  |
| `permalink` ==String==    | The unique permalink of the entity (e.g., a page URL).                          |  
| `storeId` ==String==      | The store ID associated with the permalink.                                     |  
| `userId` ==String==    | The current user Id.                          |  
| `cultureName` ==String==  | A language to retrieve data in.               |  

## Possible Returns  

| Possible Return                                                   | Description                                                                    |  
|-------------------------------------------------------------------|------------------------------------------------------------------------------------|  
| [`SlugInfoResponseType`](../Objects/SlugInfoResponseType.md)      | Details of the entity, including its ID, status, language, type, and semantic URL. |  


## Examples  

=== "Query"  
    ```json linenums="1"  
    {  
      slugInfo(  
        permalink: "/test-2"  
        storeId: "B2B-store"  
        cultureName: "en-US"  
      ) {  
        entityInfo {  
          id  
          isActive  
          languageCode  
          objectId  
          objectType  
          semanticUrl  
          __typename  
        }  
        __typename  
      }  
    }  
    ```  

=== "Return"  
    ```json linenums="1"  
    {  
      "data": {  
        "slugInfo": {  
          "entityInfo": {  
            "id": "24caa0d5a05145f3a3433a2930fbfb0f",  
            "isActive": true,  
            "languageCode": "en-US",  
            "objectId": "24caa0d5a05145f3a3433a2930fbfb0f",  
            "objectType": "Pages",  
            "semanticUrl": "/test-2",  
            "__typename": "SeoInfo"  
          },  
          "__typename": "SlugInfoResponseType"  
        }  
      }  
    }  
    ```  