# Replace AutoMapper with Explicit Mappers

AutoMapper is being removed from the xAPI (GraphQL Experience API) layer following the security advisory [GHSA-rvv3-g6hj-g44x](https://github.com/advisories/GHSA-rvv3-g6hj-g44x), and replaced with explicit, hand-written mappers. The benefits are twofold: better performance, and a cleaner, more explicit data-transformation layer. If you need an AutoMapper replacement in your own modules, apply the same process described here.

## Scope

This applies to the GraphQL Experience API layer: **x-api**, **x-catalog**, **customer-review**, **x-order**, **xprofile**, and **x-cart**. It does not apply to `ToModel()` and `FromModel()` in the Data-Entity layer, which stay as they are.

!!! note
    Removing the AutoMapper package reference from a module is the step that closes the advisory. Module-level changes are prerequisites, but the exposure remains while `Xapi.Core` still ships AutoMapper transitively.

## Process

To replace AutoMapper in a module:

1. Create a unit test that captures the current mapping scenarios.
1. Replace AutoMapper following the rules and steps below.
1. Run the tests. They should all pass, so the module keeps the same capabilities.

The module now maps data explicitly, without AutoMapper.

## Rules

Follow these rules when writing the new mappers:

1. One facade per module (`I<Module>Mapper` and `<Module>Mapper`), not one interface per mapping.
1. Methods are `public virtual`, registered via DI with `AddSingleton`, since mappers are stateless.
1. Name methods `To<Dest>(source)`, never `Map(source)`.
1. Pass explicit typed parameters instead of `ResolutionContext.Items`.
1. For in-place mapping, previously `Map(source, target)`, use `MapTo(target)`, an extension method on the source with the target as a parameter, keeping the argument order AutoMapper used.
1. Preserve null semantics: start every method with `if (source == null) return null;`.
1. Create destination objects with `AbstractTypeFactory<TDest>.TryCreateInstance()`, not `new TDest()`.
1. Do not add a generic `IMapper<TSource, TDest>`. There are no real consumers for it.

The following example is from the customer-review module, the first module migrated. See [PR 82](https://github.com/VirtoCommerce/vc-module-customer-review/pull/82) for the full reference implementation:

```csharp title="CustomerReviewMapper.cs"
public interface ICustomerReviewMapper
{
    ExpRating ToExpRating(RatingEntityDto source);
}

public class CustomerReviewMapper : ICustomerReviewMapper
{
    public virtual ExpRating ToExpRating(RatingEntityDto source)
    {
        if (source == null)
        {
            return null;
        }

        var result = AbstractTypeFactory<ExpRating>.TryCreateInstance();
        // copy each field explicitly from source to result
        return result;
    }
}
```

Register the mapper as a singleton in the module's Experience API service registration, for example the `AddExperienceApi` extension in **ServiceCollectionExtensions.cs**:

```csharp
serviceCollection.AddSingleton<ICustomerReviewMapper, CustomerReviewMapper>();
```

## Migration steps

When you migrate a module:

1. Check sibling modules for direct `.Map<TDest>(...)` calls against the same types before you delete a profile. The host-wide `IMapper` is shared across modules.
1. Insert the new DI dependency in the same position `IMapper` used to occupy. Check the git history, and do not append it at the end.
1. State two things explicitly in the pull request description: that this is a breaking change, since public constructors change, and the security-ticket status, which only closes once all dependent modules are updated.

The module now resolves its mapper through the new facade instead of the shared `IMapper`.

## Tests

Cover each mapper with the following tests:

1. A unit test for each mapper method, asserting the exact expected values.
1. A test for a null source.
1. An explicit assertion on intentionally unmapped fields, for example `Assert.Null(...)`.
1. A test for the DI registration, checked through the `ServiceDescriptor`, including its `Lifetime`, rather than by resolving from a built `ServiceProvider`.
1. A parity check against the old AutoMapper profile: temporarily keep AutoMapper in the test project only, move the old profile there, run the same input through both the old and the new mapper, and compare the results, instead of hand-picking expected values.

Green tests confirm the new mapper reproduces the old behavior.

## Finish the removal in x-api

For the **x-api** module specifically:

1. Migrate its own mappings to explicit mappers.
1. Run an `Obsolete` cycle on its public `IMapper` constructors.
1. Remove the `AddAutoMapper` call from `AddSchema`.
1. Remove the AutoMapper package reference.

Only the last step removes [GHSA-rvv3-g6hj-g44x](https://github.com/advisories/GHSA-rvv3-g6hj-g44x) from the dependency graph, so complete the module-level pull requests first.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extending-pricing-module">← Extending the pricing module </a>
    <a href="../overriding-rounding-policy">Overriding rounding policy →</a>
</div>
