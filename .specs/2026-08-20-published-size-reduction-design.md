# Published documentation size reduction

Date: 2026-08-20. Revised 2026-08-21 after review. Status: awaiting review.

## Problem

The published documentation costs real money and real deploy time. Two symptoms, one root cause.

The `vcpt/docs` repository in ACR holds 32 tags at roughly 2 GB each, about 64 GB in total, growing by about 4 GB per day at two deploys per day. The `gh-pages` branch, which every CI run checks out in full at `fetch-depth: 0`, holds 5086 MB across 27,396 files.

The root cause is that a published snapshot stores far more bytes than it has content. Two forms of redundancy dominate, and neither is inherent to versioning.

## Evidence

All figures are measured on `origin/gh-pages` as of 2026-08-21, read with `git ls-tree -r -l`, which reports exact blob sizes without a checkout. Uniqueness is counted by blob OID, so identical content is identified exactly rather than estimated.

### Composition of the published tree

| Category | Size | Files |
| --- | --- | --- |
| HTML | 3039 MB | 7905 |
| Images | 1690 MB | 14222 |
| Fonts | 241 MB | 2485 |
| JS | 77 MB | 1568 |
| JSON | 22 MB | 52 |
| CSS | 8 MB | 1008 |
| Other | 10 MB | 156 |
| **Total** | **5086 MB** | **27396** |

Five versions are published per guide, across seven guides:

| Version | HTML | Media | Other | Total |
| --- | --- | --- | --- | --- |
| latest (Edge) | 744 MB | 342 MB | 73 MB | 1160 MB |
| stable15 | 680 MB | 344 MB | 73 MB | 1097 MB |
| stable14 | 561 MB | 334 MB | 72 MB | 967 MB |
| stable12 | 533 MB | 336 MB | 72 MB | 942 MB |
| stable11 | 519 MB | 328 MB | 72 MB | 919 MB |

### Redundancy inside a page

Byte breakdown of a representative page, `platform/developer-guide/index.html`:

| Region | Size | Share |
| --- | --- | --- |
| Whole page | 550 KB | 100% |
| Primary navigation sidebar | 484 KB | 88% |
| Article content | 17 KB | 3% |

The navigation tree is emitted into every page of a guide, at roughly 520 bytes per link. Material's own 9.5 templates are whitespace-stripped and carry no Jinja comments, but `overrides/partials/nav-item.html` is a fork of a pre-9.x template that keeps both, and the deployed HTML contains the comment text.

The `minify` plugin is declared in the root config and in all seven guide configs, in every case as a bare `- minify` with no options. Its default is `minify_html: false`, so it currently does nothing. Measured on a random sample of 60 published pages, `htmlmin` with `remove_comments` cuts 20.5 MB to 8.8 MB, a **57% reduction**, at 2.33 s per 60 pages.

### Redundancy between versions

| Category | Total | Unique by blob | Duplicate |
| --- | --- | --- | --- |
| Images | 1690 MB | 355 MB | **1334 MB (79%)** |
| Fonts | 241 MB | 7 MB | 235 MB (97%) |
| JS | 77 MB | 2 MB | 75 MB (97%) |
| CSS | 8 MB | 0 MB | 8 MB (99%) |
| HTML | 3039 MB | 3039 MB | 0 MB |
| JSON | 22 MB | 22 MB | 0 MB |
| **Total** | **5086 MB** | **3428 MB** | **1659 MB (33%)** |

HTML and search indexes are legitimately unique per version. Everything else is not.

Theme assets are already handled in the image: `deduplicate_assets` in **versioned-build-cicd.py** replaces every nested `assets/` folder with a symlink to the root one, guarded by a subset check so a version built against a different Material release keeps its own content-hashed stylesheets. That guard was added in `4765be4421` after unstyled non-latest versions shipped. The fonts, JS, and CSS duplicates above therefore describe `gh-pages`, which mike owns, not the image.

Media is not handled anywhere. Nothing in the build deduplicates files under `media/`.

### The registry stores compressed layers, which inverts the priorities

This is the finding that determines the order of work. OCI layer blobs are gzip-compressed, so the composition of a 2 GB ACR tag is not the composition of the 5086 MB tree. Measured on 40 random files of each kind from a published snapshot:

| Kind | Raw | gzip | Ratio |
| --- | --- | --- | --- |
| HTML | 21.8 MB | 1.4 MB | **15.5x** |
| Images | 2.1 MB | 2.0 MB | **1.1x** |

Applying those ratios reconstructs the observed tag size and shows where its bytes actually are:

