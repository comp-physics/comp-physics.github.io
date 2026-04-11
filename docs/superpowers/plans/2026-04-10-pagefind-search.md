# Pagefind Search Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add site-wide search to the Jekyll site via Pagefind, triggered from a navbar icon that opens a modal with live results.

**Architecture:** Pagefind runs as a post-build step against `_site/`, generating a static index and UI bundle under `_site/pagefind/`. Frontend loads the Pagefind UI on demand inside a Bootstrap modal when the navbar search button is clicked. Indexing is scoped to a `data-pagefind-body` wrapper inside `_layouts/default.html`, so nav/footer/sidebar content is excluded automatically.

**Tech Stack:** Jekyll 3.x, Bootstrap 5, FontAwesome 6, Pagefind (Node CLI, used only in CI and local build).

**Test strategy note:** This is a static site with no automated test suite. "Testing" each task means a successful `bundle exec jekyll build` and, where UI is involved, a manual verification against the locally built `_site/`. Commits are small and reversible.

---

## File Structure

**Create:**
- `_includes/search-modal.html` — Bootstrap modal containing the Pagefind mount point and a lazy-init script.
- `docs/superpowers/plans/2026-04-10-pagefind-search.md` — this plan (already exists).

**Modify:**
- `_config.yml` — add `pagefind` to the `exclude` list so `node_modules/` isn't published.
- `package.json` — add `pagefind` devDependency and a `build` script.
- `_includes/head.html` — load `/pagefind/pagefind-ui.css`.
- `_includes/header.html` — add search icon button at the right of the navbar.
- `_layouts/default.html` — wrap main-content div with `data-pagefind-body`, include the search modal, load `/pagefind/pagefind-ui.js` at end of body.
- `.gitignore` — ensure `node_modules/` is ignored.
- `.github/workflows/deploy.yml` — add Node setup + `npx pagefind --site _site` step between the Jekyll build and the artifact upload.
- `README.md` — one-line note on how to build locally with search.

**Not modified:**
- `_layouts/nonav.html` — this serves `pear`-related pages (via `headpear.html`/`footerpear.html`) which are out of scope for main site search.
- `_layouts/bibtemplate.html` — no bibliography detail pages are currently generated (no `_layouts/bibtex.html` exists), so there's no duplicate-hit problem to solve.

---

## Task 1: Add pagefind to package.json and gitignore

**Files:**
- Modify: `package.json`
- Modify: `.gitignore`

- [ ] **Step 1: Read current package.json and .gitignore**

Run:
```bash
cat package.json .gitignore
```

- [ ] **Step 2: Add pagefind devDependency and build script**

Replace `package.json` with:
```json
{
  "dependencies": {
    "@popperjs/core": "^2.11.8",
    "bootstrap": "^5.3.3",
    "jquery": "^3.7.1"
  },
  "devDependencies": {
    "pagefind": "^1.1.0"
  },
  "scripts": {
    "build": "bundle exec jekyll build && npx pagefind --site _site"
  }
}
```

- [ ] **Step 3: Ensure node_modules is gitignored**

Read `.gitignore`. If it does not already contain `node_modules`, append a single line:
```
node_modules
```

- [ ] **Step 4: Verify npm can resolve pagefind**

Run:
```bash
npm install
```
Expected: installs pagefind into `node_modules/` with no errors. A `package-lock.json` is created.

- [ ] **Step 5: Commit**

```bash
git add package.json .gitignore package-lock.json
git commit -m "add pagefind devDependency and build script"
```

---

## Task 2: Exclude node_modules from Jekyll build

**Files:**
- Modify: `_config.yml`

Pagefind's `node_modules/` directory must not be copied into `_site/` — without this, Jekyll will copy thousands of files and the pagefind step will try to index its own source.

- [ ] **Step 1: Read the existing exclude list in `_config.yml`**

The `exclude:` block is near the bottom of the file.

