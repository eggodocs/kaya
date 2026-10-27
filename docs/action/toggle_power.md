#   Toggle Power

Toggles the state of a power that uses the [Toggle](../power/toggle.md) power type from an entity.


Type ID: `kaya:toggle_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The power to toggle the state of.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "kaya:toggle_power",
    "power": "example:toggleable_climbing@toggle",
    "entity": "this"
}
```

This example will toggle the state of the `example:toggleable_climbing@toggle` sub-power from the entity provided by the `kaya:this_entity` context parameter.


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
