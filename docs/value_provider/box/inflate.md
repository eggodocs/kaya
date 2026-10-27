#   Inflate

Expands the bounds of the box towards all directions of the specified axes.


Type ID: `kaya:inflate`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to inflate.
`vector` | [Vec3 Provider][vec3_provider] | | The vector to use for inflating the box.


### Example

```json
{
    "type": "kaya:offset",
    "box": {
        "type": "kaya:entity/bounds",
        "entity": "this"
    },
    "vector": [
        1.0,
        1.0,
        1.0
    ]
}
```

This example provides the bounding box of the entity provided by the `kaya:this_entity` context parameter and inflates it by 1 block.


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
