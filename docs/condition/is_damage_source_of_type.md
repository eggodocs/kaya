#   Is Damage Source of Type

Check if a damage source is of a specific damage type.


Type ID: `neo-apoli:is_damage_source_of_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`damage_type` | [Identifier]({{ mc.identifier }}) | | The ID of the damage type.
`damage_source` | [Damage Source Provider][damage_source_provider] | | The damage source to check.


### Example

```json
{
    "type": "neo-apoli:is_damage_source_of_type",
    "damage_type": "minecraft:fly_into_wall",
    "damage_source": "taken_damage/source"
}
```

This example will check if the damage type of the damage source provided by the `neo-apoli:taken_damage/source` context parameter is `minecraft:fly_into_wall`.


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
