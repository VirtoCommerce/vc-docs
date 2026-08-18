# Versioning

This repository publishes versioned documentation using [mike](https://github.com/jimporter/mike). The current version is tracked in the `VERSION` file at the repo root.

## Versioning scheme

There are two kinds of version. The rolling version documents the Edge release channel and lives on `main`. Stable versions are frozen snapshots that track Virto Commerce Platform stable releases, for example `stable14`, `stable15`.

- The rolling version occupies the `latest` slug. Its **VERSION** file reads `latest` and is never changed. In the version selector it is titled Edge.
- Stable version numbers are not contiguous. A docs version exists only for a Platform stable release that shipped documentation changes, so gaps such as the missing `stable13` are expected.
- The version-selector title is derived from the slug. `stable15` becomes Stable 15, and `latest` becomes Edge.
- Fixes to a released version overwrite the existing snapshot under the same number. There is no `stable14.1`.
- One version applies to all seven documentation subsites (`platform/*`, `marketplace/*`, `storefront/*`).

## Branch model

| Branch              | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| `main`              | The rolling version. Published as Edge at the `latest` URL.          |
| `release/<version>` | A released stable version. Editable via PR. One per released version. |
| `gh-pages`          | Built HTML artifacts. Managed by mike. Never edit manually.          |

### Branch to version map

| Branch             | Version    | Title     | URL prefix example               |
|--------------------|------------|-----------|----------------------------------|
| `main`             | `latest`   | Edge      | `/platform/user-guide/latest/`   |
| `release/stable15` | `stable15` | Stable 15 | `/platform/user-guide/stable15/` |
| `release/stable14` | `stable14` | Stable 14 | `/platform/user-guide/stable14/` |
| `release/stable12` | `stable12` | Stable 12 | `/platform/user-guide/stable12/` |
| `release/stable11` | `stable11` | Stable 11 | `/platform/user-guide/stable11/` |

The deployed version comes from the **VERSION** file on the branch, never from the branch name. CI subscribes to the `release/**` glob, so renaming a release branch does not affect what gets published. It does, however, fire a push event and redeploy that version.

`stable10` survives as a redirect alias on `release/stable11`, because the oldest version was briefly published under that wrong number. Page URLs under `/stable10/` redirect to their `/stable11/` counterpart. Assets such as images and PDFs do not, because mike emits redirect stubs for pages only.

## Content and infrastructure

A change is either content or infrastructure, and the two follow opposite rules.

Content is everything under a guide's **docs** folder. It belongs to exactly one version and is never cherry-picked between branches.

Everything else is infrastructure: the theme, **overrides**, build scripts, workflows. Infrastructure is not versioned. A fix to it is cherry-picked to every live release branch, otherwise older versions drift into building differently from the current one.

Two things sit inside the three content sections but are infrastructure: each guide's **mkdocs.yml** and the section-level **mkdocs.yml**. Restoring a version's content must not touch them.

One thing looks like infrastructure but is version specific: `redirect_maps`. It encodes where pages live, so a map written for one version can shadow real pages in another. Check it whenever content is restored.

## Editing docs

Where you open the PR determines which version snapshot gets rebuilt.

### The rolling version

The documentation maintainer may push directly to `main`. Other contributors open a PR into `main`. CI redeploys Edge on every push.

Anything documenting a feature that has not shipped in a stable release belongs here.

### A released version, for example stable14

Open a PR into the matching release branch. On merge, CI rebuilds that snapshot only. Edge is unaffected.

Use this only for corrections to what that release actually shipped. New feature documentation belongs on `main`.

## Releasing a new version

A release branch is cut at the boundary commit, which is the last commit belonging to the release. The boundary is the commit immediately preceding the first commit of the next sprint cycle. Sprint markers appear in commit subjects, for example `Sprint 26-12 updates`.

To cut a release:

1. Find the boundary commit on `main`.
2. Run the Cut a release branch workflow with the version slug and the boundary SHA.
3. Wait for the release deploy to finish before triggering any other deploy.

The workflow creates `release/<version>` at the boundary, sets its **VERSION**, pushes it, and registers the branch in **context7.json**.

`main` is not touched. It keeps its `latest` slug and keeps moving.

### Why the boundary matters

Until 2026-08 the release branch was cut automatically from `HEAD^1` of a version bump. Because a bump happens when the next version starts rather than when the current one ships, every published snapshot carried a full cycle of the following release's content. Cutting at the boundary is what prevents that.

## Deploy order

Several branches may need to deploy after a single change. The `concurrency` group in **.github/workflows/deploy.yml** is keyed on the ref, while every branch writes to the same `gh-pages`, so simultaneous runs interleave.

Deploy release branches first and `main` last. The production image is baked from `main` only, so the final `main` run is what carries every corrected snapshot into production.

## Consuming the docs programmatically

External indexers such as Context7 and VirtoOZ should resolve versions from the published site, not from the branch list.

- The authoritative list of published versions is the `versions.json` file that mike writes per subsite, for example **platform/user-guide/versions.json** on `gh-pages`. It names every version, including the rolling one, which appears under the `latest` slug.
- Do not infer the set of versions from `release/*` branches. The rolling version has no release branch, so the branch list never names it.
- To index markdown sources instead of built HTML, read `main` for Edge and `release/stable<NN>` for each stable version.

### Context7

Context7 parses one branch only, so older versions have to be declared. **context7.json** at the repo root does that:

- `branch` pins the rolling version to `main`.
- `previousVersions` lists one `{ "branch": "release/stableNN" }` entry per superseded version, newest first.

The Cut a release branch workflow appends the newly created release branch to `previousVersions` and commits the file to `main`. No manual step is required on release. The schema caps the list at 20 entries. On overflow the workflow drops the oldest entry and emits a build warning.

Pushes that touch only **context7.json** are excluded from the deploy workflow, since the file configures an external indexer and does not affect the built site.

There is a second, unrelated config: **docs/context7.json**. It claims the Context7 website project, which indexes the rendered site rather than this repository. Every non-markdown file in the root **docs** folder is published at the site root, so it is served at `https://docs.virtocommerce.org/context7.json`. Do not merge the two files. The root one describes the repository and its branches. This one describes the website and carries a different `url`.

## What not to do

- **Do not** change **VERSION** on `main`. The rolling version stays on the `latest` slug permanently.
- **Do not** cut a release branch from the tip of `main`. Use the boundary commit, or the snapshot picks up the next release's content.
- **Do not** cherry-pick content between branches. Only infrastructure moves across versions.
- **Do not** restore a version's content with a path that includes **mkdocs.yml**. Those files are infrastructure and belong at the branch tip.
- **Do not** push to `gh-pages` manually. `mike` owns that branch.
- **Do not** rename a release branch casually. GitHub fires a push event on the new name, which redeploys that version snapshot.
- **Do not** deploy `main` before the release branches when several changed. The production image is baked from `main`.

## Recovery

If the Cut a release branch workflow fails partway, the branch may exist without its **VERSION** commit or without its Context7 entry. Both are safe to complete by hand:

```bash
git checkout release/<version>
echo "<version>" > VERSION
git commit -am "Set VERSION to <version>"
git push
```

Then add `{"branch": "release/<version>"}` to the head of `previousVersions` in **context7.json** on `main`.

If the branch was cut at the wrong commit, delete it and rerun the workflow with the correct boundary. Deleting and recreating fires a redeploy of that version, which is the intended way to correct it.
