#   Vector Component

Provides the component of a vector from a specific axis.


Type ID: `kaya:vector/component`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vector to get a component from.
`axis` | [Axis][axis] | | The axis of the component to get.


### Example

```json
{
    "type": "kaya:vector/component",
    "vector": {
        "type": "kaya:block/position",
        "block": "used_block"
    },
    "axis": "y"
}
```

This example provides the Y axis component of a block *(provided by the `kaya:used_block` context parameter.)*


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
