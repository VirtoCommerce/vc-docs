# Restore

To restore data from a backup:

1. Click **Backup and restore** in the main menu.
1. In the **Data backup and restore** blade, click **Restore**.
1. In the **Data restore** blade:
    
    * Drag and drop your backup ZIP file into the designated area, or
    * Choose a backup file from the storage list.

    !!! tip
        For large backups over 100 MB use a stored backup instead of uploading it through the browser.

1. The Platform reads the backup manifest and displays Restore data information (Author, Data file created, Created in Platform version).
1. If the backup is encrypted, a **Backup password** section appears. Enter the password that was shown when the backup was created.

    !!! warning
        
        If the password you enter does not match the one used when the backup was created, the restore is rejected by the Platform. No data is changed in the Platform.

1. Under **Platform entries** and **Choose modules to restore**, select the data types and modules you want to restore.
1. Click **Start restore** in the toolbar.

The system will restore the data from the backup file. Click **Cancel** to stop an upload in progress. If an upload fails or stalls, the blade surfaces a clear message, for example a file-too-large or timeout error, instead of remaining in progress indefinitely. To choose a different file, click **Back**.

!!! note
    After a fully successful restore, the Platform automatically removes the backup file you uploaded for the restore. If the restore finishes with any errors, the file is kept so you can fix the issue and retry without uploading it again. The original backup file you downloaded when creating the backup is not affected.


Try our interactive demo to explore the feature in action:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js" data-verify-origin=""></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.57% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://app.storylane.io/demo/2ibxaohstrqi?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>


## Sensitive data restoration

When you restore a backup with **Security** enabled, the blade displays a warning banner that explains the consequences: 

**This restore will overwrite sensitive data - User passwords, API keys, and security stamps from the backup will replace the current values for every user in the file.
Your own admin account (username) will not be modified — your password and active session are preserved.**

The Platform automatically preserves the account of the administrator who initiated the restore. Your **PasswordHash**, **SecurityStamp**, **LockoutEnd**, and **AccessFailedCount** values stay unchanged, your active session is not invalidated, and the password you logged in with continues to work.

All other users in the backup file have their credentials replaced with the values stored in the backup. After the restore, they may need to use the password they had at the moment the backup was created.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../backup">← Backup</a>
    <a href="../../catalog-csv-export-import/overview">Catalog CSV Export and Import module overview →</a>
</div>