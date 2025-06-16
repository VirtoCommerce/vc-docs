# Extend Notification Types

Sometimes you might need to extend the existing notification type with new properties, or override the existing default template with some new ones.

To extend the existing notification, for example, `SampleEmailNotification`:

1. Create a new notification class based on the notification type you want to extend:

    ```csharp
    public class ExtendedSampleEmailNotification : SampleEmailNotification
    {
        public ExtendedSampleEmailNotification() : base(nameof(ExtendedSampleEmailNotification))
        {
        }
    }
    ```

1. Add the following line into the **Module.cs** file:

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
	Running the `.WithTemplates(new EmailNotificationTemplate())` extension method is optional and can be used in case you want to override the default templates.




<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../notification-templates">← Notification templates </a>
    <a href="../configuration">Configuration →</a>
</div>

