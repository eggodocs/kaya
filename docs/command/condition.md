#   /condition (Command)

Validates and invokes the specified condition.


??? note

    This command is also available as a sub-command for `/execute` with the same syntax as `/condition test`:

    ```mcfunction
    execute (if|unless) kaya:condition <condition> with <parameters>
    ```


## Syntax


### Syntax tree

`/condition ...`

<ul>
    <li>
        <code>... <a href="#test">test</a> &lt;condition&gt; with &lt;parameters&gt;</code>
    </li>
    <li>
        <code>... <a href="#dump">dump</a> &lt;condition&gt; [&lt;indent&gt;]</code>
    </li>
</ul>


### Sub-commands


#### test

Invokes a specific condition.


???+ info

    This command provides the following context parameters by default:

    Parameter | Description
    ----------|------------
    `kaya:command/entity` | The entity that executed the command, or none if the server executed the command *(can be changed with `/execute as`)*
    `kaya:command/position` | The position of the entity that executed the command, or the current world's spawn position *(can be changed with `/execute at` or `/execute positioned`)*


##### Syntax

```mcfunction
test <condition> with <parameters>
```


##### Arguments

- `<condition>`: [identifier]({{ mc.identifier }}) or [condition][condition]
    - The condition to invoke.
- `<parameters>`: [context_parameter_map][context_parameter_map]
    - The context to provide to the specified condition.


#### dump

Encodes the condition to JSON and dumps it in the chat (visible only to the executor of the command.)


##### Syntax

```mcfunction
dump <condition> [<indent>]
```


##### Arguments

- `<condition>`: [identifier]({{ mc.identifier }})
    - The ID of the condition to encode and dump its JSON.
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
