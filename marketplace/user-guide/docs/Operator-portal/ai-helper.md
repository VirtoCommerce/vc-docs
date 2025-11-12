# AI Helper

The AI Helper section displays all requests processed by AI providers - for example, tasks related to product description generation, translation, or product property generation:

![AI resolved tasks](media/ai-tasks.png)

Clicking on any request opens its details:

![AI request details](media/ai-request-details.png)

## AI Helper settings 

To configure AI Helper settings:

1. Click **Settings** in the main menu.
1. In the next blade, select **AI Helper**.
1. Configure the following settings:

    <table border="1">
        <tr>
            <th>Settings level</th>
            <th>Setting name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td rowspan="2">General</td>
            <td>AI helper enabled</td>
            <td>Enables or disables the module.</td>
        </tr>
        <tr>
            <td>AI helper logging level</td>
            <td>Specifies the logging level: Minimal, None, or Verbal (each level defines the amount of logged information).</td>
        </tr>
        <tr>
            <td rowspan="3">General providers</td>
            <td>Image generation service provider</td>
            <td>Select an AI provider from the dropdown list.</td>
        </tr>
        <tr>
            <td>Image recognition service provider</td>
            <td>Select an AI provider from the dropdown list.</td>
        </tr>
        <tr>
            <td>Text generation service provider</td>
            <td>Select an AI provider from the dropdown list.</td>
        </tr>
        <tr>
            <td rowspan="3">GrokAI</td>
            <td>Grok API secret key</td>
            <td>Add your Grok API secret key.</td>
        </tr>
        <tr>
            <td>GrokAI model</td>
            <td>Select from: Grok 3 Mini, Grok 4 Fast (non-reasoning), or Grok 4 Fast (reasoning).</td>
        </tr>
        <tr>
            <td>GrokAI service endpoint</td>
            <td>Specify the GrokAI service endpoint URL.</td>
        </tr>
        <tr>
            <td rowspan="3">OpenAI</td>
            <td>OpenAI API secret key</td>
            <td>Add your OpenAI API secret key.</td>
        </tr>
        <tr>
            <td>OpenAI model</td>
            <td>Select from: GPT 5 Nano, GPT 5 Mini, or GPT 5 Nano.</td>
        </tr>
        <tr>
            <td>OpenAI images model</td>
            <td>DALLE 3.</td>
        </tr>
        <tr>
            <td rowspan="2">Prompts - GrokAI</td>
            <td>GrokAI product description generate prompt</td>
            <td>Add the prompt text used for product description generation.</td>
        </tr>
        <tr>
            <td>GrokAI translate prompt</td>
            <td>Add the prompt text used for translations.</td>
        </tr>
        <tr>
            <td rowspan="4">Prompts - OpenAI</td>
            <td>OpenAI description generation without image prompt</td>
            <td>Add the prompt text used to generate product descriptions without images.</td>
        </tr>
        <tr>
            <td>OpenAI description generation by image prompt</td>
            <td>Add the prompt text used to generate product descriptions based on images.</td>
        </tr>
        <tr>
            <td>OpenAI fill properties by image prompt</td>
            <td>Add the prompt text used to generate product properties based on images.</td>
        </tr>
        <tr>
            <td>OpenAI translate prompt</td>
            <td>Add the prompt text used for translations.</td>
        </tr>
    </table>

1. Click **Save** in the toolbar to save the settings.

Your modifications have been applied.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../state-machines">← State machines</a>
    <a href="../../Vendor-portal/overview">Vendor portal overview→</a>
</div>