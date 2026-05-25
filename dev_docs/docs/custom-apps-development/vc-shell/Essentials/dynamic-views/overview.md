# Overview

In this article, we will explore the Dynamic Views, which revolutionize the process of creating modules and blades in VC-Shell. Using a declarative style called **schema**, dynamic views simplify the creation of extensible modules with standardized structures. 

## What are Dynamic Views?

Dynamic views present a modern approach to view creation in VC-Shell, offering a simplified and faster method through the utilization of the **schema** declaration style.

As dynamic views adhere to standardization, composable factories are essential when creating them, containing all the necessary logic. Crafting custom composables is a key element, involving the integration of necessary methods and logic into composable factories for dynamic view development.

Dynamic Views allow you to create complex UIs with ease and without writing any additional code. All you need to do is create a schema and pass it to the dynamic view.

## Purpose of Dynamic Views

The primary advantage of dynamic views over the conventional Vue template creation lies in their capacity to extend custom or third-party modules. This allows the addition of new controls and logic without altering the source code.

Due to the absence of the need to create blade templates and composable with all the default business logic (such as pagination or validation), the development becomes more efficient and streamlined. This eliminates code duplication and simplifies application maintenance.

## Features of Dynamic Views

Dynamic views come equipped with the following built-in features:

* Pagination.
* Validation.
* Permissions.
* Push notifications.
* Localization.
* Customizable toolbar.
* Customizable control templates, and more.

It also has a bunch of built-in controls from VC-Shell UI-kit and components for creating UIs:

- [VcButton](../controls/VcButton.md)
- [VcImage](../controls/VcImage.md)
- [VcStatus](../controls/VcStatus.md)
- [VcVideo](../controls/VcVideo.md)
- [VcCheckbox](../controls/VcCheckbox.md)
- [VcCard](../controls/VcCard.md)
- [VcField](../controls/VcField.md)
- [VcEditor](../controls/VcEditor.md)
- [VcInput](../controls/VcInput.md)
- [VcSelect](../controls/VcSelect.md)
- [VcInputCurrency](../controls/VcInputCurrency.md)
- [VcGallery](../controls/VcGallery.md)
- [VcDynamicProperty](../controls/VcDynamicProperty.md)
- [VcFieldset](../controls/VcFieldset.md)
- [Widgets](../controls/Widgets.md)
- [Toolbar](../controls/Toolbar.md)

## How to Create a Dynamic View?

Creating a dynamic view involves developing a new composable based on the built-in composable factory and adding all the necessary methods and other logic required for your dynamic view. You then create a new schema and pass it the name of the newly created composable. The schema contains important information about the dynamic view, including its name, blade template, composable name, and other details.

![Readmore](../../../media/readmore.png){: width="25"} [How to create page schema](Creating-Page-Schema.md)