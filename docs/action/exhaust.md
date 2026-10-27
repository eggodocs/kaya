#   Exhaust

Applies exhaustion to a player.


Type ID: `kaya:exhaust`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`amount` | [Float Provider][float_provider] | | The amount of exhaustion to apply.
`entity` | [Entity Provider][entity_provider] | | The player to apply the exhaustion to.


### Example

```json
{
    "type": "kaya:exhaust",
    "amount": 4.5,
    "entity": "this"
}
```

This example will apply exhaustion with the amount of $4.5$ to the player provided by the `kaya:this_entity` context parameter.


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
