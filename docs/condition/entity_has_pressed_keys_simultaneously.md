#   Entity Has Pressed Keys Simultaneously

Checks if a player has pressed multiple keybindings simultaneously.


Type ID: `neo-apoli:entity_has_pressed_keys_simultaneously`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`keys` | [Array][array] of [String Providers][string_provider] | | The IDs of the keybindings to check.
`offset` | [Int Provider][int_provider] | `3` | Determines the offset to apply to the time the keybindings were pressed when checked *(in ticks.)*
`entity` | [Entity Provider][entity_provider] | | The entity to get the state of the keybindings from.


### Example

```json
{
    "type": "neo-apoli:entity_has_pressed_keys_simultaneously",
    "keys": [
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
