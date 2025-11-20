---
title: "Home"
layout: default
sitemap: false
permalink: /
---

<div id="homeid" class="col-sm-8 col-xs-10">
## Welcome!
Nano-scale transistors fill warehouse-scale supercomputers, yet their performance still constrains development of the jets that defend us, the medical therapies our lives depend upon, and the energy sources that will power our generation into the next.

We're the **Computational Physics Group at Georgia Tech**.
We develop computational models and numerical methods for these applications.
Our methods buttress algorithms crafted for efficient use of the latest supercomputers and their architectures.
We develop <a href="{{ site.url }}{{ site.baseurl }}/software/" target="_blank">open-source software</a> for these methods that scales to the world's largest supercomputers. 

In August 2025 our group conducted the <a href='https://arxiv.org/abs/2505.07392' target='_blank'>largest-ever CFD simulation</a> at 200T grid points (1 quadrillion degrees of freedom) on OLCF Frontier and LLNL El Capitan without loss of accuracy.
This work was a 2025 <a href='https://en.wikipedia.org/wiki/Gordon_Bell_Prize' target='_blank'>Gordon Bell Prize</a> finalist.

Check out [our papers]({{ site.url }}{{ site.baseurl }}/papers/) to learn more.

</div>
<div id="newsid" class="col-sm-4 col-xs-12" >
<div>
{% for member in site.data.pi %}
<div class="jumbotron">
   <center>
	 <a href="{{site.url}}{{site.baseurl}}/team"><img src="{{site.url}}{{site.baseurl}}/images/teampic/{{ member.photo }}.jpeg" width="75%" style="block:inline; margin-left:auto; margin-right:auto; margin-bottom:5px;"/></a>
   <h5>{{ member.name }}</h5>
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

<div style="padding:2px;background:#000;webkit-border-radius:10px;-moz-border-radius:10px;border-radius:10px;width:75%;height=100%;margin:0 auto;overflow:hidden; text-align: center; justify-content:center">
<iframe src="https://player.vimeo.com/video/1108222522?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" width="100%" height="270" frameborder="0" allow="autoplay"></iframe>
</div>
Multiphase flow problems at the core of biological, energy, naval, and aerodynamic problems.
We developed an implementation of the IGR technique with Florian Schäfer for simulating these flows.
In August 2025 we set the record for the <a href="https://arxiv.org/abs/2505.07392" target="_blank">largest CFD simulation at 1 quadrillion degrees of freedom (200T grid points)</a> for simulating these phenomena, using the entire <a href="https://www.olcf.ornl.gov/frontier/" target="_blank">OLCF Frontier</a> system.
<a href="https://mflowcode.github.io/" target="_blank">MFC</a>, an open-source solver we maintain, demonstrates such scale-resolving simulation of a multi-rocket-booster configuration above (viz. via Ph.D. student Ben Wilfong).

<div style="padding:2px;background:#000;webkit-border-radius:10px;-moz-border-radius:10px;border-radius:10px;width:60%;height:100%;margin:0 auto;overflow:hidden; text-align: center; justify-content: center">
<iframe src="https://player.vimeo.com/video/987402712?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" frameborder="0" width="100%" height="250" allow="autoplay"></iframe>
</div>
The spectral boundary integral method leads to high-fidelity prediction and analysis of blood cells transitioning to chaos in a microfluidic device.
This method of simulation provides resolution of strong cell membrane deformation with scant computational resources.
We developed a stochastic model for the cell-scale flow, enabling microfluidic device design and improving treatment outcomes.
The video above shows a microaneurysm (viz. via student Suzan Manasreh).
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
