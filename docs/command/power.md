#   Power (Command)

Grants, revokes, or lists a set of powers to or from an entity or multiple entities.


##  Syntax

### Syntax tree

`/power ...`

<ul>
    <li>
        <code>... <a href="#grant">grant</a> &lt;targets&gt; &lt;power&gt; [&lt;source&gt;]</code>
    </li>
    <li>
        <code>... <a href="#revoke">revoke</a> &lt;targets&gt; (all|&lt;power&gt;) [&lt;source&gt;]</code>
    </li>
    <li>
        <code>... <a href="#remove">remove</a> &lt;targets&gt; &lt;power&gt;</code>
    </li>
    <li>
        <code>... <a href="#clear">clear</a> &lt;targets&gt;</code>
    </li>
    <li>
        <code>... <a href="#list">list</a> &lt;target&gt; [&lt;includeSubPowers&gt;]</code>
    </li>
    <li>
        <code>... <a href="#dump">dump</a> &lt;power&gt; [&lt;indent&gt;]</code>
    </li>
</ul>

### Sub-commands

#### grant

Grants a single or multiple powers to an entity or entities.

##### Syntax

```mcfunction
grant <targets> <power> [<source>]
```

##### Arguments

- `<targets>`: [entities](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity or entities to grant the power or powers to.
    - Must be a player name, a target selector, or a UUID.
- `<power>`: [power_identifier][power_identifier] or [power_tag]({{ mc.tag }})
    - The ID of either a specific power/sub-power, or tag that contains multiple powers to grant.
- `<source>`: [identifier]({{ mc.identifier }})
    - Specifies the ID of where the power came from.
    - If omitted, `kaya:command` will be used.


#### revoke

Revokes a single or multiple powers from a specific source from an entity or entities.

##### Syntax

```mcfunction
revoke <targets> (all|<power>) [<source>]
```

##### Arguments

- `<targets>`: [entities](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity or entities to revoke a power from.
    - Must be a player name, a target selector, or a UUID.
- `all`: literal
    - Determines all powers will be revoked from the specified source.
- `<power>`: [power_identifier][power_identifier] or [power_tag]({{ mc.tag }})
    - The ID of either a specific power/sub-power, or tag that contains multiple powers to revoke from the specified source.
- `<source>`: [identifier]({{ mc.identifier }})
    - Specifies the source ID of the powers that will be revoked.
    - If omitted, `kaya:command` will be used.


#### remove

Revokes a single or multiple powers from every source from an entity or entities.

##### Syntax

```mcfunction
remove <targets> <power>
```

##### Arguments

- `<targets>`: [entities](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity or entities to revoke the power from.
    - Must be a player name, a target selector, or a UUID.
- `<power>`: [power_identifier][power_identifier] or [power_tag]({{ mc.tag }})
    - The ID of either a specific power/sub-power, or tag that contains multiple powers to revoke.


#### clear

Clears all powers of an entity or entities.

##### Syntax

```mcfunction
clear <targets>
```

##### Arguments

- `<targets>`: [entities](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity or entities to clear the powers of.
    - Must be a player name, a target selector, or a UUID.


#### list

Lists all the powers of an entity.

##### Syntax

```mcfunction
list <target> [<includeSubPowers>]
```

##### Arguments

- `<target>`: [entity](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity to list the powers of.
    - Must be a player name, a target selector, or a UUID. And the target selector must be a single type.
- `<includeSubPowers>`: [bool](https://minecraft.wiki/w/Argument_types#brigadier:bool)
    - Determines whether to include sub-powers in the displayed list.
    - If omitted, this will default to `false`.


#### dump

Encodes the power into JSON and dumps it in the chat (visible only to the executor of the command.)

##### Syntax

```mcfunction
dump <power> [<indent>]
```

##### Arguments

- `<power>`: [power_identifier][power_identifier]
    - The ID of the power/sub-power to encode and dump its JSON.
- `<indent>`: [integer](https://minecraft.wiki/w/Argument_types#brigadier:integer)
    - Specifies the indent for each line.
    - If omitted, this will default to `4`.
