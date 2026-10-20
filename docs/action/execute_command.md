#   Execute Command

Executes a command.


Type ID: `neo-apoli:execute_command`


!!! warning

    This type is **server-side** only.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`source` | [Command Source Provider][command_source_provider] | | The command source to use for executing the command.
`command` | [String Provider][string_provider] | | The command to execute.


### Example

```json
{
    "type": "neo-apoli:execute_command",
    "source": "server",
    "command": {
        "type": "neo-apoli:weighted",
        "entries": [
            {
                "value": "say Hello world!",
                "weight": 1
            },
            {
                "value": "execute at @e run summon lightning_bolt",
                "weight": 1
            },
            {
                "type": "give @a diamond",
                "weight": 1
            }
        ]
    }
}
```

This example will execute one of the three commands picked at random with $33.33...\%$ chance each:

- The server will output "Hello world!"
- A lightning bolt will be summoned at all entities currently loaded.
- All players will be given a diamond.


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
