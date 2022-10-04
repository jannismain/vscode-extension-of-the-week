{% if include_markers %}<!-- toc-begin -->{% endif +%}
|     | Extension | Labels | Links |
| --- | --------- | ------ | ----- |
{% for post in posts %}
| {{post.week}} | [{{post.extension}}]({{ref.format(**post).replace(" ", "%20") | default(post.year+"/"+post.week+".html")}}) | {{post.labels | join(", ")}} | {{post.links | join(", ")}}
{% endfor -%}
{% if include_markers %}<!-- toc-end -->{% endif %}
