#   Is Damage Source In Tag

Checks if the damage type of the damage source is in a specified damage type tag.


Type ID: `neo-apoli:is_damage_source_in_tag`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tag` | [Damage Type Tag]({{ mc.damage_type_tag }}) | | The damage type tag to match.
`damage_source` | [Damage Source Provider][damage_source_provider] | | The damage source to check.


### Example

```json
{
    "type": "neo-apoli:is_damage_source_in_tag",
    "tag": "#minecraft:is_fall",
    "damage_source": "taken_damage/source"
}
```

This example will check if the damage type of the damage source provided by the `neo-apoli:taken_damage/source` context parameter is included in the `#minecraft:is_fall` damage type tag.


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
