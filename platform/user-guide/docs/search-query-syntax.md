# Search Query Syntax and Examples

Virto Commerce supports advanced search capabilities using a flexible query syntax. This guide provides an overview of supported operators, field-based queries, and complex examples to help you craft powerful search expressions for product discovery, catalog filtering, inventory lookup, and more.


## Basic logical operators

| Operator  | Description                                                | Examples                                                                                                                                  |
|-----------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **AND**   | Returns results that match **all** specified conditions. | gtin:44 AND code:ZQL-92511859 <br> name:laptop AND price:500 <br> category:electronics AND brand:samsung <br> sku:ABC123 AND instock:true` |
| **OR**    | Returns results that match **any** of the conditions. | code:ZQL-92511859 OR itemLineNOM:99<br>category:laptops OR category:tablets<br>brand:apple OR brand:microsoft<br>price:100 OR price:200 |
| **AND / OR** (no parentheses) | Without parentheses, OR has **lower precedence** than AND. | gtin:44 AND code:ZQL-92511859 OR itemLineNOM:99 <br>name:laptop AND brand:dell OR brand:hp |



## Parenthesized expressions (group conditions)

Parentheses allow you to group conditions and control logical precedence.

| Pattern                       | Description                                                                                       | Examples                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **OR** inside parentheses     | Returns results that match the left condition and **either** of the grouped right-side conditions | gtin:44 AND (code:ZQL-92511859 OR itemLineNOM:99) <br> brand:apple AND (category:phones OR category:tablets) <br> name:laptop AND (price:500 OR price:600) <br> sku:ABC AND (color:red OR color:blue)|
| **AND** inside parentheses    | Returns results that match the grouped left-side conditions or the right condition                | (gtin:44 AND code:ZQL-92511859) OR itemLineNOM:99  <br> (brand:apple AND category:phones) OR category:tablets <br> (name:laptop AND price:500) OR brand:dell  |
| Complex and nested conditions | Return results that satisfy one full set of conditions or another, combining and/or logic        | (brand:apple AND category:phones) OR (brand:samsung AND category:tablets) <br> (name:laptop AND price:500) OR (name:desktop AND price:800)|
| Multiple groupings            | Return results that match any condition in each group, ensuring combinations across groups       | (brand:apple OR brand:samsung) AND (category:phones OR category:tablets) <br> (price:100 OR price:200) AND (color:red OR color:blue) |



## Keyword + parentheses combinations

You can combine free-text keywords with structured filters in or around parentheses.

| Pattern                    | Description                                                                                       | Examples                               |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Keyword before parentheses | Returns results that match the keyword **and** one of the grouped filter conditions               | smartphone (brand:apple OR brand:samsung) AND category:phones <br> gaming (category:laptops AND price:1000) OR (category:desktops AND price:800) <br> laptop (gtin:44 AND code:ZQL-92511859) OR (gtin:44 AND itemLineNOM:99) |
| Keyword after parentheses  | Returns results that match one of the grouped filter conditions **and** the keyword               | (brand:apple OR brand:samsung) smartphone <br> (category:laptops OR category:desktops) gaming <br> (price:100 OR price:200) budget |
| Mixed keyword positioning  | Returns results that include keywords before or after the filters, applying all criteria together | laptop (brand:dell OR brand:hp) gaming <br> wireless (category:headphones OR category:speakers) bluetooth <br> premium (material:leather OR material:metal) luxury   |


## Field-specific searches

Use fielded search to target specific product or inventory attributes.

| Pattern                | Description                                                                      | Examples                 |
|------------------------|----------------------------------------------------------------------------------|---------------------------|
| Product identification | Searches for a product by its unique identifiers                                | gtin:1234567890123  <br> sku:ABC-123-XYZ <br> code:PROD-001 <br> itemLineNOM:LINE-99       |
| Product attributes     | Filters products based on descriptive attributes like name, brand, etc.         | name:iPhone <br> brand:Apple <br> category:Electronics <br> description:smartphone <br> price:999 <br> color:black  <br> size:large  |
| Inventory fields       | Filters products by inventory-related data such as stock status or quantity     | instock:true <br> quantity:50 <br> warehouse:WH001 <br> availability:available    |


## Complex real-world scenarios

| Pattern                   | Description                                                                                  | Examples                                                                                 |
|---------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| eCommerce product search | Filters based on multiple product attributes like brand, category, and price combinations    | (brand:apple OR brand:samsung) AND category:smartphones AND (price:500 OR price:600 OR price:700)<br>(color:black OR color:white) AND (storage:128GB OR storage:256GB) AND brand:apple<br>gaming (category:laptops OR category:desktops) AND (brand:asus OR brand:msi) AND price:1000 |
| Inventory management      | Filters items based on SKU, stock status, warehouse, and quantity                           | (sku:LAP001 OR sku:LAP002) AND instock:true AND (warehouse:WH001 OR warehouse:WH002)<br>electronics (category:phones OR category:tablets) AND (quantity:10 OR quantity:20) |
| Product catalog filtering | Combines category and attribute filters for refined browsing                                 | (category:clothing AND material:cotton) OR (category:electronics AND brand:sony)<br>seasonal (category:winter OR category:summer) AND (discount:true OR sale:true) |
| B2B specific searches     | Supports B2B conditions like quantity thresholds and supplier/lead time filtering            | wholesale (category:electronics AND quantity:100) OR (category:clothing AND quantity:500)<br>(supplier:SUPP001 OR supplier:SUPP002) AND (leadtime:7 OR leadtime:14) |



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../search">← Search options</a>
    <a href="../security/overview">Security module overview →</a>
</div>