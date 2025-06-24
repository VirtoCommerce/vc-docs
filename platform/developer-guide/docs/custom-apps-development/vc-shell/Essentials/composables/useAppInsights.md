# useAppInsights Composable

The `useAppInsights` composable provides functionality for working with Microsoft Application Insights in VC-Shell applications. It allows components to track page views, custom events, and exceptions with additional context information.

Application Insights is an extensible Application Performance Management (APM) service for developers and DevOps professionals. The `useAppInsights` composable simplifies integration with this service, making it easier to track user interactions and application performance in VC-Shell applications.

## API reference

### Return value

The `useAppInsights` composable returns an object with the following properties:

```typescript
interface IUseAppInsights {
  setupPageTracking: {
    beforeEach: (route: { name: string }) => void;  // Track page view start
    afterEach: (route: { name: string; fullPath: string }) => void;  // Track page view end
  };
  appInsights: ApplicationInsights;  // Direct access to Application Insights instance
}
```

The `setupPageTracking` object contains methods that can be used with Vue Router navigation guards to automatically track page views. The `appInsights` property provides direct access to the Application Insights instance with all standard tracking methods.

## Configuration

Before using the `useAppInsights` composable, you need to configure Application Insights in your VC-Shell application:

```typescript
import { createApp } from 'vue';
import { createRouter } from 'vue-router';
import VcShellFramework from '@vc-shell/framework';
import App from './App.vue';

const router = createRouter({
  /* router configuration */
});

const app = createApp(App);

// Install VC-Shell framework with Application Insights configuration
app.use(VcShellFramework, {
  router,
  applicationInsights: {
    instrumentationKey: 'YOUR_INSTRUMENTATION_KEY',
    appName: 'YourAppName', // Optional, adds [AppName] prefix to tracked pages
    cloudRole: 'web',       // Optional, used for cloud role name
    cloudRoleInstance: window.location.hostname // Optional, instance name
  }
});

app.mount('#app');
```

## Usage

The `useAppInsights` composable provides access to Application Insights functionality in VC-Shell applications.

### Basic usage

```typescript
import { useAppInsights } from '@vc-shell/framework';

const { setupPageTracking, appInsights } = useAppInsights();
```

### Automatic features

The VC-Shell framework automatically provides the following telemetry when Application Insights is configured:

- **Vue Router Navigation**: Automatic page view tracking for all route changes
- **Blade Navigation**: Automatic tracking of blade opening/closing in VC-Shell applications  
- **Error Tracking**: Global error handler automatically tracks exceptions and errors
- **User Context**: User information is automatically added to all telemetry events

No additional setup is required for these basic tracking features.

## Available methods

### setupPageTracking

Provides methods for manual page tracking:

- `beforeEach(route: { name: string })` - Start tracking a page view
- `afterEach(route: { name: string; fullPath: string })` - Complete tracking a page view

### appInsights

Direct access to the Application Insights instance with all standard methods:

- `trackEvent(event: IEventTelemetry)` - Track custom events
- `trackMetric(metric: IMetricTelemetry)` - Track performance metrics  
- `trackException(exception: IExceptionTelemetry)` - Track exceptions
- `trackDependency(dependency: IDependencyTelemetry)` - Track API calls and dependencies
- `trackPageView(pageView: IPageViewTelemetry)` - Track page views
- `trackTrace(trace: ITraceTelemetry)` - Track diagnostic traces

## How it works

The `useAppInsights` composable:

1. Accesses the Application Insights instance provided by the `vue3-application-insights` plugin
1. Provides utilities for page tracking with unique trace IDs 
1. Automatically adds user context to tracked events
1. Generates unique W3C trace IDs for each page view to enable distributed tracing
1. Integrates with the VC-Shell user system to add user information to telemetry

