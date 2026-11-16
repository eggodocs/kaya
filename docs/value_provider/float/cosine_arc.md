#   Cosine Arc

Provides the inverse of a cosine value, ranging from 0.0 to Pi.


Type ID: `kaya:cosine/arc`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The cosine value.


### Example

{% set radians = to_radians(175) %}
{% set degrees = to_degrees(radians) %}
{% set cos = cos(radians) %}
{% set acos = acos(cos) %}

```json
{
    "type": "kaya:cosine/arc",
    "value": {{ cos }}//(1)!
}
```

This example will provide the inverse of the cosine value {{ cos }}, which will be {{ acos }}.

1. The cosine value of the {{ radians }} radian angle, which is {{ degrees }} when converted to a degree angle.


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



[^1]: Aliases: `acos`
