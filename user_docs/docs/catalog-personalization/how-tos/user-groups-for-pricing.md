# How to Enable Special Prices for Specific Users
This guide will explain you how to show and apply specific prices to the users of your choice. In our example, we will configure Virto Platform in such a way that the store will display a disconted price for loyal customers.

## Creating User Group and Adding Contacts
Let's assume you have an item you are willing to sell at a discounted price to your loyal customers, as a reward to their loyalty. To make it happen, you need to first create a user group, as described [here](../user-groups.md#creating-new-user-group), and add all contacts of those loyal customers to this group. If any of those people are not yet registered in your system, you can easily create as many contacts as you need.

In our example, we created a group called *VIP* and assigned various contacts to it, including one named Alex Starberg, who will be our loyal customer in the example:

![Adding contact to user group](media/adding-to-ug.png)

## Assigning User Group to Price List
By default, the item we will be selling to loyal customers with a discount (Samsung smartphone in our example) has the same price for everyone who visits the store:
<!---add screen capture-->

To enable the special price for the VIP customers, you should do the following:

1. Create a dedicated price list assignment, as described [here](../../pricing/adding-new-assignment.md)
2. Assign the group in question to the price list through the ***User group contains...*** menu:

![Adding contact to user group](media/adding-ug-to-price-list-1.png)

![Adding contact to user group](media/adding-ug-to-price-list-2.png)

Now, if anyone who is not included into our *VIP* group visits our store, they will see the regular price for the item in question:
<!---add screen capture-->

However, once Alex Starberg, our loyal customer, logs into the store, he will get his discount:
<!---add screen capture-->
