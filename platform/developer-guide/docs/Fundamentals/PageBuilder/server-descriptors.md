# Server Descriptors

This guide explains how to configure external data requests using the `ServerRequestDescriptor` and `ServerResponseDescriptor` interfaces. These descriptors allow developers to define dynamic data sources for controls like dropdowns and search fields, supporting a wide range of APIs and formats.

## ServerRequestDescriptor

The `ServerRequestDescriptor` interface defines how the Page Builder fetches external data from a server. It is used in [builder settings](./builder-settings.md) and in dynamic controls like [search](./controls/search.md) and [select](./controls/select.md).

This descriptor allows you to configure all aspects of the HTTP request: the target URL, HTTP method, request payload, headers, and more. It also supports caching and request initialization logic, making it flexible for use in various data-driven builder scenarios.

## Properties

| Property        | Type                     | Description                                                                                                                                           |
|-----------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `url`           | string                   | Target URL of the request.                                                                                                                            |
| `method`        | string                   | HTTP method to use (e.g., `GET`, `POST`).                                                                                                             |
| `body`          | any                      | Optional request payload (typically used with `POST` or `PUT`).                                                                                       |
| `form`          | any                      | Optional form data to send in the request.                                                                                                            |
| `options`       | any                      | Additional fetch options like custom headers, credentials, etc.                                                                                       |
| `response`      | `ServerResponseDescriptor` | Describes how the response should be interpreted.                                                                                                     |
| `cacheable`     | boolean                  | If true, the request result will be cached to improve performance.                                                                                    |
| `init`          | boolean <br> string        | If true, the request runs when the settings are loaded.<br>If a string, it references a property in the settings<br> where the descriptor is defined. |
| `fallbackValue` | any                      | A default value used if the request fails (e.g., network error).                                                                                      |


**Example**

```json
{
  "url": "https://api.example.com/categories",
  "method": "GET",
  "response": {
    "result": "$.data.categories[*]", 
    "isArray": true,
    "value": [
      {
        "label": "$.name",
        "value": "$.id"
      }
    ]
  },
  "cacheable": true
}
```



## ServerResponseDescriptor

The `ServerResponseDescriptor` interface describes how the Page Builder should extract and transform the server response. This makes it easy to use APIs that return nested or structured data.

### Properties

| Property   | Type    | Description                                                                                    |
|------------|---------|------------------------------------------------------------------------------------------------|
| `selector` | string  | JavaScript expression to evaluate on the response. Useful for extracting or transforming data. |
| `result`   | string  | JSONPath expression that points to the desired result field within the response.               |
| `isArray`  | boolean | If true, the result is treated as a list (e.g., for dropdown options).                       |
| `value`    | string <br> (string \| `SelectValueDescriptor`)[] | Resulting value(s). Can be a primitive or an array of values or objects <br>(for `select` control options). |

**Example**

```json
{
  "url": "https://api.example.com/config",
  "method": "GET",
  "init": true,
  "response": {
    "result": "$.defaults.language",
    "isArray": false,
    "value": "$"
  },
  "fallbackValue": "en"
}
```