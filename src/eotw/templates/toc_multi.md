<!-- toc-begin -->
{% set all_posts = posts %}
{% for year in years %}

## [{{year}}]({{year}})
{% set posts = all_posts | selectattr("year", "==", year) %}
{% set include_markers = False %}
{% include 'toc.md' %}

{% endfor %}
<!-- toc-end -->
