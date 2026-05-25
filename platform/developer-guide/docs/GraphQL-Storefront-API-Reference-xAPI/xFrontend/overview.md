# xFrontend

The **xFrontend** module extends the Virto Commerce GraphQL schema and aggregates several essential backend calls into a single optimized `pageContext` request. By providing this consolidated query, the xFrontend module significantly reduces the number of API calls required during store bootstrap, improves First Contentful Paint (FCP), and simplifies frontend integration. Without this module, storefronts must continue using four separate requests to gather the same data.


## Key features

* Unified API for retrieving all page-level contextual data.
* Optimized queries tailored for frontend rendering.
* Combined response containing Store, User, Slug Info, and White-labeling settings.
* Reduced number of API calls required during storefront bootstrap.

| Queries    | Objects       | 
| -----------| ------------- | 
| [PageContext](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/xFrontend/PageContext) | [PageContextResponseType](/platform/developer-guide/GraphQL-Storefront-API-Reference-xAPI/xFrontend/objects/PageContextResponseType) | 


[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-x-frontend/releases)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-x-frontend/releases/latest)
