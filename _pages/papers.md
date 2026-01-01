---
title: "Papers"
layout: gridlay
sitemap: false
permalink: /papers/
years: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
---

<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
</style>

## Archival Publications

<div style="margin-bottom: 20px; text-align: right;">
  <a href="{{ site.url }}{{ site.baseurl }}/cv/ref.bib" download="bryngelson-publications.bib" class="btn btn-primary" style="margin: 0; border-radius: 8px;">
    <i class="fa fa-download"></i> Download BibTeX
  </a>
</div>

<div class="jumbotron" style="padding-left:0px">
{% bibliography --query @unpublished %}
{% bibliography --query @article,@inproceedings,@report %}
</div>
