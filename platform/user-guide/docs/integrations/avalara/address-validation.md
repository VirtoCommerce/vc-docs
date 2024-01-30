# Address validation

Address validation is used in storefront theme to prevent creation of orders with invalid (not acceptable by AvaTax) addresses.

To validate addresses, use:

```cmd
curl -X POST "https://my-admin.virtocommerce.com/api/tax/avatax/address/validate" -H "accept:text/json" 
```
