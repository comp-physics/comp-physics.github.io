---
title: "Software"
layout: gridlay
sitemap: false
permalink: /software/
---

<style>
img{
  border-radius: 10px;
}
iframe {
  width: 175px;
  display: inline;
  vertical-align:middle;
}
.col-md-3 {
  margin:0;
  padding:0;
  margin-top:10px;
  margin-bottom:10px;
  display:block;
  overflow:hidden;
  text-align:center;
  display: table-cell;
  height: auto;
  float: none;
  background:white;
  border-radius:20px;
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

## Software

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
  <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;">🌐 MFC Website</a>
  <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;"><i class="fab fa-github"></i> GitHub</a>
  <a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;"><i class="fab fa-slack"></i> Slack</a>
  {% include mfc_cite_dropdown.html %}
</div>

<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<center> 
<h4>
<a href="https://github.com/comp-physics" target="_blank" rel="noopener noreferrer" aria-label="Visit Computational Physics Group GitHub page"><i class="fab fa-github-square fa-1x"></i> Group GitHub page</a>
</h4>
</center>
The group writes and maintains a large amount of open source software, all available under the MIT license.
Please visit the above GitHub page to view it.
</div>
</div>


<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<center>
<a href="https://mflowcode.github.io" target="_blank" rel="noopener noreferrer">
<img src="/images/software/mfc-logo3.png" width="70%" alt="MFC (MFlowCode) logo"/>
</a>
</center>
MFC has a <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">website</a> and <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer">open source GitHub repo.</a>
It simulates <b>compressible multiphase flows</b> at <b>exascale</b> (tens of thousands of NVIDIA or AMD GPUs) via machines like Oak Ridge Summit and <a href="https://www.olcf.ornl.gov/frontier/" target="_blank" rel="noopener noreferrer">Frontier</a>.
It has many other useful features, so check out those links if it seems interesting.

<div style="margin-top: 15px; display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
<a href="https://github.com/MFlowCode/MFC/stargazers" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/stars/MFlowCode/MFC?style=social" alt="GitHub stars"/></a>
<a href="https://github.com/MFlowCode/MFC/releases/latest" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/v/release/MFlowCode/MFC" alt="Latest release"/></a>
<a href="https://github.com/MFlowCode/MFC/graphs/contributors" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/contributors/MFlowCode/MFC" alt="Contributors"/></a>
</div>

<h4 style="margin-top: 25px;">Simulation gallery</h4>
<p style="margin-bottom: 15px;">Featured simulations powered by MFC, pulled live from the <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">MFC website</a>.</p>
<div id="mfc-sims-gallery" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px;">
<p style="color: #888;"><i>Loading simulations...</i></p>
</div>

<script>
(function() {
  var MFC = "https://mflowcode.github.io";
  fetch(MFC + "/simulations.json")
    .then(function(r) { return r.json(); })
    .then(function(sims) {
      var gallery = document.getElementById("mfc-sims-gallery");
      gallery.innerHTML = sims.map(function(s) {
        var icon = s.source.indexOf("youtube.com") !== -1
          ? "fa-brands fa-youtube" : "fa-solid fa-arrow-up-right-from-square";
        return '<div style="background:#1f2020; border-radius:8px; overflow:hidden;">' +
          '<a href="' + s.source + '" target="_blank" rel="noopener noreferrer" style="display:block;">' +
            '<img src="' + MFC + '/' + s.image + '" alt="' + s.name + '" style="width:100%; display:block; background:#fff;" loading="lazy"/>' +
          '</a>' +
          '<div style="padding:10px;">' +
            '<div style="font-weight:600; margin-bottom:6px;">' +
              '<a href="' + s.source + '" target="_blank" rel="noopener noreferrer" style="color:#fff; text-decoration:none;">' +
                s.name + ' <i class="' + icon + '" style="font-size:0.85em; color:#c0995e;"></i>' +
              '</a>' +
            '</div>' +
            '<div style="display:flex; gap:12px; font-size:0.85em; color:#999;">' +
              '<span><i class="fa-solid fa-server" style="margin-right:4px;"></i>' +
                (s.computerUrl
                  ? '<a href="' + s.computerUrl + '" target="_blank" rel="noopener noreferrer" style="color:#c0995e;">' + s.computer + '</a>'
                  : s.computer) +
              '</span>' +
              '<span><i class="fa-solid fa-microchip" style="margin-right:4px;"></i>' + s.accelerators + '</span>' +
              '<span><i class="fa-solid fa-clock" style="margin-right:4px;"></i>' + s.walltime + '</span>' +
            '</div>' +
          '</div>' +
        '</div>';
      }).join("");
    })
    .catch(function() {
      document.getElementById("mfc-sims-gallery").innerHTML =
        '<p>Could not load simulations. <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer">View them on the MFC website</a>.</p>';
    });
})();
</script>

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

We have an active Slack channel where you can post questions or learn more, just <a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer">click here!</a>
You can also <a href="mailto:shb@gatech.edu">email Spencer</a> to see if it's appropriate for your use case or to discuss further.
In either case, I recommend checking out the GitHub page and website above!
</div>
</div>

<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<h4>Other open-source projects</h4>
• <strong>Pyrometheus</strong> – symbolic thermochemistry and autodiff for reacting flows<br/>
• <strong>QBMMlib</strong> – quadrature-based moment methods for multiphase flows<br/>
• <strong>RBC3D</strong> – detailed microcirculation and cell-resolved blood-flow simulation<br/>
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
<pre style="background-color: #1f2020; padding: 15px; border-radius: 5px; overflow-x: auto;"><code>@article{wilfong26,
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
