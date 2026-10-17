#   Modify Model Color Other

Modifies the color of the base model texture of other entities that can be seen by the entity holding the power.


Type ID: `neo-apoli:modify/model/color/other`


???+ info

    This type provides the following context parameters when an entity is rendered:

    Parameter | Description
    ----------|------------
    `neo-apoli:actor_entity` | The entity being rendered.
    `neo-apoli:target_entity` | The entity holding the power.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`color` | [Color][color] | | Determines the color to use to mix with the colors of the other entity's base model texture.


### Example

```json
{
    "type": "neo-apoli:modify/model/color/other",
    "color": {
        "type": "neo-apoli:dynamic/argb",
        "alpha": {
            "type": "neo-apoli:linear_interpolated",
            "delta": {
                "type": "neo-apoli:quotient",
                "dividend": {
                    "type": "neo-apoli:min",
                    "values": [
                        {
                            "type": "neo-apoli:distance_between_positions",
                            "first": {
                                "type": "neo-apoli:entity/position",
                                "entity": "actor"
                            },
                             "second": {
                                "type": "neo-apoli:entity/position",
                                "entity": "target"
                             }
                        },
                        8.0
                    ]
                },
                "divisor": 8.0
            },
            "start": 1.0,
            "end": 0.0
        },
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
    }
}
```

This example makes other entities completely visible when very near, partially visible when slightly far, and completely invisible when more than 8 blocks away to the entity holding the power.


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
