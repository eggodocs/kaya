#   Conditional Composite

Invokes and returns the value provided by an entry whose condition is fulfilled, or the specified default if no entries matched.


Type ID: `neo-apoli:conditional/composite`


!!! note

    This meta type can only provide the same kind of value of the field where it was used. (e.g: if the field is a boolean provider, the value providers to specify must be a boolean provider, etc.)


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entries` | [Array][array] of [Entries](#entry) | | The entries to check, invoke, and return the value of.
`default` | [Value Provider][value_provider] | | The value to provide if none of the entries matched.


[](){ #entry }

???+ info "Entry"

    An object that contains the [condition][condition] to check and the [value][value_provider] to provide.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `condition` | [Condition][condition] | | The condition to check.
    `value` | [Value Provider][value_provider] | | The value to provide if the condition is fulfilled.


### Example

```json
{
    "type": "neo-apoli:conditional/composite",
    "entries": [
        {
            "condition": {
                "type": "neo-apoli:is_entity_on_fire",
                "entity": "actor"
            },
            "value": {
                "type": "neo-apoli:world",
                "position": {
                    "type": "neo-apoli:entity/position",
                    "entity": "actor"
                }
            }
        },
        {
            "condition": {
                "type": "neo-apoli:is_entity_sneaking",
                "entity": "target"
            },
            "value": {
                "type": "neo-apoli:world",
                "position": {
                    "type": "neo-apoli:offset",
                    "vector": {
                        "type": "neo-apoli:entity/position",
                        "entity": "this"
                    },
                    "offset": [
                        0.0,
                        -1.0,
                        0.0
                    ]
                }
            }
        }
    ],
    "default": "example:fallback_block"
}
```

This example is a block provider which has two entries:

- the first one provides the block at the feet of the entity provided by the `neo-apoli:actor_entity` context parameter if they're on fire
- the second one provides the block below the entity provided by the `neo-apoli:target_entity` context parameter if they're sneaking. 


If none of these entries fulfilled their condition, the block provided by the `example:fallback_block` context parameter will be provided instead.


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
