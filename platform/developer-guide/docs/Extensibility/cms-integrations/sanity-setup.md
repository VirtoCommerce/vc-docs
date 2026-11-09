# Sanity Setup

The Sanity module integrates [Sanity](https://www.sanity.io/) CMS with Virto Commerce. It exposes a webhook endpoint that receives document create, update, and delete events from Sanity and publishes them to the [Pages module](cms-overview.md#pages-module-as-unification-layer). It can also fetch and index several document types from several Sanity datasets or projects at once.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-sanity/releases)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-sanity/releases/latest)


## Prerequisites

Before configuring the module, make sure you have:

* [Pages module.](https://github.com/VirtoCommerce/vc-module-pages)
* [Sanity module.](https://github.com/VirtoCommerce/vc-module-sanity)

## Set up Sanity schema

Create one or more document types in your [Sanity Studio](https://www.sanity.io/docs/sanity-studio-quickstart/setting-up-your-studio) project. List their names in the store's **Sanity.DocumentTypes** setting, or per dataset in **Sanity.Projects** when the store reads from several datasets or projects.

1. Create the schema file **schemaTypes/pageType.ts**:

    ```typescript title="schemaTypes/pageType.ts"
    import { defineType, defineField } from 'sanity'

    export const pageType = defineType({
      name: 'page',
      title: 'Page',
      type: 'document',
      fields: [
        defineField({ name: 'title', type: 'string', validation: (rule) => rule.required() }),
        defineField({ name: 'permalink', type: 'slug', options: { source: 'title' }, validation: (rule) => rule.required() }),
        defineField({ name: 'description', type: 'text' }),
        defineField({ name: 'body', type: 'array', of: [{ type: 'block' }] }),
        defineField({ name: 'storeId', type: 'string', title: 'Store ID' }),
        defineField({ name: 'cultureName', type: 'string', title: 'Culture Name' }),
        defineField({ name: 'visibility', type: 'string', options: { list: ['Public', 'Private'] } }),
        defineField({ name: 'userGroups', type: 'array', of: [{ type: 'string' }] }),
        defineField({ name: 'startDate', type: 'datetime' }),
        defineField({ name: 'endDate', type: 'datetime' }),
      ],
    })
    ```

1. Register the schema in **schemaTypes/index.ts**:

    ```typescript title="schemaTypes/index.ts"
    import { pageType } from './pageType'

    export const schemaTypes = [pageType]
    ```

The document type is now available in Sanity Studio. A document whose `_id` starts with `drafts.` is indexed with a Draft status. Every other document gets a Published status.

## Configure the webhook secret

The webhook is authorized by a signature instead of an API key in its URL, so no secret ends up in the webhook URL or Sanity's attempt log. Add a secret to the [appsettings.json **Sanity** node](/platform/developer-guide/latest/Configuration-Reference/appsettingsjson#sanity):

```json title="appsettings.json"
{
  "Sanity": {
    "WebhookSecrets": [ "whsec_current" ]
  }
}
```

The same value goes into the webhook's **Secret** field in Sanity Manage, in the next section. With no secret configured, the endpoint rejects every delivery.

## Configure webhook

The module exposes a single endpoint:

```
POST /api/pages/sanity?cultureName={cultureName}
```

To connect Sanity to this endpoint:

1. Open [Sanity Manage](https://www.sanity.io/manage) and open your project.
1. Open **API** then **Webhooks** and create a webhook with the following settings:

    | Setting | Value |
    |---|---|
    | **URL** | `https://<your-domain>/api/pages/sanity?cultureName=<cultureName>` |
    | **Secret** | the value you added to `Sanity:WebhookSecrets`. |
    | **Trigger on** | `Create, Update, Delete` |
    | **HTTP method** | `POST` |
    | **Projection** | the recommended projection below. |

    ```groq title="Recommended projection"
    {
      _id,
      storeId,
      "_operation": delta::operation(),
      "_projectId": sanity::projectId(),
      "_dataset": sanity::dataset()
    }
    ```

The webhook now sends document events from Sanity to Virto Commerce. Sanity signs every delivery over this projected body, so a document that needs a bigger projection still keeps every routing field (the ones prefixed with an underscore) inside it, rather than relying on the unsigned `sanity-*` request headers.

## Verify webhook delivery

To check whether webhooks are being delivered correctly, open **Sanity Manage** → **Webhooks** → your webhook → **Show attempt log**.

## Upgrade from the API key webhook

Earlier versions authorized the webhook by a platform API key in its URL and read the store from a **storeId** query parameter. After upgrading the module, the endpoint rejects every notification until a secret is configured. Content refreshes only through a full index rebuild until then. For each existing webhook:

1. [Add a secret to the webhook](#configure-the-webhook-secret) in both the platform configuration and the webhook's **Secret** field, then restart the platform.
1. Remove `api_key` and `storeId` from the webhook URL. Keep `cultureName` if you use it.
1. Replace the projection with the [recommended one](#configure-webhook).
1. Make sure every store that should receive the content lists its project and dataset in **Sanity.Projects**, or in **Sanity.ProjectId** and **Sanity.Dataset**. The store is now resolved from that configuration or the document's `storeId` field, not from the webhook URL.
1. Save a document in Sanity Studio. Check the attempt log in Sanity Manage and the platform log for a rejected request.

The platform API key used by the old webhook is no longer needed and can be revoked. The `sanity:update` and `sanity:delete` permissions stay registered so existing roles keep loading, but nothing checks them anymore.

For code that extends the module:

* The webhook resolves `ISanityContentProvider`, not `IPageContentProvider`. A custom provider registered only as `IPageContentProvider` is never called by the webhook. Register it as `ISanityContentProvider` too.
* `ISanityApiClient.QueryAsync` takes a `CancellationToken`. A custom implementation needs the added parameter.
* An `ISanityConverter` override that reads `cultureName` or `request` in `GetPageDocument` receives a null value for create and update notifications. That's because the webhook payload is a change notification, not the document content.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../PageBuilder/overview">← Page Builder overview </a>
    <a href="../contentful-setup">Contentful setup →</a>
</div>
