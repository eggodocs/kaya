#   ARGB

Provides an ARGB color.


Type ID: `neo-apoli:argb`


!!! note

    Usually, color components are represented as an [integer][integer] ranging from 0 to 255. To convert them into [floats][float], you can divide the value by 255.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`alpha` | [Float][float] | | The alpha (transparency) component of the color. The value should be within the range of 0.0 to 1.0.
`red` | [Float][float] | | The red component of the color. The value should be within the range of 0.0 to 1.0.
`green` | [Float][float] | | The green component of the color. The value should be within the range of 0.0 to 1.0.
`blue` | [Float][float] | | The blue component of the color. The value should be within the range of 0.0 to 1.0.


### Example

```json
{
    "type": "neo-apoli:argb",
    "alpha": 0.25,
    "red": 1.0,
    "green": 0.0,
    "blue": 1.0
}
```

This example provides a bright magenta color that's slightly transparent.


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
