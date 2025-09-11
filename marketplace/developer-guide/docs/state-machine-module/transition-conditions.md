# Transition Conditions

Transition conditions are the business rules that determine when a state machine can move from one state to another. They provide the logic layer that enforces business constraints, validates data, checks permissions, and ensures that workflows follow proper procedures. This document covers built-in conditions, custom condition development, and best practices for implementing complex business logic.

Transition conditions are boolean expressions that must evaluate to `true` for a transition to be allowed. They act as gatekeepers, ensuring:

- **Security**: Users have appropriate permissions.
- **Business rules**: Only valid business operations are performed.

## Built-in condition types

The State Machine module provides several built-in condition types that control when transitions are allowed:

* [Security conditions](#security-conditions).
* [Field conditions](#field-conditions).

### Security conditions

Security conditions check user permissions.

**Example. Permission-based condition**:

```json
{
  "id": "StateMachineConditionHasPermission",
  "permissions": [
    "operator:product:approve"
  ]
}
```

### Field conditions

Field conditions compare entity properties against specific values or patterns. This condition model is based on standard [Virto Commerce conditions engine](https://github.com/VirtoCommerce/vc-module-core/tree/master/src/VirtoCommerce.CoreModule.Core/Conditions):

**Example. Basic field comparison**:

```json
{
"id": "PublicationRequestConditionApprovalPolicyIs",
"approvalPolicy": "Auto"
}
```

The supported operators include:

| Operator             | Description                          |
|----------------------|--------------------------------------|
| **equals**           | Exact match comparison               |
| **notEquals**        | Not equal comparison                 |
| **contains**         | String contains substring            |
| **startsWith**       | String starts with value             |
| **endsWith**         | String ends with value               |
| **greaterThan**      | Numeric greater than                 |
| **lessThan**         | Numeric less than                    |
| **greaterThanOrEqual** | Numeric greater than or equal      |
| **lessThanOrEqual**  | Numeric less than or equal           |
| **in**               | Value is in a list                   |
| **notIn**            | Value is not in a list               |
| **isEmpty**          | Field is null or empty               |
| **isNotEmpty**       | Field has a value                    |


**Example. Complex field conditions**:

```json
{
  "id": "FieldCondition",
  "fieldName": "price",
  "operator": "greaterThan",
  "value": 100
}
```

## Creating custom conditions

Custom conditions allow you to extend the state machine with domain-specific rules and behaviors tailored to your business logic. You can define:

* [Backend conditions.](#backend-conditions)
* [Frontend conditions.](#frontend-conditions)

### Backend conditions

Backend conditions define the logic that evaluates whether a state transition is allowed:

1. Implement `IConditionTree` rule:

    ```csharp
    public class PublicationRequestConditionApprovalPolicyIs : ConditionTree
    {
        public string ApprovalPolicy { get; set; }

        public override bool IsSatisfiedBy(IEvaluationContext context)
        {
            if (context is StateMachineTriggerContext stateMachineTriggerContext
                && stateMachineTriggerContext.ContextObject is ProductPublicationRequest productPublicationRequest)
            {
                return productPublicationRequest.ApprovalPolicy == ApprovalPolicy;
            }

            return false;
        }
    }
    ```

1. Composite custom rules in blocks, if necessary:

    ```csharp
    public class PublicationRequestConditionTreePrototype : ConditionTree
    {
        public PublicationRequestConditionTreePrototype()
        {
            WithAvailConditions(
                new PublicationRequestCondition().WithAvailConditions(
                    new StateMachineConditionHasPermission(),
                    new PublicationRequestConditionApprovalPolicyIs()
                )
            );
            Children = AvailableChildren.ToList();
        }
    }
    ```

1. Register the condition:

    ```csharp
    // In your module's PostInitialize method
    public void PostInitialize(IApplicationBuilder appBuilder)
    {
        ...
            foreach (var conditionTree in AbstractTypeFactory<PublicationRequestConditionTreePrototype>.TryCreateInstance().Traverse<IConditionTree>(x => x.AvailableChildren))
            {
                AbstractTypeFactory<IConditionTree>.RegisterType(conditionTree.GetType());
            }
        ...
    }
    ```

1. Use in State Machine Definition:

    ```json
    {
      "trigger": "OperatorApproveTrigger",
      "icon": "fa fa-cogs",
      "toState": "Approved",
      "condition": {
        "all": false,
        "not": false,
        "id": "PublicationRequestCondition",
        "children": [
          {
            "all": false,
            "not": false,
            "id": "PublicationRequestCondition",
            "children": [
              {
                "notHas": false,
                "permissions": [
                "operator:product:approve"
                ],
                "id": "StateMachineConditionHasPermission"
              },
              {
                "approvalPolicy": "Auto",
                "id": "PublicationRequestConditionApprovalPolicyIs"
              }
            ]
          }
        ]
      }
    }
    ```

### Frontend conditions

Frontend configuration provides UI templates for users to manage conditions visually in the Operator Portal. It typically involves two steps: 

1. Define the HTML template for displaying and editing a condition:

    ```html
    <!-- example template for ConditionHasPermission  -->
    <script type="text/ng-template" id="StateMachineConditionHasPermission.html">
    <a class="__link" left-click-menu data-target="notMenu">{{element1.notHas | boolToValue:'Has no':'Has'}}</a> permission
    <ul class="menu __context" role="menu" id="notMenu">
        <li class="menu-item" ng-click='element1.notHas=false;'>Has</li>
        <li class="menu-item" ng-click='element1.notHas=true;'>Has no</li>
    </ul>
    <div class="form-input">
        <ui-select multiple ng-model="element1.permissions" ng-controller="virtoCommerce.stateMachineModule.permissionConditionController">
        <ui-select-match placeholder="Select...">{{$item|json}}</ui-select-match>
        <ui-select-choices repeat="x in permissions | filter: $select.search">
            <span ng-bind-html="x | highlight: $select.search"></span>
        </ui-select-choices>
        </ui-select>
    </div>
    </script>
    ```

1. Implement a controller (e.g., Permission Condition Controller) to supply data and bind it to the template:


    ```javascript
    angular.module('virtoCommerce.stateMachineModule')
        .controller('virtoCommerce.stateMachineModule.permissionConditionController',
            ['$scope', 'platformWebApp.roles',
                function ($scope, roles) {
                    roles.queryPermissions({ take: 10000 }, function (result) {
                        $scope.permissions = result.map(x => x.name);
                    });
                }
            ]
        );
    ```

## Condition context and data

The condition context provides the runtime information that conditions use to evaluate state transitions, including details about the state machine instance, the current user, and the target entity.  

### StateMachineTriggerContext

StateMachineTriggerContext extends EvaluationContextBase. The ContextObject provides access to all relevant data for condition evaluation:

```csharp
public class StateMachineTriggerContext : EvaluationContextBase
{
    public StateMachineInstance StateMachineInstance { get; set; }
    public ClaimsPrincipal Principal { get; set; }
    public string EntityId { get; set; }
}
```

### Accessing entity data

```csharp
// Example of using from PublicationRequestConditionApprovalPolicyIs
public override bool IsSatisfiedBy(IEvaluationContext context)
{
    if (context is StateMachineTriggerContext stateMachineTriggerContext
        && stateMachineTriggerContext.ContextObject is ProductPublicationRequest productPublicationRequest)
    {
        return productPublicationRequest.ApprovalPolicy == ApprovalPolicy;
    }

    return false;
}
```

## Best practices

- Each condition should check one specific business rule.
- Avoid complex conditions that validate multiple unrelated aspects.
- Use composite conditions to combine simple conditions.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../entity-types">← Entity types</a>
    <a href="../operator-portal-actions">Operator portal actions →</a>
</div>