# Address Validation

Address validation is used on the Frontend to prevent creation of orders with invalid (not acceptable by AvaTax) addresses.

To validate addresses, run:

```cmd
curl -X POST "https://my-admin.virtocommerce.com/api/tax/avatax/address/validate" -H "accept:text/json" 
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../tax-type-configuration">← Tax type configuration </a>
    <a href="../settings">Settings →</a>
</div>