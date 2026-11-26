#   /resource (Command)

Gets or sets the value of a float/int resource.


## Syntax


### Syntax tree

`/resource ...`

<ul>
    <li>
        <code>... <a href="#get">get</a> &lt;target&gt;</code>
        <ul>
            <li>
                <code>... float &lt;power&gt; [&lt;scale&gt;]</code>
            </li>
            <li>
                <code>... int &lt;power&gt;</code>
            </li>
        </ul>
    </li>
    <li>
        <code>... <a href="#set">set</a> &lt;targets&gt;</code>
        <ul>
            <li>
                <code>... float &lt;power&gt; &lt;floatValue&gt;</code>
            </li>
            <li>
                <code>... int &lt;power&gt; &lt;intValue&gt;</code>
            </li>
        </ul>
    </li>
</ul>


### Sub-commands


#### get

Queries the value of a resource (of a certain type) from an entity.


##### Syntax

```mcfunction
get <target> float <power> [<scale>]

get <target> int <power>
```


##### Arguments

- `<target>`: [entity](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity to get the resource from.
    - Must be a player name, a target selector, or a UUID. And the target selector must be a single type.
- `<power>`: [power_identifier][power_identifier]
    - The ID of the resource power/sub-power which value will be queried.
    - If `float` literal is specified prior to this argument, the power must be using the [Resource (Float) power type](../power/resource_float.md)
    - If `int` literal is specified prior to this argument, the power must be using the [Resource (Integer) power type](../power/resource_int.md)
- `<scale>`: [float](https://minecraft.wiki/w/Argument_types#brigadier:float)
    - Specifies the value by which the result is multiplied to.
    - If omitted, `1.0` will be used.


#### set

Sets the value of a resource (of a certain type) on an entity or entities.


##### Syntax

```mcfunction
set <targets> float <power> <value>

set <targets> int <power> <value>
```


##### Arguments

- `<targets>`: [entities](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity or entities to set the value of their resources of.
    - Must be a player name, a target selector, or a UUID.
- `<power>`: [power_identifier][power_identifier]
    - The ID of the resource power/sub-power which value will be modified.
    - If `float` literal is specified prior to this argument, the power must be using the [Resource (Float) power type](../power/resource_float.md)
    - If `int` literal is specified prior to this argument, the power must be using the [Resource (Integer) power type](../power/resource_int.md)
- `<value>`: [float](https://minecraft.wiki/w/Argument_types#brigadier:integer) or [integer](https://minecraft.wiki/w/Argument_types#brigadier:integer)
    - The new value of the resource.
    - If `float` literal is specified prior to this argument, the number must be a [float](https://minecraft.wiki/w/Argument_types#brigadier:integer).
    - If `int` literal is specified prior to this argument, the number must be an [integer](https://minecraft.wiki/w/Argument_types#brigadier:integer).


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
