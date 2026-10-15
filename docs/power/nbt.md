#   NBT

Provides a storage for storing arbitrary NBT data.


Type ID: `neo-apoli:nbt`


!!! tip

    This power type is to be used in conjunction with the `/data ... neo-apoli:power` command, which can query or modify its contents.


### Format

*No additional fields.*


!!! warning

    This power type does **not** support the `active_condition` field.


### Example

=== "Power JSON (`example:data`)"

    ```json
    {
        "type": "neo-apoli:nbt"
    }
    ```

=== "Example `.mcfunction` file"

    ```mcfunction
    #   Set the contents of the 'example:data' power
    data merge neo-apoli:power @s example:data {value: "Hello world!", cool_items: [{id: "minecraft:egg", count: 1}, {id: "minecraft:diamond", count: 1}]}

    #   Count how many elements are in the 'cool_items' NBT of the 'example:data' power
    execute store result score #stacks example if data neo-apoli:power @s example:data cool_items[]

    #   Display how many item stacks are in the 'cool_items' NBT of the 'example:data' power
    tellraw @a ["There are ", {"score": {"name": "#stacks", "objective": "example"}}, " cool item stack(s)!"]
    ```

This example provides a power to be used as a storage for NBT data and a function file that would set and display some of its contents.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>