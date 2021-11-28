bundle exec jekyll build; bundle exec htmlproofer ./_site --alt-ignore '/.*/' --http_status_ignore='999,403,301,302' --assume-extension
