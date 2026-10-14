#   Modify Glowing Self

Modifies whether the entity holding the power should glow for other entities and what color should the glowing effect have.


Type ID: `neo-apoli:modify/glowing/self`


!!! note "Context info"

    This power type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `neo-apoli:actor_entity` | The entity seeing the entity holding the power.
    `neo-apoli:target_entity` | The entity holdng the power.


###  Format

Field | Type | Default | Description
------|------|:-------:|------------
`use_team_color` | [Boolean Provider][boolean_provider] | `true` | Determines whether the glowing effect should use the entity's team color.
`color` | [Color][color] | *optional* | Determines the color that'll be used for the glowing effect.


###  Example

```json
{
    "type": "neo-apoli:modify/glowing/other",
    "use_team_color": false,
    "color": "#a727fcd9",
    "active_condition": {
        "type": "neo-apoli:inverted",
        "condition": {
            "type": "neo-apoli:is_entity_sneaking",
            "entity": "this"
        }
    }
}
```

This example will make the entity holding the power glow purple if they aren't sneaking.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
