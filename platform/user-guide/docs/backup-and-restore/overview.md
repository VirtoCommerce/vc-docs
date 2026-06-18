# Overview

The **Backup and Restore** module allows you to securely export and restore Platform data, ensuring data safety and easy recovery when needed. Backups can be encrypted with a one-time password (AES-256) so that sensitive information such as user credentials and API keys is protected at rest.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-backup-restore)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-backup-restore/releases)

Any module that supports export and import automatically participates in a backup, so its data is included alongside the Platform entries without extra configuration.

## Key features

With the Backup and Restore module, you can:

* **Back up Platform data**: Export security accounts and roles, binary data, settings, and dynamic properties into a single ZIP file.
* **Back up module data**: Select which installed modules to include, so their data is saved together with the Platform entries.
* **Protect backups with a password**: Encrypt the backup with a one-time password (AES-256) to keep credentials and API keys safe at rest.
* **Track progress**: Follow a per-module progress timeline during the operation, with a detailed log you can copy to the clipboard.
* **Restore selectively**: Choose which Platform entries and modules to restore from a backup file.
* **Preserve your admin account**: When restoring sensitive data, the account that started the restore keeps its password and active session.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../back-in-stock/settings">← Back-in-Stock settings</a>
    <a href="../backup">Backup →</a>
</div>
