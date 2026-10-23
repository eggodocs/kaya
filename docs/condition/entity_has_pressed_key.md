#   Entity Has Pressed Key

Checks if an entity has pressed a keybinding.


Type ID: `neo-apoli:entity_has_pressed_key`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`key` | [Array][array] of [Key Predicates][key_predicate] or single [Key Predicate][key_predicate] | | The key predicate to check.
`entity` | [Entity Provider][entity_provider] | | The entity to get the state of the keybindings from.


### Example

```json
{
    "type": "neo-apoli:entity_has_pressed_keys_simultaneously",
    "key": [
        "key.hotbar.0",
        "key.hotbar.1"
    ],
    "entity": "this"
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter has pressed the `key.hotbar.0` and `key.hotbar.1` keybindings simultaneously.


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
