#   Product

Multiplies all the components of two vectors and provides the product as a vector.


Type ID: `kaya:product`[^1]


## Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Vec3 Provider][vec3_provider] | | The first vector.
`second` | [Vec3 Provider][vec3_provider] | | The second vector.


## Example

{% set first = vec3f(4.06, 8.42, -9.46) %}
{% set second = vec3f(2.90, -9.45, 4.73) %}

```json
{
    "type": "kaya:product",
    "first": [
        4.06, 
        8.42,
        -9.46
    ],
    "second": [
        2.90, 
        -9.45, 
        4.73
    ]
}
```

This example multiplies the vector {{ to_str(first) }} by vector {{ to_str(second) }}, which will return vector {{ to_str(vec3f(floor(first.x * second.x, "1.00"), floor(first.y * second.y, "1.00"), floor(first.z * second.z, "1.00"))) }}.


##  History

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


[^1]: Aliases: `mul`, `multiply`
