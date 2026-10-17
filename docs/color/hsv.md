#   HSV

Provides an HSV (hue, saturation, value/brightness/lightness) color (which is then converted to ARGB.)


Type ID: `neo-apoli:hsv`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`hue` | Float | | The hue component of the color. The value should be within the range of 0.0 to 1.0.
`saturation` | Float | | The saturation component of the color. The value should be within the range of 0.0 to 1.0.
`value` | Float | | The value/brightness/lightness component of the color. The value should be within the range of 0.0 to 1.0.
`alpha` | Float | | The alpha (transparency) component of the color. The value should be within the range of 0.0 to 1.0.


### Example

```json
{
    "type": "neo-apoli:hsv",
    "hue": 0.32394366197183,
    "saturation": 1.0,
    "value": 0.90,
    "alpha": 1.0
}
```

This example provides a bright green HSV color.


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
