#   Vector Dot Product

Provides the dot product of two vectors.


Type ID: `kaya:vector/dot_product`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Vec3 Provider][vec3_provider] | | The first vector.
`second` | [Vec3 Provider][vec3_provider] | | The second vector.


### Example

{% set first = vec3f(3.015, 0.72, -9.63) %}
{% set second = vec3f(-3.00, -9.93, -6.79) %}
{% set result = floor(first.x * second.x + first.y * second.y + first.z * second.z, "1.00")%}

```json
{
    "type": "kaya:dot_product",
    "first": [
        3.015, 
        0.72, 
        -9.63
    ],
    "second": [
        -3.00, 
        -9.93, 
        -6.79
    ]
}
```

This example will provide the dot product of vector {{ to_str(first) }} and vector {{ to_str(second) }}, which will be {{ result }}


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
