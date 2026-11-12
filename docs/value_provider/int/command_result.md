#   Command Result

Executes a command and provides its result.


Type ID: `kaya:command_result`


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
    "type": "kaya:command_result",
    "source": "server",
    "command": "execute if entity @e[type = #minecraft:skeletons]"
}
```

This example will provide the amount of entities included in the `#minecraft:skeletons` entity type tag is loaded in the current world.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td rowspan="3" style="text-align: center; vertical-align: middle">1.21.5</td>
        <td rowspan="2" style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
    <tr>
        <td style="vertical-align: middle">Accidentally removed when number providers were split to int/float.</td>
    </tr>
    <tr>
        <td style="vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Re-added the type</td>
    </tr>
</table>
