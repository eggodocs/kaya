#   Dynamic RGBA

Provides an RGBA color (which is then converted to ARGB) using [float providers][float_provider].


Type ID: `kaya:dynamic/rgba`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`red` | [Float Provider][float_provider] | | The red component of the color. The value is clamped from 0.0 to 1.0.
`green` | [Float Provider][float_provider] | | The green component of the color. The value is clamped from 0.0 to 1.0.
`blue` | [Float Provider][float_provider] | | The blue component of the color. The value is clamped from 0.0 to 1.0.
`alpha` | [Float Provider][float_provider] | | The alpha (transparency) component of the color. The value is clamped from 0.0 to 1.0.


### Example

```json
{
    "type": "kaya:dynamic/rgba",
    "red": {
        "type": "kaya:linear_interpolated",
        "delta": {
            "type": "kaya:product",
            "values": [
                {
                    "type": "kaya:vector/length",
                    "vector": {
                        "type": "kaya:entity/velocity",
                        "entity": "this"
                    }
                },
                3.5
            ]
        },
        "start": 1.0,
        "end": 0.0
    },
    "green": 1.0,
    "blue": 1.0,
    "alpha": 1.0
}
```

This example provides an RGBA color with its red component being dependent on the entity's velocity magnitude. The faster the entity's velocity, the less red it becomes.


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
