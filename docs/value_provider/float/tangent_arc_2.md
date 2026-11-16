#   Tangent Arc 2

Provides the arc tangent of the Y coordinate divided by the X coordinate (in radians), ranging from -Pi to Pi.


Type ID: `kaya:tangent/arc/2`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`y` | [Float Provider][float_provider] | | The Y axis coordinate.
`x` | [Float Provider][float_provider] | | The X axis coordinate.


### Example

{% set y = 12.34 %}
{% set x = 56.78 %}
{% set atan2 = atan2(y, x) %}
{% set degrees = to_degrees(atan2) %}

```json
{
    "type": "kaya:tangent/arc/2",
    "y": {{ y }},
    "x": {{ x }}
}
```

This example will provide the arc tangent of the {{ y }} Y coordinate divided by {{ x }} X coordinate, which will be {{ atan2 }} ({{ degrees }} when converted into a degree angle.)


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>


[^1]: Aliases: `atan2`
