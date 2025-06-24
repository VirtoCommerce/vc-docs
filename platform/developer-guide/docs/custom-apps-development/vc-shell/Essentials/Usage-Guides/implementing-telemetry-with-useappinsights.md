# How-To: Implementing Telemetry with `useAppInsights`

The `useAppInsights` composable provides integration with Microsoft Application Insights for tracking user interactions, performance metrics, and application telemetry in VC-Shell applications. This guide demonstrates how to configure and use Application Insights for comprehensive application monitoring.

## Prerequisites

- Understanding of Vue 3 application setup and configuration.
- Familiarity with the `useAppInsights` composable (see [useAppInsights API Reference](../composables/useAppInsights.md)).
- Microsoft Azure account with Application Insights resource configured.
- Basic knowledge of telemetry and application performance monitoring concepts.

## Core Concept

Application Insights provides:

- **Page View Tracking**: Automatic tracking of route navigation and page views
- **Performance Monitoring**: Application performance metrics and load times
- **Error Tracking**: Automatic exception and error logging
- **User Analytics**: User behavior and interaction patterns
- **Custom Events**: Track specific business events and user actions

The `useAppInsights` composable integrates seamlessly with VC-Shell's routing and user management systems.

## Setup and Configuration

### 1. Configure Application Insights in main.ts

Add Application Insights configuration when initializing your VC-Shell application:

```typescript
// main.ts
import VirtoShellFramework, { useLanguages, useUser } from "@vc-shell/framework";
import { createApp } from "vue";
import { router } from "./router";
import * as locales from "./locales";
import { RouterView } from "vue-router";

async function startApp() {
  const { loadUser } = useUser();
  
  try {
    await loadUser();
  } catch (e) {
    console.log(e);
  }

  const { currentLocale, setLocale } = useLanguages();
  const app = createApp(RouterView);

  // Configure VC-Shell Framework with Application Insights
  app.use(VirtoShellFramework, {
    router,
    i18n: {
      locale: import.meta.env.APP_I18N_LOCALE,
      fallbackLocale: import.meta.env.APP_I18N_FALLBACK_LOCALE,
    },
    // Application Insights configuration
    applicationInsights: {
      instrumentationKey: import.meta.env.APP_INSIGHTS_INSTRUMENTATION_KEY,
      appName: 'VendorPortal', // Optional: adds [VendorPortal] prefix to tracked pages
      cloudRole: 'web',        // Optional: used for cloud role name
      cloudRoleInstance: window.location.hostname, // Optional: instance name
    }
  });

  // Rest of your application setup...
  Object.entries(locales).forEach(([key, message]) => {
    app.config.globalProperties.$mergeLocaleMessage(key, message);
  });

  setLocale(currentLocale.value);

  await router.isReady();
  app.mount("#app");
}

startApp();
```

### 2. Environment Variables Setup

Configure your environment variables for different deployment stages:

```bash
# .env.development
APP_INSIGHTS_INSTRUMENTATION_KEY=your-dev-instrumentation-key

# .env.production  
APP_INSIGHTS_INSTRUMENTATION_KEY=your-prod-instrumentation-key

# .env.staging
APP_INSIGHTS_INSTRUMENTATION_KEY=your-staging-instrumentation-key
```

### 3. TypeScript Environment Declaration

Add type definitions for your environment variables:

```typescript
// src/env.d.ts
interface ImportMetaEnv {
  readonly APP_INSIGHTS_INSTRUMENTATION_KEY: string;
  readonly APP_I18N_LOCALE: string;
  readonly APP_I18N_FALLBACK_LOCALE: string;
  // other env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## Usage Patterns

### 1. Built-in Automatic Tracking

VC-Shell provides comprehensive automatic tracking out of the box when Application Insights is configured:

```typescript
// ✅ These are automatically tracked - no additional code needed:

// Vue Router navigation (page views)
// Blade navigation (opening/closing blades)
// Global errors and exceptions
// User context (automatically added to all events)
```

**What's tracked automatically:**

- **Page Views**: All Vue Router navigation with timing and user context
- **Blade Navigation**: Opening and closing of VC-Shell blades
- **Errors**: Global error handler captures all unhandled exceptions
- **User Context**: User ID, username, and role automatically added to all telemetry

### 2. Manual Page Tracking for Virtual Pages

For components that represent virtual pages or complex single-page views:

```typescript
// VirtualPageComponent.vue
<script lang="ts" setup>
import { useAppInsights } from '@vc-shell/framework';
import { onMounted, onBeforeUnmount } from 'vue';

