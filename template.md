---
title: "{{week}}: {{extension.split('.')[-1]}}"
marketplace: https://marketplace.visualstudio.com/items?itemName={{extension}}
labels:
    - vscode
{% for label in labels %}
    - {{label}}
{% endfor %}
---

[Open {{extension.split(".")[-1]}} in VSCode](vscode:extension/{{extension}}), [{{extension.split(".")[-1]}} on VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName={{extension}})

<!-- Short Description -->

<!-- Screenshot / Gif / ... -->

## Configuration

<!-- Configuration options, recommended configuration, shown configuration, etc. -->

---

*In this article:*

- *VSCode Theme: [Atom One Light Theme] + [City Lights Icons]*

<!-- references -->

[macos]: ../../img/apple.svg
[win]: ../../img/win.svg
[atom one light theme]: https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onelight
[city lights icons]: https://marketplace.visualstudio.com/items?itemName=yummygum.city-lights-icon-vsc
