#   Is Effect In Tag

Checks if the type of the status effect instance is in a specified status effect tag.


Type ID: `neo-apoli:is_effect_in_tag`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tag` | [Damage Type Tag]({{ mc.damage_type_tag }}) | | The damage type tag to match.
`damage_source` | [Damage Source Provider][damage_source_provider] | | The damage source to check.


### Example

```json
{
    "type": "neo-apoli:is_effect_in_tag",
    "tag": "#example:is_beneficial"/*(1)!*/,
    "damage_source": "applied_effect"
}
```


1. The location of the file is `data/example/tags/mob_effect/is_beneficial.json`


This example will check if the type of the status effect instance provided by the `neo-apoli:applied_effect` context parameter is included in the `#example:is_beneficial` status effect tag.


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
