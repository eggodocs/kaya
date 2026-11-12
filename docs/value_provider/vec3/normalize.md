---
vec:
    x: 12
    y: 34
    z: 56
---


#   Normalize

Reduces the length of a vector to 1.0, unless it's a zero-length vector.


Type ID: `kaya:normalize`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vector to normalize.


### Example

```json
{
    "type": "kaya:normalize",
    "vector": [
        12,
        34,
        56
    ]
}
```

{% set length = sqrt(sqr(vec.x) + sqr(vec.y) + sqr(vec.z)) %}

This example will normalize the vector X: {{ vec.x }}, Y: {{ vec.y }}, Z: {{ vec.z }} (with a length of {{ floor(length, "1.00") }}) into X: {{ floor(vec.x / length, "1.00") }}, Y: {{ floor(vec.y / length, "1.00") }}, Z: {{ floor(vec.z / length, "1.00") }} (with a length of {{ floor(sqrt(sqr(vec.x / length) + sqr(vec.y / length) + sqr(vec.z / length)), "1.00") }})


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
