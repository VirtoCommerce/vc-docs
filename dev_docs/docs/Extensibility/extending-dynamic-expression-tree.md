# How to Extend Dynamic Expression Tree

This article will show you how to extend the existing promotion expression tree of the Marketing module with these new elements:

+ New expression block:

![New expression block](media/09-new-expression-block.png)

+ New block element:

![New block element](media/10-new-block-element.png)

To view or download our sample code, click [here](https://github.com/VirtoCommerce/vc-module-marketing/tree/dev/samples/VirtoCommerce.MarketingSampleModule.Web).

## Prerequisites
Prior to extending your dynamic expression tree, you need to:

+ Create an empty custom module, as described [here](https://docs.virtocommerce.org/new/dev_docs/Tutorials-and-How-tos/Tutorials/creating-custom-module/).
    
-   Add the [VirtoCommerce.MarketingModule.Core](https://www.nuget.org/packages/VirtoCommerce.MarketingModule.Core) NuGet dependency to your project.

## Defining New Class for Expression Tree Prototype
The following example creates a new derived [PromotionConditionAndRewardTreePrototype](https://github.com/VirtoCommerce/vc-module-marketing/blob/dev/src/VirtoCommerce.MarketingModule.Core/Model/Promotions/PromotionConditionAndRewardTreePrototype.cs) that represents the original expression tree used for marketing promotion. Here, we register a new `BlockSampleConditionroot` block and extend the existing `BlockCatalogCondition` with a new element, `SampleCondition`:

``` csharp title="SamplePromotionConditionAndRewardTreePrototype.cs"
public sealed class SamplePromotionConditionAndRewardTreePrototype : PromotionConditionAndRewardTreePrototype
    {
        public SamplePromotionConditionAndRewardTreePrototype()
        {
            //Extend existing 'If any of these catalog condition' block with a new condition element
            var blockCatalogCondition = AvailableChildren.OfType<BlockCatalogCondition>().FirstOrDefault();
            blockCatalogCondition.AvailableChildren.Add(new SampleCondition());

            // Add a new block with sample condition to the beginning of the tree
            var blockSampleConditions = new BlockSampleCondition().WithAvailConditions(new SampleCondition());
            AvailableChildren.Insert(0, blockSampleConditions);
            Children.Insert(0, blockSampleConditions);
        }
    }
```

## Registering Your Extension in module.cs
The next step includes overriding the original `PromotionConditionAndRewardTreePrototype` type with the newly created one in the `module.cs` file:

``` csharp title="module.cs"
public void Initialize(IServiceCollection serviceCollection)
        {
            // Override the original expression prototype tree with new type
            AbstractTypeFactory<PromotionConditionAndRewardTreePrototype>.OverrideType<PromotionConditionAndRewardTreePrototype, SamplePromotionConditionAndRewardTreePrototype>();
        }
```

After that, you need to add a dependency to the Marketing module into the `module.manifest` file:

``` html title="module.manifest"
...
 <dependencies>
        <dependency id="VirtoCommerce.Marketing" version="3.0.0" />
    </dependencies>
...
```

!!! note
	This line is important for correct module initialization order. You can read more about module initialization [here](https://docs.virtocommerce.org/new/dev_docs/Fundamentals/Modularity/04-loading-modules-into-app-process/#creating-solution-from-template).

## Defining HTML Templates for New Elements

It is a best practice to define all HTML templates for new elements within an individual file, where the templates will be loaded dynamically as resources.

!!! warning
	Make sure to use the following schema as a template ID: `expression-{C# element class name}.html`.

``` html title="Scripts/all-templates.js"
<script type="text/ng-template" id="expression-BlockSampleCondition.html">
    For condition evaluator with
    <a class="__link" left-click-menu data-target="allAny_menu{{element.id}}">{{element.all | boolToValue:'all':'any'}}</a> of these sample values
    <ul class="menu __context" role="menu" id="allAny_menu{{element.id}}">
        <li class="menu-item" ng-click='element.all=true;'>all</li>
        <li class="menu-item" ng-click='element.all=false;'>any</li>
    </ul>
</script>
<script type="text/ng-template" id="expression-SampleCondition.html">
    Sample condition is met: 
    <a class="__link" left-click-menu data-target="yesNo_menu{{element1.id}}">{{element1.isSatisfied | boolToValue:'yes':'no'}}</a>
    <ul class="menu __context" role="menu" id="yesNo_menu{{element1.id}}">
        <li class="menu-item" ng-click='element1.isSatisfied=true;'>yes</li>
        <li class="menu-item" ng-click='element1.isSatisfied=false;'>no</li>
    </ul>
</script>
```

## Registering New Elements in Main module.js File
The next steps include registering newly created expression elements in `dynamicExpressionService` that is used as a registry for all known tree elements:

``` js title="Script/module.js"
angular.module(moduleName, [])
    .run(['virtoCommerce.coreModule.common.dynamicExpressionService', '$http', '$compile',
        function (dynamicExpressionService, $http, $compile) {
            //Register Sample expressions
            dynamicExpressionService.registerExpression({
                id: 'BlockSampleCondition',
                newChildLabel: '+ add sample condition',
                getValidationError: function () {
                    return (this.children && this.children.length) ? undefined : 'Promotion requires at least one eligibility';
                }
            });
            dynamicExpressionService.registerExpression({
                id: 'SampleCondition',
                displayName: 'Sample condition is []'
            });

            $http.get('Modules/$(VirtoCommerce.MarketingSample)/Scripts/all-templates.html').then(function (response) {
                // compile the response, which will put stuff into the cache
                $compile(response.data);
            });
        }
    ]);
```

## Building Your Module and Restarting Platform

You can now build your solution and pack the module scripts with the following command:

``` console
npm run webpack:build
```

After that, you need to restart the platform instance to apply your changes.

Finally, open Platform Manager, go to ***Marketing>Promotions***, and click ***New promotion***. The new `For condition evaluator with any of these sample values` block with its single `Sample condition is met: no/yes` line should be there.
