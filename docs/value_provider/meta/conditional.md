#   Conditional

Provides the respective value if the specified condition is fulfilled or not.


Type ID: `neo-apoli:conditional`


!!! note

    This meta type can only provide the same kind of value of the field where it was used. (e.g: if the field is a boolean provider, the value providers to specify must be a boolean provider, etc.)


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check.
`on_true` | [Value Provider][value_provider] | | The value to provide if the condition returns true.
`on_false` | [Value Provider][value_provider] | | The value to provide if the condition returns false.


### Example

```json
{
    "type": "neo-apoli:conditional",
    "condition": {
        "type": "neo-apoli:is_entity_of_type",
        "entity_type": "minecraft:creeper",
        "entity": "target"
    },
    "on_true": 100,
    "on_false": 0
}
```

This example is an int provider that provides $100$ if the entity provided by the `neo-apoli:target_entity` context parameter is a Creeper, or $0$ if they're not.


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

