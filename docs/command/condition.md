#   /condition { #condition_command }

Validates and invokes the specified condition.


???+ info

    This command provides the following context parameters by default:

    Parameter | Description
    ----------|------------
    `kaya:command/entity` | The entity that executed the command, or none if the server executed the command *(can be changed with `/execute as`)*
    `kaya:command/position` | The position of the entity that executed the command, or the current world's spawn position *(can be changed with `/execute at` or `/execute positioned`)*


## Syntax

```mcfunction
condition dump <id> [<indent>]

condition test <condition> with <parameters>

execute if kaya:condition <condition> with <parameters> ...
```


##  Arguments

- `<id>`: [identifier]({{ mc.identifier }})
    - The ID of the condition to encode and display as JSON in chat.
- `<condition>`: [identifier]({{ mc.identifier}}), or an [inlined_condition][condition]
    - The condition to invoke.
- `<parameters>`: [context_parameter_map][context_parameter_map]
    - The context to provide to the specified action.


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
        <td style="vertical-align: middle">Added the command.</td>
    </tr>
</table>
