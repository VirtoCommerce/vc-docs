# Glossary

This glossary maps Virto Commerce developer vocabulary to the industry terms used in other ecommerce platforms. Use it as a reverse lookup when searching for a concept you know by a different name.

For business and operations vocabulary, such as Catalog, Order, or Fulfillment Center, see the [User guide glossary](../../user-guide/glossary.md).

## Dynamic property
A user-defined field added at runtime to any domain object that implements `IHasDynamicProperties`, scoped by an `ObjectType` discriminator. Values are persisted in a separate table rather than as columns on the object (the Entity-Attribute-Value pattern), so adding or removing such properties on an object requires no schema migration. Dynamic properties support multi-value, multilingual, and dictionary (lookup) modifiers. Values can be of one of the predefined types (text, number, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |

See also [Managing Dynamic Properties](Fundamentals/Dynamic-Properties/overview.md) for the object model, and the [User guide glossary](../../user-guide/glossary.md#dynamic-property) for the business-facing view.
