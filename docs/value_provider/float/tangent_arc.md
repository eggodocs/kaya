#   Tangent Arc

Provides the inverse of a [tangent](https://en.wikipedia.org/wiki/Tangent) value, ranging from -Pi / 2 through Pi / 2.


Type ID: `kaya:tangent/arc`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The tangent value.


### Example

{% set tanv = 6.7777 %}
{% set atanv = atan(tanv) %}
{% set degrees = to_degrees(atanv) %}
{% set radians = to_radians(degrees) %}

```json
{
    "type": "kaya:tangent/arc",
    "value": {{ tanv }}//(1)!
}
```

This example will provide the inverse of the tangent value {{ tanv }}, which will be {{ atanv }}.

1. This value is calculated by first calculating the radian angle of the {{ degrees }} degree angle (which will be {{ radians }}), and then calculating the tangent of the radian angle (which will then be {{ tan(radians) }}).


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


[^1]: Aliases: `atan`
