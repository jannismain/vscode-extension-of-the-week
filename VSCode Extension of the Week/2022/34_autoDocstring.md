---
title: "34: autoDocstring"
links:
    :github:: https://github.com/NilsJPWerner/autoDocstring
    VSCode Marketplace: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
labels:
    - vscode
    - python
    - documentation
---

autoDocstring is an extension that automatically generates Python docstring boilerplate for you:

![preview](34_autoDocstring_example.gif)

It is especially useful when adding documentation to existing code.

## Configuration

![autoDocstring config options](34_autoDocstring_config.png)

When you are using type hints to annotate parameter types, you should choose the `-notypes` option of the docstring format you want to generate. For me, this would be `google-notypes` (which is also shown above).
