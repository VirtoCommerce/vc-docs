# Merge Updates

To bring the latest changes from the official Virto Commerce theme (e.g., vc-theme-b2b-vue) into your project:

1. Create a dedicated branch for the update. Replace `{1_18}` with the theme version in the branch name, for example:

    ```bash
    git branch update-{1_18}
    ```

1. Add the official theme repository as an upstream remote:

    ```bash
    git remote add upstream <link>
    ```

1. Fetch the latest updates from upstream:

    ```bash
    git fetch upstream
    ```

1. Merge the upstream branch into your update branch:

    ```bash
    git merge {1_18}
    ```

1. Resolve any merge conflicts if they appear.

1. Remove the temporary upstream remote:

    ```bash
    git remote remove upstream
    ```

The latest official changes have been brought into your project.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../tests">← Testing</a>
    <a href="../migration">Migration to Storefrontless architecture →</a>
</div>