# Overview

The `Push Messages` module provides high performance API to enable efficient notification management and real-time communication within Virto Commerce.

With the API functionality, you can:

* Receive real-time updates on new push messages.
* Retrieve and manage push messages.
* Clear all push messages.
* Mark push messages as read/ unread.

| Queries                                   | Objects                                                  | Mutations                                  | Subscriptions                                      |
|-------------------------------------------|----------------------------------------------------------|--------------------------------------------|---------------------------------------------------|
| [pushMessages](Queries/pushMessages.md)   | [PushMessageType](Objects/PushMessageType.md) <br> [PushMessageResponseType](Objects/PushMessageResponseType.md) <br> [InputMarkPushMessageReadType](Objects/InputMarkPushMessageReadType.md) <br>[InputMarkPushMessageUnreadType](Objects/InputMarkPushMessageUnreadType.md) | [clearAllPushMessages](Mutations/clearAllPushMessages.md) <br> [markAllPushMessagesRead](Mutations/markAllPushMessagesRead.md) <br> [markAllPushMessagesUnread](Mutations/markAllPushMessagesUnread.md) <br> [markPushMessageRead](Mutations/markPushMessageRead.md) <br> [markPushMessageUnread](Mutations/markPushMessageUnread.md) | [pushMessageCreated](Subscriptions/pushMessageCreated.md) |

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-push-messages/releases)

![Readmore](media/readmore.png){: width="25"} [Managing Push Messages via Platform](../../../../user-guide/push-messages/manage-push-messages)