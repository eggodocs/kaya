#   Side

Executes an action when it's invoked on a specific logical side of the game.


Type ID: `neo-apoli:side`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`side` | [Environment](#environment) | | Determines when to execute the action when invoked on the specified logical side.
`action` | [Action][action] | | The action to execute.


[](){ #environment }

???+ info "Environment"

    A [string][string] that determines when an action is invoked on which logical side.

    Value | Description
    ------|------------
    `client` | The action was invoked on the logical client side.
    `server` | The action was invoked on the logical server side.


### Example

```json
{
    "type": "neo-apoli:side",
    "side": "server",
    "action": {
        "type": "neo-apoli:add_velocity",
        "method": "single",
        "space": "local",
        "entity": "this",
        "velocity": [
            0.0,
            1.0,
            1.5
        ]
    }
}
```

This example will only add velocity to the entity from the `neo-apoli:this_entity` context parameter on the server side.


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
