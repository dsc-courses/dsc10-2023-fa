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

<!-- {: .success } 
> The Final Exam is on Saturday 6/10 from 7-10PM! Read [this post on Ed](https://edstem.org/us/courses/38383/discussion/3181148) for all the details.
> - If at least 80% of the class fills out both [CAPEs](https://cape.ucsd.edu) and the [End-of-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSefDOyTsn4b9poc3I5iCbgdtXAnMnAxIjuiyHt5PHwpYoMIlg/viewform) **by Saturday 6/10 at 8AM**, then we will add 0.5% of extra credit to everyone's overall grade. **We're currently only at 51% for CAPEs and 36% for the End-of-Quarter Survey!**
> - While studying, refer to these brand-new [**tutor-created videos and guides**](https://edstem.org/us/courses/38383/discussion/3183737) and the [Diagrams](diagrams) tab on the course website. -->

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-9-prediction){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}