#   Linear Interpolated { #vec3_lerp }

Interpolates a vector.


Type ID: `kaya:linear_interpolated`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`delta` | [Float Provider][float_provider] | | A float value that indicates the progress of the interpolation.
`start` | [Vec3 Provider][vec3_provider] | | The start vector.
`end` | [Vec3 Provider][vec3_provider] | | The end vector.


???+ info

    If `delta` is 0, it will provide the `start` vector. If it's 1, it wil provide the `end` vector. Otherwise, the `delta` will be clamped within the range of 0.0 to 1.0.


### Example

{% set first = vec3f(-8.25, -8.76, -1.57) %}
{% set second = vec3f(-7.78, 3.58, -1.81) %}

```json
{
    "type": "kaya:linear_interpolated",
    "delta": 0.5,
    "start": [
        -8.25,
        -8.76,
        -1.57
    ],
    "end": [
        -7.78, 
        3.58, 
        -1.81
    ]
}
```

This example will provide an interpolated vector starting from {{ to_str(first) }} to {{ to_str(second) }}, which will be {{ to_str(vec3f(clamped_lerp(0.5, first.x, second.x), clamped_lerp(0.5, first.y, second.y), clamped_lerp(0.5, first.z, second.z))) }}.


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


[^1]: Aliases: `lerp`
