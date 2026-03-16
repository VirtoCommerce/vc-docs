# Sanity

The Sanity module integrates [Sanity](https://www.sanity.io/) CMS with Virto Commerce. It exposes a webhook endpoint that receives page create, update, and delete events from Sanity and publishes them to the [Pages module](cms-overview.md#pages-module-as-unification-layer).

## Prerequisites

Before you begin, make sure the following modules are installed:

* [Pages.](https://github.com/VirtoCommerce/vc-module-pages)
* [Sanity.](https://github.com/VirtoCommerce/vc-module-sanity)

## Set up Sanity schema

In your [Sanity Studio](https://www.sanity.io/docs/sanity-studio-quickstart/setting-up-your-studio) project, create a `virtoPage` document type.

1. Create the schema file **schemaTypes/virtoPageType.ts**:

    ```typescript title="schemaTypes/virtoPageType.ts"
    import { defineType, defineField } from 'sanity'

    export const virtoPageType = defineType({
      name: 'virtoPage',
      title: 'Virto Page',
      type: 'document',
      fields: [
        defineField({ name: 'title', type: 'string', validation: (rule) => rule.required() }),
        defineField({ name: 'permalink', type: 'slug', options: { source: 'title' }, validation: (rule) => rule.required() }),
        defineField({ name: 'description', type: 'text' }),
        defineField({ name: 'content', type: 'array', of: [{ type: 'block' }] }),
        defineField({ name: 'visibility', type: 'string', options: { list: ['Public', 'Private'] } }),
        defineField({ name: 'userGroups', type: 'array', of: [{ type: 'string' }] }),
        defineField({ name: 'startDate', type: 'datetime' }),
        defineField({ name: 'endDate', type: 'datetime' }),
      ],
    })
    ```

1. Register the schema in **schemaTypes/index.ts**:

    ```typescript title="schemaTypes/virtoPageType.ts"
    import { virtoPageType } from './virtoPageType'

    export const schemaTypes = [virtoPageType]
    ```

## Configure permissions

The webhook endpoint requires an API key for a Virto Commerce user with the following permissions:

| Permission      | Used for                      |
|-----------------|-------------------------------|
| `sanity:update` | Create and update operations. |
| `sanity:delete` | Delete operations.            |

To create an API key with these permissions, follow the [API key guide](../Fundamentals/Security/authorization/overview.md).

## Configure webhook

The module exposes a single endpoint:

```
POST /api/pages/sanity?storeId={storeId}&cultureName={cultureName}
```

To connect Sanity to this endpoint:

1. Open [Sanity Manage](https://www.sanity.io/manage) and go to your project.
1. Navigate to **API** → **Webhooks** and create a new webhook with the following settings:

    | Setting         | Value                                                                                                       |
    |-----------------|-------------------------------------------------------------------------------------------------------------|
    | **URL**         | `https://<your-domain>/api/pages/sanity?storeId=<StoreId>&cultureName=<cultureName>&api_key=<your-api-key>` |
    | **Trigger on**  | `Create, Update, Delete`                                                                                    |
    | **HTTP method** | `POST`                                                                                                      |

## Verify webhook delivery

To check whether webhooks are being delivered correctly, go to **Sanity Manage** --> **Webhooks** --> select your webhook -->  **Show attempt log**.



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../PageBuilder/overview">← Page Builder overview </a>
    <a href="../../../Operations/maintenance-tasks-for-sql">Operations. Maintenance tasks for SQL →</a>
</div>