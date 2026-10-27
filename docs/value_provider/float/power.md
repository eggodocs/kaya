#   Power

Provides a float value raised to the power of another float.


Type ID: `kaya:power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`base` | [Float Provider][float_provider] | | The base float value to raise to the power of an exponent.
`exponent` | [Float Provider][float_provider] | | The exponent to raise the value of the base value.


### Example

```json
{
    "type": "kaya:power",
    "base": 2.5,
    "exponent": 4.0
}
```

This example provides $2.5$ raised to the power of $4.0$, which will be $39.0625$. $(2.5 * 2.5 * 2.5 * 2.5 = 39.06)$


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
