#   Tangent

Provides the [trigonometric tangent](https://en.wikipedia.org/wiki/Tangent) of an angle.


Type ID: `kaya:tangent`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The angle in radians.


### Example

{% set radians = to_radians(45) %}
{% set degrees = to_degrees(radians) %}
{% set tanv = tan(radians) %}

```json
{
    "type": "kaya:tangent",
    "value": {
        "type": "kaya:to_radians",
        "degrees": {{ degrees }}//(1)!
    }
}
```

This example will convert the {{ degrees }} degree angle into a radian angle and provide its tangent value, which will be {{ tanv }}.

1. The converted radian angle will be {{ radians }}.


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


[^1]: Aliases: `tan`
