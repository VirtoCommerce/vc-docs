# Outdated Strategy

Virto Commerce ensures a smooth user migration while improving the quality of the platform. This includes necessary updates that occasionally cause disruption. We manage this by using the Obsolete attribute for deprecated methods and assigning unique DiagnosticIds to track changes and provide clear references for developers.

```cs
[Obsolete("Method1 is deprecated, please use Method2 instead.", DiagnosticId = "VC0005", UrlFormat = "https://docs.virtocommerce.org/platform/user-guide/versions/virto3-products-versions/")]
public void Method1()
{
}
```

Our approach also ensures a controlled transition period. The `Obsolete` attribute typically remains active for the next two stable releases, giving our partners ample time to adapt their code to the newer alternatives. This approach is in line with our commitment to provide a smooth migration process, giving developers the necessary timeframe to adjust their implementations. 