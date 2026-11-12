#   Cross Product

Provides the cross product of two vectors.


Type ID: `kaya:cross_product`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Vec3 Provider][vec3_provider] | | The first vector.
`second` | [Vec3 Provider][vec3_provider] | | The second vector.


### Example

{% set first = vec3f(6.20, -2.12, 9.26) %}
{% set second = vec3f(-8.45, -2.46, 9.83) %}

```json
{
    "type": "kaya:cross_product",
    "first": [
        6.20,
        -2.12,
        9.26
    ],
    "second": [
        -8.45,
        -2.46,
        9.83
    ]
}
```

This example provides the cross product of vector {{ to_str(first) }} and vector {{ to_str(second) }} (which will be {{ to_str(cross_product(first, second)) }}.)


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
