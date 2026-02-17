# Storybook

The [Virto Commerce Storybook](https://virtostart-main-storybook.govirto.com/) is an interactive component library that documents and showcases reusable UI components used in Virto Commerce Frontend.

It serves as:

* A visual catalog of UI elements
* A development sandbox for testing components in isolation
* A design system reference for consistent UI implementation
* A collaboration tool between developers and designers
* Storybook allows you to see how each component behaves with different props, states, and configurations without running the full application.

Use Storybook when:

* Developing a new frontend feature.
* Customizing storefront UI.
* Creating a new module with UI elements.
* Reviewing available components before building custom ones.
* Ensuring UI consistency across projects.
* Testing component states (loading, error, disabled, etc.)
* It should be your first stop before creating any new UI component.

## Architecture

The Virto Commerce UI Kit follows Atomic Design principles:

<table border="1" cellpadding="10" cellspacing="0" width="100%">
  <thead>
    <tr>
      <th>Group of elements</th>
      <th>Description</th>
      <th>Example</th>
      <th>Image</th>
    </tr>
  </thead>
  <tbody>

    <!-- ATOMS -->
    <tr>
      <td rowspan="3"><strong>Atoms</strong></td>
      <td rowspan="3">
        Smallest, foundational UI elements.<br>
        Use atoms when building basic UI <br> interactions or composing larger components.
      </td>
      <td>VcSwitch</td>
      <td><img src="../media/VcSwitch.png" alt="VcSwitch" width="60"></td>
    </tr>
    <tr>
      <td>VcIcon</td>
      <td><img src="../media/VcIcon.png" alt="VcIcon" width="60"></td>
    </tr>
    <tr>
      <td>VcRadioButton</td>
      <td><img src="../media/VcRadioButton.png" alt="VcRadioButton" width="50"></td>
    </tr>

    <!-- MOLECULES -->
    <tr>
      <td rowspan="3"><strong>Molecules</strong></td>
      <td rowspan="3">
        Combinations of atoms forming functional UI blocks.<br>
        Use molecules for structured UI elements <br> like forms, alerts, selectors, or cart items.
      </td>
      <td>VcButtonSeeMoreLess</td>
      <td><img src="../media/VcButtonSeeMoreLess.png" alt="VcAlert" width="100"></td>
    </tr>
    <tr>
      <td>VcButton</td>
      <td><img src="../media/VcButton.png" alt="VcButton" width="110"></td>
    </tr>
    <tr>
      <td>VcChip</td>
      <td><img src="../media/VcChip.png" alt="VcChip" width="90"></td>
    </tr>

    <!-- ORGANISMS -->
    <tr>
      <td rowspan="2"><strong>Organisms</strong></td>
      <td rowspan="2">
        Complex components composed of molecules and atoms.<br>
        Use organisms when building complete <br> functional sections of a page.
      </td>
      <td>VcTable</td>
      <td><img src="../media/VcTable.png" alt="VcTable" width="400"></td>
    </tr>
    <tr>
      <td>VcPaginaton</td>
      <td><img src="../media/VcPaginaton.png" alt="VcAddToCart" width="400"></td>
    </tr>

  </tbody>
</table>




## Best practices

* Search Storybook before creating a new component.
* Extend existing components instead of duplicating them.
* Use atoms → molecules → organisms hierarchy correctly.
* Follow existing naming conventions (Vc*).
* Keep UI consistent with the design system.

## Use Virto Commerce Storybook

1. Browse components:

    1. Open the [link](https://virtostart-main-storybook.govirto.com/).
    1. Navigate through Atoms → Molecules → Organisms.
    1. Explore variants and states.

1. Inspect props and controls on the right panel:
    1. See available props.
    1. Change values live.
    1. Instantly see how the component reacts.

1. Copy code of the component you need for further use.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../customization/texts-customization/">← Tracking and fixing localizations</a>
    <a href="../../merge">Merging Frontend updates →</a>
</div>