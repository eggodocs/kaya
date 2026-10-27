#   Round

Provides a rounded off float value.


Type ID: `kaya:round`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The float to round off.
`places` | [Int Provider][int_provider] | | Determines the decimal places to round off the float.
`rounding_mode` | [Rounding Mode][rounding_mode] | `"half_up"` | Determines how the float is rounded off.


### Example

```json
{
    "type": "kaya:round",
    "value": {
        "type": "kaya:entity/attribute",
        "attribute": "minecraft:step_height",
        "entity": "this"
    },
    "places": 0
}
```

This example will provide the value of the `minecraft:step_height` attribute from the entity provided by the `kaya:this_entity` context parameter rounded off to 1 digit.

For example, let's say the attribute has a value of $0.6$. The value will be rounded off to ${{ round_half_up(0.6) }}$.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