| Content | In the tree | In the registry |
| --- | --- | --- |
| Media | 1685 MB | ~1532 MB |
| HTML | 3039 MB | ~196 MB |
| Fonts, JS, CSS, JSON after the existing assets pass | ~30 MB | ~30 MB |
| nginx base image | | ~50 MB |
| **Total** | | **~1.8 GB** |

That matches the roughly 2 GB per tag observed in Azure, which is the check that the model is right rather than merely plausible.

The consequence is that HTML dominates the tree and media dominates the image. Minification is the larger lever on checkout time and disk; media deduplication is the larger lever on the Azure bill, by an order of magnitude.

## Decisions

1. **Binary deduplication goes first.** It removes about 1334 MB of duplicate media, roughly 1213 MB of registry bytes, taking a tag from about 2 GB to about 0.6 GB. It runs at image assembly time on the already-assembled tree, so it needs **no redeploy of any version** and no change to any release branch. It is the largest win at the lowest risk.
2. **Deduplication uses symlinks to one canonical copy, not a content-addressed pool with rewritten references.** Both remove the same bytes. Symlinks require no change to any HTML, so a version's pages keep pointing at their own paths and historical fidelity is preserved by construction. It also follows the idiom `deduplicate_assets` already established, and nginx following symlinks inside the site root is already load-bearing in production.
3. **Deduplication is deterministic.** The canonical copy is the lexicographically first path from a sorted walk. A non-deterministic choice would make the resulting tar differ between builds, defeating the Docker layer work that follows.
4. **Deduplication runs after `deduplicate_assets`.** `os.walk` does not descend into symlinked directories, so running second means the already-symlinked nested `assets/` trees are skipped instead of being hashed once per version.
5. **Minification is enabled through plugin options, not a new tool,** and it lands on `main` first. The plugin is already installed and declared; only `minify_html: true` is added.
6. **Minification reaches a frozen version only when that version is redeployed.** mike deploys one version per run, so enabling the option on `main` shrinks the `latest` tree and nothing else. Redeploying the four stable versions is a separate, deferred stage, because it costs more than it returns in the registry: 57% of 744 MB on `latest` is about 27 MB of registry bytes, and all five versions together are only about 112 MB, against about 1213 MB from media deduplication.
7. **The frozen-version redeploy is blocked on ACR retention.** A push to `release/**` builds and pushes a roughly 2 GB image that, per **.github/workflows/deploy.yml**, is never promoted to prod because it would clobber the landing pages baked from `main`. Four redeploys therefore add about 8 GB of undeployable images before returning anything. Retention must exist first.
8. **`cache_safe` stays off.** It renames `extra_css` and `extra_javascript` files under a content hash. Renaming asset files has previously broken deduplication in this repository and filled the deploy disk. Cache busting for Cloudflare is already handled by **overrides/hooks/extra_css_cache_bust.py**, which appends a query string and leaves file names alone.
9. **`minify_js` and `minify_css` stay off.** The candidates are Material's already-minified bundles plus a handful of repository scripts, so the yield is negligible while `jsmin` on **version-redirect.js** and **scroll-menu.js** is a live risk.
10. **The optimization lives in a module both build scripts import, not in either script.** **versioned-build-cicd.py** deduplicates theme assets and **versioned-build.py** does not, and never has: its nine steps end at an HTTP server with no optimization pass anywhere. Copying the new function into both files would lock that divergence in permanently, so shared code moves to **build_optimize.py**. The dash in **versioned-build-cicd.py** makes it an invalid module name, which is why sharing needs a new file.
11. **stable11 and stable12 stay published.** They are inside scope for optimization and are not retired, by explicit decision, notwithstanding their support dates.
12. **Every claim is measured, not asserted.** The size harness lands first and can read a git ref directly, so a baseline is taken from the real published tree rather than from a working copy that may be stale.

## Redeploying a frozen version is safe, and this was verified

The deferred redeploy stage was checked against the repository rather than assumed, because two objections to it turned out to be false.

**The toolchain is pinned identically on every branch.** `requirements-docs.txt` and `versioned-build-cicd.py` are byte-identical between `main`, `release/stable14`, and `release/stable15`, blobs `70bc2716` and `77667407`. On `release/stable11` and `release/stable12` the requirements blob is `b31a3e7f`, which pins the same mkdocs-material 9.5.27, mkdocs 1.6.1, mike 2.2.0, and htmlmin2 0.1.13. Everything that determines rendering is the same everywhere, so a rebuild today reproduces the same HTML modulo the minification being introduced.

