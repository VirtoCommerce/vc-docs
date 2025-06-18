# Search Control Descriptor

This control enables dynamic data retrieval based on user input. It's especially useful for querying product data, verifying inputs, or enriching content blocks with data fetched from external APIs.

It performs one or more backend requests and stores the result in a block's value, making it available for display or further logic.

## Configuration options

| Property      | Type                                         | Description                                                                                       |
| ------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`     | `ServerRequestDescriptor`                    | A single [server request](server-descriptors.md#serverrequestdescriptor) to be executed.          |
| `requests`    | `{ [key: string]: ServerRequestDescriptor }` | Use this to define **multiple requests**, executed sequentially.<br>Ignored if `request` is present. |
| `displayInfo` | `DisplaySearchResult[]`                      | Defines how the response data is displayed inside the control.                                    |
| `nodataText`  | string                                       | Text shown if the request returns no data.                                                        |
| `button`      | boolean <br> string                          | Button text to manually trigger the search.<br>If `false`, the search is triggered on input change.  |


!!! info
    * When a `button` is present, the input field and button are shown together. When `button` is `false`, the request is triggered as the user types.<br>
    * The result of a single `request` is saved to the `value` property of the control.<br>
    * When using `requests`, each request's result is stored under a named key.<br>
    * Sequential execution of `requests` allows one result to be used in the next request (e.g., pass product ID from the first to the second request).


## Single request example

Performs one API call to retrieve product details using a SKU.

??? Example "Single request example"
    ```json
    ...
        "settings": [
            {
                "id": "product",
                "label": "SKU",
                "sort": 1,
                "type": "search",
                "nodataText": "Search by SKU to retrieve product data here",
                "default": {
                    "value": {
                        "id": "9cbd8f316e254a679ba34a900fccb076",
                        "name": "3DR Solo Quadcopter (No Gimbal)",
                        "imgSrc": "/themes/assets/blocks/solo-quadcopter.jpg",
                        "description": "<ul class=\"top-section-list\">&#10;<li class=\"top-section-list-item\">Capture Aerial Photos/Video with a GoPro</li>&#10;<li class=\"top-section-list-item\">Linear Tracking with Cablecam Mode</li>&#10;<li class=\"top-section-list-item\">Follow Me: Tracks Your Mobile Device</li>&#10;<li class=\"top-section-list-item\">HDMI Output on Transmitter</li>&#10;<li class=\"top-section-list-item\">Android and iOS Mobile Apps</li>&#10;<li class=\"top-section-list-item\">Video Game-Style Controls</li>&#10;<li class=\"top-section-list-item\">Return Home and &#34;Safety Net&#34; Modes</li>&#10;<li class=\"top-section-list-item\">One-Button Flying / &#34;Pause&#34; Button</li>&#10;<li class=\"top-section-list-item\">Operate GoPro Through App</li>&#10;<li class=\"top-section-list-item\">Works with Optional Solo Gimbal</li>&#10;</ul>",
                        "price": "$995.99",
                        "url": "3dr-solo-quadcopter-no-gimbal"
                    },
                    "__nodata": false,
                    "__searchQuery": "3DRSOLO"
                },
                "displayInfo": [
                    {
                        "label": "Name",
                        "key": "name"
                    },
                    {
                        "label": "Image",
                        "key": "imgSrc",
                        "type": "image"
                    }
                ],
                "request": {
                    "url": "/api/reverse-proxy/{{location.params.storeId}}/virtocommerce/graphql",
                    "method": "post",
                    "isArray": false,
                    "body": {
                        "operationName": null,
                        "variables": {},
                        "query": "{products(storeId:\"odt\",filter:\"sku:{{__searchQuery}}\",userId:\"\"){items{id,code,name,imgSrc,descriptions{reviewType,content}prices{currency,list{formattedAmount}}seoInfo{semanticUrl}}}}"
                    },
                    "response": {
                        "result": "data.products.items",
                        "isArray": false,
                        "value": [
                            "id",
                            "name",
                            "code",
                            "imgSrc",
                            {
                                "key": "description",
                                "query": "$.descriptions[?(@.reviewType=='QuickReview')].content",
                                "isArray": false
                            },
                            {
                                "key": "price",
                                "query": "$.prices[?(@.currency=='USD')].list.formattedAmount",
                                "isArray": false
                            },
                            {
                                "key": "url",
                                "query": "$.seoInfo.semanticUrl",
                                "isArray": false
                            }
                        ]
                    }
                }
            },
            ...
        ]
    ...
    ```
<br>
<br>


![Search results](media/sku-found-not-found.png){: style="display: block; margin: 0 auto;" }


## Multiple requests example

Uses two API calls: one to get the product by SKU, and another to fetch its price by product ID.

??? Example "Multiple request example"
    ```json
    ...
        "settings": [
            {
                "id": "product",
                "label": "SKU",
                "sort": 1,
                "type": "search",
                "nodataText": "Search by SKU to retrieve product data here",
                "default": {
                    "product": {
                        "id": "9cbd8f316e254a679ba34a900fccb076",
                        "name": "3DR Solo Quadcopter (No Gimbal)",
                        "imgSrc": "/themes/assets/blocks/solo-quadcopter.jpg",
                        "description": "<ul class=\"top-section-list\">&#10;<li class=\"top-section-list-item\">Capture Aerial Photos/Video with a GoPro</li>&#10;<li class=\"top-section-list-item\">Linear Tracking with Cablecam Mode</li>&#10;<li class=\"top-section-list-item\">Follow Me: Tracks Your Mobile Device</li>&#10;<li class=\"top-section-list-item\">HDMI Output on Transmitter</li>&#10;<li class=\"top-section-list-item\">Android and iOS Mobile Apps</li>&#10;<li class=\"top-section-list-item\">Video Game-Style Controls</li>&#10;<li class=\"top-section-list-item\">Return Home and &#34;Safety Net&#34; Modes</li>&#10;<li class=\"top-section-list-item\">One-Button Flying / &#34;Pause&#34; Button</li>&#10;<li class=\"top-section-list-item\">Operate GoPro Through App</li>&#10;<li class=\"top-section-list-item\">Works with Optional Solo Gimbal</li>&#10;</ul>",
                        "url": "3dr-solo-quadcopter-no-gimbal"
                    },
                    "price": {
                        "effectiveValue": "995.99"
                    },
                    "__nodata": false,
                    "__searchQuery": "3DRSOLO"
                },
                "displayInfo": [
                    {
                        "label": "Name",
                        "path": "product.name"
                    },
                    {
                        "label": "Price",
                        "path": "price.effectiveValue"
                    },
                    {
                        "label": "Image",
                        "path": "product.imgSrc",
                        "type": "image"
                    }
                ],
                "requests": {
                    "product": {
                        "url": "/api/reverse-proxy/{{location.params.storeId}}/odt/api/catalog/search/products",
                        "method": "post",
                        "isArray": false,
                        "body": {
                            "objectType": "Product",
                            "storeId": "odt",
                            "catalogId": "4974648a41df4e6ea67ef2ad76d7bbd4",
                            "searchPhrase": "{{__searchQuery}}",
                            "skip": 0,
                            "take": 1
                        },
                        "response": {
                            "result": "items",
                            "isArray": false,
                            "value": [
                                "id",
                                "name",
                                "code",
                                "imgSrc",
                                {
                                    "key": "description",
                                    "query": "$.reviews[?(@.reviewType=='QuickReview')].content",
                                    "isArray": false
                                },
                                {
                                    "key": "url",
                                    "query": "$.seoInfos[0].semanticUrl",
                                    "isArray": false
                                }
                            ]
                        }
                    },
                    "price": {
                        "url": "/api/reverse-proxy/{{location.params.storeId}}/odt/api/products/{{item.product.id}}/prices",
                        "method": "get",
                        "response": {
                            "result": "$",
                            "isArray": false,
                            "value": [
                                "effectiveValue"
                            ]
                        }
                    }
                }
            },
            ...
        ]
    ...
    ```


!!! info

    * `displayInfo` uses the `path` to extract nested values from the response.
    * Each request result is stored under its key (`product`, `price`), accessible in the final display or subsequent requests.

![Value preview](media/default-value-preview.png){: style="display: block; margin: 0 auto;" }


![Readmore](media/readmore.png){: width="25"} [ServerRequestDescriptor](server-descriptors.md#serverrequestdescriptor)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../paragraph">← Paragraph </a>
    <a href="../select">Select →</a>
</div>