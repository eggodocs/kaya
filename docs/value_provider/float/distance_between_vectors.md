#   Distance Between Vectors

Provides the distance between two vectors.


Type ID: `neo-apoli:distance_between_vectors`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Vec3 Provider][vec3_provider] | | The first vector.
`second` | [Vec3 Provider][vec3_provider] | | The second vector.


### Example

```json
{
    "type": "neo-apoli:distance_between_vectors",
    "first": {
        "type": "neo-apoli:entity/position",
        "entity": "this"
    },
    "second": {
        "type": "neo-apoli:block/position",
        "block": "broken_block"
    }
}
```

This example provides the distance between an entity *(provided by the `neo-apoli:this_entity` context parameter)* and a block *(provided by the `neo-apoli:broken_block` context parameter.)*


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
