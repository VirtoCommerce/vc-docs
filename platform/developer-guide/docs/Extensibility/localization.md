# Localization

Virto Commerce supports localization through JSON-based language files stored in each module’s GitHub repository (**src** --> **web** --> **Localizations**). By contributing new or updated translations, you can extend the Platform to support additional languages.

Each Virto Commerce module contains JSON files, one per language. For example, **en.json** for English, **de.json** for German, etc. The Platform loads these files automatically after they are merged into the module repository.


## Prepare localization file

1. Open the **English** localization file (**en.json**) for the module you want to localize.
1. Use an AI tool (such as ChatGPT or Grok) to translate it. The simplest prompt is **“Localize this JSON into ...”**.
1. Review and adjust the translation for accuracy and terminology consistency.
1. Save the translated file as **<language_code>.json**, for example: **sv.json**.

## Contribute 

To add your translation to Virto Commerce:

1. **Fork the repository** of the module you are localizing.
1. **Create a feature branch**.
1. **Add your new JSON file** to the localization folder.
1. **Add or update tests** related to localization or affected UI components.
1. **Run all tests** to ensure the module builds successfully.
1. **Commit and push** your changes.
1. **Submit a pull request** to the main repository.


Once the PR is merged the new localization file becomes part of the module. The new language will appear as an available localization option inside the Platform UI.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../page-builder-extension">← Adding new blocks to Page Builder </a>
    <a href="../../Operations/maintenance-tasks-for-sql">Maintenance tasks for SQL  →</a>
</div>