# Property ==~object~==

This type represents a type or category of properties. Properties are used to provide additional information or attributes for products and variations.

## Fields

| Field                                                                	| Description                                                                       	|
|----------------------------------------------------------------------	|-----------------------------------------------------------------------------------	|
| `id`  ==String==                                                  	| The Id of the property type.                                                         	|
| `name`  ==String!==                                               	| The name of the property type.                                                       	|
| `hidden`  ==Boolean!==                                            	| Indicates whether the property type is hidden or visible.                           	|
| `multivalue`  ==Boolean!==                                        	| Indicates whether the property type allows multiple values.                       	|
| `displayOrder`  ==Int==                                           	| The order in which the property type should be displayed.                         	|
| `label`  ==String==                                               	| The label of the property type.                                   	                |
| `propertyType`  ==PropertyType!==                                 	| The entity the property applies to: `Product`, `Variation`, `Category`, or `Catalog`.  	|
| `propertyValueType`  ==PropertyValueType!==                       	| The data type of the property values. See [Value types](#value-types) below for the full list.  	|
| `value`  ==PropertyValue==                                        	| The default value or values associated with the property type.                    	|
| `valueId`  ==String==                                             	| The Id of the default value for the property type.                 	                |
| `valueDisplayOrder`  ==Int==                                      	| The display order of the property value.                          	                |
| `colorCode`  ==String==                                           	| Color code in CSS format, used when `propertyValueType` is `Color`.  	            |
| `group`  ==PropertyGroup==                                        	| The property group the property belongs to.                       	                |
| `propertyDictionaryItems(...)` [ ==PropertyDictionaryItemsConnection== ](PropertyDictItemConnection.md)  	| A connection to retrieve the dictionary items associated with the property type.  	|

## Value types

The `valueType` determines how a property value is stored and edited:

| Value type | Description |
| --- | --- |
| `ShortText` | A single-line string. |
| `LongText` | A multi-line string. |
| `Html` | Rich text stored as HTML. |
| `Number` | A decimal number. |
| `Integer` | A whole number. |
| `Boolean` | A true or false flag. |
| `DateTime` | A date and time. |
| `GeoPoint` | A geographic coordinate (latitude and longitude). |
| `Measure` | A number paired with a unit of measure. |
| `Color` | A color stored as a CSS color code. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Price/CatalogDiscountType">← CatalogDiscountType</a>
    <a href="../PropertyConnection">PropertyConnection →</a>
</div>
