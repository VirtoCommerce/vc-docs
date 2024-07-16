# Messaging via Firebase Cloud

Firebase Cloud Messaging (FCM) is a cross-platform messaging solution that lets you reliably send messages at no cost. The Virto Commerce Push Messages module uses FCM to notify a client across platforms, including web, Android, and iOS that a new notification is available:

=== "Regular desktop notification"
    ![Regular notification](media/regular-desktop-notification.gif)


=== "Android Chrome notification"
    ![Android notification](media/android-chrome-notification.png)


=== "White labeled desktop notification"
    ![White labeled notification](media/white-labeling-icon.gif)


## Send Messages

To start sending push messages via FCM:

1. [Create a project in Firebase console.](firebase-cloud-messaging.md#create-project-in-firebase-console)
1. [Configure sender settings.](firebase-cloud-messaging.md#configure-sender-settings)
1. [Configure receiver settings.](firebase-cloud-messaging.md#configure-receiver-settings)
1. [Configure the **appsettings.json** file.](firebase-cloud-messaging.md#configure-appsettingsjson)
1. [Configure the **environments.yml** file.](firebase-cloud-messaging.md#configure-environmentsyml)

### Create Project in Firebase Console

To begin setting up FCM for Virto Commerce:

1. Open [Firebase Console](https://console.firebase.google.com/).
1. Click **Add project**.
1. Enter project name, then click **Continue**.
1. Enable or disable Google Analytics for the project, then click **Continue**.
1. Click **Create project**.
1. Click **Continue** once the project is created.

### Configure Sender Settings

To configure the sender settings:

1. In the left menu, click **Project Overview** --> **Project settings**:
1. In the **Project settings** field, click on the **Service accounts** tab.
1. Click **Generate new private key**.

    ![Project settings](media/project-settings.png){: width="950"}

1. In the popup window, click **Generate key**.
1. Open the downloaded **JSON** file and copy all fields to the corresponding fields in the **appssettings.json** file.

!!! warning
    When using a YAML file for settings, remove all `\n` characters from the `private_key` field and place the resulting value in the Key Vault:

    ![Delete /n characters](media/delete-n-characters.png)


### Configure Receiver Settings

To configure the receiver settings:

1. In the left menu, click **Project Overview** --> **Web**.

    ![Web app](media/add-web-app.png){: width="650"}

1. Enter application name, then click **Register app**.
1. In the **Add Firebase SDK** section, locate settings to paste to the `PushMessages.FcmReceiverOptions` section in the **appsettings.json** file.
1. Click **Continue to console**.
1. In the left menu, click **Project Overview** --> **Project settings**.
1. In the **Cloud Messaging** tab, find **Web Push certificates** section, and click **Generate key pair**.
1. Copy the generated key value and paste it to `PushMessages.FcmReceiverOptions.VapidKey` section in  the **appSettings.json** file.

### Configure appsettings.json

To integrate FCM with Virto Commerce, configure the `appSettings.json` file as follows:

```json
{
  "PushMessages": {
    "UseFirebaseCloudMessaging": true,
    "FcmSenderOptions": {
      "Type": "service_account",
      "ProjectId": "vc-push-86046",
      "PrivateKeyId": "956335b2eeccd3b37ef8f6871b406a6a31e1b29a",
      "PrivateKey": "-----BEGIN PRIVATE KEY-----\n…-----END PRIVATE KEY-----\n",
      "ClientEmail": "firebase-adminsdk-5gw7s@vc-push-86046.iam.gserviceaccount.com",
      "ClientId": "117271734888260111772",
      "AuthUri": "https://accounts.google.com/o/oauth2/auth",
      "TokenUri": "https://oauth2.googleapis.com/token",
      "AuthProviderX509CertUrl": "https://www.googleapis.com/oauth2/v1/certs",
      "ClientX509CertUrl": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5gw7s%40vc-push-86046.iam.gserviceaccount.com",
      "UniverseDomain": "googleapis.com"
    },
    "FcmReceiverOptions": {
      "ApiKey": "AIzaSyCy9gsvKM1e77GRYw6M9rKRRSekZNAgRnI",
      "AuthDomain": "vc-push-86046.firebaseapp.com",
      "ProjectId": "vc-push-86046",
      "StorageBucket": "vc-push-86046.appspot.com",
      "MessagingSenderId": "647691501458",
      "AppId": "1:647691501458:web:2b18fc3a864469ac378b4b",
      "VapidKey": "BJyVagnZqcHI6_vwxILEfxpbVAq0F-ASE5k3WwX_F72WaQr_ysHKqhH5-8yWfUhNs9oecGcOy8kJ_m4b-OXrNFs"
    }
  }
}
```

### Configure environments.yml

To ensure proper configuration across different environments, update the **environments.yml** file as follows:

```yaml
- name: vcst-dev
  platform:
    config:
      PushMessages__UseFirebaseCloudMessaging: true
      PushMessages__FcmSenderOptions__Type: service_account
      PushMessages__FcmSenderOptions__ProjectId: test-97e05
      PushMessages__FcmSenderOptions__PrivateKeyId: c97aff16d81e599cd48bdb63d5f7700a4daa1e99
      PushMessages__FcmSenderOptions__ClientEmail: firebase-adminsdk-ekgb8@test-97e05.iam.gserviceaccount.com
      PushMessages__FcmSenderOptions__ClientId: 117937666492085292599
      PushMessages__FcmSenderOptions__AuthUri: https://accounts.google.com/o/oauth2/auth
      PushMessages__FcmSenderOptions__TokenUri: https://oauth2.googleapis.com/token
      PushMessages__FcmSenderOptions__AuthProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs
      PushMessages__FcmSenderOptions__ClientX509CertUrl: https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ekgb8%40test-97e05.iam.gserviceaccount.com
      PushMessages__FcmSenderOptions__UniverseDomain: googleapis.com
      PushMessages__FcmReceiverOptions__ApiKey: AIzaSyAh1GH8SFIx4ULiaZUNZRnxNNM2jFLGdaE
      PushMessages__FcmReceiverOptions__AuthDomain: test-97e05.firebaseapp.com
      PushMessages__FcmReceiverOptions__ProjectId: test-97e05
      PushMessages__FcmReceiverOptions__StorageBucket: test-97e05.appspot.com
      PushMessages__FcmReceiverOptions__MessagingSenderId: 518395609520
      PushMessages__FcmReceiverOptions__AppId: 1:518395609520:web:53952423cba605aa771675
      PushMessages__FcmReceiverOptions__VapidKey: BE1iGYmRsbdI1FB-qTiIUvGrWvC91GCfnXSHtfzcPLgXfQ28fbpKFlD8YlbI7w-aHVepW3Ih17oRB53ceYNaM6k
    secretConfig:
      PushMessages__FcmSenderOptions__PrivateKey: fcm-private-key
```

## Receive Messages

You will start receiving push messages as soon as you approve them:

![Approval](media/allow-block.png){: width="400"}

Browser notifications appear in the lower right corner of your screen:

![Browser notifications](media/browser-notifications.png)

If you block messages in your browser, you will still be able to see them in the Frontend Application.

You can change your decision at any time:

![Change decision](media/change-decision.png){: width="400"}

