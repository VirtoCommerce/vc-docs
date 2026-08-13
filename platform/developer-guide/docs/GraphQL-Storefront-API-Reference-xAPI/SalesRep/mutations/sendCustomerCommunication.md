# sendCustomerCommunication

This mutation sends a communication, a storefront push notification and/or an email, to the members of a customer organization the rep serves. It backs the "My customers" contact action.

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepCommunicationResultType`](../objects/SalesRepCommunicationResultType.md) | The per-channel delivery outcome. |

## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation {
  sendCustomerCommunication(command: {
    organizationId: "7b8c..."
    sendPush: true
    sendEmail: true
    title: "New products available"
    message: "I've shared a new product list with your team: https://store.example.com/lists/new"
    storeId: "B2B-store"
    cultureName: "en-US"
  }) {
    succeeded
    pushSent
    emailSent
    warnings
  }
}
```

```json title="Return"
{
  "data": {
    "sendCustomerCommunication": {
      "succeeded": true,
      "pushSent": true,
      "emailSent": false,
      "warnings": ["EmailNoRecipients"]
    }
  }
}
```

</div>

## Validation

The request is rejected with a GraphQL error only when it is malformed or not allowed: not authenticated, `message` missing or over 1000 characters, `title` over 128 characters, no channel selected, or the rep does not serve the organization (`Access denied.`). Everything else is reported through `warnings`:

| Warning code | Channel | When |
|--------------|---------|------|
| `NoRecipients` | — | The organization has no members to notify. The rep is excluded from their own send. |
| `EmailUnavailable` | email | The store's email is not configured: no `SalesRepMessageEmailNotification` template, or the store has no sender address. |
| `EmailStoreAccessDenied` | email | The `storeId` is not the caller's own store, nor one of its trusted groups. Email uses the store's template and sender address, so it is scoped to the caller's store. Push is store-agnostic and unaffected. |
| `EmailNoRecipients` | email | Recipients exist, but none has an email address. |
| `EmailSendFailed` | email | The email could not be scheduled (transient). |
| `PushSendFailed` | push | The push could not be saved (transient). |

Codes are plain strings (see `ModuleConstants.Communication.Warnings`), not an enum, so a downstream project can contribute its own codes. The storefront maps each to a localized message.

## Recipients

Recipients are resolved once and fed to both channels, so the audience is identical regardless of which channels are selected. The default policy targets every member of the organization. It is a pluggable seam (`ISalesRepRecipientResolver`) a project can replace, for example with the bundled primary-contact-only policy, via a later DI registration.

Delivery still depends on what each channel needs: push reaches members with a storefront login account, and email reaches members with an email address. The email renders the store-scoped `SalesRepMessageEmailNotification` template, localized by `cultureName`. `message` is required (max 1000 characters) and may contain a URL; `title` is optional (max 128 characters).

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../objects/SalesRepCommunicationResultType">← SalesRepCommunicationResultType</a>
    <a href="../../../Recommend/overview">xRecommend module overview →</a>
</div>
