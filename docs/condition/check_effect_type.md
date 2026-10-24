#   Check Effect Type

Check if the effect of a status effect instance is of a type or if it's included in an effect type tag.


Type ID: `neo-apoli:check_effect_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`key` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, checks if the effect of a status effect instance is of this specific type.
`tag` | [Effect Type Tag]({{ mc.tag }}) | *optional* | If specified, checks if the effect of a status effect instance is included in this effect type tag.
`effect` | [Effect Provider][effect_provider] | | The status effect instance to check.


???+ warning

    Both `key` and `tag` fields should **not** be present or absent at the same time! Otherwise an error will be thrown.


### Example

```json
{
    "type": "neo-apoli:check_effect_type",
    "key": "minecraft:poison",
    "effect": "applied_effect"
}
```

This example will check if the effect of the status effect instance provided by the `neo-apoli:applied_effect` context parameter is of a `minecraft:poison` effect type.


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
