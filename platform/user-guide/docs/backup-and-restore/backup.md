# Backup

To create a backup of your data:

1. Click **Backup and restore** in the main menu.
1. In the **Data backup and restore** blade, click **Backup**.
1. In the **Data backup** blade, check the data types you want to back up, such as security accounts, binary data, and more:

    | Platform entry         | Description                                                                                                                  | Notes|
    | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---- |
    | **Password protect**   | Encrypt the backup with a one-time password (AES-256). Enabled by default and recommended for all backups that include sensitive data. | If you also disable **Password protect**, an additional red warning banner is displayed, alerting you that the backup will be unencrypted. |
    | **Security**           | Include accounts and roles.   | When you include **Security** in the backup, the blade displays a contextual warning banner above the Platform entries section, informing you that password hashes, API keys, and security stamps will be included in the backup file. |
    | **Binary**             | Include binary data.                                                                                                                   | |
    | **Settings**           | Include Platform settings.                                                                                                             | |
    | **Dynamic properties** | Include Platform dynamic properties.                                                                                                   | |

    !!! tip
        Keep **Password protect** enabled whenever the backup includes Security, Binary, or Settings entries. The one-time password is the only thing that stops a stolen backup file from being used to take over user accounts.

1. Check the modules you want to back up.
1. Click **Start export** in the toolbar. The backup process starts and a per-module progress timeline appears. Each module renders as a card showing its current state (in progress, completed, or failed) and the elapsed time. Use **Show detailed log** to reveal the full progress log:

    ![Backup](media/backup-data.gif){: style="display: block; margin: 0 auto;" width="700"}

1. When the backup finishes:

    * A green **Backup finished** banner is displayed.
    * A **Download backup** link appears. Click it to download the resulting ZIP file.
    * If password protection is enabled, the **Backup password** card displays the one-time password. Use the **Copy** button next to the password to copy it to the clipboard.

    !!! warning
        The backup password is shown only once on this screen. If you navigate away from the blade without copying it, the password cannot be recovered, and the backup file cannot be restored.

    ![Password](media/one-time-password-backup.png){: style="display: block; margin: 0 auto;" }

You can now download a ZIP file containing your backup for future restoration.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Backup and Restore overview</a>
    <a href="../restore">Restore →</a>
</div>