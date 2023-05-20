---
title: "Papers"
layout: gridlay
sitemap: false
permalink: /papers/
years: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
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

## Publications

<div class="jumbotron">
{% bibliography --query @unpublished %}
{% bibliography --query @article,@inproceedings,@report %}
</div>
