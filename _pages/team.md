---
title: "Team"
layout: gridlay
sitemap: false
permalink: /team/
---

## Team

<center>	
<img src="{{site.url}}{{site.baseurl}}/images/teampic/group-photo-fall2024.jpeg" width="100%" style='  border-radius: 20px;' alt="Group photo of Computational Physics Group members"/>
L to R: Tianyi, Lian, Jesus, Henry, Spencer, Melody, Ben, Haocheng, Max, Jack, Dimitri, Brian. <br/><i>Not Pictured: Anand, Ansh</i> <br/>
<b>We are always looking for new students to <a href='{{ site.url }}{{ site.baseurl }}/vacancies'>join the team!</a></b>
</center>

<!-- ### PI -->

{% for member in site.data.pi %}
<div class="jumbotron">
<div class="row">
<h3>{{ member.name }}</h3>
<div class="col-sm-3">
<center>
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}.jpeg" width="90%" style="max-width:250px" alt="Photo of {{ member.name }}"/>
</center>
</div>
<div class="col-sm-9 col-xs-12">
  <h6>{{ member.infoshort }}</h6>
   {% if member.gt %}<a href="{{ member.gt }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s Georgia Tech profile"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank" rel="noopener noreferrer" aria-label="Email {{ member.name }}"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s CV"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s Google Scholar profile"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s GitHub profile"><i class="fab fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s ResearchGate profile"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
</div>
</div>
</div>
{% endfor %}


### Members

<div class="jumbotron">

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2 col-xs-12">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}.jpeg" width="100%" style="max-width:250px" alt="Photo of {{ member.name }}"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h5>{{ member.name }}</h5>
  <h6><i>{{ member.info }}</i> {% if member.coadvise %}(with {{member.coadvise}}){% endif %}<br></h6>
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank" rel="noopener noreferrer" aria-label="Email {{ member.name }}"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.website %} <a href="{{ member.website }}" target="_blank" rel="noopener noreferrer" aria-label="Visit {{ member.name }}'s website"><i class="fas fa-square-up-right fa-2x"></i></a> {% endif %} {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s CV"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s Google Scholar profile"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s GitHub profile"><i class="fab fa-github-square fa-2x"></i></a> {% endif %} {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s LinkedIn profile"><i class="fab fa-linkedin fa-2x"></i></a> {% endif %} {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s ResearchGate profile"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

</div>

### Ph.D graduates
<div class="jumbotron">
<div class="row">
<div class="col-sm-12 clearfix">
{% for member in site.data.alumni_phd %}
* {{ member.name }}. <i>{{ member.info }}</i> <br> <b>Dissertation:</b> {{member.dissertation}}
{% endfor %}
</div>
</div>
</div>

### Undergraduate alumni
<div class="jumbotron">
<div class="row">
<div class="col-sm-12 clearfix">
{% for member in site.data.alumni_bsms %}
* {{ member.name }}. <i>{{ member.info }}</i>
{% endfor %}
</div>
</div>
</div>