**No branch has unpublished content.** Comparing each release branch tip with the last mike deploy of its version in `gh-pages`: stable11 2026-08-13 against 2026-08-13, stable14 2026-08-18 against 2026-08-18, stable15 2026-08-18 against 2026-08-18, and stable12's deploy of 2026-08-06 is newer than its branch tip of 2026-06-18. A rebuild republishes the same content and changes only the markup.

**Redeploy is the sanctioned mechanism.** `VERSIONING.md:12` states that fixes to a released version overwrite the existing snapshot under the same number, and line 133 describes redeploy as the intended way to correct a version.

Two residual differences survive and set the scope of the port:

- `release/stable11` and `release/stable12` carry an older **versioned-build-cicd.py**, 12 KB and 20 KB against 22 KB on `main`. Porting minification to those two also means porting the build script and **build_optimize.py**, which is a code change, not a config change. `release/stable14` and `release/stable15` need only the `mkdocs.yml` edit.
- `release/stable11` and `release/stable12` pin `mkdocs-awesome-pages-plugin==2.10.1` alongside `awesome-nav`. Two navigation plugins are active there, so page paths before and after a rebuild must be compared for those two versions specifically.

## Out of scope

Three adjacent pieces of work belong in their own plans. None blocks this one.

**Docker layer stratification and ACR retention.** 99.7% of an image is content that does not change between builds, yet it is rewritten into a fresh layer twice a day. Stratifying layers by change frequency would let 32 tags share one frozen layer, roughly an 8x reduction with no documentation change. This lands in `VirtoCommerce/vc-github-actions`, which owns the Dockerfile, plus a retention policy in Azure. `vc-docs` contains no Dockerfile. Decision 7 makes retention a prerequisite for the deferred redeploy stage.

**`navigation.prune` and the Material template resync.** Minification removes the whitespace and comments around the duplicated navigation tree; it does not remove the tree. `navigation.prune` does, and installed Material 9.5.27 supports it. Reaching it means resyncing forked partials against current stock templates and re-applying the megamenu and tabs customizations. **overrides/assets/scripts/scroll-menu.js** relies on the full tree being present in the DOM, so pruning changes its behavior and the deep-navigation visibility bug it exists to fix may return.

**Animated GIF conversion.** The heaviest media files are GIFs of 3 MB to 17 MB. Converting them to webm or mp4 yields 20x to 50x, is the only measure that shrinks the source tree as well, and lands squarely on the media bytes that dominate the image. It changes the authoring format, since a `<video>` element replaces an image reference, so it needs its own content decision. This is the natural follow-up to decision 1.

## Expected result

| Measure | Tree | Registry, per tag |
| --- | --- | --- |
| Now | 5086 MB | ~2 GB |
| After media deduplication, no redeploys | 5086 MB | **~0.6 GB** |
| After minification on `main` | 4662 MB | ~0.58 GB |
| After the deferred redeploy of all four stable versions | 3354 MB | ~0.5 GB |

The tree column is what CI checks out on every run. The registry column is what Azure bills. They are optimized by different measures, which is why the two are reported separately.

## Risks

**Minification alters every byte of every page it touches.** Safe for content, but it invalidates any Docker layer holding that version, once. Cheaper to land before the layer work than after.

**Whitespace collapse can join adjacent inline words.** `htmlmin` preserves `pre` and `textarea`, and the plugin is widely used with Material, but this repository leans on inline markup for abbreviation tooltips and bold UI labels. Verification compares the rendered text of every page in a before and after tree, with whitespace normalized, and requires exact equality on every path.

**Symlinks must survive the image build.** `COPY` preserves symlinks and nginx follows them within the root, and the existing `assets/` symlinks prove both in production. Two failure modes remain untested by anything in this repository: a Docker step that dereferences links, which would silently erase the entire saving, and one that drops them, which would produce media 404s. The image is built by an external action pinned to `@master`, so its behavior can change without a change here.

**Directory symlinks are invisible to a naive file walk.** `deduplicate_assets` creates symlinks to directories, which appear in `dirnames` rather than `filenames`. Any verification that only inspects files will report zero symlinks on an assets-optimized tree and will never check whether those links are broken or escape the tree.

**Redeploy grows `gh-pages` history irreversibly.** mike commits a full version tree rather than a patch. Four versions across seven guides is 28 commits, and the history keeps both the un-minified and the minified copy forever. The working tree shrinks while the repository grows, which partly offsets the checkout-time gain that motivates the redeploy.

**Redeploys must be serialized.** `concurrency` in the deploy workflow is keyed on the ref while every branch writes the same `gh-pages`, so parallel release deploys conflict.
