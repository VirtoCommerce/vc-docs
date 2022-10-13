# How to Show or Hide Catalog Items for Specific Users
This guide will explain you how to show or hide specific products or categories from the users of your choice. In our example, we will configure Virto Platform in such a way that an item will be available for view and purchase only for selected customers.

## Creating User Group and Adding Contacts
Let's assume you have an item you are willing to sell only to your loyal customers, as a reward to their loyalty. To make it happen, you need to first create a user group, as described [here](../user-groups.md#creating-new-user-group), and add all contacts of those loyal customers to this group. If any of those people are not yet registered in your system, you can easily create as many contacts as you need.

In our example, we created a group called *VIP* and assigned various contacts to it, including one named Alex Starberg, who will be our loyal customer in the example:

![Adding contact to user group](media/adding-to-ug.png)

## Assigning User Group to Category or Product
By default, the item we will be selling to loyal customers only (Samsung smartphone in our example) is visible to everyone who visits the store:
<!---add screen capture-->

To limit the access and allow only our *VIP* customers to see it, we need to assign the *VIP* group to the product or category in question, as described [here](../user-groups.md#assigning-user-group-to-contact).

!!! warning
	Once we do so, we must rebuild the index so that our changes may come into effect.

Now, if anyone who is not included into our *VIP* group visits our store, they won't see the item in question:
<!---add screen capture-->

However, once Alex Starberg, our loyal customer, logs into the store, he will be immediately able to purchase it:
<!---add screen capture-->
