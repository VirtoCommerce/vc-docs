# Storybook

The Virto Commerce Storybook is an interactive component library that documents and showcases reusable UI components used across Virto Commerce frontends.

It serves as:

* A visual catalog of UI elements
* A development sandbox for testing components in isolation
* A design system reference for consistent UI implementation
* A collaboration tool between developers and designers
* Storybook allows you to see how each component behaves with different props, states, and configurations without running the full application.

Use Storybook when:

* Developing a new frontend feature
* Customizing storefront UI
* Creating a new module with UI elements
* Reviewing available components before building custom ones
* Ensuring UI consistency across projects
* Testing component states (loading, error, disabled, etc.)
* It should be your first stop before creating any new UI component.


## Architecture

The Virto Commerce UI Kit follows Atomic Design principles:


| Group of elements| Description| Examples|
| ---|---|---|
| Atoms | Smallest, foundational UI elements. <br> Use atoms when building basic UI interactions or composing larger components. |  |
| Molecules | Combinations of atoms forming functional UI blocks. <br> Use molecules for structured UI elements like forms, alerts, selectors, or cart items. | |
| Organisms | Complex components composed of molecules and atoms. <br> Use organisms when building complete functional sections of a page. | VcProductCard <br> VcAddToCart |

## Best practices

* Always search Storybook before creating a new component.
* Extend existing components instead of duplicating them.
* Use atoms → molecules → organisms hierarchy correctly.
* Follow existing naming conventions (Vc*).
* Keep UI consistent with the design system.

## How to use Virto Commerce Storybook

1. Browse components:
    1.Open the link → navigate through Atoms → Molecules → Organisms.
    1. Explore variants and states.

1. Inspect props and controls on the right panel:
    1. See available props.
    1. Change values live.
    1. Instantly see how the component reacts.

1. Copy code of the component you need for further use.