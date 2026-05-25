# Use llms.txt

Using **llms.txt** is the fastest way to ground any AI assistant on current Virto Commerce documentation. It does not require installation, MCP server, editor plugin, just a URL you paste into a prompt.

[llms.txt](https://llmstxt.org/) is an emerging convention (similar to **robots.txt** or **sitemap.xml**) that lets a project publish a curated, machine-readable index of its documentation for Large Language Models. The Virto Commerce documentation site hosts a hub at 
**https://docs.virtocommerce.org/llms.txt**.

The hub routes the AI to product-specific sub-indexes. Each file lists the most authoritative documentation pages for its scope, with one-line descriptions, so the AI can fetch the specific page it needs instead of guessing.

| Sub-index | Use it for | Example prompt |
|---|---|---|
| **llms.txt** | General entry point across all Virto Commerce documentation, cross-product questions, initial exploration | Before answering, please read https://docs.virtocommerce.org/llms.txt to learn about the latest Virto Commerce documentation, then answer my question: What are the main extensibility options in Virto Commerce? |
| **platform.txt** | Backend development, modules, extensibility, REST and GraphQL xAPI, CLI, admin UI, store configuration, integrations | Before answering, please read https://docs.virtocommerce.org/llms/platform.txt to learn about the latest Virto Commerce Platform documentation, then answer my question: How do I register a custom payment method in a Virto Commerce module? |
| **frontend.txt** | vc-frontend (Vue 3 SPA), theming, customization, xAPI integration, localization | Before answering, please read https://docs.virtocommerce.org/llms/frontend.txt to learn about the latest Virto Commerce Frontend documentation, then answer my question: How do I add a new locale to vc-frontend and override product page content? |
| **marketplace.txt** | Operator Portal, Vendor Portal, marketplace configuration, vendor workflows | Before answering, please read https://docs.virtocommerce.org/llms/marketplace.txt to learn about the latest Virto Commerce Marketplace documentation, then answer my question: How do I onboard a new vendor in the marketplace? |
| **vc-shell.txt** | Custom admin application framework, building and extending admin UI apps | Before answering, please read https://docs.virtocommerce.org/llms/vc-shell.txt to learn about the latest VC-Shell documentation, then answer my question: How do I create a custom admin module using VC-Shell? |
| **cloud.txt** | Virto Cloud deployment, environment management, scaling, CI/CD with vc-build | Before answering, please read https://docs.virtocommerce.org/llms/cloud.txt to learn about the latest Virto Cloud documentation, then answer my question: How do I deploy a custom Docker image to a Virto Cloud environment? |
| **rosetta.txt** | Cross-platform concept mapping (Shopify, Adobe Commerce, commercetools, BigCommerce), migration and comparison scenarios | Before answering, please read https://docs.virtocommerce.org/llms/rosetta.txt to learn about platform mappings, then answer my question: What is the equivalent of Shopify metafields in Virto Commerce? |


## Key benefits 

When asked Virto Commerce questions, AI assistants often answer from training data. They may reference removed APIs or deprecated extension points. **llms.txt** solves this by pointing the AI at current, authoritative sources.

* No installation required.
* Works in any chat or editor.
* Always reflects the current documentation site.
* Reduces hallucinated APIs and deprecated patterns.

<br>
<br>
![Readmore](media/readmore.png){: width="25"} [AI quick start](../../Getting-Started/ai-quick-start.md)



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../using-context7">← Setting up Context7 </a>
    <a href="../swagger-api">Swagger/API integration  →</a>
</div>
