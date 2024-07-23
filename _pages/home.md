---
title: "Home"
layout: default
sitemap: false
permalink: /
---

<div id="homeid" class="col-sm-7 col-xs-12">
## Welcome!
Nano-scale transistors fill warehouse-scale supercomputers, yet their performance still constrains development of the jets that defend us, the medical therapies our lives depend upon, and the renewable energy sources that will power our generation into the next.
The **Computational Physics Group at Georgia Tech** develops computational models and numerical methods to push these applications forward.
We accompany our methods with algorithms crafted to make efficient use of the latest exascale machines and computer architectures, including AMD GPUs, Arm/RISC CPUs, and quantum computers.
We develop <a href="{{ site.url }}{{ site.baseurl }}/software/" target="_blank">open-source software</a> for these methods that scales to the world's largest supercomputers. 
Check out the rest of this website to learn more.
</div>
<div id="newsid" class="col-sm-5 col-xs-12" >
<div>
{% for member in site.data.pi %}
<div class="jumbotron">
   <center>
	 <a href="{{site.url}}{{site.baseurl}}/team"><img src="{{site.url}}{{site.baseurl}}/images/teampic/{{ member.photo }}" width="55%" style="block:inline; margin-left:auto; margin-right:auto; margin-bottom:5px;"/></a>
   <h5>PI: {{ member.name }}</h5>
   <h6>{{ member.info }}</h6>
   <div style="margin-bottom:5px">
   {% if member.gt %}<a href="{{ member.gt }}" target="_blank"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %}
   {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
   {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
   {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
   {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fab fa-github-square fa-2x"></i></a> {% endif %}
   {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
  </div>
  </center>
</div>
{% endfor %}
</div>
</div>
<div class="col-sm-12">

<div class="jumbotron">
__Openings? Visit [this page]({{ site.url }}{{ site.baseurl }}/vacancies.html) if you're interested in joining our group.__
</div>

<div class="jumbotron">
<h2>Examples of our work</h2>


<div style="padding:2px;background:#fff;webkit-border-radius:10px;-moz-border-radius:10px;border-radius:10px;width:60%;height=100%;margin:0 auto;overflow:hidden; text-align: center; justify-content:center">
<iframe src="https://player.vimeo.com/video/905208069?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" width="100%" height="200" frameborder="0" allow="autoplay"></iframe>
</div>
Bubble cavitation and droplet shedding are fundamental multiphase flow problems at the core of naval hydrodynamics, aerospace propulsion, and more.
We developed a <a href="{{ site.url }}{{ site.baseurl }}/papers/charalampopoulos-RSA-21.pdf" target="_blank">sub-grid method</a> for simulating these phenomena.
<a href="https://mflowcode.github.io/" target="_blank">MFC</a>, our open-source exascale-capable multi-phase flow solver, demonstrates such scale-resolving simulation of a shock-droplet interaction in the above video (via Ph.D. student Ben Wilfong).

<div style="padding:2px;background:#000;webkit-border-radius:10px;-moz-border-radius:10px;border-radius:10px;width:60%;height:100%;margin:0 auto;overflow:hidden; text-align: center; justify-content: center">
<iframe src="https://player.vimeo.com/video/987402712?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" frameborder="0" width="100%" height="250" allow="autoplay"></iframe>
</div>
The spectral boundary integral method leads to <a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-PRF-18.pdf" target="_blank">high-fidelity prediction and analysis</a> of blood cells transitioning to chaos in a microfluidic device. This method of simulation provides resolution of strong cell membrane deformation with scant computational resources.
We developed a <a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-PRE-19.pdf" target="_blank">stochastic model</a> for the cell-scale flow, enabling microfluidic device design and improving treatment outcomes.
The video above shows a microaneurysm (simulated by Suzan Manasreh).
</div>

<div class="jumbotron">
<h2>News</h2>
  {% for article in site.data.news limit:10%}
  <b>{{ article.date }}</b>
    {{ article.headline }}
  {% endfor %}
  
  <h5><a href="{{ site.url }}{{ site.baseurl }}/allnews.html">... see all News</a></h5>
</div>
</div>