- [ ] **Step 2: Append `node_modules` and `package.json`/`package-lock.json` to exclude**

Change the `exclude:` block to:
```yaml
exclude:
  - Gemfile
  - Gemfile.lock
  - update_boostrap.sh
  - tags
  - Rakefile
  - LICENSE
  - .DS_Store
  - jekcheck.sh
  - node_modules
  - package.json
  - package-lock.json
  - docs
```

Note: `docs/` is also added so the `docs/superpowers/` plans and specs aren't published to the live site.

- [ ] **Step 3: Build Jekyll and verify node_modules is not in \_site**

Run:
```bash
bundle exec jekyll build
ls _site/ | grep -E "node_modules|package" || echo "clean"
```
Expected: `clean`

- [ ] **Step 4: Commit**

```bash
git add _config.yml
git commit -m "exclude node_modules and plan docs from Jekyll build"
```

---

## Task 3: Wrap main content with data-pagefind-body in default layout

**Files:**
- Modify: `_layouts/default.html`

- [ ] **Step 1: Read current default.html**

The current body contains:
```html
<div class="container-fluid" id="main-content">
  <div class="row">
    {{ content }}
  </div>
</div>
```

- [ ] **Step 2: Add data-pagefind-body attribute**

Replace the main-content div with:
```html
<div class="container-fluid" id="main-content" data-pagefind-body>
  <div class="row">
    {{ content }}
  </div>
</div>
```

Only this single attribute change. Nothing else in the file should move.

- [ ] **Step 3: Verify Jekyll still builds**

Run:
```bash
bundle exec jekyll build
grep -l "data-pagefind-body" _site/index.html
```
Expected: `_site/index.html`

- [ ] **Step 4: Commit**

```bash
git add _layouts/default.html
git commit -m "scope search indexing to main content with data-pagefind-body"
```

---

## Task 4: Create the search modal include

**Files:**
- Create: `_includes/search-modal.html`

- [ ] **Step 1: Create the modal include**

Write `_includes/search-modal.html`:
```html
<div class="modal fade" id="searchModal" tabindex="-1" aria-labelledby="searchModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="searchModalLabel">Search</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div id="search"></div>
      </div>
    </div>
  </div>
</div>

<script>
  (function () {
    var initialized = false;
    var modalEl = document.getElementById('searchModal');
    if (!modalEl) return;
    modalEl.addEventListener('shown.bs.modal', function () {
      if (initialized) {
        var input = modalEl.querySelector('.pagefind-ui__search-input');
        if (input) input.focus();
        return;
      }
      if (typeof PagefindUI === 'undefined') {
        console.warn('PagefindUI not loaded');
        return;
      }
      new PagefindUI({
        element: '#search',
        showImages: false,
        resetStyles: false,
        showSubResults: true
      });
      initialized = true;
      setTimeout(function () {
        var input = modalEl.querySelector('.pagefind-ui__search-input');
        if (input) input.focus();
      }, 50);
    });
  })();
</script>
```

- [ ] **Step 2: Verify Jekyll still builds**

Run:
```bash
bundle exec jekyll build
```
Expected: build succeeds (the include is not yet referenced, so no visible change).

- [ ] **Step 3: Commit**

```bash
git add _includes/search-modal.html
git commit -m "add search modal include with lazy PagefindUI init"
```

---

## Task 5: Load Pagefind UI CSS in head

**Files:**
- Modify: `_includes/head.html`

- [ ] **Step 1: Read head.html**

Find the existing stylesheet block near the top:
```html
<link rel="stylesheet" href="{{ "/assets/main.css" | relative_url }}">
```

- [ ] **Step 2: Add Pagefind UI CSS link after main.css**

Insert one line immediately after the `main.css` link:
```html
<link rel="stylesheet" href="{{ site.url }}{{ site.baseurl }}/pagefind/pagefind-ui.css">
```

