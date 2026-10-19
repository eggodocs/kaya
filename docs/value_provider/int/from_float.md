---
example:
    velocity:
        x: 0.0
        y: 1.0
        z: 0.3
---


#   From Float

Provides a float converted as an integer.


Type ID: `neo-apoli:from_Float`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The float value to convert as an integer.


### Example

```json
{
    "type": "neo-apoli:from_float",
    "value": {
        "type": "neo-apoli:round",
        "value": {
            "type": "neo-apoli:vector/length",
            "vector": {
                "type": "neo-apoli:entity/velocity",
                "entity": "this"
            }
        },
        "places": 0
    }
}
```

This example will round off the length of the velocity of an entity *(provided by the `neo-apoli:this_entity` context parameter)* and convert it into an integer.

{% set result = sqrt(example.velocity.x * example.velocity.x + example.velocity.y * example.velocity.y + example.velocity.z * example.velocity.z) %}

For example, let's say the entity's velocity vector is X: ${{ example.velocity.x }}$, Y: ${{ example.velocity.y }}$, Z: ${{ example.velocity.z }}$. The length of the velocity vector will be ${{ result }}$, which will then be truncated to ${{ round_down(result) }}$.


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
