#   Sine Arc

Provides the inverse of the sine value, ranging from -Pi / 2 through Pi / 2.


Type ID: `kaya:sine/arc`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The sine value.


### Example

{% set radians = to_radians(-35) %}
{% set degrees = to_degrees(radians) %}
{% set sin = sin(radians) %}
{% set asin = asin(sin) %}

```json
{
    "type": "kaya:sine/arc",
    "value": {{ sin }}//(1)!
}
```

This example will provide the inverse of the sine value {{ sin }}, which will be {{ asin }}.


1. This value is calculated from the radian angle of a {{ degrees }} degree angle, which will be {{ radians }}.


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


[^1]: Aliases: `asin`