Resulting block:
```html
<link rel="stylesheet" href="{{ "/assets/main.css" | relative_url }}">
<link rel="stylesheet" href="{{ site.url }}{{ site.baseurl }}/pagefind/pagefind-ui.css">
```

Note: this URL returns 404 during local `jekyll serve` (no pagefind run), but the site will render fine — browsers ignore missing stylesheets.

- [ ] **Step 3: Verify Jekyll still builds**

Run:
```bash
bundle exec jekyll build
grep "pagefind-ui.css" _site/index.html
```
Expected: matching line in the built HTML.

- [ ] **Step 4: Commit**

```bash
git add _includes/head.html
git commit -m "load Pagefind UI stylesheet in head"
```

---

## Task 6: Add search button to navbar

**Files:**
- Modify: `_includes/header.html`

- [ ] **Step 1: Read header.html**

Find the closing `</ul>` of the navbar-nav, just before `</div>` of `navbar-collapse`.

- [ ] **Step 2: Add a right-aligned search button after the nav list**

The current block ends with:
```html
        </ul>
    </div>
    </div>
</nav>
```

Replace that block with:
```html
        </ul>
        <button
          type="button"
          class="btn btn-outline-light btn-sm ms-auto"
          data-bs-toggle="modal"
          data-bs-target="#searchModal"
          aria-label="Search site">
          <i class="fa fa-search"></i>
        </button>
    </div>
    </div>
</nav>
```

This places the button to the right of the nav items on wide screens (via `ms-auto`) and below them on collapsed screens (Bootstrap default).

- [ ] **Step 3: Verify Jekyll still builds**

Run:
```bash
bundle exec jekyll build
grep "searchModal" _site/index.html
```
Expected: matching `data-bs-target="#searchModal"` line in built HTML.

- [ ] **Step 4: Commit**

```bash
git add _includes/header.html
git commit -m "add navbar search button"
```

---

## Task 7: Include search modal and Pagefind UI script in default layout

**Files:**
- Modify: `_layouts/default.html`

- [ ] **Step 1: Read current default.html**

The current body ends with:
```html
    {% include footer.html %}

  </body>
```

- [ ] **Step 2: Include the modal and the Pagefind UI JS before closing body**

Replace that block with:
```html
    {% include footer.html %}

    {% include search-modal.html %}

    <script src="{{ site.url }}{{ site.baseurl }}/pagefind/pagefind-ui.js"></script>

  </body>
```

Order matters: the `<script>` tag for `pagefind-ui.js` must come BEFORE the init script that lives inside `search-modal.html`. Wait — `search-modal.html` registers a listener on a DOM event (`shown.bs.modal`) that doesn't fire until the user opens the modal, so by the time it runs, `PagefindUI` will already be defined regardless of tag order. The order above is fine.

- [ ] **Step 3: Verify Jekyll still builds**

Run:
```bash
bundle exec jekyll build
grep -c "searchModal\|pagefind-ui.js" _site/index.html
```
Expected: at least 2 matching lines.

- [ ] **Step 4: Commit**

```bash
git add _layouts/default.html
git commit -m "include search modal and Pagefind UI script in default layout"
```

---

## Task 8: Run pagefind locally and verify search works

**Files:** None (verification only).

- [ ] **Step 1: Full build with pagefind**

Run:
```bash
npm run build
```
Expected: Jekyll build succeeds, then pagefind runs. Output lists a non-zero number of pages indexed. Example:
```
[Pagefind] Running Pagefind v1.x
[Pagefind] Indexed N pages
```

- [ ] **Step 2: Verify the pagefind directory was created in \_site**

Run:
```bash
ls _site/pagefind/ | head
```
Expected: `pagefind-ui.js`, `pagefind-ui.css`, `pagefind.js`, a `fragment/` dir, an `index/` dir.

- [ ] **Step 3: Serve and manually test search in a browser**