const { setupPageTracking } = useAppInsights();

onMounted(() => {
  // Track virtual page view start
  setupPageTracking.beforeEach({ 
    name: 'ProductDetailsModal' 
  });
});

onBeforeUnmount(() => {
  // Track virtual page view end
  setupPageTracking.afterEach({ 
    name: 'ProductDetailsModal', 
    fullPath: '/products/modal/details'
  });
});
</script>
```

### 3. Custom Event Tracking

Track specific business events and user interactions using the `appInsights` instance:

```typescript
// useCustomTelemetry.ts
import { useAppInsights } from '@vc-shell/framework';

export function useCustomTelemetry() {
  const { appInsights } = useAppInsights();

  function trackCustomEvent(eventName: string, properties?: Record<string, any>) {
    if (appInsights) {
      appInsights.trackEvent({
        name: eventName,
        properties: {
          timestamp: new Date().toISOString(),
          ...properties
        }
      });
    }
  }

  function trackUserAction(action: string, target: string, properties?: Record<string, any>) {
    trackCustomEvent('UserAction', {
      action,
      target,
      ...properties
    });
  }

  function trackBusinessEvent(eventType: string, data: Record<string, any>) {
    trackCustomEvent('BusinessEvent', {
      eventType,
      ...data
    });
  }

  function trackMetric(name: string, value: number, properties?: Record<string, any>) {
    if (appInsights) {
      appInsights.trackMetric({
        name,
        average: value,
        properties
      });
    }
  }

  return {
    trackCustomEvent,
    trackUserAction,
    trackBusinessEvent,
    trackMetric
  };
}
```

### 4. Custom Error Tracking

While global errors are tracked automatically, you can track specific exceptions manually:

```typescript
// useErrorTracking.ts
import { useAppInsights } from '@vc-shell/framework';

export function useErrorTracking() {
  const { appInsights } = useAppInsights();

  function trackException(error: Error, properties?: Record<string, any>) {
    if (appInsights) {
      appInsights.trackException({
        exception: error,
        properties: {
          timestamp: new Date().toISOString(),
          ...properties
        }
      });
    }
  }

  function trackApiError(endpoint: string, error: Error, statusCode?: number) {
    trackException(error, {
      errorType: 'API_ERROR',
      endpoint,
      statusCode: statusCode?.toString(),
      errorMessage: error.message
    });
  }

  return {
    trackException,
    trackApiError
  };
}

// Usage in components
export function useProductsWithErrorTracking() {
  const { trackApiError } = useErrorTracking();

  async function loadProducts() {
    try {
      const products = await api.getProducts();
      return products;
    } catch (error) {
      // Track specific API error (in addition to automatic global error tracking)
      trackApiError('/api/products', error as Error, error.status);
      throw error;
    }
  }

  return { loadProducts };
}
```

### 5. Performance Tracking

Track custom performance metrics using the `appInsights` instance:

```typescript
// usePerformanceTracking.ts
import { useAppInsights } from '@vc-shell/framework';

export function usePerformanceTracking() {
  const { appInsights } = useAppInsights();

  function trackLoadTime(operationName: string, startTime: number) {
    const duration = performance.now() - startTime;
    
    if (appInsights) {
      appInsights.trackMetric({
        name: `${operationName}_LoadTime`,
        average: duration,
        properties: {
          operation: operationName,
          timestamp: new Date().toISOString()
        }
      });
    }
  }

  function trackApiCall(endpoint: string, method: string, duration: number, success: boolean) {
    if (appInsights) {
      appInsights.trackDependency({
        target: endpoint,
        name: `${method} ${endpoint}`,
        data: endpoint,
        duration,
        success,
        dependencyTypeName: 'HTTP'
      });
    }
  }

  function trackComponentRender(componentName: string, renderTime: number) {
    if (appInsights) {
      appInsights.trackMetric({
        name: 'ComponentRenderTime',
        average: renderTime,
        properties: {
          componentName,
          timestamp: new Date().toISOString()
        }
      });
    }
  }

  return {
    trackLoadTime,
    trackApiCall,
    trackComponentRender
  };
}
```

## Integration with Composables

### 1. API Client Integration

Track API calls automatically:

```typescript
// Enhanced API client with telemetry
import { useApiClient } from '@vc-shell/framework';
import { usePerformanceTracking } from './usePerformanceTracking';

