# Packaged Business Capabilities (PBCs)

Packaged Business Capabilities (PBCs) are a core component of Virto Commerce's modular and flexible approach, known as the Virto Atomic Architecture. These PBCs are designed to encapsulate specific business functionalities, making them an ideal choice for decision-makers across various business entities.

Each Virto PBC includes:

* **Business end-to-end scenarios:** Each PBC includes complete business scenarios that guide the implementation of the capability.
* **Set of compatible modules:** PBCs come with a curated set of modules that work seamlessly together to deliver the desired functionality.
* **Package.json for fast installation:** Installation is simplified with a pre-configured **package.json** file, making it quick to get started.

Key benefits of PBCs:

* **Faster time to market:** PBCs streamline the deployment process, enabling businesses to launch new features and services quickly.
* **Lower cost of ownership:** By leveraging pre-packaged capabilities, companies can reduce development costs and maintenance efforts.
* **Higher flexibility and scalability:** PBCs are designed to be adaptable, allowing businesses to scale operations and customize solutions as needed.
* **Greater innovation and differentiation:** With PBCs, businesses can innovate rapidly, differentiating themselves in the marketplace with unique offerings.

Virto Commerce offers the following PBCs:

- [Virto Start](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/virto-start-packages.json): Foundational package for starting your e-commerce journey. Provides B2B and B2C configurations with native Virto Commerce Frontend integration.  
- [Identity Provider (IdP)](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/idp-packages.json): Authenticates and authorizes user access to applications. Enables quick customer authorization and authentication.  
- [Digital catalog](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/digital-product-packages.json): Facilitates creating and managing a digital product catalog. Includes PIM and rich search capabilities like semantic search and personalization.  
- [PIM (Product Information Manager)](https://github.com/VirtoCommerce/vc-module-profile-experience-api/releases/tag/3.811.0): Enables setting up and customizing product catalogs to meet business needs.  
- [Purchase](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/purchase-packages.json): Provides shopping cart and checkout functionality integrated with customer and order management.  
- [Customer & organizations (CRM)](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/crm-packages.json): Supports managing customers and organizations, enhancing relationship management.  

Install a PBC by running:

```console
vc-build install -PackageManifestPath path to package.json
```

![Readmore](media/readmore.png){: width="25"} [Release strategy](../../Updating-Virto-Commerce-Based-Project/release-strategy-overview.md)

