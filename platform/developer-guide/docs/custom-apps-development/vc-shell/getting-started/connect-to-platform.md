# Connect to Platform

Use `/vc-app connect` to point a generated VC-Shell app at a Virto Commerce Platform instance and generate typed API clients from Platform module OpenAPI documents.

If you do not use the AI skill, follow [Manual Platform API Setup](manual-platform-api-setup.md) for the equivalent CLI and configuration steps.

## Run the command

Inside the app root, ask your AI tool:

```text
/vc-app connect
```

The skill asks for:

- Platform URL, for example `https://admin.example.com`.
- Platform modules to generate clients for, for example `VirtoCommerce.Catalog,VirtoCommerce.Orders`.

## Files updated

The command updates `.env` with API generation settings:

```env
APP_PLATFORM_MODULES=VirtoCommerce.Catalog,VirtoCommerce.Orders
APP_API_CLIENT_DIRECTORY=./src/api_client
APP_TYPE_STYLE=Interface
```

It updates `.env.local` with the machine-local Platform URL:

```env
APP_PLATFORM_URL=https://admin.example.com
```

Do not commit secrets or machine-specific credentials. `.env.local` is the place for local overrides.

## Generated clients

The skill runs the app's API generation command and writes clients under `src/api_client/`. Application code should use `useApiClient(ClientCtor)` rather than instantiating clients directly.

```ts
import { useApiClient, useAsync } from "@vc-shell/framework";
import { OrdersClient } from "../api_client/orders";

const { getApiClient } = useApiClient(OrdersClient);

const { action: loadOrders, loading } = useAsync(async () => {
  const client = await getApiClient();
  return client.searchOrders({ skip: 0, take: 20 });
});
```

- [Promote a prototype module.](promote-prototype-to-api.md)
