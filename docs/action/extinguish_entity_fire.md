#   Extinguish Entity Fire

Extinguishes an entity that's on fire.


Type ID: `neo-apoli:extinguish_entity_fire`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to extinguish.


### Example

```json
{
    "type": "neo-apoli:extinguish_entity_fire",
    "entity": "actor"
}
```

This example will extinguish the entity provided by the `neo-apoli:actor_entity` context parameter.


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
