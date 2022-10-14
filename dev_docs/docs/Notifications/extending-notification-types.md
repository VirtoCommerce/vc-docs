# Extending Notification Types

Sometimes, there is a need to extend an existing notification type with new properties, or override the existing default template with some new ones.

If you want to extend an existing notification, say, `SampleEmailNotification`, you need to complete the following steps.

Create a new notification class based on the notification type you want to extend:

```csharp
public class ExtendedSampleEmailNotification : SampleEmailNotification
{
    public ExtendedSampleEmailNotification() : base(nameof(ExtendedSampleEmailNotification))
    {
    }
}
```

Add the following line into the `Module.cs` file:

```csharp title="Module.cs"
public void PostInitialize(IApplicationBuilder appBuilder)
{
...
var registrar = appBuilder.ApplicationServices.GetService<INotificationRegistrar>();
registrar.OverrideNotificationType<SampleEmailNotification, ExtendedSampleEmailNotification>()
         .WithTemplates(new EmailNotificationTemplate()
          {
              Subject = "Extended SampleEmailNotification subject",
              Body = "Extended SampleEmailNotification body test"
          });
...
}
```

!!! note
	Running the `.WithTemplates(new EmailNotificationTemplate()` extension method is optional and can be used in case you want to override the default templates.
