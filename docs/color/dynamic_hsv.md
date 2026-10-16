#   Dynamic HSV

Provides an HSV color (which is then converted to ARGB) with [float providers][float_provider].


Type ID: `neo-apoli:dynamic/hsv`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`hue` | [Float Provider][float_provider] | | The hue component of the color. The value is clamped from 0.0 to 1.0.
`saturation` | [Float Provider][float_provider] | | The saturation component of the color. The value is clamped from 0.0 to 1.0.
`value` | [Float Provider][float_provider] | | The value/brightness/lightness component of the color. The value is clamped from 0.0 to 1.0.
`alpha` | [Float Provider][float_provider] | | The alpha (transparency) component of the color. The value is clamped from 0.0 to 1.0.


### Example

```json
{
    "type": "neo-apoli:dynamic/hsv",
    "hue": {
        "type": "neo-apoli:quotient",
        "dividend": {
            "type": "neo-apoli:time",
            "period": 200
        },
        "divisor": 200
    },
    "saturation": 1.0,
    "value": 1.0
}
```

This example provides an HSV color with its hue component changing every tick, essentially making it cycle through every color.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
