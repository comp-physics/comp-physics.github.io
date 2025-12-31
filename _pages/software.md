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

<div style="text-align: center; margin: 20px 0;">
  <a href="https://mflowcode.github.io/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;">🌐 MFC Website</a>
  <a href="https://github.com/MFlowCode/MFC" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;"><i class="fab fa-github"></i> GitHub</a>
  <a href="https://join.slack.com/t/mflowcode/shared_invite/zt-y75wibvk-g~zztjknjYkK1hFgCuJxVw" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;"><i class="fab fa-slack"></i> Slack</a>
  <a href="#cite" class="btn btn-primary" style="margin: 5px; border-radius: 0.375rem;">📄 Cite MFC</a>
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
<center> 
<a href="https://mflowcode.github.io" target="_blank" rel="noopener noreferrer">
<img src="/images/software/shockdrop.png" width="70%" alt="Shock-droplet interaction simulation using MFC"/>
</a>
</center>
Above is an example of simulating shock-droplet interaction using MFC at thousands of modern GPUs.
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
B. Wilfong, H. Le Berre, A. Radhakrishnan, et al. "MFC 5.0: An exascale many-physics flow solver." <i>arXiv preprint</i> arXiv:2503.07953 (2025).<br/>
<a href="https://arxiv.org/abs/2503.07953" target="_blank" rel="noopener noreferrer">arXiv:2503.07953</a> | <a href="https://doi.org/10.48550/arXiv.2503.07953" target="_blank" rel="noopener noreferrer">DOI: 10.48550/arXiv.2503.07953</a>
</p>

<p><strong>MFC 3.0 (original release):</strong><br/>
S. H. Bryngelson, K. Schmidmayer, V. Coralic, J. Meng, K. Maeda, and T. Colonius. "MFC: An open-source high-order multi-component, multi-phase, and multi-scale compressible flow solver." <i>Computer Physics Communications</i> 266 (2021): 108029.<br/>
<a href="https://doi.org/10.1016/j.cpc.2021.108029" target="_blank" rel="noopener noreferrer">DOI: 10.1016/j.cpc.2021.108029</a>
</p>

<p><strong>BibTeX for MFC 5.0:</strong></p>
<pre style="background-color: #1f2020; padding: 15px; border-radius: 5px; overflow-x: auto;"><code>@unpublished{wilfong2025mfc50,
  title={MFC 5.0: An exascale many-physics flow solver},
  author={Wilfong, Benjamin and {Le Berre}, Henry and Radhakrishnan, Anand and others},
  note={arXiv:2503.07953},
  year={2025},
  doi={10.48550/arXiv.2503.07953}
}</code></pre>
</div>
</div>
