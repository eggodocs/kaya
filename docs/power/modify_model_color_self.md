#   Modify Model Color Self

Modifies the color of the base model texture of the entity holding the power for other entities.


Type ID: `neo-apoli:modify/model/color/self`


???+ info

    This type provides the following context parameters when the entity holding the power is rendered:

    Parameter | Description
    ----------|------------
    `neo-apoli:actor_entity` | The entity seeing the entity holding the power.
    `neo-apoli:target_entity` | The entity holding the power.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`color` | [Color][color] | | Determines the color to use to mix with the colors of the base model texture of the entity holding the power.


### Example

```json
{
    "type": "neo-apoli:modify/model/color/self",
    "color": {
        "type": "neo-apoli:dynamic/argb",
        "alpha": {
            "type": "neo-apoli:linear_interpolated",
            "delta": {
                "type": "neo-apoli:product",
                "values": [
                    {
                        "type": "neo-apoli:vector/length",
                        "vector": {
                            "type": "neo-apoli:entity/velocity",
                            "entity": "this"
                        }
                    },
                    3.5
                ]
            },
            "start": 0.0,
            "end": 1.0
        },
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
    }
}
```

This example makes the visibility of the entity holding the power depend on its velocity magnitude. The faster the entity's velocity, the more it's visible to other entities.


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
