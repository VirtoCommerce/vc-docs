# Installation and Configuration

The Intent Search module requires several external services and platform-level settings to function correctly. Follow the steps below to prepare your environment, configure dependencies, and validate the integration.

## Prerequisites

This module integrates with external AI services. You'll need accounts for:

1. Weaviate.io used as the vector database for semantic search, similarity matching, and storing embeddings:
    1. Create an account at [Weaviate Cloud](https://weaviate.io/).
    1. Create a new Weaviate cluster.
    1. Note your cluster URL and API key

1. Hugging Face to provide embedding models used to convert user queries and product text into semantic vectors:
    1. Create an account at [Hugging Face](https://huggingface.co/).
    1. Generate an API token from your account settings
    1. The module uses public models but requires authentication for optimal performance

## Configuration

To connect the Intent Search module to Weaviate and Hugging Face and to control networking, retry logic, and resilience settings:

1. Add the following node to your Virto Commerce Platform [settings](../../Configuration-Reference/appsettingsjson.md#weaviate):

    {% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--weaviate-start-->" end="<!--weaviate-end-->" %}

1. Register the module in your Virto Commerce Platform following standard module installation procedures.
1. Run the integration test `IntegrationScenarios.Test_Complete_Scenario()` to verify your setup.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Intent Search overview</a>
    <a href="../examples">Examples →</a>
</div>
