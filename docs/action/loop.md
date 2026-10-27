#   Loop

Executes an action at the specified amount of times in a single tick.


Type ID: `kaya:loop`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`before_action` | [Action][action] | *optional* | If specified, this action will be executed before the loop starts.
`after_action` | [Action][action] | *optional* | If specified, this action will be executed after the loop completes.
`iterations` | [Int Provider][int_provider] | | Determines the amount of times this action should be looped.
`action` | [Action][action] | | The action to execute for each iteration in the loop.


### Example

```json
{
    "type": "kaya:loop",
    "iterations": {
        "type": "kaya:random/uniform",
        "min": 0,
        "max": 10
    },
    "action": {
        "type": "kaya:execute_command",
        "source": {
            "type": "kaya:entity",
            "entity": "this"
        },
        "command": "say Hello!"
    }
}
```

This example makes the entity say "Hello!" a random amount of times (0 to 10 times).


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
