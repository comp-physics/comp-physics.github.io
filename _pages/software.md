---
title: "MFC"
layout: gridlay
sitemap: false
permalink: /software/
description: "MFC is an open-source exascale multiphase flow solver. 2025 Gordon Bell Prize Finalist. Scales to 200+ trillion grid points on 43,000+ GPUs."
og_image: "https://mflowcode.github.io/res/banner.png"
---

<style>
img{
  border-radius: 8px;
}
iframe:not([allowfullscreen]) {
  width: 100%;
  max-width: 175px;
  display: inline;
  vertical-align:middle;
}
.col-md-3 {
  margin:0;
  padding:0;
  margin-top:10px;
  margin-bottom:10px;
  overflow:hidden;
  text-align:center;
  display: table-cell;
  height: auto;
  float: none;
  background:white;
  border-radius:8px;
}
</style>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": "MFC",
  "alternateName": "Multi-Component Flow Code",
  "description": "Open-source exascale multiphase flow solver for compressible flows. 2025 Gordon Bell Prize Finalist. Scales to 200+ trillion grid points on 43,000+ GPUs.",
  "url": "https://mflowcode.github.io",
  "codeRepository": "https://github.com/MFlowCode/MFC",
  "license": "https://opensource.org/licenses/MIT",
  "programmingLanguage": ["Fortran", "Python"],
  "operatingSystem": "Linux",
  "applicationCategory": "Computational Fluid Dynamics",
  "author": {
    "@type": "ResearchOrganization",
    "name": "Computational Physics Group at Georgia Tech",
    "url": "https://comp-physics.group"
  },
  "maintainer": {
    "@type": "Person",
    "name": "Spencer H. Bryngelson",
    "url": "https://comp-physics.group",
    "affiliation": {
      "@type": "Organization",
      "name": "Georgia Institute of Technology"
    }
  },
  "award": "2025 ACM Gordon Bell Prize Finalist"
}
</script>

## MFC

### Who is MFC for?

• Researchers and engineers running **compressible multiphase** or **shock-dominated** flows<br/>
• HPC practitioners targeting **GPU supercomputers** (Frontier, El Capitan, JUPITER, etc.)<br/>
• Students who want to see _real_ exascale CFD code and contribute to it

### How to get started with MFC

