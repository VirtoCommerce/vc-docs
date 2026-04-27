# Glossary

This glossary maps Virto Commerce developer vocabulary to the industry terms used in other ecommerce platforms. Use it as a reverse lookup when searching for a concept you know by a different name.

For business and operations vocabulary, such as Catalog, Order, or Fulfillment Center, see the [User guide glossary](../../user-guide/glossary.md).

## Catalog property
A user-defined field added at runtime to a catalog, category, product, or product variation. Values are persisted in a separate table (the Entity-Attribute-Value pattern) and cascade down the catalog hierarchy, so a variation receives its product's properties, a product its category's, and a category its catalog's. Catalog properties support multi-value, multilingual, and dictionary (lookup) modifiers, plus validation rules and display ordering. Values can be of one of the predefined types (text, number, measure, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Catalog property | Product option | n/a (uses EAV) | Attribute definition | Product option |

See also [Manage Properties](../../user-guide/catalog/managing-properties.md) for the configuration walkthrough, and the [User guide glossary](../../user-guide/glossary.md#catalog-property) for the business-facing view.

## Dynamic property
A user-defined field added at runtime to any domain object that implements `IHasDynamicProperties`, scoped by an `ObjectType` discriminator. Values are persisted in a separate table rather than as columns on the object (the Entity-Attribute-Value pattern), so adding or removing such properties on an object requires no schema migration. Dynamic properties support multi-value, multilingual, and dictionary (lookup) modifiers. Values can be of one of the predefined types (text, number, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |

See also [Managing Dynamic Properties](Fundamentals/Dynamic-Properties/overview.md) for the object model, and the [User guide glossary](../../user-guide/glossary.md#dynamic-property) for the business-facing view.
