#   Reverse

Multiplies the components of a vector with a negative factor, reversing its direction.


Type ID: `kaya:reverse`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vector to reverse.


### Example

```json
{
    "type": "kaya:reverse",
    "vector": {
        "type": "kaya:entity/view",
        "entity": "this"
    }
}
```

This example reverses the view vector of the entity provided by the `kaya:this_entity` context parameter.


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
