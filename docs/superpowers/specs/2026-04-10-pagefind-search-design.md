# Pagefind Search — Design

## Goal

Add site-wide search to the comp-physics Jekyll site using [Pagefind](https://pagefind.app/). Search is triggered from a navbar icon that opens a modal overlay with live results.

## Why Pagefind

- Runs as a post-build step against `_site/`, so it needs no Jekyll plugin and no Ruby changes.
- Produces a static index; no runtime service.
- Ships a drop-in UI that handles input, debouncing, result rendering, and keyboard nav.
- Handles the papers page well — each jekyll-scholar bibliography entry becomes searchable text inside a single page.

Alternatives considered and rejected: Simple-Jekyll-Search (weaker ranking, UI we'd have to build), Lunr.js (older, clunkier), Algolia DocSearch (external dependency, overkill).

## Architecture

### Build pipeline

1. Jekyll builds `_site/` as today.
2. New post-build step: `npx pagefind --site _site`. This scans the built HTML, generates a static index under `_site/pagefind/`, and copies the Pagefind UI bundle in alongside it.
3. GH Actions workflow (`.github/workflows/deploy.yml`) adds a Node setup step and the pagefind invocation between the existing "Build site" and "Upload artifact" steps.

### Frontend

1. `_includes/head.html` loads `/pagefind/pagefind-ui.js` and `/pagefind/pagefind-ui.css`.
2. `_includes/header.html` gets a search icon button (FontAwesome `fa-search`, matching existing nav icon style) at the right side of the navbar. The button has `data-bs-toggle="modal"` targeting the search modal.
3. New `_includes/search-modal.html` — a Bootstrap modal containing `<div id="search"></div>`. Included once from `_layouts/default.html` so every page that uses the default layout gets it.
4. Small inline script in `search-modal.html` initializes `PagefindUI({ element: "#search", showImages: false, resetStyles: false })` on the modal's first `shown.bs.modal` event (lazy init so the library isn't touched until the user opens search).

### Indexing control

- Wrap main page content in `_layouts/default.html` (and any sibling top-level layouts that don't extend default, e.g. `nonav.html`, `homelay.html`) with a `<main data-pagefind-body>` element. Content outside that element — nav, footer, sidebar — is excluded from the index.
- Add `data-pagefind-ignore` to the jekyll-scholar bibliography detail layout (`_layouts/bibtemplate.html`). Each paper has its own detail page; without this exclusion every paper would match twice (once from `/papers`, once from its detail page).
- The `/papers` page itself is indexed, so individual bib entries become searchable.

### Local dev

- Add `pagefind` as a devDependency in the existing `package.json`.
- Document the full build as `bundle exec jekyll build && npx pagefind --site _site` in `README.md` (or add a script to `package.json` / `Rakefile` — final choice during implementation).
- `jekyll serve` alone will NOT have a working search index. Local search testing requires the full build. This is acceptable: search isn't typically something that's iterated on during content editing.

## Scope / Out of Scope

**In scope:**
- Pagefind index generated in CI.
- Navbar search button → modal UI with live results.
- Sensible indexing boundaries (main content only, no duplicate bibliography pages).

**Out of scope:**
- Custom search result styling beyond whatever minor CSS is needed to make Pagefind's default UI match the site's dark navbar theme.
- Faceted search, filters, or category scoping.
- Analytics on search queries.
- Serving search index during `jekyll serve` local dev.

## Success Criteria

1. CI builds the site without errors; `_site/pagefind/` exists in the deployed artifact.
2. Clicking the navbar search icon opens a modal with a working input.
3. Typing a query (e.g., "multiphase", a known paper title word) returns relevant results that link to the correct pages.
4. Nav, footer, and sidebar text do not appear in results.
5. A single paper does not appear twice in results (once from `/papers`, once from its detail page).
6. No regression in existing Jekyll build time beyond the added Node + pagefind steps (~20s total in CI).

## Risks

- **Pagefind UI styling clash:** Pagefind ships opinionated default CSS. May need minor overrides to avoid clashing with Bootstrap. Mitigation: `resetStyles: false` and scoped override CSS if needed.
- **Layout coverage gaps:** If some pages use a layout that doesn't wrap content in `data-pagefind-body`, those pages get no indexed content. Mitigation: audit layouts during implementation, add the wrapper to each top-level one.
- **Jekyll-scholar detail pages:** If the `data-pagefind-ignore` placement is wrong, duplicates will show up. Mitigation: verify by searching for a known paper after first deploy.
