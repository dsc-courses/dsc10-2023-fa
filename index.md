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
> Welcome to DSC 10! 👋 To get started:
> - Read the entire [**Syllabus**](syllabus) and complete the actions in the [**Getting Started**](syllabus#-getting-started) section.
> - Complete the [**pretest**](https://practice.dsc10.com/pretest) this weekend. We'll release solutions on Monday.

{{ site.staffersnobio }}

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->

[Jump to the current week](#week-1-python-basics){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}