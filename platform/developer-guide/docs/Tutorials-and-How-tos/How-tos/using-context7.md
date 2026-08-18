# Setting Up Context7

When using an AI assistant for Virto Commerce specific issues, the generated output may only appear correct. This happens because language models are trained on static datasets. Since Virto Commerce evolves continuously, the AI-generated content may reference outdated patterns.

To eliminate this, Virto Commerce documentation is now available through [Context7](https://context7.com/virtocommerce/vc-docs), an MCP (Model Context Protocol) server that dynamically augments the LLM prompt with current official documentation before code generation.

Context7 automatically loads the latest, version-specific documentation and real code examples directly from Virto Commerce source repositories into the AI’s working context. This helps AI coding assistants base their answers on actual, current documentation instead of assumptions or outdated knowledge.

## Key benefits

For fast-evolving platforms such as Virto Commerce, Context7:

* Reduces compile-time errors caused by outdated APIs
* Prevents use of deprecated extension points
* Aligns generated code with current DI and module registration patterns
* Improves reliability of xAPI and GraphQL schema extensions
* Decreases refactoring time caused by AI hallucinations

It transforms AI-assisted development from speculative scaffolding into documentation-aligned code generation.

## Installation

Select your preferred environment and follow the steps to set up Context7 as an MCP server:

=== "Cursor"

    1. Navigate to **Settings --> MCP --> Add new global MCP server**

    1. Add:

         ```json
         {
           "mcpServers": {
              "context7": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp@latest"]
              }
            }
         }
         ```

    1. Restart Cursor after configuration.


=== "Claude Code"

    Run the following command in your terminal to register Context7 as an MCP server in Claude Code:

    ```bash
    claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
    ```


=== "One-Off Execution (No Installation)"

    To run Context7 without installing it, execute the following command directly in your terminal:
    
    ```bash
    npx -y @upstash/context7-mcp@latest
    ```

    Context7 is model-agnostic and compatible with any MCP-capable editor environment, including Claude, GPT-4-class models, and Gemini.


## Usage

Append **use context7** to any platform-specific prompt to ground the generation on current Virto Commerce documentation retrieved at runtime. The directive triggers documentation retrieval before the AI generates its response.

```
Implement a custom pricing calculator service in a Virto Commerce module. use context7
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../adding-case-sensitive-search-support-for-postgre">← Adding case-insensitive search support for PostgreSQL </a>
    <a href="../swagger-api">Swagger/API integration  →</a>
</div>