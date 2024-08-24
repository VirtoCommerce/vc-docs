# Register New Shipping Method

In case your customers have any shippable products to choose from, they can also choose a shipping option during checkout.

## Define new shipping method

To define a new shipping method:

1. [Create a new module](../../Tutorials-and-How-tos/Tutorials/creating-custom-module.md).
1. Create a class derived from the `ShippingMethod` abstract class and override all abstract methods; each of them will be called on the appropriate stage of the payment processing workflow: 

    ```cs
      public class FixedRateShippingMethod : ShippingMethod
        {
            public FixedRateShippingMethod() : base("FixedRate")
            {
            }
        public override IEnumerable<ShippingRate> CalculateRates(IEvaluationContext context)
            {
          //Implement logic of shipping rates calculation here
        }
      }
    ```

1. Register your module class in the DI container. This must be done in the `PostInitialize` method. You can also associate the settings, which will be used in your method and can be changed in the management UI. 

    ```cs
    public void PostInitialize(IApplicationBuilder applicationBuilder)
    {
      ...

        var settingsRegistrar = applicationBuilder.ApplicationServices.GetRequiredService<ISettingsRegistrar>();
            var shippingMethodsRegistrar = applicationBuilder.ApplicationServices.GetRequiredService<IShippingMethodsRegistrar>();
        //Associate the settings with the particular shipping provider
        settingsRegistrar.RegisterSettingsForType(ModuleConstants.Settings.FixedRateShippingMethod.AllSettings, typeof(FixedRateShippingMethod).Name);
            shippingMethodsRegistrar.RegisterShippingMethod<FixedRateShippingMethod>();

      ...
    }
    ```

All settings may have default values that can be used for default methods if not overridden by custom values later.

[![Sample code](media/sample-code.png)](https://github.com/VirtoCommerce/vc-module-shipping/blob/master/src/VirtoCommerce.ShippingModule.Data/FixedRateShippingMethod.cs)

## Enable and configure shipping method for store

After your module is installed in your target system, all your shipping methods should appear and be available for configuration in every store in your system under the `Store->Shipping methods` widget. You can also configure shipping methods for each store individually:

1. Enable or disable a method for the current store
1. Change priority to determine the order in which the shipping methods will be displayed at checkout
1. Edit all settings and what you define for the shipping method
1. Use a custom UI for more detailed shipping method configuration

After you are done configuring, your shipping method will appear in the front end checkout page, and the customer will be able to select it as an option.

## UI customization

If our standard user interface is not enough, you may consider implementing your own UI for managing shipping methods through the standard UI extension point (widget container with the `shippingMethodDetail` group).

![Readmore](media/readmore.png){: width="25"} [Extending existing UI with widgets](../../Platform-Manager/Extensibility-Points/widgets.md)
