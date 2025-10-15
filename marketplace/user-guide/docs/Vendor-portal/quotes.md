# Quotes 

The Quotes segment contains all quotes submitted to the vendor:

![Quotes list](media/quotes-list-vendor-portal.png)

Clicking a quote opens its details. The vendor can either accept the quoted price or modify it.

The created quotes are processed in accordance with the defined [states flow](../Operator-portal/state-machines.md). In this example, the quotes are processed as follows:

1. The submitted quotes require processing. The vendor can either send a proposal or cancel it. Canceled quotes cannot be further processed.
1. If the vendor sends a proposal, the buyer can either place an order if the proposal is acceptable, or decline it. 

    ![Statuses](media/quote-statuses.png){: style="display: block; margin: 0 auto;" }


![Readmore](media/readmore.png){: width="25"} [Setting order states and order flows](../Operator-portal/state-machines.md)


<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/le1gzcbrxjyl?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../orders">← Orders</a>
    <a href="../products-management">Products →</a>
</div>