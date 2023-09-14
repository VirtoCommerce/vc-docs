# Promotion combination policies

The Virto Commerce Marketing module provides two basic promotion combination policies:  

* [Best reward policy](combining-active-promotions.md#best-reward-policy) (default): Only the promotion that is most beneficial to the customer will be applied.
* [Stackable policy](combining-active-promotions.md#stackable-policy): Customers can qualify for multiple promotions at the same time.

## Best reward policy

This policy follows the common **Not valid with any other offer** principle, meaning that only one promotion can be applied. This promotion will be the most beneficial to the customer and will have the highest priority.

A simple example of such a policy might be two promotions, 10% off product and $10 off shipping. The system will calculate the most rewarding offer of these two and apply it at the customer's checkout.

## Stackable policy

With this policy, any promotion can be combined with any other promotion in an order. This means, for example, that if you have five active promotions and a customer qualifies for all of them, they will be applied at checkout.

!!! note
	The stackable policy has the following limitation: if the total order amount or any item price is less than zero after the promotion is applied, this reward will be skipped and the next one will be applied, in line with the priority settings.

[Read more about configuring combination policies](settings.md){ .md-button }