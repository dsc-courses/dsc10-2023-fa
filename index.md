---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{: .success }
> Welcome to DSC 10! 👋 Make sure to:
> - Read the entire [**Syllabus**](syllabus) and complete the actions in the [**Getting Started**](syllabus#-getting-started) section.
> - Complete the [**pretest**](https://practice.dsc10.com/pretest).
> - Stop by the Meet the Professors mixer on Friday from 11:30AM-12:30PM in the patio of the [**HDSI Building**](https://map.concept3d.com/?id=1005#!m/246301) – there'll be free pizza! 🍕
> 
> See you in lecture on Friday!

{{ site.staffersnobio }}

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->

[Jump to the current week](){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}