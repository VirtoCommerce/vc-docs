# Roles and Permissions

Proper assignment of roles and permissions ensures that employees have the appropriate access levels to complete their tasks. This article describes assigning roles and permissions to help maintain security and productivity within your organization. 

## Create roles

To create a role:

1. Open the platform and go to **Security** --> **Roles** --> **Add**.
1. Enter the role's name and description.
1. Assign the required permissions. Select permissions from at least following sections: **Platform**, **Customer**, and **Task management**.

    | Permission                 	| Description                        	|
    |----------------------------	|---------------------------------	|
    | platform:asset:access      	| Seeing Assets in the main menu. 	|
    | platform:asset:delete      	| Deleting platform assets.       	|
    | platform:asset:update      	| Changing platform assets.       	|
    | platform:asset:create      	| Uploading new platform assets.  	|
    | platform:asset:read        	| Downloading platform assets.    	|
    | customer:read                     | View available users to assign task to.|
    | task:access                	| Accessing tasks.                	|
    | task:create                	| Creating tasks.                 	|
    | task:read                  	| Reading tasks.                  	|
    | task:update                	| Updating tasks.                 	|
    | task:delete                	| Deleting tasks.                 	|
    | task:finish                	| Finishing tasks.                	|
    | task:attachment:management 	| Managing attachments to tasks.  	|

1. Click **Create** to save changes.


## Define role scopes

To define the scope of the role:

1. Open the platform and go to **Security** -> **Roles**. 
1. Select the required role.
1. Select the permissions marked with **Assigned scopes: 0**.
1. Select a task permission scope to allow a user to assign tasks:

    * To anyone in the organization.
    * To themselves only.
1. Click **OK** to save changes.
1. Click **Save** in the Roles blade to save changes.


## Assign roles

To assign a created role to a user:

1. Go to **Stores** and choose a user.
1. In the new blade, click the **Accounts** widget.
1. Select the user's account.
1. In the new blade, select the **Roles** widget.
1. In the new blade, click **Assign**.
1. In the new blade, tick the roles to assign and click **OK**.
1. Click **Save** in the **User information blade** to save the changes. 



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../settings">← Settings</a>
    <a href="../../tax/overview">Tax module overview →</a>
</div>