1. **Read the quickstart** on the <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">MFC website</a>.
2. **Run a sample case** from the GitHub repo on a workstation or small cluster.
3. **Join the Slack** (<a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer">link here</a>) to ask questions and discuss use cases.
4. If you're at GT, **email Spencer** (<a href="mailto:shb@gatech.edu">shb@gatech.edu</a>) to discuss using MFC in your research or course projects.

<div style="text-align: center; margin: 20px 0;" markdown="0">
  <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">🌐 MFC Website</a>
  <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer" class="btn btn-primary"><i class="fab fa-github"></i> GitHub</a>
  <a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer" class="btn btn-primary"><i class="fab fa-slack"></i> Slack</a>
  {% include mfc_cite_dropdown.html %}
</div>

<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<center>
<a href="https://mflowcode.github.io" target="_blank" rel="noopener noreferrer">
<img src="/images/software/mfc-logo3.png" width="70%" alt="MFC (MFlowCode) logo"/>
</a>
</center>
MFC has a <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">website</a> and <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer">open source GitHub repo.</a>
It simulates <b>compressible multiphase flows</b> at <b>exascale</b> (tens of thousands of NVIDIA or AMD GPUs) on machines like <a href="https://www.olcf.ornl.gov/frontier/" target="_blank" rel="noopener noreferrer">OLCF Frontier</a> and <a href="https://asc.llnl.gov/exascale/el-capitan" target="_blank" rel="noopener noreferrer">LLNL El Capitan</a>.

<div style="margin-top: 15px; display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
<a href="https://github.com/MFlowCode/MFC/stargazers" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/stars/MFlowCode/MFC?style=social" alt="GitHub stars"/></a>
<a href="https://github.com/MFlowCode/MFC/releases/latest" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/v/release/MFlowCode/MFC" alt="Latest release"/></a>
<a href="https://github.com/MFlowCode/MFC/graphs/contributors" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/contributors/MFlowCode/MFC" alt="Contributors"/></a>
</div>

<div style="margin-top: 20px; text-align: center;">
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
<iframe src="https://www.youtube.com/embed/NSn3OVF8N4I?autoplay=1&mute=1&loop=1&playlist=NSn3OVF8N4I&rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="MFC: Mach 12 Starship Super Heavy simulation"></iframe>
</div>
<p style="margin-top: 8px; font-size: 0.9em; color: #999;">Mach 12 Starship Super Heavy booster simulation &mdash; <a href="https://www.youtube.com/@MFCode" target="_blank" rel="noopener noreferrer">more videos on YouTube</a></p>
</div>

<h4 style="margin-top: 25px;">Simulation gallery</h4>
<p>See featured simulations on the <a href="https://mflowcode.github.io/#simulations" target="_blank" rel="noopener noreferrer">MFC website</a>.</p>

<h4 style="margin-top: 25px;">Contributors</h4>
<div id="mfc-contributors" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
<p style="color: #888;"><i>Loading contributors...</i></p>
</div>
<script>
(function() {
  fetch("https://api.github.com/repos/MFlowCode/MFC/contributors?per_page=100")
    .then(function(r) { return r.json(); })
    .then(function(contributors) {
      var el = document.getElementById("mfc-contributors");
      el.innerHTML = contributors.filter(function(c) { return c.type === "User"; }).map(function(c) {
        return '<a href="' + c.html_url + '" target="_blank" rel="noopener noreferrer" title="' + c.login + ' (' + c.contributions + ' contributions)">' +
          '<img src="' + c.avatar_url + '&s=48" alt="' + c.login + '" width="48" height="48" style="border-radius:50%; border:2px solid #eee;" loading="lazy"/>' +
        '</a>';
      }).join("");
    })
    .catch(function() {
      document.getElementById("mfc-contributors").innerHTML =
        '<p>Could not load contributors. <a href="https://github.com/MFlowCode/MFC/graphs/contributors" target="_blank" rel="noopener noreferrer">View them on GitHub</a>.</p>';
    });
})();
</script>

</div>
</div>

<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<h4>Other open-source projects</h4>
• <strong><a href="https://github.com/pyrometheus/pyrometheus" target="_blank" rel="noopener noreferrer">Pyrometheus</a></strong> – symbolic thermochemistry and autodiff for reacting flows<br/>
• <strong><a href="https://github.com/comp-physics/QBMMlib" target="_blank" rel="noopener noreferrer">QBMMlib</a></strong> – quadrature-based moment methods for multiphase flows<br/>
• <strong><a href="https://github.com/comp-physics/RBC3D" target="_blank" rel="noopener noreferrer">RBC3D</a></strong> – detailed microcirculation and cell-resolved blood-flow simulation<br/>
<br/>
👉 See the <a href="https://github.com/comp-physics" target="_blank" rel="noopener noreferrer">group GitHub page</a> for these and more.
</div>
</div>

<div class="jumbotron" id="cite">
<div class="col-md-12 col-sm-12">
<h4>How to cite MFC</h4>
If you use MFC in your research, please cite our papers:

<p><strong>MFC 5.0 (recommended for recent work):</strong><br/>
B. Wilfong, H. Le Berre, A. Radhakrishnan, et al. "MFC 5.0: An exascale many-physics flow solver." <i>Computer Physics Communications</i> 322 (2026): 110055.<br/>
<a href="https://doi.org/10.1016/j.cpc.2026.110055" target="_blank" rel="noopener noreferrer">DOI: 10.1016/j.cpc.2026.110055</a>
</p>

<p><strong>MFC 3.0 (original release):</strong><br/>
S. H. Bryngelson, K. Schmidmayer, V. Coralic, J. Meng, K. Maeda, and T. Colonius. "MFC: An open-source high-order multi-component, multi-phase, and multi-scale compressible flow solver." <i>Computer Physics Communications</i> 266 (2021): 108029.<br/>
<a href="https://doi.org/10.1016/j.cpc.2021.108029" target="_blank" rel="noopener noreferrer">DOI: 10.1016/j.cpc.2021.108029</a>
</p>

<p><strong>BibTeX for MFC 5.0:</strong></p>
<pre style="background-color: #1f2020; padding: 15px; border-radius: 8px; overflow-x: auto;"><code>@article{wilfong26,
  title={MFC 5.0: An exascale many-physics flow solver},
  author={Wilfong, Benjamin and {Le Berre}, Henry and Radhakrishnan, Anand and Gupta, Ansh and Vickers, Daniel J. and Vaca-Revelo, Diego and Adam, Dimitrios and Yu, Haocheng and Lee, Hyeoksu and Chreim, Jose Rodolfo and {Carcana Barbosa}, Mirelys and Zhang, Yanjun and Cisneros-Garibay, Esteban and Gnanaskandan, Aswin and {Rodriguez Jr.}, Mauro and Budiardja, Reuben D. and Abbott, Stephen and Colonius, Tim and Bryngelson, Spencer H.},
  journal={Computer Physics Communications},
  volume={322},
  pages={110055},
  year={2026},
  doi={10.1016/j.cpc.2026.110055}
}</code></pre>
</div>
</div>
