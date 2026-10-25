#   Translate

Moves the position of a box with a vector.


Type ID: `neo-apoli:translate`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to translate.
`vector` | [Vec3 Provider][vec3_provider] | | The translation to apply to the box.


### Example

```json
{
    "type": "neo-apoli:translate",
    "box": [
        -4.0,
        -4.0,
        -4.0,
        4.0,
        4.0,
        4.0
    ],
    "vector": {
        "type": "neo-apoli:entity/position",
        "entity": "this"
    }
}
```

This example creates a bounding box with a size of 8.0 (4 blocks wide/high in every direction) and re-positions it to be relative to the position of the entity provided by the `neo-apoli:this_entity` context parameter.


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
