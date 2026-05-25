# Register New Notification Type

This guide describes the basic steps to define a new email notification type, including its registration in the notification registry.

[![Sample code](media/sample-code.png)](https://github.com/VirtoCommerce/vc-module-notification/tree/dev/samples)

## Prerequisites

* [Configure the notification gateway.](/platform/developer-guide/latest/Getting-Started/Post-Installation-Steps/02-configuring-email-notifications)

## Define custom email notification type

Create a notification and give it a name, for example, `SampleEmailNotification`, basing it on the `EmailNotification` class (as opposed to another standard class, `SmsNotification`):

```csharp title="SampleEmailNotification.cs"
public class SampleEmailNotification : EmailNotification
{
    public SampleEmailNotification() : base(nameof(SampleEmailNotification)) {}
    public string Greeting { get; set; }
}
```

## Registration in notification registry

Register your `SampleEmailNotification` in the notification registry:

```csharp title="module.cs" linenums="1"
public void PostInitialize(IApplicationBuilder appBuilder)
	{
	...
	var registrar = appBuilder.ApplicationServices.GetService<INotificationRegistrar>();
	registrar.RegisterNotification<SampleEmailNotification>().WithTemplates(new EmailNotificationTemplate()
            {
                Sample = "",
                Subject = "Hi { greeting }",
                Body = "My cool email body
            });
	...
	}
```

**Notes to the code:**
	
**Line 4:** Getting the instance of `INotificationRegistrar` type that stores all known notification types used in the system.
	
**Line 5:** Registering `SampleEmailNotification` and setting a default template by running the `WithTemplates` extension method. In `Template.Subject`, we use the `{greeting}` liquid expression that will be replaced with the `Greeting` property value of the `SampleEmailNotification` class instance after rendering.

!!! tip
	  You can [register your notification templates as files being part of your solution](notification-templates.md).

## Localize notifications

Virto Platform Manager supports localization resources for notification types. This is achieved by adding a JSON object to the `notificationTypes` section, the key having the same name as the notification type:

```json title="Localization/en.VirtoCommerce.NotificationsExample.json"
 "notificationTypes": {
 ...
    "SampleEmailNotification": {
      "displayName": "Sample email notification",
      "description": "Some sample email description"
    },
...
  }
```

## Send notifications

To send a notification from your code, use two interfaces: `INotificationSearchService` and `INotificationSender`.

You can send a notification based on this code sample as follows:

```csharp linenums="1" hl_lines="15 16 17 18 19"
public class SampleSenderService 
{
    private readonly INotificationSearchService _notificationSearchService;
    private readonly INotificationSender _notificationSender;

    public SampleService(INotificationSender notificationSender, INotificationSearchService notificationSearchService)
    {
        _notificationSender = notificationSender;
        _notificationSearchService = notificationSearchService;
    }
    
   public async Task SendSampleNotification()
   {
     //Resolve the notification instance from known notification types via registry
     var notification = await _notificationSearchService.GetNotificationAsync<SampleEmailNotification>();
     //Set the language code to use template that has this language or left empty, then template with empty language will be used
     notification.LanguageCode = 'en-US';
     notification.From = "from@test.com";
     notification.To = "to@test.com";
     notification.Greeting = "John"
     //Sending notification asynchronously
     await _notificationSender.ScheduleSendNotificationAsync(notification);     
   }
}
```

**Notes to the code:**
	
**Line 15:** Constructing a new instance of the `SampleEmailNotification` type by calling the `INotificationSearchService.GetNotificationAsync<>` extension method.
	
**Lines 16 to 19:** Populating the required email notification properties, such as `From` and `To`, and setting a value for our custom `Greeting` property; this value will be eventually interpolated in the email subject, for example, **Hi { greeting } → Hi John**.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Notifications overview </a>
    <a href="../notification-templates">Notification templates →</a>
</div>

