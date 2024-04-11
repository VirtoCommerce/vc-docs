# QuoteShipmentMethodType ==~object~==

The `QuoteShipmentMethodType` is an object that contains information about a shipment method associated with a quote.

## Fields

| Field                                                                 | Description                                        |
| --------------------------------------------------------------------- | -------------------------------------------------- |
| `shipmentMethodCode`  ==String==                                      | The code for the shipment method.                  |
| `optionName`  ==String==                                              | The name of the shipment method option.            |
| `logoUrl`  ==String==                                                 | The URL of a logo representing the shipment method.|
| `typeName`  ==String==                                                | The type  of the shipment method.                  |
| `currency` [ ==CurrencyType== ](../../Order/objects/currency-type.md) | The currency used for pricing the shipment method. |
| `price` [ ==MoneyType== ](../../Cart/objects/money-type.md)           | The price associated with the shipment method.     |
