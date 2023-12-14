# Setting Up Prerender.io with Azure Application Gateway

[Prerender.io](http://Prerender.io)  is a valuable tool for optimizing your website's SEO performance by rendering JavaScript content for search engine crawlers.

![Readmore](media/readmore.png){: width="25"} [Enhancing SEO with Prerender.io](../../storefront-development/integrations/prerender_io.md)

In this guide, we will learn how to set up [Prerender.io](http://Prerender.io) with Azure Application Gateway for our https://virtostart-demo-store.govirto.com single-page application using the Azure Portal.

![Scheme](media/prerender-io-scheme.png)

## Prerequisites

* Azure subscription.
* Prerender.io token. [Sign up](http://Prerender.io) to get your token.

## Set Up Prerender.io

To set up [Prerender.io](http://Prerender.io) with Azure Application Gateway:

1. Create Application Gateway in the [Azure portal](https://portal.azure.com/) (Home--> Create a resource --> Marketplace --> Application Gateway).
1. Configure **Basics**:
    1. Select a unique name for the Application Gateway.
    1. Select a region.
    1. Select an SKU based on your requirements.

        The basic settings of selecting a resource group, naming the application gateway, and selecting a VNET subnet are as follows:

        ![Create Gateway](media/create-gateway.png)

    1. Click **Next:Frontends**.

1. Configure **Frontends**:
    1. Select or create the Public IP Address to be assigned to this gateway.
    1. Under the **Frontend IP configuration** section, create or select the existing IP configuration.

        ![Frontends](media/forntends.png)

    1. Click **Next:Backends**.


1. Configure **Backends**:
    1. Click **Add a backend pool**. In this case, we will add two example backend pools. 
    1. Add a pool for the **service.prerender.io**. Fill in the fields as follows, then click **Add**.
    
        ![Add pool 1](media/pool1.png)
    
    1. Add a pool for our downstream frontend https://virtostart-demo-store.govirto.com which runs as a single-page application written in Vue.js. Fill in the fields as follows, then click **Add**.
    
        ![Add pool 2](media/pool2.png)
    
    1. The added pools appear in the list:

        ![Pools](media/pools.png)

    1. Click **Next:Configuration**.

1. Manage **Configuration** to connect the frontend and backend pool you created using a routing rule:
    1. Click **Add a routing rule** in the **Routing rules** column.
    1. In the new window, fill in the fields in the **Listener** tab. Configure HTTPS settings to define how the Application Gateway should handle the incoming requests, then click **Add**. You must already have an ssl certificate issued for your public IP domain. In our case, we use the RSA certificate (.pfx) issued by the **ZeroSSL** service for the **vc-prerender.westeurope.cloudapp.azure.com** domain.

        ![Listener](media/routing-rule1.png)
    
    1. In the **Backend targets** tab, fill in the fields as follows:

        ![Backend targets](media/routing-rule2.png)
    
    1. For the **Backend Settings**, click **Add new**. Fill in the fields as follows, then click **Save**:

        ![Backend settings](media/backend-settings.png) 

    1. ???? Add a path

        ![Path](media/path.png)
    
    1. The path appears in the paths section:

        ![Paths](media/path-section.png)

    1. In the **Add a routing rule** window, click **Add** to save the routing rule and return to the **Configuration** tab.

    1. Click **Next:Tags** to manage tags. Then click **Next: Review + Create**.

1. Review your configurations and click **Create** to deploy the Application Gateway.

1. Configure URL rewrite to redirect requests to **service.prerender.io**:

    Once the application gateway is deployed, we need to redirect all incoming **GET** requests to **service.prerender.io**. 

    !!! Example
        If a customer requests https://vc-prerender.westeurope.cloudapp.azure.com/catalog, our rewrite rule redirects and rewrites this request to https://service.prerender.io/https://virtostart-demo-store.govirto.com/catalog and add an **X-Prerender-Token header** with our auth token value to authorize these requests in the prerender.io service.

    1. Select **All resources**, then select your recently created application gateway (**app-gateway**) in the list.
    1. Select **Rewrites** in the left panel, then click **Rewrite set**:

        ![Rewrite](media/rewrite-set.png)

    1. Rewrite rule configuration.

        ![Rewrite](media/rewrite-rule.png)

    1. Add a rule to add the x-prerender-token header to each request:

        ![Rule 1](media/rule1.png)

    1. Add a rule to rewrite the path for all incoming requests according to this rule /https://virtostart-demo-store.govirto.com{var_uri_path} before sending to backend url service.prerender.io. 

        !!! Example
            The incoming request to the public url https://vc-prerender.westeurope.cloudapp.azure.com/foo will be redirected to https://service.prerender.io/https://virtostart-demo-store.govirto.com/foo after processing this rule.

        ![Rule 2](media/rule2.png)

Prerender.io has been successfully set up!