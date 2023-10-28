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


{{ site.staffersnobio }}

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->

{: .success }
> - **The Midterm Exam is this Monday during lecture. See [this post on Ed](https://edstem.org/us/courses/48101/discussion/3734836) for lots of details, including what is covered, what to bring, and how to study.**
> - Over the weekend, practice by working through old exams at [practice.dsc10.com](https://practice.dsc10.com). The solutions to Quiz 1 and Quiz 2 can be found linked below.

[Jump to the current week](#week-4-probability-and-simulation){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}