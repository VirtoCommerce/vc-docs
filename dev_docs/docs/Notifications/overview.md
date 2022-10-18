VirtoCommerce provides a customizable logic for managing and sending end user notifications via different channels, such as email or text messages. This guide will explain technical details of the notifications logic data model and outline some basic development scenarios.

## Notification Data Model

The chart below shows how notification data is sent:
![Notification data model](media/data-model.png)

Each notification sent by the system is represented with an individual notification type. Each Notification type, in its turn, can contain multiple notification templates, each being individual per language.

At the time of sending, the system converts the object belonging to a specific notificaction type and having a notification template into a notification message, and then forwards it through one of the channels, e.g. email or text.

For data modeling purposes, the notification data model contains the following elements:

**Notification type:** A custom class derived from `EmailNotification` or `SmsNotifcation`. The type defines a set of attribute data properties that can be used when rendering a specific instance of the notification type and notification template into the resulting Notification message.

**Notification template:** Houses notification content with syntax based on [Liquid by Shopify](https://shopify.github.io/liquid/). The Liquid elements in templates act as placeholders: just before the message is sent to the recipient, Liquid is replaced and interpreted using the data taken from properties, which in their turn come from the incoming notification type instance; the data is then output into the resulting message text.

!!! note
	To edit the notifications sent from your store, you can [provide basic customization](https://docs.virtocommerce.org/new/user_docs/notifications/notification-templates) to your notification templates.

**Notification message:** The resulting text or email message scheduled or sent by a specific sender and stored in the notification feed within the system.

## Next Steps
Check out these guides to continue working with notifications:

[Registering a new notification type](registering-new-notification-type.md)

[Extending the existing notification types](extending-notification-types.md)

[Define notification templates in the project](notification-templates.md)

[Configuration](configuration.md)

## Recommended Content
Here are some more references for you to consider:

+ [Notification Module Overview](https://docs.virtocommerce.org/new/user_docs/notifications/overview)

+ [Scriban Liquid Reference](https://github.com/scriban/scriban/blob/master/doc/liquid-support.md)
