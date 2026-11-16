#   To Degrees

Provides an angle measured by degrees by converting another angle measured by radians.


Type ID: `kaya:to_degrees`


!!! note

    The formula for this type is as follows: $deg = rad \times {{ rad_to_deg }}$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`radians` | [Float Provider][float_provider] | | The radian angle to convert to degrees.


### Example

{% set radians = to_radians(90) %}
{% set degrees = to_degrees(radians) %}

```json
{
    "type": "kaya:to_degrees",
    "radians": {{ radians }}
}
```

This example will provide the computed radian angle from degree angle {{ degrees }}, which will be {{ radians }}.


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
