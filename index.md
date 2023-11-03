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

{: .success }
> - **The deadline for the Midterm Project has been extended until Monday, November 6th! You can still use up to 2 slip days on it.**
> - **If at least 80% of the class completes the [Mid-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSenMue3wGwX7OVIE0RMJ4OFzMtg0YG3T2PqXikcB7594ij5kg/viewform) by Saturday, November 11th, then everyone will receive an addition 2 points on the Midterm Exam!**

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->

[Jump to the current week](#week-5-midterm-exam){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}