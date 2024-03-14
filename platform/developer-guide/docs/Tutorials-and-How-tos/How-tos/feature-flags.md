Feature flags, also known as feature toggles or feature switches, are a powerful technique used in software development to enable or disable features in an application or service. They provide developers with the ability to dynamically control the activation and visibility of features at runtime without deploying new code. This allows for safer experimentation, gradual feature rollouts, and targeted feature releases.

## Benefits of Using Feature Flags

Integrating feature flags into Virto Commerce and Virto Storefront offers several significant benefits:

* **Modularity**: Feature flags enable safe and controlled feature releases by allowing developers to enable or disable features remotely by installing/uninstalling Virto Commerce module. 
* **A/B Testing**: Feature flags facilitate A/B testing and experimentation by enabling developers to test new features with a subset of users before rolling them out to the entire user base.
* **Rollback Control**: In case of issues or unexpected behaviour, feature flags provide the ability to quickly roll back changes by disabling the problematic feature.
* **Configuration Management**: Feature flags provide a centralized mechanism for managing feature configurations, making it easier to manage feature variations across different environments.

## Architecture 

[Virto Commerce Platform 3.813+](https://github.com/VirtoCommerce/vc-platform) and [Virto Commerce XAPI 3.812+](https://github.com/VirtoCommerce/vc-module-experience-api) introduce Public Store Settings. This architecture enables seamless integration of feature flags into Virto Commerce and Virto Storefront.

* Virto Commerce extended `SettingDescriptor` with the `IsPublic` property, indicating that a setting is accessible for client applications via the XAPI. 
* Virto Commerce XAPI extended store query with modules that grant access to Public Store Settings per module. 


## Example. Create Public Property Based on Google Analytics Module

The following code snippet demonstrates how to create public properties for the Google Analytics module using the extended `SettingDescriptor`:

```cs
public static SettingDescriptor EnableTracking { get; } = new SettingDescriptor
{
    Name = "GoogleAnalytics4.EnableTracking",
    GroupName = "Google Analytics 4",
    ValueType = SettingValueType.Boolean,
    IsPublic = true
};

public static SettingDescriptor MeasurementId { get; } = new SettingDescriptor
{
    Name = "GoogleAnalytics4.MeasurementId",
    GroupName = "Google Analytics 4",
    ValueType = SettingValueType.ShortText,
    IsPublic = true
};
```

### XAPI/GraphQL Schema

To retrieve store settings and module settings via GraphQL queries, you can use the following schema examples:

=== "Query"

    ```graphql
    query{
    store(storeId: "B2B-store", cultureName: "en-US") {
        storeId
        settings {
        modules { moduleId settings {name value} }
        }
    }
    }
    ```

=== "Return"
    ```graphql
    {
    "data": {
        "store": {
        "storeId": "B2B-store",
        "settings": {
            "modules": [
            {
                "moduleId": "VirtoCommerce.GoogleEcommerceAnalytics",
                "settings": [
                {
                    "name": "GoogleAnalytics4.EnableTracking",
                    "value": true
                },
                {
                    "name": "GoogleAnalytics4.MeasurementId",
                    "value": "GA-B2B-STORE"
                }
                ]
            }
            ]
        }
        }
    }
    }
    ``` 

## How to Do GraphQL Call in Virto Storefront

In Virto Storefront, you can use GraphQL queries to request modules with public settings. Here's an example of how to check if the Google Analytics module is installed and retrieve its settings.

In this utility class, we define methods to check if a feature is enabled and to get the value of a feature based on the provided `moduleId` and `featureName`. This approach encapsulates feature flag logic and promotes reusability and maintainability in your VueJS application.

```js
class FeatureFlags {
  constructor(modules) {
    this.modules = modules;
  }

  isEnabled(moduleId, featureName) {
    const module = this.modules.find(module => module.moduleId === moduleId);
    if (module) {
      const feature = module.settings.find(setting => setting.name === featureName);
      if (feature && feature.value === true) {
        return true;
      }
    }
    return false;
  }

  getValue(moduleId, featureName) {
    const module = this.modules.find(module => module.moduleId === moduleId);
    if (module) {
      const feature = module.settings.find(setting => setting.name === featureName);
      if (feature && feature.value !== undefined) {
        return feature.value;
      }
    }
    return null;
  }

  isEnabled(moduleId) {
    const module = this.modules.find(module => module.moduleId === moduleId);
    return !!module;
  }
}

```

In this example, the GraphQL query retrieves store settings, including modules and their settings. The returned data can then be processed to determine if the Google Analytics module is installed and retrieve its settings.

```js
// Instantiate FeatureFlags with modules data
const featureFlags = new FeatureFlags(result.data.store.settings.modules);

// Check if a module is enabled
const isModuleEnabled = featureFlags.isEnabled("VirtoCommerce.GoogleEcommerceAnalytics");

// Check if a feature is enabled
const isTrackingEnabled = featureFlags.isEnabled("VirtoCommerce.GoogleEcommerceAnalytics", "GoogleAnalytics4.EnableTracking");

// Get feature value
const measurementId = featureFlags.getValue("VirtoCommerce.GoogleEcommerceAnalytics", "GoogleAnalytics4.MeasurementId");

```

Integrating feature flags with Virto Commerce and Virto Storefront using public store settings and GraphQL queries provides developers with a flexible and efficient way to manage feature variations and configurations in their applications.

## Summary

Implementing feature flags with Virto Commerce and Virto Storefront provides developers with a flexible and efficient way to manage feature variations and configurations in their applications. By leveraging public store settings and GraphQL queries, developers can easily control feature activation and visibility at runtime, enabling safer experimentation, gradual rollouts, and targeted releases.