#   Biome Foliage

Provides the foliage color of the biome from the specified position.


Type ID: `neo-apoli:biome/foliage`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to get the foliage color of the biome from.
`alpha` | [Float Provider][float_provider] | | The alpha (transparency) component to be mixed with the foliage color. The value is clamped from 0.0 to 1.0.
`dry` | [Boolean Provider][boolean_provider] | | Determines whether to get the dry foliage color of the biome.


### Example

```json
{
    "type": "neo-apoli:biome/foliage",
    "position": {
        "type": "neo-apoli:entity/position",
        "entity": "this"
    },
    "alpha": 1.0,
    "dry": {
        "type": "neo-apoli:condition_result",
        "condition": {
            "type": "neo-apoli:is_entity_sneaking",
            "entity": "this"
        }
    }
}
```

This example will provide the foliage color (dry if the entity is sneaking) of the biome at the entity's feet position.


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
