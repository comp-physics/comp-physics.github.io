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
  <!-- margin-bottom:5px; -->
  <!-- margin-left:5px; -->
  <!-- border: 1px solid red; -->
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
  <!-- border: 1px solid black; -->
}
</style>

## Software

<div class="jumbotron">
<div class="col-md-12 col-sm-12">
<center> 
<h4>
<a href="https://github.com/comp-physics" target="_blank"><i class="fab fa-github-square fa-1x"></i> Group Github page</a>
</h4>
</center>
</div>
</div>

### Some examples

<div class="jumbotron">
<a href="https://mflowcode.github.io" target="_blank">
<img src="{{ site.url }}{{ site.baseurl }}/images/software/mfc-logo2.png" width="50%" />
</a>
<h4><b>High-fidelity Multiphase Flow Simulation</b></h4>
<a href="https://mflowcode.github.io" target="_blank"><button class="btn btn-primary btn-sm">WEBSITE</button></a>
<a href="https://github.com/MFlowCode/MFC" target="_blank"><button class="btn btn-success btn-sm">GITHUB</button></a>
<a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-CPC-20.pdf" target="_blank"><button class="btn btn-danger btn-sm">PAPER</button></a> 

<b>Authors:</b>
<i>S. H. Bryngelson, T. Colonius, V. Coralic,  H. Le Berre, K. Maeda, J. Meng, A. Radhakrishnan, M. Rodriguez, K. Schmidmayer, J.-S. Spratt, and more!</i> (alpha by last name)

<b>MFC</b> is an open source parallel simulation software for multi-component, multi-phase, and bubbly flows. 
Its efficient simulation algorithm is capable of solving flows like droplet atomization, bubble cavitation, and their interactions with strong shocks.
The simulation method consists of:
- 5- and 6-equation diffuse-interface models
- High-order-accurate WENO interface-capturing methods
- HLL-type Riemann solvers
- Sub-grid bubble models, including QBMMs
- TVD time-integration schemes 
</div>

<div class="jumbotron">
<h4><b>QBMMlib: Moment Methods for Fully-coupled Flows</b></h4>
<a href="https://github.com/comp-physics/QBMMlib" target="_blank"><button class="btn btn-success btn-sm">GIT: QBMMLIB</button></a>
<a href="https://github.com/comp-physics/PyQBMMlib" target="_blank"><button class="btn btn-success btn-sm">GIT: PyQBMMLIB</button></a>
<a href="{{ site.url }}{{ site.baseurl }}/papers/bryngelson-SoftX-20.pdf" target="_blank"><button class="btn btn-danger btn-sm">PAPER</button></a> 

<b>Authors:</b>
<i>S. H. Bryngelson, E. Cisneros, and Q. Wang</i> (alpha by last name)

<b>QBMMlib</b> is an <a href="https://github.com/comp-physics/QBMMlib" target="_blank">open source Mathematica package</a> for solving populating balance equations with quadrature-based moment methods (QBMMs).
QBMMs are used for fully-coupled disperse flow and combustion problems.
However, formulating and closing the corresponding governing equations can be complex.
QBMMlib makes using these methods simple and accessible:
- Symbolic and automatic formulation of moment transport equations for a population balance equation and dynamical system
- Moment inversion trades moment sets for quadrature points
    - Algorithms: QMOM, HyQMOM, CQMOM, and more
- Quadratures closes the moment transport and governing flow equations 
- Embedded Runge--Kutta algorithms for _realizable_ time integration

The algorithm initialization and solution can span _just 13 lines of code_.
Example notebooks demonstrate QBMMlib on bubble dynamics problems.

<b><a href="https://github.com/comp-physics/PyQBMMlib" target="_blank">PyQBMMlib:</a></b> With Esteban Cisneros we developed a Python version of QBMMlib that leverages JIT compiling for significantly improved performance.

</div>
