# Getting Started

The fastest path into VC-Shell is AI-assisted generation with the `vc-app` skill. Use it to create a working prototype, connect it to a Virto Commerce Platform instance, and then promote generated mock modules to real API clients.

## New to VC-Shell?

Start with [Tutorial: Your First VC-Shell Module](your-first-module.md). It walks through the whole loop in about thirty minutes — scaffold an app, generate a real ecommerce module with the `vc-app` skill, explore the running result, and edit a column. By the end you have hands-on grounding in every concept the rest of the documentation reuses.

## Recommended path

1. [Install the vc-app skill](install-vc-app-skill.md).
2. [Generate an app from a prompt](generate-app-from-prompt.md).
3. [Connect the app to Platform](connect-to-platform.md).
4. [Promote prototype modules to API clients](promote-prototype-to-api.md).
5. Use [guides](../guides/blades/index.md), [components](../components/layout/vc-app.md), and [composables](../composables/blade-navigation/useBlade.md) to productionize the app.

## Manual path

Use the manual path when you need deterministic commands or when your team does not use the `vc-app` skill:

1. [Manual CLI start](manual-cli-start.md) creates the app and empty module skeletons.
2. [Manual Platform API setup](manual-platform-api-setup.md) connects the app to Platform, generates API clients, and wires module composables to `useApiClient`.

## What you have after this path

After either path, you have a running VC-Shell app, one or more modules, a Platform URL in local configuration, typed API clients under `src/api_client/`, and a clear route from prototype data to production API calls.
