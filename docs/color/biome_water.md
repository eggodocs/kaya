#   Biome water

Provides the water color of the biome from the specified position.


Type ID: `kaya:biome/water`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to get the water color of the biome from.
`alpha` | [Float Provider][float_provider] | | The alpha (transparency) component to be mixed with the water color. The value is clamped from 0.0 to 1.0.


### Example

```json
{
    "type": "kaya:biome/water",
    "position": {
        "type": "kaya:entity/position",
        "entity": "this",
        "anchor": "eyes"
    },
    "alpha": 1.0
}
```

This example will provide the water color of the biome at the entity's eyes position.


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
