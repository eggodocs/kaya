#   Offset

Offsets a vec3 by adding another vec3.


Type ID: `kaya:offset`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vec3 to offset.
`offset` | [Vec3 Provider][vec3_provider] | | The vec3 to use as the offset.


### Example

```json
{
    "type": "kaya:offset",
    "vector": {
        "type": "kaya:entity/position",
        "entity": "this"
    },
    "offset": [
        0.0,
        -1.0,
        0.0
    ]
}
```

This example provides the position of the entity provided by the `kaya:this_entity` context parameter, offset by 1 block under.


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
