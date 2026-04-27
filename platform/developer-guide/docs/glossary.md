# Glossary

This glossary maps Virto Commerce developer vocabulary to the industry terms used in other ecommerce platforms. Use it as a reverse lookup when searching for a concept you know by a different name.

For business and operations vocabulary, such as Catalog, Order, or Fulfillment Center, see the [User guide glossary](/platform/user-guide/latest/glossary).

## Catalog property
A user-defined field added at runtime to a catalog, category, product, or product variation. Values are persisted in a separate table (the Entity-Attribute-Value pattern) and cascade down the catalog hierarchy, so a variation receives its product's properties, a product its category's, and a category its catalog's. Catalog properties support multi-value, multilingual, and dictionary (lookup) modifiers, plus validation rules and display ordering. Values can be of one of the predefined types (text, number, measure, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Catalog property | Product option | n/a (uses EAV) | Attribute definition | Product option |

See also [Manage Properties](/platform/user-guide/latest/catalog/managing-properties) for the configuration walkthrough, and the [User guide glossary](/platform/user-guide/latest/glossary#catalog-property) for the business-facing view.

## Dynamic property
A user-defined field added at runtime to any domain object that implements `IHasDynamicProperties`, scoped by an `ObjectType` discriminator. Values are persisted in a separate table rather than as columns on the object (the Entity-Attribute-Value pattern), so adding or removing such properties on an object requires no schema migration. Dynamic properties support multi-value, multilingual, and dictionary (lookup) modifiers. Values can be of one of the predefined types (text, number, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |

See also [Managing Dynamic Properties](Fundamentals/Dynamic-Properties/overview.md) for the object model, and the [User guide glossary](/platform/user-guide/latest/glossary#dynamic-property) for the business-facing view.

## Module
A self-contained .NET project that plugs into the Virto Commerce Platform process at runtime to deliver a single bounded slice of functionality (Catalog, Pricing, Orders, etc.) end-to-end: back-end services, REST endpoints, persistence, and Admin UI extensions. Each module implements `IModule` (lifecycle methods `Initialize`, `PostInitialize`, `Uninstall`) and ships a **module.manifest** file declaring its identifier, version, and dependencies. The Platform follows the Modular Monolith pattern with vertical slices: it is composed from the modules a solution needs, with cross-module communication through integration events, shared services, or extension points rather than direct references. A module is distinct from a custom App built on the VC-Shell SDK, which is a standalone web UI that talks to the Platform over its public APIs.

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Module | n/a (uses Apps) | Module | n/a (composable architecture) | n/a (uses Apps) |

See also [Modular Architecture Overview](Fundamentals/Modularity/01-overview.md) for the architecture deep-dive, [VC-Shell custom apps overview](custom-apps-development/overview.md) for the App concept, and the [User guide glossary](/platform/user-guide/latest/glossary#module) for the business-facing view.
