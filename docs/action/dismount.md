#   Dismount

Dismounts an entity.


Type ID: `neo-apoli:dismount`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to dismount.


### Example

```json
{
    "type": "neo-apoli:dismount",
    "entity": {
        "type": "neo-apoli:selector",
        "selector": "@e[sort = random, limit = 1]"
    }
}
```

This example will dismount a random entity from the world.


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
