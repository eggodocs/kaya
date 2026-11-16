#   To Radians

Provides an angle measured by radians by converting another angle measured by degrees.


Type ID: `kaya:to_radians`


!!! note

    The formula for this type is as follows: $rad = deg \times {{ deg_to_rad }}$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`radians` | [Float Provider][float_provider] | | The degree angle to convert to radians.


### Example

{% set radians = to_radians(67) %}
{% set degrees = to_degrees(radians) %}

```json
{
    "type": "kaya:to_radians",
    "degrees": {{ degrees }}
}
```

This example will provide the computed degree angle from radian angle {{ radians }}, which will be {{ degrees }}.


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
