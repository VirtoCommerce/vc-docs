# Versioning

This repository publishes versioned documentation using [mike](https://github.com/jimporter/mike). The current version is tracked in the `VERSION` file at the repo root.

## Versioning scheme

- Versions are stable snapshots that track the Virto Commerce Platform stable releases: `stable11`, `stable12`, `stable14`, `stable15`. The mike title is rendered as `Stable 15`. No minor or patch numbers.
- The version numbers are not contiguous. A docs version exists only for a Platform stable release that shipped documentation changes, so gaps such as the missing `stable13` are expected.
- The version number must match the Platform stable release it documents. Getting it wrong misfiles the whole snapshot, so confirm the number against the Platform release before deploying it.
- Fixes to a released version overwrite the existing snapshot under the same number (no `stable14.1`).
- One version number applies to all seven documentation subsites (`platform/*`, `marketplace/*`, `storefront/*`).

## Branch model

| Branch             | Role                                                                          |
|--------------------|-------------------------------------------------------------------------------|
| `main`             | Current version. `VERSION` on this branch holds the latest version.           |
| `release/<version>`| A previously released version. Editable via PR. One per released version.      |
| `gh-pages`         | Built HTML artifacts. Managed by `mike`. Never edit manually.                  |

The current version has no `release/*` branch. It lives on `main`, and its `release/*` branch is created only when the next version supersedes it. So the number of `release/*` branches is always one less than the number of published versions.

### Branch to version map

| Branch                | Version    | Alias             | URL prefix example                       |
|-----------------------|------------|-------------------|------------------------------------------|
| `main`                | `stable15` | `latest`, default | `/platform/user-guide/latest/`           |
| `release/stable14`    | `stable14` |                   | `/platform/user-guide/stable14/`         |
| `release/stable12`    | `stable12` |                   | `/platform/user-guide/stable12/`         |
| `release/stable11`    | `stable11` | `stable10`        | `/platform/user-guide/stable11/`         |

The deployed version number comes from the `VERSION` file on the branch, never from the branch name. CI subscribes to the `release/**` glob, so renaming a release branch does not affect what gets published. It does, however, fire a push event and redeploy that version.

Two naming schemes predate the current one. Versions were once numbered `1.0`, `2.0`, and `3.0`, which map to `stable11`, `stable12`, and `stable14` respectively. The branches `release/1.0` and `release/2.0` were renamed to `release/stable11` and `release/stable12` on 2026-08-12. No `release/3.0` branch exists: that version was renamed to `stable14` before its release branch was cut.

The oldest version was first renamed to `stable10`, which was the wrong Platform release number. It was corrected to `stable11` on 2026-08-13. `stable10` survives as a redirect alias so that links published under the wrong number keep working. Page URLs under `/stable10/` redirect to their `/stable11/` counterpart. Assets such as images and PDFs do not, because mike emits redirect stubs for pages only.

## Editing docs

Where you open the PR determines which version snapshot gets rebuilt.

### Current version (whatever `main` points to)

The documentation maintainer may push directly to `main`. CI redeploys the current version on every push.

Other contributors must open a PR into `main`. On merge, CI redeploys the same way.

### Older version (e.g. stable12)

Open a PR into the matching release branch (`release/stable12` for `stable12`) with your markdown changes. On merge, CI rebuilds the `stable12` snapshot only. `latest`/`default` remain on the current version.

## Releasing a new version

1. Open a PR titled `Bump docs to stableNN`. The diff **must contain only** a change to `VERSION` (e.g., `stable14` → `stable16`).
2. Review and merge the PR as a **merge commit** (not squash, not rebase). Merge commit is required because automation needs `HEAD^1` of the merge to snapshot the previous version.
3. On merge, automation:
   - Creates `release/<previous>` from `HEAD^1` and pushes it (e.g. `release/stable14`).
   - Appends that branch to `previousVersions` in **context7.json** and commits it to `main`.
   - Deploys the new version as `latest` and `default`.
4. From that point, the new version is current on `main` and the old version is editable on its `release/<previous>` branch.

## Consuming the docs programmatically

External indexers such as Context7 and VirtoOZ should resolve versions from the published site, not from the branch list.

- The authoritative list of published versions is the `versions.json` file that mike writes per subsite, for example **platform/user-guide/versions.json** on `gh-pages`. It names every version and marks which one carries the `latest` alias.
- Do not infer the set of versions from `release/*` branches. The current version has no release branch, so the branch list is always missing the newest entry.
- To index markdown sources instead of built HTML, read `main` for the current version and `release/stable<NN>` for each older one.

### Context7

Context7 parses one branch only, so older versions have to be declared. **context7.json** at the repo root does that:

- `branch` pins the current version to `main`.
- `previousVersions` lists one `{ "branch": "release/stableNN" }` entry per superseded version, newest first.

The bump workflow appends the newly created release branch to `previousVersions` and commits the file to `main`. No manual step is required on release. The schema caps the list at 20 entries. On overflow the workflow drops the oldest entry and emits a build warning.

Pushes that touch only **context7.json** are excluded from the deploy workflow, since the file configures an external indexer and does not affect the built site.

There is a second, unrelated config: **docs/context7.json**. It claims the Context7 website project, which indexes the rendered site rather than this repository. Every non-markdown file in the root **docs** folder is published at the site root, so it is served at `https://docs.virtocommerce.org/context7.json`. Do not merge the two files. The root one describes the repository and its branches. This one describes the website and carries a different `url`.

## What not to do

- **Do not** squash-merge a bump PR. Automation relies on the merge-commit's first parent.
- **Do not** combine a version bump with markdown changes in the same PR. The bump-detection workflow requires the diff to contain only `VERSION`.
- **Do not** push to `gh-pages` manually. `mike` owns that branch.
- **Do not** rename a release branch casually. GitHub fires a push event on the new name, which redeploys that version snapshot.

## Recovery

If the automatic `release/<prev>` creation fails (e.g., the bump PR was accidentally squashed), you can create the branch manually from the commit immediately before the bump:

```bash
git checkout -b release/<prev> <commit-before-bump>
echo "<prev>" > VERSION
git commit -am "Add VERSION file"
git push -u origin release/<prev>
```
