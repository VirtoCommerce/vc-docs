# Tax Type Configuration

Assign cart/order items to tax categories for correct tax calculation by applying tax codes to the catalog items. In the Virto Commerce Platform, tax code is also called **Tax type**. 

**Tax code (tax type)** is a system of regulations that governs the collection and administration of taxes in a particular jurisdiction. Tax codes define the types of taxes that are collected, the rates at which they are levied, and the criteria used to determine tax liability.

Define the available tax types in the general settings of the Virto Commerce Platform and apply them to the items. 

To assign no code to the item, leave **Tax Type** property value blank. Avalara will calculate taxes using the default code. 

!!! note
    * You can apply tax type to the whole category of items. In this case, all items in a given category and in nested subcategories will have the selected tax type code.

The tax type can be selected in the following locations:

| Location            | Path                                                                         |
|---------------------|------------------------------------------------------------------------------|
| **Category**        | Catalogs > (your catalog) > (your category) > Manage > Tax type              |
| **Item**            | Catalogs > (your catalog) > (your category) > (your item) > Tax type         |
| **Shipping method** | Stores > (your store) > Shipping methods > (your shipping method) > Tax type |

!!! note
    * The available tax types can be configured in the VC Platform settings:<br>
     **Settings > Commerce > General > Tax types**

## Tax exemptions

To provide the exemption number for selected customers to the Avalara Tax API:

1. Open **Customer details** for the customer you want to configure exemption for.
1. Open **Dynamic properties** for the customer.
1. Add `Tax exempt` dynamic property and select the `ShortText` type.
1. Fill the exemption certificate number to the value of this property.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../taxes-calculation">← Taxes calculation </a>
    <a href="../address-validation">Address validation →</a>
</div>