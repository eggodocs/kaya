#   Power Cooldown Remaining Ticks

Provides the remaining ticks of a power that has a cooldown.


Type ID: `neo-apoli:power/cooldown/remaining_ticks`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The ID of the power.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "neo-apoli:power/cooldown/remaining_ticks",
    "power": "example:lightning_strike"/*(1)!*/,
    "entity": "this"
}
```


1. The location of the file is `data/example/neo-apoli/lightning_strike.json`


This example will provide the remaining ticks of the cooldown for the `example:lightning_strike` power.


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
