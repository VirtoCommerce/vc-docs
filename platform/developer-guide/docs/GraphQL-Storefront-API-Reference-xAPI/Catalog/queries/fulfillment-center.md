# FulfillmentCenter ==~query~==

This query allows you to get a fulfillment center by its Id.

## Argument

| Argument           	| Description                         	|
|--------------------	|-------------------------------------	|
| `id`  ==String!==  	| The Id of the fulfillment center. 	  |

## Possible returns

| Possible return                                	                    | Description                       	|
|--------------------------------------------------------------------	|------------------------------------	|
| [`FulfillmentCenterType`](../objects/FulfillmentCenterType.md) 	    | A type or category of properties.  	|

## Example

<div class="grid" markdown>

```json title="Query"
{
  fulfillmentCenter(id: "vendor-fulfillment") {
    id
    name
    description
    shortDescription
    outerId
    geoLocation
    address {
      city
    }
    nearest(take: 3) {
      name
      id
    }
  }
}
```

```json title="Return"
{
  "data": {
    "fulfillmentCenter": {
      "id": "vendor-fulfillment",
      "name": "Los Angeles Branch",
      "description": "<h3>Branch Hours</h3>\n<table class=\"table\">\n  <tbody>\n    <tr>\n      <th class=\"day\">Day</th>\n      <th><span class=\"hours\">Hours</span></th>\n    </tr>\n    <tr>\n      <td>MON</td>\n      <td>7:30 AM - 5:00 PM</td>\n    </tr>\n    <tr>\n      <td>TUE</td>\n      <td>7:30 AM - 5:00 PM</td>\n    </tr>\n    <tr>\n      <td>WED</td>\n      <td>7:30 AM - 5:00 PM</td>\n    </tr>\n    <tr>\n      <td>THU</td>\n      <td>7:30 AM - 5:00 PM</td>\n    </tr>\n    <tr>\n      <td>FRI</td>\n      <td>7:30 AM - 5:00 PM</td>\n    </tr>\n    <tr>\n      <td>SAT</td>\n      <td>CLOSED</td>\n    </tr>\n    <tr>\n      <td>SUN</td>\n      <td>CLOSED</td>\n    </tr>\n  </tbody>\n</table>",
      "shortDescription": null,
      "outerId": null,
      "geoLocation": null,
      "address": {
        "city": "Los Angeles"
      },
      "nearest": [
        {
          "name": "Bristol Branch",
          "id": "e5aea833-dfce-4347-bf38-a479d33dce28"
        },
      // ... more branches      ]
    }
  }
}
```

</div>