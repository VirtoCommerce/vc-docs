# Partial Update for Entities in the Top Modules Using PATCH Endpoint

According to the [RFC-6902 specification](https://datatracker.ietf.org/doc/html/rfc6902), REST API methods allow updating individual entity fields  avoiding  unintentionally overwriting data and make API calls more efficient and safer. 

[.Net Core](https://learn.microsoft.com/en-us/aspnet/core/web-api/jsonpatch?view=aspnetcore-5.0) has its own implementation of this specification and allows you to implement similar approaches to updating entities out of the box.

There are also special [free online update request constructors](https://json-patch-builder-online.github.io/) according to the specified specification.

Developers integrating with the Virto Commerce API can update only specific fields in entities in different modules of the Platform.


## JSON patches

A patch document is a JSON array of operations, where each operation includes:

* `op`: The operation to perform (`add`, `remove`, `replace`, `move`, `copy`, or `test`):

    * **add**: Inserts a value at the target location. 
        * If the target is an array:
            * Inserting at an index **equal** to the array’s current length **appends** the value.
            * Inserting beyond the length returns a **400 Bad Request**.
        * If the target is a non-array field, `add` creates or replaces the value.

    * **remove**: Deletes the value at the target location. For arrays, the element at the given index is removed, and following elements shift left.
    * **replace**: Replaces the value at the target location. Equivalent to a `remove` followed by an `add`.
    * **move**: Moves a value from `from` to `path`. The original value is removed.
    * **copy**: Copies a value from `from` to `path` without removing the original.
    * **test**: Asserts that the value at `path` matches `value`. If the test fails, the patch is aborted with **400 Bad Request**.

* `path`: A JSON pointer indicating the target location in the document.
* `value`: The new value (for `add`, `replace`, and `test` operations).
* `from`: The source location (for `move` and `copy` operations).

```json title="Example"
[
  { "op": "add", "path": "/newField", "value": "New value" },
  { "op": "remove", "path": "/oldField" },
  { "op": "replace", "path": "/existingField", "value": "Updated value" },
  { "op": "move", "from": "/tempField", "path": "/finalField" },
  { "op": "copy", "from": "/sourceField", "path": "/destinationField" },
  { "op": "test", "path": "/testField", "value": "Expected value" }
]
```

Only the fields included in your request body will be modified; omitted fields remain unchanged.

![Readmore](media/readmore.png){: width="25"} [JSON‑Patch in ASP.NET Core](https://learn.microsoft.com/aspnet/core/web-api/jsonpatch)


## Supported endpoints

The following table outlines the supported `PATCH` endpoints across Virto Commerce modules, along with example request paths for each.

<table>
  <thead>
    <tr>
      <th>Module</th>
      <th>API Endpoint</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr><td rowspan="9"><strong>Catalog</strong></td><td>Update catalog</td><td><code>PATCH /api/catalog/catalogs/{id}</code></td></tr>
    <tr><td>Update category</td><td><code>PATCH /api/catalog/categories/{id}</code></td></tr>
    <tr><td>Update product configuration</td><td><code>PATCH /api/catalog/products/configurations/{id}</code></td></tr>
    <tr><td>Update measure</td><td><code>PATCH /api/catalog/measures/{id}</code></td></tr>
    <tr><td>Update product</td><td><code>PATCH /api/catalog/products/{id}</code></td></tr>
    <tr><td>Update property</td><td><code>PATCH /api/catalog/properties/{id}</code></td></tr>
    <tr><td>Update product association</td><td><code>PATCH /api/catalog/products/associations/{id}</code></td></tr>
    <tr><td>Update dictionary item</td><td><code>PATCH /api/catalog/dictionaryitems/{id}</code></td></tr>
    <tr><td>Update product video</td><td><code>PATCH /api/catalog/videos/{id}</code></td></tr>

    <tr><td rowspan="3"><strong>Pricing</strong></td><td>Update price assignment</td><td><code>PATCH /api/pricing/assignments/{id}</code></td></tr>
    <tr><td>Update product price</td><td><code>PATCH /api/products/prices/{id}</code></td></tr>
    <tr><td>Update pricelist</td><td><code>PATCH /api/pricing/pricelists/{id}</code></td></tr>

    <tr><td><strong>Store</strong></td><td>Update store</td><td><code>PATCH /api/stores/{id}</code></td></tr>

    <tr><td rowspan="2"><strong>Inventory</strong></td><td>Update fulfillment center</td><td><code>PATCH /api/inventory/fulfillmentcenters/{id}</code></td></tr>
    <tr><td>Update inventory</td><td><code>PATCH /api/inventory/{id}</code></td></tr>

    <tr><td rowspan="4"><strong>Cart</strong></td><td>Update cart</td><td><code>PATCH /api/carts/patch{id}</code></td></tr>
    <tr><td>Update cart item</td><td><code>PATCH /api/carts/patch/{cartId}/items/{lineItemId}</code></td></tr>
    <tr><td>Update cart payment</td><td><code>PATCH /api/carts/patch{cartId}/payments/{paymentId}</code></td></tr>
    <tr><td>Update cart shipment</td><td><code>PATCH /api/carts/patch{cartId}/shipments/{shipmentId}</code></td></tr>

    <tr><td rowspan="3"><strong>Order</strong></td><td>Update customer order</td><td><code>PATCH /api/order/customerOrders/{id}</code></td></tr>
    <tr><td>Update order payment</td><td><code>PATCH /api/order/payments/{id}</code></td></tr>
    <tr><td>Update order shipment</td><td><code>PATCH /api/order/shipments/{id}</code></td></tr>
  </tbody>
</table>


## Response codes

* **204 No Content**: Update succeeded.
* **400 Bad Request**: Invalid payload (e.g., malformed JSON, invalid JSON‑Pointer syntax).
* **403 Forbidden**: Insufficient permissions (see your API permissions guide).
* **404 Not Found**: No entity found with the specified ID.


## Examples

* **Update a single field** (replace the Member’s middle name):

    ```json
    [
      {
        "op": "replace",
        "path": "/middleName",
        "value": "Michel"
      }
    ]
    ```

* **Add a phone number** to the beginning of the `phones` array (index 0 appends at front):

    ```json
    [
      {
        "op": "add",
        "path": "/phones/0",
        "value": "+19995558545"
      }
    ]
    ```

* **Remove a phone number** (delete index 1):

    ```json
    [
      {
        "op": "remove",
        "path": "/phones/1"
      }
    ]
    ```

* **Add an address object** at index 1 of the `addresses` array:

    ```json
    [
      {
        "op": "add",
        "path": "/addresses/1",
        "value": {
          "addressType": "BillingAndShipping",
          "line1": "c/ Eucaliptus 10",
          "line2": "pta. 10",
          "city": "Valencia",
          "postalCode": "44375",
          "countryCode": "ESP",
          "firstName": "John",
          "lastName": "Doe",
          "email": "test@test.com",
          "isDefault": false
        }
      }
    ]
    ```

* **Move** a temporary field into its final location:

    ```json
    [
      {
        "op": "move",
        "from": "/tempField",
        "path": "/finalField"
      }
    ]
    ```

![Readmore](media/readmore.png){: width="25"} [JSON Patch Builder Online](https://json-patch-builder-online.github.io/)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../using-responseGroups-in-rest-api">← Using responseGroups in Rest API </a>
    <a href="../generating-pdfs">Generating PDFs  →</a>
</div>