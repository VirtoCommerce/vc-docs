# Frontend Localization

Virto Commerce Frontend supports localization through JSON-based language files stored in the following folders:

| Folder path                                 | Description                                                             |
|---------------------------------------------|-------------------------------------------------------------------------|
| /locales/*.json                             | Localizations for shared UI components and global Frontend strings.     |
| /client-app/ui-kit/locales/*.json           | Localizations for UI Kit components (buttons, inputs, alerts, layouts). |
| /client-app/modules/[module]/locales/*.json | Localizations for each frontend module (checkout, etc.).                |

By contributing new or updated translations, you can extend the Frontend to support additional languages.


## Prepare localization file

1. **Open the English localization file** in the appropriate folder:
1. Use an AI tool (such as ChatGPT or Grok) to translate it. The simplest prompt is **“Localize this JSON into ...”**.
1. Review and adjust the translation for accuracy and terminology consistency.
1. **Save the translated file**.

## Contribute

To add your translation to Virto Commerce Frontend:

1. **Fork the repository**.
1. **Create a feature branch**, e.g.:
1. **Add the new JSON translation file** to a relevant folder.
1. **Run frontend build/tests** to ensure the localization loads correctly.
1. **Commit and push** your changes.
1. **Submit a pull request** to the main repo.

Once your localization PR is accepted, the new language files are included in the Frontend source. The language becomes available in the Frontend.

<br>

![Read more](media/readmore.png){: width="20"} [Tracking and fixing missing locales](texts-customization.md)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../accelerators-guidelines">← Guidelines for using accelerators</a>
    <a href="../texts-customization">Tracking and fixing locales →</a>
</div>