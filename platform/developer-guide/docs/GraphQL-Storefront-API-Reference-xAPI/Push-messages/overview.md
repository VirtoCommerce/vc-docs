# Push Messages

The **Push Messages** module provides high performance API to enable efficient notification management and real-time communication within Virto Commerce.

With the API functionality, you can:

* Receive real-time updates on new push messages.
* Retrieve and manage push messages.
* Clear all push messages.
* Mark push messages as read/ unread.

| Queries                                   | Objects                                                  | Mutations                                  | Subscriptions                                      |
|-------------------------------------------|----------------------------------------------------------|--------------------------------------------|---------------------------------------------------|
| [pushMessages](Queries/pushMessages.md) <br> [FcmSettings](Queries/FcmSettings.md)  | [PushMessageType](Objects/PushMessageType.md) <br> [PushMessageEdge](Objects/PushMessageEdge.md) <br> [PushMessageConnection](Objects/PushMessageConnection.md) <br> [InputMarkPushMessageReadType](Objects/InputMarkPushMessageReadType.md) <br>[InputMarkPushMessageUnreadType](Objects/InputMarkPushMessageUnreadType.md) <br>[FcmSettingsType](Objects/FcmSettingsType.md) <br>[InputAddFcmTokenType](Objects/InputAddFcmTokenType.md) <br>[InputDeleteFcmTokenType](Objects/InputDeleteFcmTokenType.md) | [clearAllPushMessages](Mutations/clearAllPushMessages.md) <br> [markAllPushMessagesRead](Mutations/markAllPushMessagesRead.md) <br> [markAllPushMessagesUnread](Mutations/markAllPushMessagesUnread.md) <br> [markPushMessageRead](Mutations/markPushMessageRead.md) <br> [markPushMessageUnread](Mutations/markPushMessageUnread.md) <br> [addFcmToken](Mutations/addFcmToken.md) <br> [deleteFcmToken](Mutations/deleteFcmToken.md)  | [pushMessageCreated](Subscriptions/pushMessageCreated.md) |


[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-push-messages/releases)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-push-messages/releases/latest)

![Readmore](media/readmore.png){: width="25"} [Managing Push Messages via Platform](../../../../user-guide/push-messages/manage-push-messages)