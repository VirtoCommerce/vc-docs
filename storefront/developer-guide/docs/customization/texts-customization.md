# Track and Fix Locales

Virto Commerce Frontend provides flexible tools to customize all text content displayed in the Frontend. This includes modifying static texts, translating them into multiple languages, and ensuring consistent localization across the entire application. Text customization is handled through locale files, which define translation keys and their corresponding values for different languages.

## Check for missing locale keys

To ensure that all locale files have consistent keys across different languages and avoid missing translations, run:


```bash
yarn check-locales -- path/to/locales_folder path/to/**/locales
```

The script outputs warnings for any missing keys in the locale files. Review these warnings to ensure all necessary translations are present. This check is also integrated into the CI pipeline to automate the validation process.

## Fix missing locales

To automatically fix missing translations in the locale files using AI translation, run.

```bash
yarn fix-locales -- path/to/locales_folder path/to/**/locales
```

This command analyzes all locale files, identifies missing keys, translates the missing content from the source language to the target language, and updates the locale files accordingly.

!!! note
    This command requires the `APP_GEMINI_API_KEY` environment variable to be set. You can obtain this API key from the [Google AI Studio](https://aistudio.google.com/app/apikey) website.

!!! warning
    This is an experimental feature and may not work as expected.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../localization">← Localization</a>
    <a href="../../storybook">Storybook →</a>
</div>