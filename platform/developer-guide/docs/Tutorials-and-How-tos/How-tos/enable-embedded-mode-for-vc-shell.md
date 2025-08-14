# Enable Embedded Mode for VC-Shell Instances in Platform

Vue-based external modules (such as VC-Shell apps like [Push Messages](../../../../user-guide/push-messages/overview)) can now be launched directly from the AngularJS-based Virto Commerce back office using **embedded mode**.

This feature allows module developers to open a new VC-Shell instance from the VC Platform menu, creating a more seamless and unified user experience across both AngularJS and VueJS applications.

1. Update VC-Shell to 1.1.61+ version.

1. In your **module.manifest** file, add the `<supportEmbeddedMode>` element set to `true` inside the `<app>` definition:

    ```xml hl_lines="7" title="module.manifest"
    <apps>
        <app id="push-messages">
        <title>Push Messages</title>
        <description>Push Messages</description>
        <iconUrl>/apps/push-messages/img/icons/safari-pinned-tab.svg</iconUrl>
        <permission>PushMessages:access</permission>
        <supportEmbeddedMode>true</supportEmbeddedMode>
        </app>
    </apps>
    ```

1. Rebuild your module and deploy it to the Platform. 

Once installed, it will now open within the back office in embedded mode:
![Embedded mode](media/first-blade.png)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../user-email-verification">← User email verification </a>
    <a href="../migration-to-new-xapi-modules">Migration to new xAPI modules  →</a>
</div>
