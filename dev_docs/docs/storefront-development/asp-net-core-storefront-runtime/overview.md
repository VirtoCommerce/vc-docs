﻿`vc-storefront` is essentially an [ASP.NET](http://asp.net) Core project that is primary used as a runtime for hosting single or multiple websites (stores) with their own themes that are connected to Virto Commerce Platform. It also handles most of the front end work, such as server side rendering, authentication, and integrating middleware with the platform REST and GraphQL APIs.

## Key Features

- ***Multistore and multi-theme***: You can run multiple stores or websites based on `vc-storefront`. Each store might have its own theme with a specific layout still being based on the same catalog and customer data. As a result, you can host multiple websites with [custom themes](../../under-construction/under-construction.md)<!---link to themes--> in a single application.
    
- ***Native integration with VC Platform API*** to use data based on the [platform API resources on the theme pages](../../under-construction/under-construction.md)<!---Link to WorkContext and dynamic data sources-->.
    
- ***Customer sessions and all security aspects*** that are specific to web ecommerce projects, such as [anonymous checkout, single sign on with popular social media, 2F authentication, and more](../../under-construction/under-construction.md)<!---link to Security aspects-->.
    
- ***Out-of-the-box Server Side Rendering and SEO capabilities***: `vc-storefront` generates server-side rendered pages to improve SEO results and provides rich capabilities to handle slug routes, automatic site map generations, and redirect rules, along with caching for data and even page improvements for [boosting the overall SEO rating for websites running on `vc-storefront`](../../under-construction/under-construction.md)<!---link to SEO details-->.
    

## Technologies and Frameworks Used
`vc-storefront` uses:

-  [ASP.NET](http://asp.net/) MVC Core 6.0 on .NET 6.0
    
- [Scriban](https://github.com/scriban/scriban) as a lightweight `liquid` scripting language and engine
    

## How to Work with `vc-storefront`

As a developer, you will use Storefront as a precompiled application to host custom themes. Since the custom themes are the primary point of customization, you will rarely have to make any changes to the `vc-storefront` solution.

### Useful Links
Click [here](https://github.com/VirtoCommerce/vc-storefront) to browse Virto Commerce's Storefront project on hour GitHub repository.
