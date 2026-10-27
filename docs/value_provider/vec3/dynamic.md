#   Dynamic

Provides a vec3 with dynamic coordinates.


Type ID: `kaya:dynamic`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`x` | [Float Provider][float_provider] | | The X coordinate of the point.
`y` | [Float Provider][float_provider] | | The Y coordinate of the point.
`z` | [Float Provider][float_provider] | | The Z coordinate of the point.


### Example

```json
{
    "type": "kaya:dynamic",
    "x": {
        "type": "kaya:vector/component",
        "vector": {
            "type": "kaya:entity/position",
            "entity": "this"
        },
        "axis": "x"
    },
    "y": {
        "type": "kaya:vector/component",
        "vector": {
            "type": "kaya:block/position",
            "block": "broken_block"
        },
        "axis": "y"
    },
    "z": {
        "type": "kaya:vector/component",
        "vector": {
            "type": "kaya:entity/position",
            "entity": "this"
        },
        "axis": "z"
    }
}
```


This example provides a vec3 where the X and Z coordinates are from the entity provided by the `kaya:this_entity` context parameter, and the Y coordinate is from the block provided by the `kaya:broken_block` context parameter.


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
