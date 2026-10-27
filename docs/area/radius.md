#   Radius

Defines an area that's based on a position (as its center) and a radius.


Type: `kaya:radius`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The center position of the area.
`radius` | [Float Provider][float_provider] | | The radius of the area.


### Example

```json
{
    "type": "kaya:radius",
    "target": "entity",
    "shape": "star",
    "position": {
        "type": "kaya:block/position",
        "block": "broken_block"
    },
    "radius": 8.0
}
```

This example will provide an area with a radius of 8.0 blocks relative to the position of the block provided by the `kaya:broken_block` context parameter that will target entities.


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
