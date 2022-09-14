# CartType

The chart below shows the components and relations of the `CartType` object:

![CartType chart](media/CartType.jpeg)

## CartType Address Field

The `Cart.Addresses` field in `CartType` is a functional enabler. Currently, it is not featured in any internal business logic and is separated from `Cart.Billing.Addresses` and `Cart.Shipping.Addresses`. Feel free to add your own business logic to it.

You can find the address type structure [here](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/VirtoCommerce.ExperienceApiModule.Core/Schemas/AddressType.cs).