{% for year in years %}

## {{year}}

|     | Extension | Labels | Links |
| --- | --------- | ------ | ----- |
{% for post in posts %}
{% if post.year == year %}
| {{post.week}} | [{{post.extension}}]({{ref.format(**post).replace(" ", "%20") | default(post.year+"/"+post.week+".html")}}) | {{post.labels | join(", ")}} | {{post.links | join(", ")}}
{% endif %}
{% endfor %}
{% endfor %}
