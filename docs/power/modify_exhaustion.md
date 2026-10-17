#   Modify Exhaustion

Modifies the exhaustion received by the entity holding the power.


Type ID: `neo-apoli:modify/exhaustion`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`modifiers` | [Array][array] of [Modifiers][modifier] | | The modifiers to apply to the received exhaustion.


### Example

```json
{
    "type": "neo-apoli:modify/exhaustion",
    "modifiers": [
        {
            "type": "neo-apoli:multiply_multiplicative",
            "phase": "total",
            "amount": 0.6
        }
    ]
}
```

This example essentially adds 60% more exhaustion to the entity holding the power.


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
