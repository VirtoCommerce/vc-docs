# Overview

=== "For new users"

    Virto Commerce Frontend is a single-page web application (SPA) with a fresh look on ecommerce solutions. This is where common B2B and B2C scenarios are combined with the most bleeding-edge technologies to deliver blazing-fast and fully functional solutions. It implements common business use cases needed for a vast majority of projects we build.

    Virto Commerce Frontend is designed to be used as-is within the actual Virto Commerce Platform. You can modify it by implementing desired components, pages, and shared logic to correspond with your project goals.

    [Deploy Frontend Application](deployment.md)


=== "For current Storefront and Theme users"

    As of July 2024, Virto Commerce Storefront and Theme have been replaced with the Frontend Application. 
    
    !!! note
        Current users now have the following options:

        1. Migrate to the new storefrontless architecture [on your own](migration.md) or with our [assistance](https://help.virtocommerce.com/support/home).
        1. Continue using the Storefront with the [1.62 version](https://github.com/VirtoCommerce/vc-theme-b2b-vue/tree/support/1.62), which will receive updates until the end of 2024. After that, while it will still be possible to use the Storefront, no further updates will be provided.
    
    The primary objective of the new Virto Commerce Frontend Architecture is to simplify and expedite the development of ecommerce solutions based on the Virto Commerce Platform. This architecture replaces the custom **vc-storefront** with a standard load balancer, such as **nginx** or **Azure Load Balancer**. All business logic previously handled by **vc-storefront** is now integrated into the Platform through XAPI modules. This change ensures that developing business logic for client applications is now consistent with platform development.

    Virto Commerce Frontend (B2B-Theme 2.x) is now a Single Page Application (SPA) stored in static resources. The load balancer is configured to route requests from the client machine to both static content and XAPI endpoints. Additionally, this architecture supports the integration and utilization of third-party SPA applications.


![Frontend application](media/desktop.png)

[![Storefront demo site](media/public-demo-site.png)](https://virtostart-demo-store.govirto.com/)


## Technologies Used

- **[Vue3](https://vuejs.org/):** Progressive frontend framework with its key features allowing one to build fast applications.
    
- [**TypeScript**](https://www.typescriptlang.org/)**:** All components and composables have type definitions, so that IDE could help you build clean and working code.
    
- [**TailwindCSS**](https://tailwindcss.com)**:** The most popular and growing CSS framework providing wonderful flexible structure to speed up styling.
    
- **Husky + ESLint + Prettier:** Autoformat, check, and fix your code and prevent ugly code style within repository.
    
- [**Vite**](https://vitejs.dev/)**:** Faster than Webpack, it is used to develop code with HMR benefits and build for production.
    
- [**GraphQL**](https://graphql.org/) **:** Use flexible GraphQL queries and mutations to safely work with back end.

## Key Non-functional Features

- **Development Performance**: Achieve rapid development using the most effective solution. Deploy the SPA in seconds and start modifying code with [HMR features](https://vitejs.dev/guide/api-hmr).

- **Client Performance**: Reach and maintain high performance metrics as provided by Google PageSpeed Insights.

- **[Atomic Design Pattern](https://virtocommerce.com/atomic-architecture)**: Base the UI on Atoms, Molecules, and Organisms, combined within Pages and shared Components for high code reusability.

- **Fully Responsive**: Ensure the application works seamlessly on multiple devices, from desktops to mobile phones, providing an excellent UI and UX.

- **Simple Styling and Customization**: Use TailwindCSS for straightforward and convenient CSS usage, minimizing code and leveraging a highly customizable framework.

- **Fully Aligned with Virto Commerce Platform**: Integrate the SPA with the [Virto Commerce Platform](https://github.com/VirtoCommerce/vc-platform) to support all common B2B and B2C scenarios.

## Key Functionalities

The key functionalities include:

* [Registration and signing in.](../../../storefront/user-guide/registration_and_signing_in/create-account)
* [Password management.](../../../storefront/user-guide/registration_and_signing_in/password-management)
* [Managing personal and corporate accounts.](../../../storefront/user-guide/account/overview)
* [Managing quote requests.](../../../storefront/user-guide/shopping/submit-quotes)
* [Managing lists.](../../../storefront/user-guide/shopping/lists)
* [Access assignment.](../../../storefront/user-guide/account/company-members)
* [Product comparison.](../../../storefront/user-guide/shopping/compare-products)
* [Bulk orders.](../../../storefront/user-guide/shopping/bulk-orders)
* [Intuitive navigation.](../../../storefront/user-guide/navigation/homepage-layout)
* [Buying digital and physical products.](../../../storefront/user-guide/shopping/checkout-process) 
* [Searching and filtering products.](../../../storefront/user-guide/shopping/searching-for-products)
* [Managing push messages](../../../storefront/user-guide/account/notifications)