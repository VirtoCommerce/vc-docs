# In Progress

Address validation is used in storefront theme to prevent creation of orders with invalid (not acceptable by AvaTax) address.

To validate addresses, use:

1. Path: `/api/tax/avatax/address/validate`.
2. Method: `POST`.
3. Parameters: `request` — an instance of `AddressValidationRequest` class. 
    It contains:
    * The address to validate. 
    * `StoreId` to extract AvaTax connection settings for address validation.
