In order to calculate taxes in Virto Commerce, you've got to register at least one `TaxProvider` implementation.

## Defining New Tax Provider

In order to define a new tax provider, you need to:

+ Create a new module by following [this guide](../../../Tutorials-and-How-tos/Tutorials/creating-custom-module.md)
+ Create a class derived from the `TaxProvider` abstract class and override the `CalculateRate` method:

```C#
 public class FixedRateTaxProvider : TaxProvider
    {
        public FixedRateTaxProvider()
        {
            Code = "FixedRate";
        }
        public override IEnumerable<TaxRate> CalculateRates(IEvaluationContext context)
        {
          //Implement logic of tax calculation here
        }
    }

```

+ Register your module class in the DI container. This must be done in the `PostInitialize` method. You can also associate the settings, which will be used in your method and can be changed in the management UI.

```C#
public void PostInitialize(IApplicationBuilder applicationBuilder)
{
  ...
            var settingsRegistrar = applicationBuilder.ApplicationServices.GetRequiredService<ISettingsRegistrar>();
            var taxProviderRegistrar = applicationBuilder.ApplicationServices.GetRequiredService<ITaxProviderRegistrar>();
            taxProviderRegistrar.RegisterTaxProvider<FixedRateTaxProvider>();
            //Associate the settings with the particular tax provider
            settingsRegistrar.RegisterSettingsForType(Core.ModuleConstants.Settings.FixedTaxProviderSettings.AllSettings, typeof(FixedRateTaxProvider).Name);
  ...
}
```

All settings may have default values that can be used for default methods if not overridden by custom values later.

To view or download our sample code, click [here](https://github.com/VirtoCommerce/vc-module-tax/blob/master/src/VirtoCommerce.TaxModule.Data/Provider/FixedRateTaxProvider.cs).

## Enabling and Configure Tax Provider for Store

After your module is installed in your target system, all tax providers should appear and be available for configuration in every store in your system under the `Store->Tax providers` widget. You can configure tax provider for each store individually:

+ Enable or disable a provider for the current store
+ Edit all settings and what you define for the tax calculation provider
+ Use a custom UI for a more detailed tax provider configuration

After you complete the configuration, your tax provider will be used for tax calculation of orders in the store.

## UI Customization

If our standard user interface is not enough, you may consider implementing your own UI for managing tax providers through the standard UI extension point (widget container with the `taxProviderDetail` group). You can read more about extending the existing UI with widgets [here](widgets.md).
