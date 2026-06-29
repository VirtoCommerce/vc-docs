# Versioning

This repository publishes versioned documentation using [mike](https://github.com/jimporter/mike). The current version is tracked in the `VERSION` file at the repo root.

## Versioning scheme

- Versions are stable snapshots that track the Virto Commerce Platform stable releases: `stable10`, `stable12`, `stable14`. The mike title is rendered as `Stable 14`. No minor or patch numbers.
- The currently published versions are `stable10`, `stable12`, and `stable14`. `stable14` is the latest (aliased as `latest`/`default`).
- Fixes to a released version overwrite the existing snapshot under the same number (no `stable14.1`).
- One version number applies to all seven documentation subsites (`platform/*`, `marketplace/*`, `storefront/*`).

## Branch model

| Branch             | Role                                                                          |
|--------------------|-------------------------------------------------------------------------------|
| `main`             | Current version. `VERSION` on this branch holds the latest version.           |
| `release/<version>`| A previously released version. Editable via PR. One per released version.      |
| `gh-pages`         | Built HTML artifacts. Managed by `mike`. Never edit manually.                  |

The bump automation names a release branch after the previous `VERSION` content, so new release branches are `release/stable12`, `release/stable14`, and so on. Two legacy branches predate this naming: `release/1.0` holds `stable10`, and `release/2.0` holds `stable12`.

## Editing docs

### Current version (whatever `main` points to)

The documentation maintainer may push directly to `main`. CI redeploys the current version on every push.

Other contributors must open a PR into `main`. On merge, CI redeploys the same way.

### Older version (e.g. stable12)
Open a PR into the matching release branch (`release/2.0` for `stable12`) with your markdown changes. On merge, CI rebuilds the `stable12` snapshot only. `latest`/`default` remain on the current version.

## Releasing a new version

1. Open a PR titled `Bump docs to stableNN`. The diff **must contain only** a change to `VERSION` (e.g., `stable14` → `stable16`).
2. Review and merge the PR as a **merge commit** (not squash, not rebase). Merge commit is required because automation needs `HEAD^1` of the merge to snapshot the previous version.
3. On merge, automation:
   - Creates `release/<previous>` from `HEAD^1` and pushes it (e.g. `release/stable14`).
   - Deploys the new version as `latest` and `default`.
4. From that point, the new version is current on `main` and the old version is editable on its `release/<previous>` branch.

## What not to do

- **Do not** squash-merge a bump PR. Automation relies on the merge-commit's first parent.
- **Do not** combine a version bump with markdown changes in the same PR. The bump-detection workflow requires the diff to contain only `VERSION`.
- **Do not** push to `gh-pages` manually — `mike` owns that branch.

## Recovery

If the automatic `release/<prev>` creation fails (e.g., the bump PR was accidentally squashed), you can create the branch manually from the commit immediately before the bump:

```bash
git checkout -b release/<prev> <commit-before-bump>
echo "<prev>" > VERSION
git commit -am "Add VERSION file"
git push -u origin release/<prev>
```
