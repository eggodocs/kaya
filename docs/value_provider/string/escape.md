#   Escape

Escapes certain characters from a string by prepending the character with the `\` character.


Type ID: `neo-apoli:escape`


???+ info

    This type escapes the following characters:

    Escape sequence | Character represented
    ----------------|----------------------
    `\b` | Backspace
    `\f` | Formfeed
    `\n` | Newline
    `\r` | Carriage Return
    `\\` | Backslash
    `\'` | Apostrophe/single quotation mark
    `\"` | Double quotation mark
    `\xhh` | Unicode point below `0x100` (256 in decimal)


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`string` | [String Provider][string_provider] | | The string to escape.


### Example

```json
{
    "type": "neo-apoli:escape",
    "string": {
        "type": "neo-apoli:nbt",
        "source": {
            "type": "neo-apoli:block",
            "block": "used_block"
        },
        "path": "{}"
    }
}
```

This example escapes the stringified NBT of the block provided by the `neo-apoli:used_block` context parameter.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
