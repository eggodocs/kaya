#   Conditional Composite

Executes the action of an entry whose condition is fulfilled, or executes the specified default action if no entries matched.


Type ID: `neo-apoli:conditional/composite`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entries` | [Array][array] of [Entries](#entry) | | The pairs of action and condition to check and execute.
`default` | [Action][action] | *optional* | If specified, this action will be executed if none of the specified entries were executed.


[](){ #entry }

???+ info "Entry"

    An object that contains the [condition][condition] to check and the [action][action] to execute.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `condition` | [Condition][condition] | | The condition to check.
    `action` | [Action][action] | | The action to execute if the condition is fulfilled.


### Example

```json
{
    "type": "neo-apoli:conditional/composite",
    "entries": [
        {
            "condition": {
                "type": "neo-apoli:is_entity_sneaking",
                "entity": "this"
            },
            "action": {
                "type": "neo-apoli:set_entity_on_fire",
                "entity": "this",
                "ticks": 200
            }
        },
        {
            "condition": {
                "type": "neo-apoli:is_entity_climbing",
                "entity": "this"
            },
            "action": {
                "type": "neo-apoli:explode",
                "block_interaction": "destroy",
                "power": 8.0,
                "position": {
                    "type": "neo-apoli:entity/position",
                    "entity": "this"
                }
            }
        }
    ],
    "default": {
        "type": "neo-apoli:execute_command",
        "source": "server",
        "command": "tellraw @a {\"text\": \"None of the entries matched!\", \"color\": \"gray\", \"italic\": true}"
    }
}
```

This example has two entries: the entity will be set on fire for 5 seconds if they're sneaking, and the entity will explode (with an explosion that has a power of 8 and destroys blocks) if they're climbing.


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
