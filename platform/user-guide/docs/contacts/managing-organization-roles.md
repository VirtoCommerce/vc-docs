# Manage Organization-Scoped Roles

Organization-scoped roles let you grant access to every employee of a company at once, instead of assigning the same role to each member by hand.

A member's effective permissions are the union of three role sources, re-evaluated each time they sign in:

* [Global roles](../security/roles-and-permissions.md#create-new-role-and-assign-permissions) are assigned to the user account itself via the Security module.
* [Sales rep roles](../sales-rep/managing-sales-reps.md) are assigned to the user account via the Sales Rep module.
* [Organization roles](#assign-organization-level-role) are assigned to a whole organization and inherited by all its employees.
* [Membership roles](#assign-membership-role) are assigned to one person within one organization.


In this article we are going to explore the organization and membership roles assigned via the Contacts module.

## Assign organization-level role

To assign a role to every employee of an organization at once:

1. Click **Contacts** in the main menu.
1. In the next blade, click the three dots to the left of the required organization and select **Manage** from the popup menu.
1. In the next blade, locate the **Roles** field, click **Add** and select a role from the dropdown (for example, a purchasing agent).
1. Click **Save** in the toolbar.

![Organization role dropdown](media/org-role-dropdown.png){: style="display: block; margin: 0 auto;" }

All the company members receive a purchasing agent role:

![Frontend organization-level roles](media/purchasing-agent.png){: style="display: block; margin: 0 auto;" }

Only roles allowed by the [Organization roles whitelist](#organization-roles-whitelist) appear in the dropdown. Every employee of the organization now inherits the role's permissions, with no per-member action needed. To revoke it from everyone at once, remove the role's chip and save.

!!! warning
    Employees must sign in again. Effective permissions are recalculated at sign-in. An employee with an open Frontend session keeps their previous permissions until they sign out and back in. The change is applied on the server immediately, so only the active session is stale.

### Organization roles whitelist

To edit an organization role whitelist:

1. Click **Settings** in the main menu.
1. In the search field of the next blade, type **Roles** to find the settings related to the feature.
1. Click ![Pencil](media/pencil.png){: width="25"} to edit **Organization roles whitelist**.
1. In the editor blade, click **Add** to add a role, or select a row and click **Delete** to remove one.
1. Click ![Floppy](media/floppy.png){: width="20"}, then **Save** in the editor toolbar.


!!! tip
    After editing a whitelist, click **Reset cache** in the Settings toolbar and reload the page. The role pickers read the whitelist through the settings cache, so a newly added or removed role appears in the dropdowns only after the cache refreshes.

The whitelist has been updated and the selected roles appear in the dropdown when assigning organization-level roles:

<div class="grid cards" markdown>

-   __Organization roles whitelist:__

    ---

    ![Whitelist](media/organization-roles-whitelist.png)

-   __Visible organization roles options:__

    ---

    ![Options](media/visible-org-roles-options.png)

</div>


## Assign membership role

To assign a role to one member within one organization:

1. Click **Contacts** in the main menu.
1. In the next blade, open the required contact.
1. In the next blade, click the **Organization memberships** widget.
1. In the next blade, select the organization.
1. In the next blade, click **Add** to add the roles to the **Roles** field.
1. Click **Save** in the toolbar.

    ![Membership roles](media/membership-roles.png){: style="display: block; margin: 0 auto;" }

The role has been added to the contact.

![Frontend roles](media/ron-wisley.png)

Only roles allowed by the [Membership roles whitelist](#membership-roles-whitelist) appear in the dropdown. 

### Membership roles whitelist

To edit a membership role whitelist:

1. Click **Stores** in the main menu.
1. In the next blade, select your store.
1. In the next blade, click **Settings** widget.
1. In the search field of the settings blade, type **Roles** to find the settings related to the feature.
1. Click ![Pencil](media/pencil.png){: width="25"} to edit **Membership roles whitelist**.
1. In the editor blade, click **Add** to add a role, or select a row and click **Delete** to remove one.
1. Click ![Floppy](media/floppy.png){: width="20"}, then **Save** in the toolbar.

The whitelist has been updated and the selected roles appear in the dropdown when assigning membership roles:

<div class="grid cards" markdown>

-   __Membership roles whitelist:__

    ---

    ![Whitelist](media/membership-roles-whitelist.png)

-   __Visible membership roles options:__

    ---

    ![Options](media/visible-membership-roles-options.png)

</div>


On the Frontend, the selected roles appear in the roles list:

![Frontend](media/frontend-membership-roles.png)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../managing-contacts">← Managing companies and contacts</a>
    <a href="../filtering-options">Filtering options →</a>
</div>