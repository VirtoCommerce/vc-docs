# vendor ==~query~==

This query is used to retrieve detailed information about a vendor, including contact information, addresses, dynamic properties, SEO info, and rating.

## Arguments

| Field                                      | Description                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------|
| `id` ==String!==                            | Vendor unique identifier.                                                   |
| `outerId` ==String==                        | External ID of the vendor.                                                  |
| `memberType` ==String!==                     | Type of member.                                                             |
| `name` ==String==                            | Vendor name.                                                                |
| `status` ==String==                          | Vendor status.                                                              |
| `phones` ==[String]!==                       | List of vendor phone numbers.                                              |
| `emails` ==[String]!==                       | List of vendor emails.                                                     |
| `groups` ==[String]!==                       | Groups the vendor belongs to.                                              |
| `seoObjectType` ==String!==                  | Type used for SEO objects.                                                 |
| `seoInfo` [==SeoInfo==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/SeoInfo) | Returns SEO-related information for the vendor.|
| `defaultBillingAddress` [==MemberAddressType==](../Objects/MemberAddressType.md) | Default billing address.                                   |
| `defaultShippingAddress` [==MemberAddressType==](../Objects/MemberAddressType.md) | Default shipping address.                                 |
| `addresses` [==MemberAddressConnection==](../Objects/MemberAddressConnection.md) | List of all addresses associated with the vendor.          |
| `dynamicProperties` [==[DynamicPropertyValueType]!==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type) | Dynamic properties of the vendor.  |
| `about` ==String==                           | About the vendor.                                                          |
| `iconUrl` ==String==                         | URL to the vendor icon.                                                    |
| `siteUrl` ==String==                         | Vendor website URL.                                                        |
| `rating` [==Rating==](../Objects/rating.md)  | Vendor rating for the given store.                                         |


## Example

<div class="grid" markdown>

```json title="Query"
query($vendorId: String!) {
  vendor(id: $vendorId) {
    id
    outerId
    memberType
    name
    status
    phones
    emails
    groups
    defaultBillingAddress {
      postalCode
      countryName
      regionName
      city
      line1
      line2
    }
    defaultShippingAddress {
      postalCode
      countryName
      regionName
      city
      line1
      line2
    }
    addresses {
      items {
        postalCode
        countryName
        regionName
        city
        line1
        line2
        name
      }
    }
    dynamicProperties {
      name
      valueType
      value
    }
    about
    iconUrl
    siteUrl
  }
}
```

```json title="Return"
{
  "data": {
    "vendor": {
    "id": "vendor-001",
    "outerId": "EXT-12345",
    "memberType": "Supplier",
    "name": "Example Vendor",
    "status": "Active",
    "phones": ["+1-555-1234"],
    "emails": ["contact@examplevendor.com"],
    "groups": ["Group A"],
    "defaultBillingAddress": {
        "postalCode": "12345",
        "countryName": "USA",
        "regionName": "CA",
        "city": "San Francisco",
        "line1": "123 Market St",
        "line2": "Suite 400"
    },
    "defaultShippingAddress": {
        "postalCode": "12345",
        "countryName": "USA",
        "regionName": "CA",
        "city": "San Francisco",
        "line1": "123 Market St",
        "line2": "Suite 400"
    },
    "addresses": {
        "items": [
        {
            "postalCode": "12345",
            "countryName": "USA",
            "regionName": "CA",
            "city": "San Francisco",
            "line1": "123 Market St",
            "line2": "Suite 400",
            "name": "Headquarters"
        }
        ]
    },
    "dynamicProperties": [
        {"name": "CustomField1", "valueType": "String", "value": "Value1"}
    ],
    "about": "This is an example vendor.",
    "iconUrl": "https://example.com/icon.png",
    "siteUrl": "https://examplevendor.com"
    }
  }
}
```

</div>