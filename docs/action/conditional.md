#   Conditional

Executes the respective action if the specified condition is fulfilled or not.


Type ID: `neo-apoli:conditional`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check.
`on_true` | [Action][action] | *optional* | If specified, this action will be executed if the condition returns true.
`on_false` | [Action][action] | *optional* | If specified, this action will be executed if the condition returns false.


### Example

```json
{
    "type": "neo-apoli:conditional",
    "condition": {
        "type": "neo-apoli:is_entity_of_type",
        "entity_type": "minecraft:creeper",
        "entity": "target"
    },
    "on_true": {
        "type": "neo-apoli:execute_command",
        "source": {
            "type": "neo-apoli:entity",
            "entity": "target"
        },
        "command": "summon lightning_bolt"
    }
}
```

This example will summon a lightning bolt at the entity referenced by the `neo-apoli:target_entity` context parameter if it's a creeper.


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
