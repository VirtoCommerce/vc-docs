# Roles and Permissions

In Virto Commerce Platform, each user must have at least one role assigned. Virto Commerce offers pre-defined roles by default, which you can customize or create new ones according to your needs.

Managing roles includes:

* [Creating new roles and assigning permissions.](roles-and-permissions.md#create-new-role)
* [Editing new roles.](roles-and-permissions.md#edit-roles)

## Create new role and assign permissions

To create new roles and assign permissions to them:

1. Click **Security** in the main menu.
1. In the next blade, click **Roles** to open the **Roles** blade.
1. Click **Add** in the toolbar.

	![Path](media/roles-path.png){: style="display: block; margin: 0 auto;" }

1. Fill in the following fields:

	![New user](media/new-role-fields.png){: style="display: block; margin: 0 auto;" }

1. Click **Create** to save the changes.

The new role has been added to the list in the **Roles** blade.

## Edit roles

To edit a role:

1. Follow steps 1-2 from the instruction above.
1. Click the required role and edit it in the next blade: assign new permissions or delete the existing ones.
1. Click **Save** in the toolbar to save the changes.

The role has been modified.

## Granular catalog entity permissions

Catalog access can be configured separately for categories and products within a catalog. A role can be granted full write access to categories while limiting products to read-only, or vice versa. This replaces the umbrella `catalog:*` permissions that cover both entity types together.

Eight permissions are registered under the **Catalog** group in the role editor:

| Permission | Purpose |
| --- | --- |
| `catalog:categories:create` | Create categories |
| `catalog:categories:read` | View categories |
| `catalog:categories:update` | Edit categories |
| `catalog:categories:delete` | Delete categories |
| `catalog:products:create` | Create products |
| `catalog:products:read` | View products |
| `catalog:products:update` | Edit products |
| `catalog:products:delete` | Delete products |

All permissions are localized for the 13 Platform languages.

### Catalog scope

The new permissions support the existing **Selected catalog** scope. For example, a role can be granted `catalog:categories:update` only for Catalog A. Operations on entities outside the user's scoped catalogs return HTTP 403.

### Behavior in the admin UI

The **Catalog** blade and detail blades respect entity-level permissions:

* The unified catalog list filters automatically to show only the entity types the user can read.
* Toolbar actions like **Add**, **Cut**, **Paste**, and **Delete** appear only for entity types the user has the corresponding permission for.
* **Save** and **Reset** on the category detail blade require `catalog:categories:update`. On the product detail blade, they require `catalog:products:update`.
* **Add variation** and **Delete variation** depend on `catalog:products:create` and `catalog:products:delete`.
* Read-only users still see **Copy ID** and **Copy SKU** actions.

### Backward compatibility

Existing roles that use the legacy `catalog:create`, `catalog:read`, `catalog:update`, and `catalog:delete` permissions continue to work unchanged. The Platform automatically maps each legacy permission to both entity-level equivalents:

| Legacy permission | Maps to |
| --- | --- |
| `catalog:create` | `catalog:categories:create` + `catalog:products:create` |
| `catalog:read` | `catalog:categories:read` + `catalog:products:read` |
| `catalog:update` | `catalog:categories:update` + `catalog:products:update` |
| `catalog:delete` | `catalog:categories:delete` + `catalog:products:delete` |

No migration is required for existing roles.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../managing-users">← Managing user accounts</a>
    <a href="../marketer">Marketer →</a>
</div>