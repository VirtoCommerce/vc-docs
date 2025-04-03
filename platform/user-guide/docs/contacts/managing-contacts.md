# Manage Contacts

Managing contact entities (companies, employees, customers, and vendors) includes:

* [Adding contacts.](managing-contacts.md#adding-contacts)
* [Editing contacts.](managing-contacts.md#editing-contacts)
* [Deleting contacts.](managing-contacts.md#deleting-contacts)
* [Exporting contacts.](managing-contacts.md#export-contacts)
* [Importing contacts.](managing-contacts.md#import-contacts)
* [Updating contacts.](managing-contacts.md#import-contacts)
* [Sharing contacts.](managing-contacts.md#share-contacts)
* [Setting default company.](managing-contacts.md#set-default-company)
* [Assigning multiple organizations to contacts and employees.](managing-contacts.md#assign-multiple-organizations-to-contacts-and-employees)

## Add contacts

To add a contact:

1. Click **Contacts** in the main menu.
1. In the next blade, click **Add** in the toolbar to open the **New Contact** blade.
1. Select the entity you need and start creating your contact. We will use **Organization** as an example. Adding employees, contacts, and vendors is a similar process.

	![enter image description here](media/new_company_screen.png)

	Assigning organizations or users to particular user groups enables showing personal offers to them.

	![Readmore](media/readmore.png){: width="25"} [Assigning user groups to products and categories](../catalog-personalization/user-groups.md)
	
	![Readmore](media/readmore.png){: width="25"} [Managing personal prices](../pricing/adding-new-assignment.md)


	!!! note
		When adding store customers (**Contacts**), you can set the default language and default currency for their accounts:

		![Default language](media/default-language.png)
	
	!!! note
		If a user is listed in the Contacts, they can now upload their personal photos to customize and brand their workspace:

		![User photo](media/user-photo.png)

1. Click **Create** to save the changes.

The company appears in the **Companies and Contacts** list.

## Edit contacts

To edit any previously added contact:

1. Click **Contacts** in the main menu.
1. In the **Companies and Contacts** blade, click the three dots to the left of the required contact's name and click **Manage** in the popup menu. 
1. In the next blade, update the contact, for example, change the email account by clicking on the **Accounts** widget, then click **Save** in the toolbar to save the changes.

![Edit contact](media/edit-contact.png){: width="650"}

!!! note
	Editing the **Company details** blade allows you to upload and assign assets (images, documents, etc.) to this company. Use the **Assets** widget that appears when editing the company details. 

The contact has been edited.

## Delete contacts

To delete a contact:

1. Click **Contacts** in the main menu.
1. In the **Companies and Contacts** blade, check the contact you need to delete. 
1. Click **Delete** in the toolbar.
1. Confirm your action.

The contact has been deleted.

## Export contacts

!!! note
	Exporting contacts requires the preinstalled [Customer Export and Import module](../customer-export-import/overview.md). 

To export contacts into a CSV file:

1. Click **Contacts** in the main menu.
1. In the next **Companies and Contacts** blade, check the required contact (vendor/ organization/ person).

	!!! note
		If you do not check any contact, all the contacts of all the organizations will be exported into a CSV file.

1. Click **Export** in the top toolbar and confirm your action.
1. In the next blade, click on the generated links to download the contacts:

![Export contacts](media/export-finished.png)

The contacts have been saved as a CSV file.

## Import contacts

!!! note
	Importing contacts requires the preinstalled [Customer Export and Import module](../customer-export-import/overview.md). 

To import contacts into the Contacts module:

1. Prepare a CSV file of contacts. We recommend to [export a sample CSV file](managing-contacts.md#export-contacts) and use it as a template.
1. Click **Contacts** in the main menu.
1. In the next **Companies and Contacts** blade, click **Import** in the top toolbar.

	!!! tip
		In this step, you can specify an organization to import your contacts into. 

1. In the next blade, select the data type from the dropdown list (Contacts or Organizations).
1. Browse your file or drag and drop it to the specified field.

	![Import Contacts](media/import-contacts.png)

1. After uploading files, click **Preview** to open the uploaded contacts in the next blade.
1. Verify the result. Click **Import** in the top toolbar to complete the process. Otherwise, click **Close**.
1. Confirm your action.

Your contacts have been uploaded.

## Update contacts

The procedure for updating contacts is similar to the one for [importing contacts](managing-contacts.md#import-contacts). The system finds organizations by Id or outer Id and updates them. 


## Share contacts

Contact URLs now include the member ID slug, allowing for easy sharing with colleagues or partners:

![Contact URLs](media/contact-urls.png)

You can also share company name and company ID by copying them from the dropdown menu:

![Contact ID](media/contact-id-name.png)

## Set default company

Administrators can now set a default company for an employee, so that they can log in to that company by default upon first login or after changing the default company:

1. Click **Contacts** in the main menu.
1. In the next blade, select an employee.
1. In the next blade, set a default company for them.

	![Default company](media/default-company.png)

1. Click **Save** in the toolbar to save the changes. 

## Assign multiple organizations to contacts and employees

For corporate accounts in the Frontend Application, you can assign multiple organizations to any contact or employee:

1. Click **Contacts** in the main menu.
1. In the **Companies and Contacts** blade, select the required contact. 
1. In the next blade, add as many companies to the **Member of company (ies)** segment as needed from the dropdown list.
1. Click **Save** in the top toolbar to save the changes.

	![Assign multiple organizations](media/assign-multiple-organizatopns.png)

The contact can now switch between the assigned organizations in the Frontend Application:

![Storefront multiple organizations](media/storefront-multiple-organizations.png)

