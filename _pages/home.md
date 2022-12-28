---
title: "Home"
layout: default
sitemap: false
permalink: /
---

<div id="homeid" class="col-sm-7 col-xs-12">
## Welcome!
Nano-scale transistors fill warehouse-scale supercomputers, yet their performance still constrains development of the jets that defend us, the medical therapies our lives depend upon, and the renewable energy sources that will power our generation into the next.
The **Computational Physics Group at Georgia Tech CSE** develops computational models and numerical methods to push these applications forward.
We accompany our methods with algorithms crafted to make efficient use of the latest computer architectures, including AMD GPUs, Arm CPUs, FPGAs, and even quantum computers.
We develop <a href="{{ site.url }}{{ site.baseurl }}/software/" target="_blank">open-source software</a> for these methods that scales to the world's largest supercomputers. 
Check out the rest of this website to learn more and visit [this page]({{ site.url }}{{ site.baseurl }}/vacancies.html) if you're interested in joining our group.

## Examples of our work

Bubble cavitation can ablate kidney stones, but wreaks havoc on marine propellers.
We developed a <a href="{{ site.url }}{{ site.baseurl }}/papers/charalampopoulos-RSA-21.pdf" target="_blank">sub-grid method</a> for simulating this phenomenon.
It uses a hybrid quadrature method of moments scheme to close the governing equations at low cost.
<a href="https://mflowcode.github.io/" target="_blank">MFC</a>, our open-source multi-phase flow solver, demonstrates this method.
MFC is also capable of fully-resolved multi-phase fluid dynamics via the diffuse-interface method.

<iframe src="https://player.vimeo.com/video/455688517?autoplay=1&loop=1&autopause=0&muted=1&quality=360p&background=1"  style="border-style:solid;border-radius:5px;" frameborder="0" width="100%" allow="autoplay"></iframe>

The spectral boundary integral method leads to <a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-PRF-18.pdf" target="_blank">high-fidelity prediction and analysis</a> of blood cells transitioning to chaos in a microfluidic device (above).
We developed a <a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-PRE-19.pdf" target="_blank">low-order model</a> for the cell-scale flow, important for guiding microfluidic device design and improving treatment outcomes.
</div>
<div id="newsid" class="col-sm-5 col-xs-12" >
<div>
{% for member in site.data.pi %}
<div class="jumbotron">
   <center>
<!-- <a href="{{site.url}}{{site.baseurl}}/team"><img src="{{site.url}}{{site.baseurl}}/images/teampic/{{ member.photo }}" width="50%" style="block:inline; margin-left:auto; margin-right:auto; margin-bottom:5px;"/></a> -->
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

<div class="jumbotron">
<h2>News</h2>
  {% for article in site.data.news limit:7%}
  <b>{{ article.date }}</b>
    {{ article.headline }}
  {% endfor %}
  
  <h5><a href="{{ site.url }}{{ site.baseurl }}/allnews.html">... see all News</a></h5>
</div>
</div>