Run:
```bash
python3 -m http.server 8000 --directory _site
```

Open http://localhost:8000/ in a browser. Manually verify:
1. Search icon appears at the right of the navbar.
2. Clicking the icon opens a Bootstrap modal with an input field.
3. Typing a known term (e.g. "multiphase", "MFC", or the name of a paper author) returns at least one relevant result.
4. Clicking a result navigates to the correct page.
5. The modal's results do NOT contain obvious navbar/footer text (e.g. "Georgia Tech" from the footer should not be the top hit for an unrelated query).

Stop the server with Ctrl-C when done.

- [ ] **Step 4: No commit needed**

If any check fails, stop and debug before continuing. Likely causes:
- Results missing entirely → `data-pagefind-body` wrapper missing or in the wrong layout.
- Too many irrelevant results → the wrapper is in the wrong place (e.g. wrapping the whole page).
- Modal opens but empty → `pagefind-ui.js` not loaded; check Network tab in devtools.

---

## Task 9: Add Node setup and Pagefind step to GH Actions

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Read current workflow**

The current `build` job runs Ruby setup → `jekyll build` → `upload-pages-artifact`.

- [ ] **Step 2: Add Node setup and pagefind run between build and upload**

Replace the `build` job steps (everything under `steps:` in the `build` job) with:
```yaml
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.2.4'
          bundler-cache: true

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Configure Pages
        uses: actions/configure-pages@v5

      - name: Build site
        run: bundle exec jekyll build
        env:
          JEKYLL_ENV: production

      - name: Build search index
        run: npx -y pagefind@1.1.0 --site _site

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: _site
```

Notes on the change:
- Added `Set up Node` step.
- Added `Build search index` step using `npx -y pagefind@1.1.0` — pinned to avoid surprise version bumps, `-y` auto-confirms the install prompt.
- Step order: Jekyll build → pagefind → upload.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "run Pagefind after Jekyll build in CI"
```

---

## Task 10: Document the local build in README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Read current README**

Run:
```bash
cat README.md
```

- [ ] **Step 2: Append a brief build section**

Append the following to `README.md`:
```markdown

## Local build

```bash
bundle install   # once
npm install      # once
npm run build    # jekyll build + pagefind index
```

For rapid content iteration (no search index), `bundle exec jekyll serve` is still fine — the search modal will open but show no results until a full `npm run build` is run.
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "document local build with search index"
```

---

## Task 11: Push and verify the deployed site

**Files:** None (verification only).

- [ ] **Step 1: Push to main**

```bash
git push origin main
```

- [ ] **Step 2: Watch the GH Actions run**

Run:
```bash
gh run watch
```
Expected: `build` and `deploy` jobs succeed. The "Build search index" step shows pagefind indexing output.

- [ ] **Step 3: Verify on live site**

Open https://comp-physics.group/ (or whichever URL the CNAME points to). Manually check:
1. Search icon visible in navbar.
2. Clicking it opens the modal.
3. Typing a known query returns results.
4. Clicking a result navigates correctly.

- [ ] **Step 4: If anything fails in production but worked locally**

Most likely cause: a path-related issue with `baseurl`. The site's `_config.yml` has `baseurl: ""` so `/pagefind/...` should work. If there's a problem, check devtools Network tab for 404s on pagefind assets and adjust the paths in `head.html` / `default.html` accordingly.

---

## Self-review notes

- All spec sections (build pipeline, frontend, indexing control, local dev) are covered by explicit tasks.
- The spec mentioned `data-pagefind-ignore` on bibliography detail pages, but investigation showed no `_layouts/bibtex.html` exists and no `/bibliography/` pages are generated, so that step was dropped (noted in File Structure section).
- Type/name consistency: `#searchModal` / `#search` / `PagefindUI` / `searchModal` are used consistently across tasks 4, 6, and 7.
- No placeholders, no "similar to task N" references, all code is shown in full.
