# Update

New releases are published every two weeks on the [GitHub repository releases page](https://github.com/VirtoCommerce/vc-frontend/releases).

!!! note
    It is strongly recommended to update with every release to reduce the risk of merge conflicts and integration issues.

## Update from original repository (upstream)

To fetch and merge changes from the original repository into your current project:

1. Create a new branch for the update. Replace **1_18** from our example with the target version or tag you are syncing to:

    ```
    git checkout -b update-1_18
    ```

1. Add the upstream remote. Replace the URL with the actual upstream repository:

    ```
    git remote add upstream https://github.com/VirtoCommerce/vc-frontend.git
    ```

1. Fetch upstream changes. This will download all branches and commits from upstream, without merging:

    ```
    git fetch upstream
    ```

1. Merge changes from the dev branch of the upstream into your current branch:

    ```
    git merge upstream/dev
    ```

    !!! note
        Resolve any merge conflicts if prompted.

1. (Optional) Remove the upstream remote if you don’t need to keep the upstream reference:

    ```
    git remote remove upstream
    ```

!!! note
    Use `git remote -v` to list current remotes.
    If you plan to pull updates frequently, you can skip removing upstream.
    Always test merged code before pushing to production.


## Merge specific release from upstream (recommended)

If you need a specific version instead of a branch:

1. Select the desired release from https://github.com/VirtoCommerce/vc-frontend/releases

1. Add the upstream remote:
    
    ```
    git remote add upstream https://github.com/VirtoCommerce/vc-frontend.git
    ```

1. Fetch all tags:

    ```
    git fetch upstream --tags
    ```

1. Merge the specific release tag (e.g. 2.22.0):

    ```
    git merge tags/2.22.0
    ```