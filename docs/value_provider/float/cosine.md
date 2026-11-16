#   Cosine

Provides the trigonometric cosine of an angle.


Type: `kaya:cosine`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The angle in radians.


### Example

{% set degrees = 45 %}
{% set radians = to_radians(45) %}
{% set cos = cos(radians) %}

```json
{
    "type": "kaya:cosine",
    "value": {
        "type": "kaya:to_radians",
        "degrees": {{ degrees }}//(1)!
    }
}
```

This example will convert the {{ degrees }} degree angle into radians and calculate its cosine value, which will be {{ cos }}.

1. The converted radian angle will be {{ radians }}.


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


[^1]: Aliases: `cos`
