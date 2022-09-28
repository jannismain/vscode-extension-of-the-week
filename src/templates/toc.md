{% for year in years %}
## {{year}}

|     | Extension | Labels | Links |
| --- | --------- | ------ | ----- |
{% for post in posts %}
{% if post.year == year %}
| {{post.week}} | [{{post.extension}}]({{post.year}}/{{post.week}}.html) | {{post.labels | join(", ")}} | [Marketplace]({{post.marketplace}}), [VSCode]({{post.vscode}})
{% endif %}
{% endfor %}

{% endfor %}
