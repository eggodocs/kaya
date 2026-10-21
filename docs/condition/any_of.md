#   Any Of

Checks if any of the conditions are fulfilled.


Type ID: `neo-apoli:any_of`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`conditions` | [Array][array] of [Conditions][condition] | | The conditions to check.


### Example

```json
{
    "type": "neo-apoli:any_of",
    "conditions": [
        {
            "type": "neo-apoli:is_entity_on_fire",
            "entity": "actor"
        },
        {
            "type": "neo-apoli:is_entity_invisible",
            "entity": "target"
        }
    ]
}
```

This example will check if the entity provided by the `neo-apoli:actor_entity` context parameter is on fire **or** if the entity provided by the `neo-apoli:target_entity` context parameter is invisible.


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
