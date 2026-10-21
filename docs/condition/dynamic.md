#   Dynamic

Returns the boolean value of a boolean provider as the result.


Type ID: `neo-apoli:dynamic`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Boolean Provider][boolean_provider] | | The boolean to return as the result.


### Example

```json
{
    "type": "neo-apoli:dynamic",
    "value": {
        "type": "neo-apoli:weighted",
        "entries": [
            {
                "value": true,
                "weight": 1
            },
            {
                "value": false,
                "weight": 2
            }
        ]
    }
}
```

This example will return true 33.33% of the time and false 66.66% of the time.


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
