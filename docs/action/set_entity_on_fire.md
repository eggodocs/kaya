#   Set Entity on Fire

Sets an entity on fire for a specified amount of ticks.


Type ID: `kaya:set_entity_on_fire`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`ticks` | [Int Provider][int_provider] | | The amount of ticks the entity will be on fire for.
`entity` | [Entity Provider][entity_provider] | | The entity to set on fire.


### Example

```json
{
    "type": "kaya:set_entity_on_fire",
    "ticks": 100,
    "entity": "damaging_entity"
}
```

This example will set the entity provided by the `kaya:damaging_entity` context parameter on fire for 5 seconds.


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
