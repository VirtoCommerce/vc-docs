# REST API Testing

To test the created rule, use REST API testing as follows:

1. Let's say that according to the created rule you have 6 products to promote (products to diplay) as related products to 6 items (matching products).

    ![Number of matching products](media/products-to-match-total.png)

1. Copy any of the matching products ids from the Catalog module.

    ![Matching product id](media/any-matching-product-id.png)

1. Access the [REST API endpoint](https://virtostart-demo-admin.govirto.com/docs/index.html) and select **VirtoCommerce.DynamicAssociationsModule** from the drodown list.

    ![Dropdown](media/api-testing-1.png)

1. Go to **/api/dynamicassociations/evaluate**, paste the Id of the product from clipboard, and complete the request as follows:

    ![Request](media/api-testing-2.png)

1. Click **Execute** to receive the response:

    ![Response](media/api-testing-3.png)

You can see, the rule is correct returning 6 relatde items that will be displayed with the specified item. 