# Docs image: split the single COPY into layers by change frequency

Draft for a ticket in the VCST project. The work lands in `VirtoCommerce/vc-github-actions/update-virtocommerce-docs-versioned`, which owns the Dockerfile, plus a retention policy in Azure. `vc-docs` contains no Dockerfile.

Supersedes the earlier draft. Revised 2026-08-21 after media deduplication was implemented, measured, and verified inside a real container image.

## Problem

The `vcpt/docs` repository in ACR holds 32 tags. A tag is produced on every push to `main` or `release/**`, about twice a day. Nothing is shared between tags, so the registry stores the whole site 32 times over.

The reason is one line. The image is built as:

```dockerfile
FROM nginx:alpine
COPY ./site /usr/share/nginx/html
```

A single `COPY` makes the entire site one layer. Any change anywhere produces a new blob for the whole thing, so consecutive tags share nothing even though almost none of their content differs.

## What has already changed, and why it matters here

Media deduplication has landed in `vc-docs` on branch `feat/published-size-reduction`. It replaces byte-identical binaries across published versions with relative symlinks to one canonical copy, at build-assembly time, before the image is built. It needs no version redeploy and takes effect on the next image build.

Measured on the fully assembled tree: 13,545 file symlinks and 9 directory symlinks, 1.6 GB freed, resulting tree 3.4 GB, remaining duplicates 0.0 B. Verified inside a real `nginx:alpine` image built from the deduplicated tree: 2910 symlinks present after `COPY`, and a symlinked PNG served over HTTP with status 200 and a full 124,066-byte body. `COPY` does not dereference the links and nginx follows them.

That takes a tag from about 2 GB to about 0.6 GB. This ticket is about the remaining factor: that 0.6 GB is still stored 32 times.

Deduplication also satisfies a precondition this work depends on. Layer blobs are only shared when their tars are byte-identical, so the tree must be reproducible. The deduplication chooses its canonical copy as the first path yielded by a sorted walk, and that determinism was confirmed by removing each sort in turn and observing the guard test fail.

## Composition of a deduplicated tag

Registry layer blobs are gzip-compressed, and the compression ratio differs sharply by content type. Measured on 40 random files of each kind from the published tree: HTML compresses about 15.5x, images about 1.1x.

| Content | In the tree | In the registry | Changes when |
| --- | --- | --- | --- |
| nginx base | | ~50 MB | nginx is upgraded |
| Theme assets: fonts, JS, CSS, icons | ~110 MB | ~50 MB | Material is upgraded |
| Shared media pool | 355 MB | ~322 MB | a screenshot is added or changed |
| HTML of frozen versions | ~2.3 GB | ~150 MB | a version is cut |
| HTML of the rolling version | ~310 MB | ~20 MB | every build |
| Non-versioned landing pages | ~1 MB | ~1 MB | a landing page is edited |

The rolling version's HTML is the only part that changes on a normal deploy, and it is about 3% of the compressed tag.

## Proposed change

Replace the single `COPY` with ordered copies, least frequently changed first, following the table above. Order matters for the build cache rather than for registry deduplication: blob identity does not depend on the layers beneath, but rebuilding a step is what makes its bytes drift.

Expected effect. The first four layers are stored once and shared by every tag, about 570 MB in total. Each build adds only its rolling layer, about 20 to 30 MB. Thirty-two tags then cost roughly 1.5 GB instead of the 19 GB they would cost after deduplication alone, and instead of the 64 GB they cost today.

| Scenario | Total in ACR |
| --- | --- |
| Today | ~64 GB |
| Media deduplication only, already implemented | ~19 GB |
| Deduplication plus layers | **~1.5 GB** |

## Cut the layers by content type, not by version

This is the non-obvious requirement, and it comes directly from how deduplication works.

Deduplication points a symlink from one version's tree at a file physically stored under another version. A page under `stable11` can reference an image whose only real copy lives under `stable14`. Splitting layers **by version** would put such a link and its target in different layers. At runtime that is harmless, because the overlay filesystem merges every layer before nginx serves anything. But the layers stop being independent: the `stable11` layer cannot be shipped without the `stable14` layer, and a change to one version's media can invalidate another version's layer.

Splitting **by content type** avoids this entirely. All media lives in one layer regardless of which version references it, so every symlink and its target sit together.

## Determinism, the one thing that can silently defeat this

Byte-identical tars are what make a layer shared rather than re-pushed. Two things still threaten that and both need closing:

1. **File modification times.** `COPY` carries mtimes from the build context, and a fresh CI checkout produces new timestamps on every run, so identical content yields a different digest. Needs mtime normalization, or BuildKit's `COPY --link`.
2. **`git-revision-date-localized`.** The plugin stamps a revision date into every page it regenerates. It does not affect a version that is not rebuilt, so it bears on the rolling layer rather than the frozen ones, but it is worth knowing about when reasoning about why a layer changed.

A cheap acceptance test for both: build the image twice from the same commit with no changes in between, and compare the layer digests. Identical digests mean the mechanism works. Different digests mean something is still drifting and the sharing will not happen in practice.

## Retention, and a question worth deciding

A retention policy that keeps the last N tags per channel and purges the rest, including untagged manifests, remains worthwhile as a safety net. After layers it stops being urgent, because holding 32 tags becomes cheap.

Separately: per `.github/workflows/deploy.yml`, a push to `release/**` builds and pushes an image that is never promoted to production, because it would clobber the non-versioned landing pages baked from `main`. That image exists only as a side effect of publishing a version to `gh-pages` through mike. Worth deciding whether `release/**` needs to push an image at all.

## Out of scope

HTML minification has also landed in `vc-docs`, cutting 58% of HTML bytes on the version being deployed. It is worth about 20 MB of compressed registry bytes per tag, against roughly 280 MB from deduplication, so it is not a lever on the registry bill and is not part of this ticket. Redeploying the four frozen versions to spread minification to them has been dropped: it would cost four sequenced deploys and about 8 GB of undeployable images to save around 90 MB of registry bytes.

## Verification the change should carry

1. Build the image twice from the same commit and compare layer digests. They must match.
2. Confirm the symlink count inside the built image matches the count in the source tree. A count of zero means `COPY` dereferenced the links and the entire saving is gone.
3. Request a symlinked media file over HTTP from the running container and confirm a 200 with a full body.
4. Push two consecutive tags and confirm from the registry that only the rolling layer was uploaded the second time.

The first three are already reproducible against the current single-layer image; the fourth is what proves the layering itself.
