#   Rotate

Adjusts the pitch, yaw, and/or roll of a vector.


Type ID: `kaya:rotate`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vector to rotate.
`pitch` | [Float Provider][float_provider] | *optional* | If specified, the pitch of the vector is adjusted by this value.
`yaw` | [Float Provider][float_provider] | *optional* | If specified, the yaw of the vector is adjusted by this value.
`roll` | [Float Provider][float_provider] | *optional* | If specified, the roll of the vector is adjusted by this value.


???+ warning

    Any of `pitch`, `yaw`, or `roll` fields **must be present**. Otherwise, an error will be thrown.


### Example

```json
{
    "type": "kaya:rotate",
    "vector": {
        "type": "kaya:entity/view",
        "entity": "this"
    },
    "pitch": 8.0
}
```

This example will adjust the pitch of the direction vector of the entity provided by the `kaya:this_entity` context parameter by 8.0 degrees.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
