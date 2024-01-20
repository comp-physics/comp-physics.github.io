---
title: "Team"
layout: gridlay
sitemap: false
permalink: /team/
---

## Team

<!-- <div class="jumbotron"> -->
<center>	
<img src="{{site.url}}{{site.baseurl}}/images/teampic/group.jpg" width="100%" style='  border-radius: 20px;'/>
L to R: Anshuman, Ben, Jesus, Spencer, Anand, Arjun, Sriharsha, Henry, Fatima, Qi. <i>Not Pictured: Ajay, Jack, Yash</i> <br/>
<b>We are always looking for new students to <a href='{{ site.url }}{{ site.baseurl }}/vacancies'>join the team!</a></b>
</center>
<!-- </div> -->

### PI

{% for member in site.data.pi %}
<div class="jumbotron">
<div class="row">
<div class="col-sm-2">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-9 col-xs-12">
  <h5>{{ member.name }}</h5>
  <h6>{{ member.infoshort }}</h6>
   {% if member.gt %}<a href="{{ member.gt }}" target="_blank"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fab fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
</div>
</div>
</div>
{% endfor %}

### Administration


<div class="jumbotron">
<div class="row">
{% for member in site.data.admin %}

<div class="col-sm-2 col-xs-12">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h5>{{ member.name }}</h5>
  <h6><i>{{ member.info }}<br></i></h6>
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %}
</div>

{% endfor %}
</div>
</div>


### Members

<div class="jumbotron">

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2 col-xs-12">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h5>{{ member.name }}</h5>
  <h6><i>{{ member.info }}</i> {% if member.coadvise %}(with {{member.coadvise}}){% endif %}<br></h6>
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.website %} <a href="{{ member.website }}" target="_blank"><i class="fas fa-square-up-right fa-2x"></i></a> {% endif %} {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fab fa-github-square fa-2x"></i></a> {% endif %} {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fab fa-linkedin fa-2x"></i></a> {% endif %} {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
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



### Graduate alumni

<div class="jumbotron">

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2 col-xs-12">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-10 col-xs-12">
  <h5>{{ member.name }}</h5>
  <h6>{{ member.info }}<br></h6>
  <h6><b>Dissertation:</b> <i>{{ member.thesis }}</i> </h6>
  <h6><b>Now at:</b> {{member.now}}</h6>
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

{% if site.data.alumni_bsms %}
### Undergraduate alumni
<div class="jumbotron">
<div class="row">
<div class="col-sm-6 clearfix">
{% for member in site.data.alumni_bsms %}
* {{ member.name }}. <i>{{ member.info }}</i>
{% endfor %}
</div>
</div>
</div>
{% endif %}
