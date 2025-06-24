# Error Handling in VC-Shell

VC-Shell provides a comprehensive and automatic error handling system that ensures a smooth user experience when errors occur in your application. This guide explains how the framework handles errors and how you should work with them as a developer.

## Overview

The VC-Shell framework implements error handling at multiple levels to provide a robust and user-friendly experience:

1. **Automatic Blade Error Handling**: All errors within blade components are automatically captured and displayed
2. **Global Error Handling**: Application-wide errors are handled through Vue's error handling system
3. **User-Friendly Error Display**: Errors are presented in a consistent, non-disruptive manner

The key principle is **simplicity**: you don't need to set up complex error handling - just throw errors where appropriate, and the framework handles the rest.

## How Error Handling Works

### Automatic Error Capture in Blades

Every blade in VC-Shell is automatically wrapped with error handling. When an error occurs within a blade:

1. **Error is Caught**: The framework automatically captures any thrown errors
2. **User Interface**: A user-friendly error message is displayed within the blade
3. **Application Stability**: The error doesn't crash the entire application
4. **Error Recovery**: Users can dismiss the error and continue working

```vue
<!-- Your blade component -->
<script lang="ts" setup>
import { useApiClient } from '@vc-shell/framework';

const { getApiClient } = useApiClient(ProductsClient);

async function loadProduct(id: string) {
  try {
    const client = await getApiClient();
    const product = await client.getProductById(id);
    return product;
  } catch (error) {
    // Simply throw the error - the framework will handle display
    throw new Error(`Failed to load product: ${error.message}`);
  }
}

// Or even simpler - let the API error bubble up naturally
async function loadProductSimple(id: string) {
  const client = await getApiClient();
  // If this fails, the error will be automatically caught and displayed
  return await client.getProductById(id);
}
</script>
```

### Error Display in Blades

When an error occurs, the blade automatically shows:

- **Error Message**: Clear description of what went wrong
- **More Button**: Allows users to see more details about the error

## Global Error Handling

For errors that occur outside of blades or need special handling, VC-Shell provides global error handling:

```typescript
// In main.ts - global error handler is automatically configured
// You typically don't need to modify this, but it's available if needed

app.config.errorHandler = (err) => {
  // Global errors are automatically logged and displayed via notifications
  console.error('Global error:', err);
};
```

## Best Practices

1. **Keep It Simple**: Just throw errors where appropriate - the framework handles the display
2. **Clear Messages**: Write error messages that help users understand what happened and what to do next
3. **Don't Over-Handle**: Avoid complex error handling unless specifically needed
4. **User-Focused**: Write error messages from the user's perspective, not the technical perspective

## What You Don't Need to Do

- ❌ Set up error boundaries manually
- ❌ Create custom error display components
- ❌ Handle error state management
- ❌ Implement error logging (it's automatic)
- ❌ Worry about error recovery UI

## Integration with Other Features

### With Notifications
```typescript
import { notification } from '@vc-shell/framework';

async function saveProduct(product: Product) {
  try {
    await api.saveProduct(product);
    notification.success('Product saved successfully');
  } catch (error) {
    // Error will be displayed in blade automatically
    // Optionally, you can also show a notification
    notification.error('Failed to save product');
    throw error; // Let blade error handling take over
  }
}
```

### With Loading States
```typescript
import { useAsync } from '@vc-shell/framework';

// useAsync automatically handles errors from your async operations
const { action: saveProduct, loading } = useAsync(async (product: Product) => {
  // Any errors thrown here will be caught by blade error handling
  const client = await getApiClient();
  await client.saveProduct(product);
});
```

By following these guidelines, you can build robust applications with excellent error handling while keeping your code simple and maintainable. The VC-Shell framework takes care of the complex error handling infrastructure, allowing you to focus on your business logic.

## Related Resources

- [useAsync Composable](../composables/useAsync.md) - For handling errors in asynchronous operations
- [useApiClient Composable](../composables/useApiClient.md) - For API error handling patterns
- [Notification System](../shared/components/notifications.md) - For additional user feedback
- [Blade Navigation](../shared/components/blade-navigation.md) - Understanding the blade system where errors are displayed 
