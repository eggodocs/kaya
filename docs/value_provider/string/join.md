#   Join

Joins all the specified strings into a single string and uses it as the provided value.


Type ID: `kaya:join`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`strings` | [Array][array] of [String Providers][string_provider] | | The strings to join together.
`separator` | [String Provider][string_provider] | | The string to place between each string when joined.


### Example

```json
{
    "type": "kaya:join",
    "strings": [
        "tellraw @a {\"text\": \"",
        {
            "type": "kaya:escape",
            "string": {
                "type": "kaya:nbt",
                "source": {
                    "type": "kaya:block",
                    "block": "used_block"
                },
                "path": "{}"
            }
        },
        "\", \"color\": \"gray\", \"italic\": true}"
    ],
    "separator": ""
}
```

This example joins three strings:

1. A constant *'`tellraw @a {"text": "`'* string.
2. An escaped stringified NBT of the block provided by the `kaya:used_block` context parameter.
3. A constant *'`", "color": "gray", "italic": true}`'* string.


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
