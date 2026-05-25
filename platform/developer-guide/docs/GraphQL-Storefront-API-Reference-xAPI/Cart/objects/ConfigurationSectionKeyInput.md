# ConfigurationSectionKeyInput ==~object~==

This type represents the identifying input data for a configuration section of a configurable product.

## Fields

| Field                                                 | Description                                                                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `sectionId` ==String!==                               | The Id of the configuration section.                                                                    |
| `type` ==String!==                                    | The type of configuration section. Possible values: `'Product'`, `'Variation'`, `'Text'`, `'File'`.     |
| `option` [==ConfigurableProductOptionKeyInput==](ConfigurableProductOptionKeyInput.md) | Identifies a subset of the configuration section option. Applicable only for `Product` and `Variation` section types. |