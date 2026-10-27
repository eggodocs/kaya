#   Trigger Power Cooldown

Triggers the cooldown of a power from an entity.


Type ID: `kaya:trigger_power_cooldown`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The power to trigger the cooldown of.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "kaya:trigger_power_cooldown",
    "power": "example:cooldown",
    "entity": "actor"
}
```

This example will trigger the cooldown of the `example:cooldown` power from the entity provided by the `kaya:actor_entity` context parameter.


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