export function useProductsApi() {
  const { getApiClient } = useApiClient(ProductsClient);
  const { trackApiCall } = usePerformanceTracking();

  async function searchProducts(query: SearchQuery) {
    const startTime = performance.now();
    
    try {
      const client = await getApiClient();
      const result = await client.searchProducts(query);
      
      // Track successful API call
      trackApiCall('/api/products/search', 'POST', performance.now() - startTime, true);
      
      return result;
    } catch (error) {
      // Track failed API call
      trackApiCall('/api/products/search', 'POST', performance.now() - startTime, false);
      throw error;
    }
  }

  return { searchProducts };
}
```

### 2. User Action Tracking

Track user interactions in components:

```typescript
// ProductListComponent.vue
<script lang="ts" setup>
import { useAppInsights } from '@vc-shell/framework';

const { appInsights } = useAppInsights();

function trackUserAction(action: string, target: string, properties?: Record<string, any>) {
  if (appInsights) {
    appInsights.trackEvent({
      name: 'UserAction',
      properties: {
        action,
        target,
        timestamp: new Date().toISOString(),
        ...properties
      }
    });
  }
}

function onProductClick(product: Product) {
  trackUserAction('click', 'product-item', {
    productId: product.id,
    productName: product.name,
    category: product.category
  });
  
  // Navigate to product details
  router.push(`/products/${product.id}`);
}

function onFilterApplied(filterType: string, filterValue: string) {
  trackUserAction('filter', 'product-list', {
    filterType,
    filterValue,
    resultCount: products.value.length
  });
}
</script>
```

## Advanced Configuration

### 1. Custom Telemetry Initializers

Add custom properties to all telemetry:

```typescript
// main.ts - Advanced Application Insights setup
app.use(VirtoShellFramework, {
  router,
  applicationInsights: {
    instrumentationKey: import.meta.env.APP_INSIGHTS_INSTRUMENTATION_KEY,
    appName: 'VendorPortal',
    cloudRole: 'web',
    
    // Custom telemetry initializer
    onInit: (appInsights) => {
      appInsights.addTelemetryInitializer((envelope) => {
        // Add custom properties to all telemetry
        envelope.data.baseData = envelope.data.baseData || {};
        envelope.data.baseData.properties = envelope.data.baseData.properties || {};
        
        // Add application version
        envelope.data.baseData.properties.appVersion = import.meta.env.PACKAGE_VERSION;
        
        // Add user tenant information
        const user = getCurrentUser();
        if (user) {
          envelope.data.baseData.properties.tenantId = user.tenantId;
          envelope.data.baseData.properties.userRole = user.role;
        }
        
        return true;
      });
    }
  }
});
```

### 2. Conditional Telemetry

Enable telemetry only in specific environments:

```typescript
// main.ts - Conditional telemetry setup
const shouldEnableTelemetry = import.meta.env.PROD || import.meta.env.STAGING;

app.use(VirtoShellFramework, {
  router,
  i18n: {
    locale: import.meta.env.APP_I18N_LOCALE,
    fallbackLocale: import.meta.env.APP_I18N_FALLBACK_LOCALE,
  },
  // Only enable Application Insights in production/staging
  ...(shouldEnableTelemetry && {
    applicationInsights: {
      instrumentationKey: import.meta.env.APP_INSIGHTS_INSTRUMENTATION_KEY,
      appName: 'VendorPortal',
      cloudRole: 'web'
    }
  })
});
```

## Best Practices

1. **Environment-Specific Configuration**: Use different instrumentation keys for development, staging, and production.

2. **Privacy Compliance**: Ensure telemetry collection complies with privacy regulations (GDPR, CCPA).

3. **Performance Impact**: Monitor the performance impact of telemetry collection on your application.

4. **Data Retention**: Configure appropriate data retention policies in Azure Application Insights.

5. **Custom Properties**: Add meaningful custom properties to help with debugging and analytics.

6. **Error Context**: Include relevant context information when tracking exceptions.

## Monitoring and Analytics

### Key Metrics to Track

- **Page Load Times**: Monitor application performance
- **User Flows**: Track common user navigation patterns  
- **API Response Times**: Monitor backend performance
- **Error Rates**: Track application stability
- **Feature Usage**: Understand which features are most used

### Creating Dashboards

Use Azure Application Insights to create dashboards for:
- Application performance overview
- User behavior analytics
- Error tracking and debugging
- Business metrics and KPIs

By following this guide, you can implement comprehensive telemetry in your VC-Shell application, providing valuable insights into user behavior, application performance, and system health.

