# Overview

## What are Dynamic Views?

Dynamic views represent a novel approach to creating views in VC-Shell. They enable the creation of extensible modules and blades using a new declaration style called `schema`. Thanks to this, the process of creating new views and adding controls becomes simpler and faster.

As dynamic views adhere to standardization, composable factories are essential when creating them, containing all the necessary logic. Crafting a custom composable involves utilizing the composable factory and incorporating all required methods and other logic that will be employed in your dynamic view.

Dynamic Views allows you to create complex UIs with ease and without the need to write any additional code. The only thing you need to do is to create a schema and pass it to the dynamic view.

## Purpose of Dynamic Views

The primary advantage of dynamic views over the conventional Vue template creation lies in their capacity to extend custom or third-party modules. This allows the addition of new controls and logic without altering the source code.

Due to the absence of the need to create blade templates and composable with all the default business logic (such as pagination or validation), development becomes more efficient and streamlined. This eliminates code duplication and simplifies application maintenance.

## Features of Dynamic Views

Dynamic views come equipped with the following built-in features:

- **Pagination**
- **Validation**
- **Permissions**
- **Push notifications**
- **Localization**
- **Customizable toolbar**
- **Customizable control templates**

and more.

Also it has a bunch of built-in controls from VC-Shell UI-kit and components for creating UIs:

Atoms:

- **[VcButton](./../Controls/Atoms/VcButton.md)**
- **[VcImage](./../Controls/Atoms/VcImage.md)**
- **[VcStatus](../Controls/Atoms/VcStatus.md)**
- **[VcVideo](../Controls/Atoms/VcVideo.md)**
- **[VcCheckbox](../Controls/Atoms/VcCheckbox.md)**
- **[VcCard](../Controls/Atoms/VcCard.md)**

Molecules:

- **[VcField](../Controls/Molecules/VcField.md)**
- **[VcEditor](../Controls/Molecules/VcEditor.md)**
- **[VcInput](../Controls/Molecules/VcInput.md)**
- **[VcSelect](../Controls/Molecules/VcSelect.md)**
- **[VcInputCurrency](../Controls/Molecules/VcInputCurrency.md)**

Organisms:

- **[VcGallery](../Controls/Organisms/VcGallery.md)**
- **[VcDynamicProperty](../Controls/Organisms/VcDynamicProperty.md)**
- **[VcFieldset](../Controls/Organisms/VcFieldset.md)**

- **[Widgets](../Controls/widgets.md)**
- **[Toolbar](../Controls/toolbar.md)**

## How to Create a Dynamic View?

In essence, creating a dynamic view involves developing a new composable based on the built-in composable factory and adding all the necessary methods and other logic required for your dynamic view. Subsequently, you create a new schema and pass the newly created composable name to it. The schema encompasses vital information about the dynamic view, including the name, blade's template, composable name, and other details.

For more information on creating schemas, refer to the [How to create page schema](./how-to-create-page-schema.md) section.
