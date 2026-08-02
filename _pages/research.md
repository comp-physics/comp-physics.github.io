---
title: "Research"
layout: gridlay
sitemap: true
permalink: /research/
---

## Research

Our group builds numerical methods, computational models, and open-source software for problems in defense, energy, and medicine — optimized for the world's largest supercomputers. See <a href="{{ site.baseurl }}/papers">our papers</a> for the full picture.

<div class="research-grid">

{% for theme in site.data.research.themes %}
<div class="research-card">
{% if theme.thumb %}<img src="{{ site.baseurl }}{{ theme.thumb }}" class="research-thumb" alt="{{ theme.alt | default: theme.title }}" loading="lazy">{% endif %}
<div class="research-body">
<h4 class="research-title" id="theme-{{ theme.title | slugify }}">{{ theme.title }}</h4>
<p class="research-desc">{{ theme.summary }}</p>
<ul class="research-bullets">
{% for b in theme.bullets %}
<li>{{ b }}</li>
{% endfor %}
</ul>
<div class="research-footer" markdown="0">
{% if theme.papers %}<span class="research-pubs">{% include icon.html name="file-lines" %} {% for key in theme.papers %}<a href="{{ site.baseurl }}/papers/#{{ key }}">{{ key }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</span>{% endif %}
{% if theme.links %}<div class="research-links">{% for link in theme.links %}<a href="{{ link.url }}" target="_blank" rel="noopener noreferrer" class="research-link">{% include icon.html name="github" %} {{ link.text }}</a>{% endfor %}</div>{% endif %}
</div>
</div>
</div>
{% endfor %}

</div>
