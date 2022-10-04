<!-- toc-begin -->
{% set all_posts = posts %}
{% for year in years %}

## [{{year}}]({{title_ref.format(year=year).replace(" ", "%20")}})
{% set posts = all_posts | selectattr("year", "==", year) %}
{% set include_markers = False %}
{% include 'toc.md' %}

{% endfor %}
<!-- toc-end -->
