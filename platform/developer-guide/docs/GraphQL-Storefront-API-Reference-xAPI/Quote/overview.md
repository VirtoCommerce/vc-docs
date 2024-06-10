# Overview

The Virto Commerce Quote Module is a quote management system. It allows shop owners to easily manage customer quotes and send out accurate quotes without having to create them manually.

The module offers the following key features:

* Unlimited tiers.
* Discounts can be applied either per tier or to the entire quote.
* Full line item management, even after the initial quote has been created.
* Support for attachments and dynamic properties.
* The ability to create a Regular Order once the Quote is confirmed by the customer.
* The option to set a default quote status.
* Organization maintainers have the capability to update quotes created by members of their organization.

| Queries                    	| Objects                                               | Mutations                                                                                                      	|
|----------------------------	|-----------------------------------------------------	|----------------------------------------------------------------------------------------------------------------	|
| [Quote](queries/quote.md) <br> [Quotes](queries/quotes.md)  	| [QuoteType](objects/QuoteType.md)<br> [QuoteConnection](objects/QuoteConnection.md)<br> [QuoteTotalsType](objects/QuoteTotalsType.md)<br> [QuoteItemtype](objects/QuoteItemtype.md)<br> [QuoteTierPriceType](objects/QuoteTierPriceType.md)<br> [QuoteAddressType](objects/QuoteAddressType.md)<br> [QuoteAttachmentType](objects/QuoteAttachmentType.md)<br> [QuoteShipmentMethodType](objects/QuoteShipmentMethodType.md)<br> [QuoteTaxDetailType](objects/QuoteTaxDetailType.md)<br> [QuoteEdge](objects/QuoteEdge.md)<br> [CancelQuoteCommandType](objects/CancelQuoteCommandType.md)<br> [ChangeQuoteCommentCommandType](objects/ChangeQuoteCommentCommandType.md)<br> [ChangeQuoteItemQuantityCommandType](objects/ChangeQuoteItemQuantityCommandType.md)<br> [CreateQuoteFromCartCommandType](objects/CreateQuoteFromCartCommandType.md)<br> [RemoveQuoteItemCommandtype](objects/RemoveQuoteItemCommandtype.md)<br> [SubmitQuoteCommandType](objects/SubmitQuoteCommandType.md)<br> [UpdateQuoteAddressCommandType](objects/UpdateQuoteAddressCommandType.md)<br> [InputQuoteAddressType](objects/InputQuoteAddressType.md)<br> [ApproveQuoteResultType](objects/ApproveQuoteResultType.md)<br>	| [cancelQuoteRequest](mutations/cancel-quote-request.md)<br> [changeQuoteComment](mutations/change-quote-comment.md)<br> [changeQuoteItemQuantity](mutations/change-quote-item-quantity.md)<br> [createQuoteFromCart](mutations/create-quote-from-cart.md)<br> [removeQuoteItem](mutations/remove-quote-item.md)<br> [submitQuoteRequest](mutations/submit-quote-request.md)<br> [updateQuoteAddresses](mutations/update-quote-address.md)<br> [addQuoteAttachments](mutations/addQuoteAttachments.md)<br> [approveQuoteRequest](mutations/approveQuoteRequest.md)<br>	[createQuote](mutations/createQuote.md)<br> [declineQuoteRequest](mutations/declineQuoteRequest.md)<br> [deleteQuoteAttachments](mutations/deleteQuoteAttachments.md)<br> [updateQuoteAttachments](mutations/updateQuoteAttachments.md)<br>|


[![Download module](../media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-quote/releases)
