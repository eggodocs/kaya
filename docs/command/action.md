#   /action (Command)

Validates and executes the specified action.


???+ info

    This command provides the following context parameters by default:

    Parameter | Description
    ----------|------------
    `kaya:command/entity` | The entity that executed the command, or none if the server executed the command *(can be changed with `/execute as`)*
    `kaya:command/position` | The position of the entity that executed the command, or the current world's spawn position *(can be changed with `/execute at` or `/execute positioned`)*


## Syntax

### Syntax tree

`/action ...`

<ul>
    <li>
        <code>... <a href="#execute">execute</a> &lt;action&gt; with &lt;parameters&gt;</code>
    </li>
    <li>
        <code>... <a href="#dump">dump</a> &lt;action&gt; [&lt;indent&gt;]</code>
    </li>
</ul>

### Sub-commands

#### execute

Executes a specific action.

##### Syntax

```mcfunction
execute <action> with <parameters>
```

##### Arguments

- `<action>`: [identifier], [tag]({{ mc.tag }}), or [action][action]
    - The action(s) to execute.
- `<parameters>`: [context_parameter_map][context_parameter_map]
    - The context to provide to the specified action.


#### dump

Encodes the action to JSON and dumps it in the chat (visible only to the executor of the command.)

##### Syntax

```mcfunction
dump <action> [<indent>]
```

##### Arguments

- `<action>`: [identifier]({{ mc.identifier }})
    - The ID of the action to encode and dump its JSON.
- `<indent>`: [integer](https://minecraft.wiki/w/Argument_types#brigadier:integer)
    - Specifies the indent for each line.
    - If omitted, this will default to `4`.


## History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the command.</td>
    </tr>
</table>
