# Computational Physics at GT

This website is modified from my template, [here](https://github.com/sbryngelson/academic-website-template).

## Local build

```bash
bundle install          # once
bundle exec jekyll build
```

Or `bundle exec jekyll serve` to preview locally with live rebuilds.

## Git hooks

Hooks live in `.githooks/` so they are version controlled. Point git at them once per clone:

```bash
git config core.hooksPath .githooks
```

`pre-commit` checks that every `file = {...}` reference in `cv/ref.bib` matches a file
tracked under `papers/` **exactly, including case**. macOS filesystems are
case-insensitive, so a mismatched reference renders fine locally and then silently
drops that paper's PDF button on Linux CI. Bypass with `git commit --no-verify`.
