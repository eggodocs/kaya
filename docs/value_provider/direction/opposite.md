#   Opposite

Provides the opposite of a direction.


Type ID: `kaya:opposite`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`direction` | [Direction Provider][direction_provider] | | The direction to get its opposite.


### Example

```json
{
    "type": "kaya:opposite",
    "direction": "north"
}
```

This example will provide the opposite of north, which will be south.


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
