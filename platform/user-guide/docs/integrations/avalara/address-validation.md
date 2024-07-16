# Address validation

Address validation is used in the Frontend Application to prevent creation of orders with invalid (not acceptable by AvaTax) addresses.

To validate addresses, run:

```cmd
curl -X POST "https://my-admin.virtocommerce.com/api/tax/avatax/address/validate" -H "accept:text/json" 
```
