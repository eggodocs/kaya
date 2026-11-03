#   /action { #action_command }

Validates and executes the specified action.


???+ info

    This command provides the following context parameters by default:

    Parameter | Description
    ----------|------------
    `kaya:command/entity` | The entity that executed the command, or none if the server executed the command *(can be changed with `/execute as`)*
    `kaya:command/position` | The position of the entity that executed the command, or the current world's spawn position *(can be changed with `/execute at` or `/execute positioned`)*


## Syntax

```mcfunction
action dump <id> [<indent>]

action execute <action> with <parameters>
```


##  Arguments

- `<id>`: [identifier]({{ mc.identifier }})
    - The ID of the action to encode and display as JSON in chat.
- `<action>`: [identifier]({{ mc.identifier}}), [tag]({{ mc.tag }}), or an [inlined_action][action]
    - The action(s) to execute.
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
