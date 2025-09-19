# Guidelines for Using Accelerators

To ensure your project remains stable, maintainable, and easy to update, please follow these core principles: 

* **Preserve the core, extend with new files**: Avoid modifying the original scripts directly. Doing so will create significant merge conflicts when you pull future updates from the base repository. Instead, always create new files for your custom logic and compose them with the base tooling if needed.
* **Follow established conventions**: Build upon the existing foundation to ensure consistency. Place your new scripts in the **scripts/** directory, write them in TypeScript, and add corresponding commands to **package.json**. Mimicking the existing patterns will make your project easier for your team to understand and maintain.
* **Namespace your custom scripts**: To prevent naming conflicts with future updates and to clearly distinguish your project's specific tooling, it is best practice to prefix your custom **package.json** scripts. For example: `custom:generate-component` or `myproject:validate-theme`.
* **Ensure compatibility**: After adding a new accelerator, always validate that you have not broken any core functionalities. Run the main workflows (build, test, lint) to guarantee that your new tooling coexists safely with the base platform and does not introduce regressions.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../accelerators-overview">← Development accelerators</a>
    <a href="../texts-customization">Locales management →</a>
</div>