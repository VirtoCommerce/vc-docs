# How to Partially Update Member Entities Using the PATCH Endpoint

This guide walks you through updating specific fields of a Member (or Contact/Organization) entity without sending the full object. 


## JSON‑Patches

JSON‑Patch is defined in [RFC 6902](https://tools.ietf.org/html/rfc6902). A patch document is a JSON array of operations, where each operation includes:

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

* `path`: A JSON Pointer indicating the target location in the document.
* `value`: The new value (for `add`, `replace`, and `test` operations).
* `from`: The source location (for `move` and `copy` operations).

```json title="Example"
[
  { "op": "add", "path": "/newField", "value": "New Value" },
  { "op": "remove", "path": "/oldField" },
  { "op": "replace", "path": "/existingField", "value": "Updated Value" },
  { "op": "move", "from": "/tempField", "path": "/finalField" },
  { "op": "copy", "from": "/sourceField", "path": "/destinationField" },
  { "op": "test", "path": "/testField", "value": "Expected Value" }
]
```

Only the fields included in your request body will be modified; omitted fields remain unchanged.

![Readmore](media/readmore.png){: width="25"} [JSON‑Patch in ASP.NET Core](https://learn.microsoft.com/aspnet/core/web-api/jsonpatch)


## Supported endpoints

| Method                          | Description                             |
| ------------------------------- | --------------------------------------- |
| `PATCH /api/members/{id}`       | Partially update a Member entity.        |
| `PATCH /api/contacts/{id}`      | Partially update a Contact entity.       |
| `PATCH /api/organizations/{id}` | Partially update an Organization entity. |


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


## Permissions

Ensure your API token has the **Member.Update** (or **Contact.Update**, **Organization.Update**) scope. Without the correct scope, requests return **403 Forbidden**.
