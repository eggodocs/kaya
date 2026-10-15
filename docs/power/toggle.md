#   Toggle

Provides a boolean state that can be cycled with either a [key][key_reference] or the `toggle_power` action type.


Type ID: `neo-apoli:toggle`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`action` | [Action][action] | *optional* | If specified, this action will be executed when the boolean state of the power is cycled.
`key` | [Key Reference][key_reference] | *optional* | If specified, the boolean state of this power will be cycled if a key that matches this reference is pressed.
`retain_state` | [Boolean Provider][boolean_provider] | `true` | Determines whether the boolean state will remain even if the power is no longer active.
`active_by_default` | [Boolean Provider][boolean_provider] | `true` | Determines whether the boolean state should be active by default.


### Example

```json
{
    "type": "neo-apoli:toggle",
    "action": {
        "type": "neo-apoli:execute_command",
        "source": {
            "type": "neo-apoli:entity",
            "entity": "this"
        },
        "command": "me toggled a power!"
    },
    "key": "key.loadToolbarActivator"
}
```

This example provides a toggle that can be cycled by pressing the `key.loadToolbarActivator` keybinding.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
