[VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=wmaurer.vscode-jumpy)

![demo of jump vscode extension](https://cloud.githubusercontent.com/assets/2899448/19660934/0481c44c-9a32-11e6-87cc-1f8913922ccb.gif)

This is an extension that provides fast cursor movements to arbitrary points in your code for us mere mortals, that have not reached enlightenment level with vim yet. You simply hit a keyboard shortcut you can configure yourself (for me it is `alt+return` for now) and 2-letter combinations will appear at every word (or line, if you prefer). You press the letters to move your cursor to that location.

## Configuration

1. Open the command palette (`cmd+shift+p`)
2. Search for *Keyboard Shortcuts (JSON)* and `enter` to open the `keybinding.json` file
3. Paste the following entry:

    ```javascript
    // jumpy extension
    {
        "key": "alt+enter",
        "command": "extension.jumpy-word",
        "when": "editorTextFocus"
    }
    ```

Of course, feel free to choose another key combination (but be careful not to shadow any builtin shortcuts) or use `extension.jumpy-line` instead to navigate lines only.
