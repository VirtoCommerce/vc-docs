The Virto Commerce Storefront is essentially an [ASP.NET](http://asp.net) Core project that is primary used as a runtime for hosting single or multiple websites (stores) with their own themes that are connected to Virto Commerce Platform. It also handles most of the front end work, such as server side rendering, authentication, and integrating middleware with the platform REST and GraphQL APIs.

## Key Features

- **Multistore and multi-theme**: You can run multiple stores or websites based on Storefront. Each store might have its own theme with a specific layout still being based on the same catalog and customer data. As a result, you can host multiple websites with custom themes <!---link to themes--> in a single application.
    
- [Native integration with VC Platform API](../getting-started/quickstart-on-windows.md) to use data based on the platform API resources on the theme pages.
    
- [Customer sessions and all security aspects](../../../../platform/developer-guide/Fundamentals/Security/overview) that are specific to web ecommerce projects, such as anonymous checkout, single sign on with popular social media, 2F authentication, and more.
    
- [Out-of-the-box Server Side Rendering and SEO capabilities](../../../../platform/user-guide/catalog/managing-categories): Storefront generates server-side rendered pages to improve SEO results and provides rich capabilities to handle slug routes, automatic site map generations, and redirect rules, along with caching for data and even page improvements for boosting the overall SEO rating for websites running on Storefront<!---link to SEO details-->.
    

## Technologies and Frameworks Used

Storefront uses:

- [ASP.NET](http://asp.net/) MVC Core 6.0 on .NET 6.0
    
- [Scriban](https://github.com/scriban/scriban) as a lightweight `liquid` scripting language and engine
    

## Working with Storefront

As a developer, you will use Storefront as a precompiled application to host custom themes. Since the custom themes are the primary point of customization, you will rarely have to make any changes to the Storefront solution.

[![Download latest release](../media/latest_release.png)](https://github.com/VirtoCommerce/vc-storefront/releases/latest)
