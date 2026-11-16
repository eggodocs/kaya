#   Sine

Provides the trigonometric sine of an angle.


Type ID: `kaya:sine`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The angle in radians.


### Example

{% set radians = to_radians(75) %}
{% set degrees = to_degrees(radians) %}
{% set sin = sin(radians) %}

```json
{
    "type": "kaya:sine",
    "value": {
        "type": "kaya:to_radians",
        "degrees": {{ degrees }}
    }
}
```

This example will convert the {{ degrees }} degree angle into radians and calculate its sine value, which will be {{ sin }}.


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


[^1]: Aliases: `sin`
