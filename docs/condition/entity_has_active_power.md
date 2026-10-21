#   Entity Has Active Power

Checks if a specified power from an entity is considered active.


Type ID: `neo-apoli:entity_has_active_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The power to check.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "neo-apoli:entity_has_active_power",
    "power": "example:powder_snow_runner",
    "entity": "this" 
}
```

This example will check if the `example:powder_snow_runner` power from the entity provided by the `neo-apoli:this_entity` context parameter is considered active.


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
