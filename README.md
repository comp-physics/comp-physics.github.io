# Computational Physics at GT

This website is modified from my template, [here](https://github.com/sbryngelson/academic-website-template).

## Local build

```bash
bundle install   # once
npm install      # once
npm run build    # jekyll build + pagefind index
```

For rapid content iteration (no search index), `bundle exec jekyll serve` is still fine — the search modal will open but show no results until a full `npm run build` is run.
