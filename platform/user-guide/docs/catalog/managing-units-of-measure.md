
# Manage Units of Measure

The Catalog module allows you to sell products in different units of measure. 

Managing units of measure includes:

* [Adding default units of measure]
* [Adding new units.](managing-units-of-measure.md#add-new-unit-of-measure)
* [Adding measure units to a specific unit of measure.](managing-units-of-measure.md#add-measure-unit-to-specific-unit)
* [Setting measure unit as default.](managing-units-of-measure.md#set-unit-as-default)
* [Deleting units.](managing-units-of-measure.md#set-unit-as-default)

## Add default units of measure

To simplify initial configuration, we have added default dimensions and their measure units to the Catalog:

=== "Weight"
    | Name     | Code | Conversion Rate (to Base) | Base Unit | Is Default |
    |----------|------|--------------------------|-----------|------------|
    | Kilogram | KG   | 1                        | KG        | ✅ Yes      |
    | Gram     | G    | 0.001                    | KG        | ❌ No       |
    | Pound    | LB   | 0.453592                 | KG        | ❌ No       |
    | Ounce    | OZ   | 0.0283495                | KG        | ❌ No       |

=== "Volume"
    | Name         | Code  | Conversion Rate (to Base) | Base Unit | Is Default |
    |-------------|-------|--------------------------|-----------|------------|
    | Liter       | L     | 1                        | L         | ✅ Yes      |
    | Milliliter  | ML    | 0.001                    | L         | ❌ No       |
    | Gallon      | GAL   | 0.264172                 | L         | ❌ No       |
    | Fluid Ounce | FL OZ | 33.814                   | L         | ❌ No       |

=== "Length"
    | Name       | Code | Conversion Rate (to Base) | Base Unit | Is Default |
    |-----------|------|--------------------------|-----------|------------|
    | Meter     | M    | 1                        | M         | ✅ Yes      |
    | Centimeter| CM   | 0.01                     | M         | ❌ No       |
    | Inch      | IN   | 39.3701                  | M         | ❌ No       |
    | Foot      | FT   | 3.28084                  | M         | ❌ No       |

=== "Quantity"
    | Name   | Code  | Conversion Rate (to Base) | Base Unit | Is Default |
    |--------|-------|--------------------------|-----------|------------|
    | Piece  | PCS   | 1                        | PCS       | ✅ Yes      |
    | Dozen  | DOZ   | 12                       | PCS       | ❌ No       |
    | Pack   | PACK  | 1                        | PCS       | ❌ No       |
    | Case   | CASE  | 24                       | PCS       | ❌ No       |

=== "Time"
    | Name  | Code | Conversion Rate (to Base) | Base Unit | Is Default |
    |-------|------|--------------------------|-----------|------------|
    | Hour  | HR   | 1                        | HR        | ✅ Yes      |
    | Day   | DAY  | 24                       | HR        | ❌ No       |
    | Week  | WK   | 168                      | HR        | ❌ No       |
    | Month | MO   | 730                      | HR        | ❌ No       |


To add the pre-filled dimensions and their measure units to your initial configuration:

1. Click **Units of measure** in the main menu. 
1. In the next blade, click **Create default**.
1. In the next blade, check the dimensions you want to include in your configuration.
1. Click **Create** in the toolbar. 

The selected dimensions from the default list have been added to your configuration.

To set new default units of measure:

1. Click on the required dimension.
1. In the next blade, click on the **Units** widget.
1. In the next blade, click on the measure unit from the list.
1. In the next blade, click **Set as default** in the toolbar.

The selected unit of measure is now the default for this dimension.

![Default units of measure](media/units-of-measure.gif)

## Add new dimension

To add a new dimension:

1. Click **Units of measure** in the main menu. 
1. The next blade lists all the registered units of measure. Click **Add** in the toolbar to add a new dimension.
1. In the next blade, fill in the required fields, then click **Save** in the toolbar:

![Add new UoM](media/add-uom.png)

Your new dimension appears in the list.

## Add unit of measure to dimension 

To extend a dimension from the list with new measure units:

1. Click on the desired dimension. 
1. In the next blade, click on the **Units** widget.
1. In the next blade, click **Add** in the toolbar.

    ![New measure unit](media/new-measure-unit.png)

1. Fill in the following fields, then click **OK**:

    ![New measure unit 1](media/add-uom1.png)

Your new unit of measure has been added.

## Set unit as default

The first added measure unit is automatically set as the default. To set another unit as the default:

1. Complete steps 1-2 from the [instruction above](managing-units-of-measure.md#add-unit-of-measure-to-dimension).
1. Click the unit in the list that you want to set as the default.
1. In the next blade, click **Set as default** in the toolbar.

    ![Default unit](media/default-uom.png)

1. Click **OK** to save the changes.

The unit has been set as the default.

## Delete unit

To delete a unit:

1. Complete steps 1-2 from the [instruction above](managing-units-of-measure.md#add-unit-of-measure-to-dimension).
1. Check the unit you want to delete.
1. Click **Delete** in the toolbar.
1. Confirm your action.

The unit has been deleted from the list.