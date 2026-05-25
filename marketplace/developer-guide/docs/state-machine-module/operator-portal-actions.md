# State Machine Actions in Operator Portal  

The Operator Portal provides comprehensive state machine management capabilities for administrators and operators. This guide explains how to integrate state machine actions into the Operator interface and manage entity life cycles through the administrative portal.  

The following example shows how state machine actions are implemented for a Product Publication Request. The controller defines toolbar commands, adds available state machine actions dynamically, and executes triggers through the backend API:

```javascript
angular.module('virtoCommerce.marketplaceModule')
    .controller('virtoCommerce.marketplaceModule.sellerProductDetailsController',
        ['$scope', ...
        function ($scope, ...) {
          ...
          // Step 1: Initialize the blade and set up commands
          function initializeBlade(data) {
            ...
              fillTollbarCommands();
            ...
          }

          // Step 2: Populate toolbar commands, including state machine actions
          function fillTollbarCommands() {
              blade.toolbarCommands = [];
              
              // Add regular tool buttons first
              ...
              
              // Add state machine actions dynamically
              if (blade.stateMachineInstance
                  && blade.stateMachineInstance.currentState
                  && blade.stateMachineInstance.currentState.transitions
                  && blade.stateMachineInstance.permittedTriggers
              ) {
                  blade.stateMachineInstance.currentState.transitions.forEach((element, index) => {
                      if (blade.stateMachineInstance.permittedTriggers.includes(element.trigger)) {
                          var command = {
                              id: 'command' + element.trigger,
                              name: element.localizedValue || element.trigger,
                              title: element.description,
                              icon: element.icon,
                              executeMethod: function () {
                                  doAction(element.trigger);
                              }
                          };
                          if (!blade.toolbarCommands.find(x => x.id === "command" + element.trigger)) {
                              blade.toolbarCommands.splice(index, 0, command);
                              addedButtonsCount++;
                          }
                      }
                  });
              }
              
              // Add more tool buttons after state machine actions if needed
          }

          // Step 3: Execute a state machine action
          function doAction(trigger) {
              blade.isLoading = true;
              var stateMachineAction = stateMachineRegistrar.getStateAction(trigger);
              
              // Call registered action if exists, then fire backend trigger
              if (stateMachineAction && stateMachineAction.callbackFn && typeof stateMachineAction.callbackFn === "function") {
                  function successCallback() {
                      doStateMachineStep(trigger);
                  };
                  stateMachineAction.callbackFn(blade, successCallback);
              } else {
                  doStateMachineStep(trigger);
              }

              blade.isLoading = false;
          }

          // Step 4: Fire the backend state machine trigger
          function doStateMachineStep(trigger) {
              stateMachineApi.fireStateMachineInstanceTrigger({
                  stateMachineInstanceId: blade.stateMachineInstance.id,
                  trigger: trigger,
                  entityId: publicationRequestId
              },
              function (data) {
                  // Refresh the blade to reflect state changes
                  blade.refresh(true);
              });
          }

          ...
          // Other blade logic
}]);
```

In the Operator Portal, the applied modifications look as follows:

![Product Publication actions in Operator Portal](media/operator-product-publication-actions.png){: style="display: block; margin: 0 auto;" width="400"}

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../transition-conditions">← Transition conditions</a>
    <a href="../vendor-portal-actions">Vendor Portal actions →</a>
</div>