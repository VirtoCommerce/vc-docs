# Overview

The Virto Commerce **State Machine** module provides a comprehensive framework for modeling and managing complex business processes through configurable finite state machines. This module enables organizations to define, visualize, and control the lifecycle of any business entity by establishing clear states, transitions, and business rules.

A **state machine** (also known as a finite state machine or FSM) is a computational model used to design algorithms and model complex behaviors. In business contexts, state machines help manage the lifecycle of entities by defining:

- [States](#states).
- [Transitions and triggers](#transitions-and-triggers).
- [Conditions](#conditions).


## States

States represent the current condition of an entity. For example, an e-commerce order moves through the following states:

| State      | Description              |
|------------|--------------------------|
| New        | Customer places order.   |
| Paid       | Payment is processed.    |
| Shipped    | Order is dispatched.     |
| Delivered  | Customer receives order. |
| Completed  | Process finished.        |

Each [transition](#transitions-and-triggers) has rules (e.g., "can only ship after payment") and may [trigger](#transitions-and-triggers) actions (e.g., "send notification email").

Each state has several attributes:

| Attribute   | Description                                     |
|-------------|-------------------------------------------------|
| Name        | Human-readable identifier.                      |
| IsInitial   | Marks the starting state for new entities.      |
| IsFinal     | Indicates the workflow has completed.           |
| IsSuccess   | Marks successful completion (for final states). |
| IsFailed    | Marks failed completion (for final states).     |

### Transitions and triggers

Transitions define how entities move between states:

| Component     | Description                                     |
|---------------|-------------------------------------------------|
| Trigger       | The event name that initiates the transition.   |
| From State    | Source state.                                   |
| To State      | Destination state.                              |
| Conditions    | Optional business rules that must be satisfied. |

### Conditions

Conditions are business rules that determine if a transition can occur:

| Condition           | Description                                        |
|---------------------|----------------------------------------------------|
| Built-in conditions | Pre-defined rules for common scenarios.            |
| Custom conditions   | User-defined logic specific to business needs.     |
| Expression-based    | Use simple expressions or complex code.            |

## Module architecture

The State Machine module follows the Virto Commerce's modular architecture:

![Architecture](media/architecture.png){: style="display: block; margin: 0 auto;" width="400"}

## Key benefits

* **Business process clarity**:

    - Visual representation of complex workflows.
    - Clear documentation of business rules.
    - Consistent process execution across the organization.

* **Flexibility and maintainability**:

    - No-code/low-code workflow design.
    - Easy modification of business rules.

* **Integration ready**:

    - RESTful API for external system integration.
    - Event-driven architecture for real-time updates.
    - Webhook support for process notifications.

* **Audit and compliance**:
    - User tracking for all transitions.
    - Configurable approval workflows.

* **Multi-language support**:

    - Localized state and transition names.
    - Cultural adaptation of workflows.

## Core mechanisms

The workflow system is powered by several core mechanisms that define how states, transitions, and rules are managed:

* State machine engine. The engine is built on the **Stateless** library, providing:
    - Thread-safe state management.
    - Hierarchical state machines.
    - Guard conditions and entry/exit actions.

* Condition. The extensible condition system supports:
    - **Role conditions**: Check user permissions.
    - **Custom conditions**: Domain-specific logic.

## Use cases

| **Field**             | **Description**                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| eCommerce             | Order processing workflows, product approval processes, customer onboarding, return/refund management.                |
| B2B marketplaces      | Vendor registration approval, product catalog management, contract negotiation workflows, supplier onboarding.        |
| Content management    | Content approval workflows, publication processes, review and moderation, multi-stage content lifecycle.              |
| Healthcare            | Patient care pathways, treatment approval processes, medical device certification, regulatory compliance workflows.   |


## Getting started

1. **Define your process**: Identify states and transitions for your business entity.
1. **Register entity type**: Bind your entity to the state machine system.
1. **Create state machine**: Use the visual editor to design your workflow.
1. **Configure conditions**: Set up business rules and validation logic.
1. **Integrate Frontend**: Implement state actions in your user interfaces.
1. **Test and deploy**: Validate your workflow with real data.

<br>
<br>
********

<div style="display: flex; justify-content: flex-end;">
    <a href="../data-structure">Data structure →</a>
</div>

