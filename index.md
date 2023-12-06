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
**The Final Exam is on Saturday from 7-10PM. Read [this Ed post](https://edstem.org/us/courses/48101/discussion/3988059) for more details, and check your assigned room and seat [here](https://docs.google.com/spreadsheets/d/13oQoPFSTEvFCpKqiTjvybolzUNOlkGLRPnAAdUETjiU/edit#gid=0). In lecture on Wednesday, we will take up the solutions to the [Spring 2023 Final Exam](https://practice.dsc10.com/sp23-final), so you should work on it before then.<br><br>If at least 85% of the class fills out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) and the [End-of-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSeaQYHSzfjHIVnn-XtIxEBjEacddwEVC2bomgkTV_vVM--wCA/viewform) by Saturday at 8AM, then we will add 1% of extra credit to everyone's overall grade. We appreciate your feedback!<br><br>The solutions to the [Spring 2023 Final Exam](https://practice.dsc10.com/sp23-final) have been posted; video walkthroughs of some problems (taken from Wednesday's lectures) can be found at the top.**

[Jump to the current week](#week-10-review){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}