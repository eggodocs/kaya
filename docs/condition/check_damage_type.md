#   Check Damage Type

Check if the damage type of a damage source is of a type or if it's included in a damage type tag.


Type ID: `kaya:check_damage_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`key` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, checks if the damage type of the damage source is of this specific type.
`tag` | [Damage Type Tag]({{ mc.damage_type_tag }}) | *optional* | If specified, checks if the damage type of the damage source is included in this damage type tag.
`damage_source` | [Damage Source Provider][damage_source_provider] | | The damage source to check.


???+ warning

    Both `key` and `tag` fields should **not** be present or absent at the same time! Otherwise an error will be thrown.


### Example

```json
{
    "type": "kaya:check_damage_type",
    "tag": "#minecraft:is_fall",
    "damage_source": "taken_damage/source"
}
```

This example will check if the damage type of the damage source provided by the `kaya:taken_damage/source` context parameter is included in the `#minecraft:is_fall` damage type tag.


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
