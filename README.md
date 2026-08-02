# Computational Physics at GT

This website is modified from my template, [here](https://github.com/sbryngelson/academic-website-template).

## Local build

```bash
bundle install          # once
bundle exec jekyll build
```

Or `bundle exec jekyll serve` to preview locally with live rebuilds.

## Checks

`./script/check-bib-refs` verifies every `file = {...}` in `cv/ref.bib` names a real
file in `papers/`, matching exactly including case. CI runs it before each build.

Case matters because macOS filesystems are case-insensitive and Linux ones are not:
a mismatched reference renders fine locally and then silently drops that paper's PDF
button on the deployed site.
