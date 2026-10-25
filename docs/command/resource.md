#   /resource

Gets or sets the value of a float/int resource.


## Syntax

```mcfunction
resource get <target> float <power> [<scale>]

resource get <target> int <power>

resource set <targets> float <power> <floatValue>

resource set <targets> int <power> <intValue>
```


##  Arguments

- `<target>`: [entity](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity to get the power from and modify its value.
    - Must be a player name, a target selector, or a UUID. And the target selector must be a single type.
- `<targets>`: [entity](https://minecraft.wiki/w/Argument_types#minecraft:entity)
    - The entity/entities to get the power from and modify its value.
    - Must be a player name, a target selector, or a UUID.
- `<power>`: [power_identifier][power_identifier]
    - Specifies the power to get/set the value of.
- `<scale>`: [float](https://minecraft.wiki/w/Argument_types#brigadier:float)
    - Specifies the value by which the result is multiplied
    - If omitted, `1.0` is used.
- `<floatValue>`: [float](https://minecraft.wiki/w/Argument_types#brigadier:float)
    - The new float value for the power.
- `<intValue>`: [integer](https://minecraft.wiki/w/Argument_types#brigadier:integer)
    - The new integer value for the power.
