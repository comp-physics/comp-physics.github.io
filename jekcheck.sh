bundle exec jekyll build; bundle exec htmlproofer ./_site --ignore-status-codes 999,403,301,302 --ignore-urls https://f.vimeocdn.com
# --enforce-https=false 
# --ignore-missing-alt=true 
# --ignore-missing-alt true

# bundle exec jekyll build; bundle exec htmlproofer ./_site --alt-ignore '/.*/' --http_status_ignore='999,403,301,302' --assume-extension

# bundle exec jekyll build; bundle exec htmlproofer --help

# bundle exec jekyll build; bundle exec htmlproofer ./_site --alt-ignore '/.*/' --http_status_ignore='999,403,301,302' --assume-extension
