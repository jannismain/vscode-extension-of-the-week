{% for year in years %}

## {{year}}

|     | Extension | Labels | Links |
| --- | --------- | ------ | ----- |
{% for post in posts %}
{% if post.year == year %}
| {{post.week}} | [{{post.extension}}]({{ref.format(**post) | default(post.year+"/"+post.week+".html")}}) | {{post.labels | join(", ")}} | {{post.links | join(", ")}}
{% endif %}
{% endfor %}
{% endfor %}
