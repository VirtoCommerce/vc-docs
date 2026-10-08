# Add Custom Grant Type

The Platform's token endpoint supports a fixed set of built-in grant types, such as password and client credentials. A module can add its own grant type through `IGrantTypeHandler` and its base implementation `GrantTypeHandlerBase`.

A module that registers through `GrantTypeHandlerBase` gets the standard sign-in pipeline for free: the same events and the same sign-in log entries a built-in grant produces. The OTP module's `otp_email` grant is a real example of this pattern.

## Register custom grant type

Register the handler in your module's `Initialize` method:

```csharp title="module.cs"
public void Initialize(IServiceCollection serviceCollection)
{
    ...
    serviceCollection.AddGrantTypeHandler<MyCustomGrantTypeHandler>("my_grant_type");
    ...
}
```

`MyCustomGrantTypeHandler` derives from `GrantTypeHandlerBase` and implements `IGrantTypeHandler`. The string passed to `AddGrantTypeHandler` is the `grant_type` value a client sends to `/connect/token` to reach this handler.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../adding-google-as-sso-provider">← Google SSO provider </a>
    <a href="../../security-in-depth">Security in Depth →</a>
</div>