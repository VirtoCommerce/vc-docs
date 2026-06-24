# Webhooks

The **Webhooks** module allows you to monitor important changes within your Virto Commerce ecosystem, such as order changes, catalog and product updates, and more.
When a change you're subscribed to is triggered, you receive a notification at the URL you specified.
You can also configure which fields or parameters to include in the report you receive.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-webhooks)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-webhooks/releases)

## Key features

With the Webhooks module:

* Employees can manage webhooks within their permission level.
* Admin users have full control over webhook management.
* It resolves domain events for installed Virto Commerce modules.
* It quietly sends webhook notifications in the background via a POST request, with event data serialized in JSON, to the specified URL.
* It supports Basic, Bearer Token, and Custom Header authentication methods.
* You can access previous values of selected fields.
* The retry policy is configurable, with intervals that increase exponentially.
* Error messages are available for viewing in case a webhook notification fails.

## Configuration

The WebHooks module does not require a dedicated configuration section in **appsettings.json**. It uses a standard database connection string:

```json title="appsettings.json"
"ConnectionStrings": {
  "VirtoCommerce.WebHooks": "Data Source=.;Initial Catalog=Virto.WebHooks;Integrated Security=True"
}
```


## Delivery and retries

The module sends each webhook as an HTTP `POST` with a JSON body:

```json
{
  "EventId": "<event id>",
  "Attempt": 1,
  "EventBody": { }
}
```

`Attempt` increases with each delivery attempt.

If the receiver does not return a success (2xx) status, the delivery is retried with an exponential backoff. The number of retries is set by `Webhooks.General.SendRetryCount` (default `3`), configured under **Settings --> Webhooks --> General**. The delay doubles each attempt: 1, 2, 4, 8 minutes, and so on.

When the retries are exhausted, the failure is recorded in the webhook error log with the response status code and body. The module keeps only the most recent failures per webhook, controlled by `Webhooks.General.LatestErrorCount` (default `5`). There is no dead-letter queue.

Delivery is best-effort: the module guarantees neither exactly-once delivery nor ordering. Because a delivery can be retried, make your receiver **idempotent**, so that processing the same `EventId` more than once is safe.

## Securing webhook receiver

The module authenticates to the receiver with the method you configure on the webhook: Basic, Bearer token, or a custom header. It does **not** sign the payload: there is no HMAC or signature header, so the receiver cannot verify the body cryptographically. To secure delivery:

* Use an HTTPS endpoint together with one of the supported authentication methods.
* Restrict the endpoint to Virto Commerce by network controls, such as an IP allowlist, where possible.
* Use `EventId` as a de-duplication key on the receiver.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../using-domain-events">← Using domain events </a>
    <a href="../event-bus">Event Bus →</a>
</div>
