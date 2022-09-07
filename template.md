---
title: "{{week}}: {{extension.split('.')[-1]}}"
marketplace: https://marketplace.visualstudio.com/items?itemName={{extension}}
labels:
    - vscode
{% for label in labels %}
    - {{label}}
{% endfor %}
---

[VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName={{extension}})

<!-- Short Description -->

<!-- Screenshot / Gif / ... -->

## Configuration

<!-- Configuration options, recommended configuration, etc. -->


<!-- references -->
[macos]: ../../img/apple.svg
[win]: ../../img/win.svg
