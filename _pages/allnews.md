---
title: "News"
layout: textlay
sitemap: false
permalink: /allnews.html
---

## News

<div class="jumbotron">
{% for article in site.data.news %}
<div style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1);">
  <p style="margin-bottom: 8px;"><strong style="color: #c0995e;">{{ article.date }}</strong></p>
  <p style="margin: 0;">{{ article.headline }}</p>
</div>
{% endfor %}
</div>
