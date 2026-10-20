#   Time

Provides the current game time *(in ticks.)*


Type ID: `neo-apoli:time`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`period` | [Int Provider][int_provider] | *optional* | If specified, the remainder of the game time divided by this value will be provided instead.


### Example

```json
{
    "type": "neo-apoli:time",
    "period": 12000
}
```

This example will provide the remainder of the current game time divided by $12000$.


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
