# Entity Types

Entity types are the foundation of the State Machine module, allowing you to bind state machine workflows to any business entity in your system. This document explains how to register entity types, create custom actions, and integrate state machines with your business logic.

An entity type represents a category of business objects that can be managed by state machines:

![Entity types](media/entity-types.png){: style="display: block; margin: 0 auto;" }

## Registration services

The module provides two key services for entity type management:

* [stateMachineTypes.js](#statemachinetypesjs)
* [stateMachineRegistrar.js](#statemachineregistrarjs)

### stateMachineTypes.js

This service manages the registry of available entity types:

```javascript
angular.module('virtoCommerce.stateMachineModule')
    .factory('virtoCommerce.stateMachineModule.stateMachineTypes', [function () {
        var registeredTypes = [];

        return {
            addType: function (entityType) {
                registeredTypes.push(entityType);
            },
            getAllTypes: function () {
                return registeredTypes;
            },
            getTypeInfo: function (type) {
                return registeredTypes.find(x => x.value === type);
            }
        };
    }]);
```

### stateMachineRegistrar.js

This service manages Operator Portal custom state actions:

```javascript
angular.module('virtoCommerce.stateMachineModule')
    .factory('virtoCommerce.stateMachineModule.stateMachineRegistrar', [function () {
        var registeredStates = {};

        return {
            registerStateAction: function (stateName, action) {
                registeredStates[stateName] = action;
            },
            getStateAction: function (stateName) {
                return registeredStates[stateName];
            }
        };
    }]);
```


## Register entities and frontend actions

1.  Register your entity type in your module's main JavaScript file as follows:

    ```javascript
    // Example from vc-module-marketplace-registration
    angular.module('virtoCommerce.marketplaceRegistrationModule')
        .run(['virtoCommerce.stateMachineModule.stateMachineTypes', function (stateMachineTypes) {
            // Register the RegistrationRequest entity type
            stateMachineTypes.addType({
                caption: 'marketplaceRegistration.state-machine-entity-types.registration-request',
                value: 'VirtoCommerce.MarketplaceRegistrationModule.Core.Models.RegistrationRequest'

            });
        }]);
    ```

1. Create custom Operator Portal frontend actions. They allow you to implement specific business logic when state transitions occur. To register custom actions:

    ```javascript
    // Example from vc-module-marketplace-registration
    angular.module('virtoCommerce.marketplaceRegistrationModule')
        .run(['virtoCommerce.stateMachineModule.stateMachineRegistrar', function (stateMachineRegistrar) {
            stateMachineRegistrar.registerStateAction('CompleteRegistrationRequest', {
                callbackFn: function (blade, successCallback) {
                    var foundMetaFields = metaFormsService.getMetaFields('SellerAdd');
                    var createSellerCommand = {
                        sellerName: blade.currentEntity.organizationName,
                        ownerDetails: {
                            firstName: blade.currentEntity.firstName,
                            lastName: blade.currentEntity.lastName,
                            email: blade.currentEntity.contactEmail
                        }
                    };
                    var newBlade = {
                        id: 'registrationRequestComplete',
                        command: createSellerCommand,
                        title: 'marketplace.blades.seller-add.title',
                        subtitle: 'marketplace.blades.seller-add.subtitle',
                        controller: 'virtoCommerce.marketplaceModule.sellerAddController',
                        template: 'Modules/$(VirtoCommerce.MarketplaceVendor)/Scripts/blades/seller-add.tpl.html',
                        metaFields: foundMetaFields,
                        successCallback: successCallback
                    };
                    blade.childBlade = newBlade;
                    bladeNavigationService.showBlade(newBlade, blade);
                }
            });
        }]);
    ```

## Best practices

* Naming conventions:

    - Use PascalCase for entity type values: `RegistrationRequest`, `ProductApproval`.
    - Use descriptive display names: "Vendor Registration Request", "Product Approval Workflow".
    - Keep trigger names consistent: `SubmitTrigger`, `ApproveTrigger`, `RejectTrigger`, `CancelTrigger`.

* Error handling:
    ```javascript
    $scope.executeAction = function(trigger) {
        $scope.loading = true;

        stateMachineApi.fireTrigger({
            instanceId: $scope.stateMachineInstance.id,
            trigger: trigger
        }).$promise.then(function(result) {
            // Success handling
            notificationService.success('Action completed successfully');
            $scope.loadStateMachine();
        }).catch(function(error) {
            // Error handling
            notificationService.error('Action failed: ' + error.data.message);
        }).finally(function() {
            $scope.loading = false;
        });
    };
    ```

* Performance optimization:

    - Cache state machine instances when possible.
    - Use lazy loading for entity lists with state information.
    - Implement pagination for large datasets.

* Security considerations:
    - Always validate permissions before executing actions.
    - Sanitize user input in custom actions.
    - Use HTTPS for all state machine API calls.

## Troubleshooting

* Common issues:

    | **Issue**                 | **Troubleshooting**                                                         |
    |---------------------------|-----------------------------------------------------------------------------|
    | Entity type not appearing | Ensure the registration code runs after the state machine module is loaded. |
    | Actions not working       | Check that permissions are correctly configured.                            |
    | State not updating        | Verify that the entity ID and type match exactly.                           |


* Debugging tips:

    ```javascript
    // Enable debug logging
    angular.module('yourModule')
        .run(['$log', function($log) {
            $log.debug('Registering entity type: YourEntityType');
        }]);

    // Check registered types
    console.log(stateMachineTypes.getAllTypes());

    // Verify action registration
    console.log(stateMachineRegistrar.getStateAction('YourState'));
    ```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../data-structure">← Data structure</a>
    <a href="../transition-conditions">Transition conditions →</a>
</div>