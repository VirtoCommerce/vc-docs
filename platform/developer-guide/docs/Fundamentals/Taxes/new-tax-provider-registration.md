In order to calculate taxes in Virto Commerce, register at least one `TaxProvider` implementation.

## Defining New Tax Provider

To define a new tax provider, you need to:

1. [Create a new module](../../Tutorials-and-How-tos/Tutorials/creating-custom-module.md).
1. Create a class derived from the `TaxProvider` abstract class and override the `CalculateRate` method:

    ```cs
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

1. Register your module class in the DI container. This must be done in the `PostInitialize` method. You can also associate the settings, which will be used in your method and can be changed in the management UI.

    ```cs
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

[![Sample code](media/sample-code.png)](https://github.com/VirtoCommerce/vc-module-tax/blob/master/src/VirtoCommerce.TaxModule.Data/Provider/FixedRateTaxProvider.cs)

## Enable and Configure Tax Provider for Store

After your module is installed in your target system, all tax providers should appear and be available for configuration in every store in your system (**Store --> Tax providers --> widget**). You can configure tax provider for each store individually:

1. Enable or disable a provider for the current store.
1. Edit all settings and what you define for the tax calculation provider
1. Use a custom UI for a more detailed tax provider configuration

After you complete the configuration, your tax provider will be used for tax calculation of orders in the store.

## UI Customization

If our standard user interface is not enough, you may consider implementing your own UI for managing tax providers through the standard UI extension point (widget container with the `taxProviderDetail` group). 

![Readmore](media/readmore.png){: width="25"} [Extending Existing UI with Widgets](../../Platform-Manager/Extensibility-Points/widgets.md)

