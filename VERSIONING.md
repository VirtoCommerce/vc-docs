# Versioning

This repository publishes versioned documentation using [mike](https://github.com/jimporter/mike). Major version numbers are tracked in the `VERSION` file at the repo root.

## Versioning scheme

- Only major versions: `1.0`, `2.0`, `3.0`. No minor or patch numbers.
- Fixes to a released major overwrite the existing snapshot under the same number (no `X.0.1`).
- One version number applies to all seven documentation subsites (`platform/*`, `marketplace/*`, `storefront/*`).

## Branch model

| Branch        | Role                                                                 |
|---------------|----------------------------------------------------------------------|
| `main`        | Current major. `VERSION` on this branch is the latest major.         |
| `release/X.0` | A previously released major. Editable via PR. One per released major.|
| `gh-pages`    | Built HTML artifacts. Managed by `mike`. Never edit manually.        |

## Editing docs

### Current version (whatever `main` points to)
Open a PR into `main` with your markdown changes. On merge, CI redeploys that version and keeps the `latest`/`default` aliases on it.

### Older version (e.g. 2.0)
Open a PR into `release/2.0` with your markdown changes. On merge, CI rebuilds the `2.0` snapshot only. `latest`/`default` remain on the current major.

## Releasing a new major version

1. Open a PR titled `Bump docs to X.0`. The diff **must contain only** a change to `VERSION` (e.g., `3.0` → `4.0`).
2. Review and merge the PR as a **merge commit** (not squash, not rebase). Merge commit is required because automation needs `HEAD^1` of the merge to snapshot the previous version.
3. On merge, automation:
   - Creates `release/<previous>` from `HEAD^1` and pushes it.
   - Deploys the new major as `latest` and `default`.
4. From that point, the new major is current on `main` and the old major is editable on its `release/<previous>` branch.

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
