#   Dynamic ARGB

Provides an ARGB color using [float providers][float_provider].


Type ID: `kaya:dynamic/argb`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`alpha` | [Float Provider][float_provider] | | The alpha (transparency) component of the color. The value is clamped from 0.0 to 1.0.
`red` | [Float Provider][float_provider] | | The red component of the color. The value is clamped from 0.0 to 1.0.
`green` | [Float Provider][float_provider] | | The green component of the color. The value is clamped from 0.0 to 1.0.
`blue` | [Float Provider][float_provider] | | The blue component of the color. The value is clamped from 0.0 to 1.0.


### Example

```json
{
    "type": "kaya:dynamic/argb",
    "alpha": {
        "type": "kaya:linear_interpolated",
        "delta": {
            "type": "kaya:quotient",
            "dividend": {
                "type": "kaya:from_int",
                "value": {
                    "type": "kaya:time",
                    "period": 200
                }
            },
            "divisor": 200
        },
        "start": 1.0,
        "end": 0.0
    },
    "red": 1.0,
    "green": 1.0,
    "blue": 1.0
}
```

This example provides an ARGB color where the alpha component periodically changes from opaque to transparent every 200 ticks.


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
