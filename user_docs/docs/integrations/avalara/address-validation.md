
Address validation can be used in storefront theme to prevent creation of orders with invalid (not acceptable by AvaTax) address.

To validate addresses:

1. Go to **api > tax > avatax > address > validate**.
2. Use **POST** method.
3. Apply `request` parameter — an instance of `AddressValidationRequest` class. It contains:
    * The address to validate. 
    * StoreId to extract Ava.Tax connection settings for address validation.

