# cancelQuoteRequest ==~mutation~==

This mutation cancels a specific quote request.

## Arguments

The `CancelQuoteCommandType!` is used for a command to cancel a quote.

|Field|	Description|
|-----|------------|
|`quoteId` ==String!==|	The Id of the quote to be canceled.|
|`comment` ==String!==|	A comment or reason for canceling the quote.|


## Possible returns

| Possible return                                          	| Description                     |
|---------------------------------------------------------	|---------------------------------|
| [`QuoteType`](../objects/QuoteType.md)                   	| Information about the order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: CancelQuoteCommandType!) {
      cancelQuoteRequest(command: $command) {
        id
        status
        storeId
        customerId
        customerName
        comment
        number
        items {
          productId
          name
          sku
          product {
            id
            name
          }
        }
        addresses {
          countryCode
          countryName
          city
          regionName
          line1
          line2
          email
          firstName
          lastName
          phone
          postalCode
          organization
          addressType
        }
        totals {
          originalSubTotalExlTax {
            amount
          }
          subTotalExlTax {
            amount
          }
          shippingTotal {
            amount
          }
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {"command": 
      {"quoteId": "80d92257-5286-4fe2-933c-e1280d16677f",
        "comment": "Sample comment"
      }
    }
    ```
