# Packaged Business Capabilities (PBCs)

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


| **PBC** | **Description** | **Benefits** |
|---------|-----------------|--------------|
| [Virto Start](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/virto-start-packages.json) | Foundational package for starting your e-commerce journey.<br>Provides B2B and B2C configurations with native <br> Virto Commerce Frontend integration. | - Quick setup for B2B/B2C stores. <br>- Pre-built tools and templates. <br>- Scalable and cost-effective. |
| [Identity Provider (IdP)](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/idp-packages.json) | Authenticates and authorizes user access to applications. <br> Enables quick customer authorization and authentication. | - Secure customer login. <br>- Role-based access control. <br>- Centralized authentication. |
| [Digital Catalog](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/digital-product-packages.json) | Facilitates creating and managing a digital product catalog. <br> Includes PIM and rich search capabilities like semantic search <br> and personalization. | - Real-time product data. <br>- Accurate, fast search. <br>- Catalog sharing without purchase. |
| [PIM (Product Information Manager)](https://github.com/VirtoCommerce/vc-module-profile-experience-api/releases/tag/3.811.0) | Enables setting up and customizing product catalogs <br> to meet business needs. | - Simplifies product management. <br>- Ensures data accuracy. <br>- Supports catalog scaling. |
| [Purchase](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/purchase-packages.json) | Provides shopping cart and checkout functionality integrated <br> with customer and order management. | - Supports diverse catalogs. <br>- Customizable checkout. <br>- Flexible purchase workflows. |
| [Customer & Organizations (CRM)](https://github.com/VirtoCommerce/vc-modules/blob/master/pbc/crm-packages.json) | Supports managing customers and organizations, <br> enhancing relationship management. | - Organizes customer data. <br>- Improves relationship management. <br>- Scales with business. |


Install a PBC by running:

```console
vc-build install -PackageManifestPath <path to package.json>
```

