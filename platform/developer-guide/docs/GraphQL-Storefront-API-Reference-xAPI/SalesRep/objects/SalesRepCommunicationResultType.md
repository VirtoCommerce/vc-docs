# SalesRepCommunicationResultType ==~object~==

This type reports the per-channel outcome of a customer communication, so a partial success (one channel delivered, the other could not) is visible to the Frontend.

## Fields

| Field | Description |
|-------|-------------|
| `succeeded`  ==Boolean!== | `true` when at least one requested channel was accepted for delivery (`pushSent || emailSent`). |
| `pushSent`  ==Boolean!== | Whether the push notification was accepted. Each channel is attempted independently, so one failing never blocks the other. |
| `emailSent`  ==Boolean!== | Whether the email was accepted. Each channel is attempted independently. |
| `warnings`  ==[String!]!== | Stable string codes explaining any channel that did not deliver. Empty on full success. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../SalesRepCustomerFilterRuleType">← SalesRepCustomerFilterRuleType</a>
    <a href="../../mutations/sendCustomerCommunication">sendCustomerCommunication mutation →</a>
</div>
