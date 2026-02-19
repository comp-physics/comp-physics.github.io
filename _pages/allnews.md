---
title: "News"
layout: textlay
sitemap: false
permalink: /allnews.html
---

## News

<div class="jumbotron">
{% assign current_year = "" %}
{% for article in site.data.news %}
{% assign article_year = article.date_iso | default: article.date | date: "%Y" %}
{% if article_year != current_year %}
{% if current_year != "" %}
</div>
{% endif %}
<h3 style="color: #c0995e; margin-top: 30px; margin-bottom: 15px;">{{ article_year }}</h3>
<div>
{% assign current_year = article_year %}
{% endif %}
<div style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1);">
<p style="margin-bottom: 8px;">
<strong style="color: #c0995e;">{{ article.display_date | default: article.date }}</strong>
</p>
<p style="margin: 0;">{{ article.headline }}</p>
</div>
{% endfor %}
</div>
</div>
