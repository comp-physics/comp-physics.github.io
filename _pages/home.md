---
title: "Home"
layout: default
sitemap: false
permalink: /
---

<div id="homeid" class="col-sm-8 col-10">
## Welcome!

We're the **Computational Physics Group at Georgia Tech**. We build numerical methods, computational models, and <a href="{{ site.url }}{{ site.baseurl }}/software/" target="_blank" rel="noopener noreferrer">open-source software</a> for problems in defense, energy, and medicine — optimized for the world's largest supercomputers.


**Research areas:**
<div class="research-chips" markdown="0">
  <span class="chip">Computational fluid dynamics</span>
  <span class="chip">Shock-laden flow</span>
  <span class="chip">Multi-phase flow</span>
  <span class="chip">Rheological materials</span>
  <span class="chip">Reacting flow</span>
  <span class="chip">High-performance computing</span>
  <span class="chip">Scientific computing</span>
  <span class="chip">Quantum computing</span>
</div>

<div class="highlight-callout">
<span class="highlight-label">2025 Gordon Bell Prize Finalist</span>
In August 2025 we ran the <a href='https://arxiv.org/abs/2505.07392' target='_blank' rel='noopener noreferrer'>largest CFD simulation ever</a> — 1 quadrillion DOFs across 200 trillion grid points on OLCF Frontier and LLNL El Capitan.
</div>

Check out [our papers]({{ site.url }}{{ site.baseurl }}/papers/) to learn more.

</div>
<div id="newsid" class="col-sm-4 col-12" >
<div>
{% for member in site.data.pi %}
<div class="jumbotron">
   <center>
	 <a href="{{site.url}}{{site.baseurl}}/team"><img src="{{site.url}}{{site.baseurl}}/images/teampic/{{ member.photo }}.jpeg" width="75%" style="display:inline-block; margin-left:auto; margin-right:auto; margin-bottom:5px;" alt="Photo of {{ member.name }}"/></a>
   <h5>{{ member.name }}</h5>
   <h6>{{ member.info }}</h6>
   <div style="margin-bottom:5px">
   {% if member.gt %}<a href="{{ member.gt }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s Georgia Tech profile"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %}
   {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank" rel="noopener noreferrer" aria-label="Email {{ member.name }}"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
   {% if member.cv %} <a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s CV"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
   {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s Google Scholar profile"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
   {% if member.github %} <a href="{{ member.github }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s GitHub profile"><i class="fab fa-github-square fa-2x"></i></a> {% endif %}
   {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank" rel="noopener noreferrer" aria-label="View {{ member.name }}'s ResearchGate profile"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
  </div>
  </center>
</div>
{% endfor %}
</div>
</div>
<div class="col-sm-12">

<div class="jumbotron">
<h2>Thinking about joining the group?</h2>

We're always looking for new Ph.D. and undergraduate students who like building models, algorithms, and software.
* Strong coding + numerics background is a plus
* Projects span exascale CFD, cavitation, microfluidics, and more

Visit the <a href="{{ site.url }}{{ site.baseurl }}/vacancies.html">Vacancies</a> page for detailed instructions.<br/>
<br/>
<strong>What strong applicants usually have:</strong> Experience with C/C++/Fortran, numerical methods, and HPC. Familiarity with CFD, continuum mechanics, or scientific computing is helpful but not required.
</div>

<div class="jumbotron">
<h2>Examples of our work</h2>

<div style="padding:2px;background:#000;border-radius:8px;width:75%;height:100%;margin:0 auto;overflow:hidden; text-align: center; justify-content:center">
<iframe src="https://player.vimeo.com/video/1108222522?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" width="100%" height="270" frameborder="0" allow="autoplay" title="Multiphase flow simulation video"></iframe>
</div>
<br/>
<b>Exascale multiphase flow</b>: Scale-resolving simulation of a multi-rocket-booster configuration via <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">MFC</a> and information geometric regularization (IGR), developed with Florian Schäfer. Record-setting at <a href="https://arxiv.org/abs/2505.07392" target="_blank" rel="noopener noreferrer">1 quadrillion DOFs (200T grid points)</a> on <a href="https://www.olcf.ornl.gov/frontier/" target="_blank" rel="noopener noreferrer">OLCF Frontier</a> (viz. via Ph.D. student Ben Wilfong).

<div class="callout-box">
<strong>Interested in using MFC?</strong><br/>
MFC is our flagship open-source solver for compressible multiphase flow at exascale.<br/>
• GPU-optimized for AMD and NVIDIA<br/>
• Validated on rocket, cavitation, and bubbly-flow problems<br/>
• Actively maintained and used on OLCF Frontier and LLNL El Capitan<br/>
<br/>
Visit the <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">MFC website</a> or the <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer">GitHub repo</a> to get started.
</div>

<div style="text-align: center; margin: 20px 0;" markdown="0">
  <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">MFC Website</a>
  <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer" class="btn btn-primary"><i class="fab fa-github"></i> GitHub</a>
  <a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer" class="btn btn-primary"><i class="fab fa-slack"></i> Slack</a>
  {% include mfc_cite_dropdown.html id="Home" external=true %}
</div>

<div class="badge-row">
<a href="https://github.com/MFlowCode/MFC/stargazers" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/stars/MFlowCode/MFC?style=social" alt="GitHub stars"/></a>
<a href="https://github.com/MFlowCode/MFC/releases/latest" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/v/release/MFlowCode/MFC" alt="Latest release"/></a>
</div>

Many of the techniques used in our record-setting rocket simulations are available in MFC, so external users can reproduce similar workflows on their own clusters.

<div style="padding:2px;background:#000;border-radius:8px;width:60%;height:100%;margin:0 auto;overflow:hidden; text-align: center; justify-content: center">
<iframe src="https://player.vimeo.com/video/987402712?autoplay=1&loop=1&autopause=0&muted=1&quality=720p&background=1" frameborder="0" width="100%" height="250" allow="autoplay" title="Blood cell simulation video"></iframe>
</div>
<br/>
<b>Cell-scale flow in microfluidics</b>: High-fidelity spectral boundary integral simulation of blood cells transitioning to chaos. We developed stochastic models enabling microfluidic device design and improved treatment outcomes. Above: a microaneurysm (viz. via student Suzan Manasreh).
</div>

<div class="jumbotron">
<h2>News</h2>
  {% for article in site.data.news limit:10%}
  <p>
    <span class="news-date">{{ article.display_date | default: article.date }}</span>
    <br/>
    {{ article.headline }}
  </p>
  {% endfor %}
  
  <h5><a href="{{ site.url }}{{ site.baseurl }}/allnews.html">... see all News</a></h5>
</div>
</div>
