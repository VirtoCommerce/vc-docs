# Configure Multiple Stores on Virto Cloud

Virto Commerce lets you run multiple websites (stores) on a single platform instance, each with its domain, theme, and configurations while sharing the same catalogs and customer data. In practice, you create separate stores in the Virto Commerce Manager, assign catalogs/pricing, and upload individual themes. The new Virto Commerce frontend is fully headless and composable, so you can flexibly add any number of front-end sites. 

Below is a step-by-step guide to set up multiple stores on Virto Cloud.

## Prerequisites

* Your Virto Commerce Platform is [deployed and running on Virto Cloud](../../../../deployment-on-cloud/deploy-on-virto-cloud).

* Review [Virto Commerce Frontend Architecture](../../../../../storefront/developer-guide/architecture).

## Create and configure new stores

Follow the [guide](../../../../deployment-on-cloud/store-configuration) to configure a new store.

## Create new Frontend Application

You can either create a new Virto Commerce Frontend Application or use ready ready-created artefact from [Frontend releases](https://github.com/VirtoCommerce/vc-frontend/releases)

## Integrate Frontend Application 

To integrate a Frontend Application (for example, **B2B-loyalty**) into your Virto Commerce deployment:

!!! note
    You can find all changes in [this commit](https://github.com/VirtoCommerce/vc-deploy-dev/commit/b6b672abbec6236fca5f704ec2d12998143296a0).

1. Navigate to the **infra** directory of your deployment repository and open the **environments.yml** file.

1. Within the **themes** section, add an entry for **B2B-loyalty** pointing to the appropriate theme package. For example:

    ```yaml
    themes:
      B2B-loyalty: https://github.com/VirtoCommerce/vc-frontend/releases/download/2.22.0/vc-theme-b2b-vue-2.22.0.zip
    ```

1. Under the **frontend** section, add a new entry for **B2B-loyalty** with **prerender** set to **true**. For example:

    ```yaml
    frontend:
      - name: B2B-loyalty
    ```

1. Configure domain and routing in ingress:

    !!! note
      3rd-level domain for **govirto.com** will be enabled automatically. If you need additional steps for custom domain assignment, follow [Virto Cloud documentation](../../../../deployment-on-cloud/index) for it. 

    ```yaml
        - host: virtostart-loyalty-store.govirto.com
          root: B2B-loyalty
          paths:
          - path: /xapi
            route: platform
          - path: /files
            route: platform
          - path: /connect/token
            route: platform
          - path: /graphql
            route: platform
          - path: /revoke/token
            route: platform
          - path: /api/files
            route: platform
          - path: /externalsignin
            route: platform
          - path: /signin-oidc
            route: platform
          - path: /signin-google
            route: platform
    ```

1. Apply the changes to your deployment environment using your standard deployment process.


The **B2B-loyalty** Frontend Application has been successfully added to your Virto Commerce deployment configuration:

![New frontend app added](media/multiple-stores.png)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuring-multiple-stores">← Configuring multiple stores </a>
    <a href="../extending-cart-query-with-custom-parameter">Extending Cart query with custom parameter  →</a>
</div>