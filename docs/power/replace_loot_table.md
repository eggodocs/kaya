#   Replace Loot Table

Replaces a loot table with another loot table.


Type ID: `kaya:replace_loot_table`


???+ info

    This type provides the following context parameters depending on the type of the loot table:

    === "Barter"

        Parameter | Description
        ----------|------------
        `kaya:actor_entity` | The entity holding the power.
        `kaya:target_entity` | The Piglin that was bartered with.

    === "Block"

        Parameter | Description
        ----------|------------
        `kaya:actor_entity` | The entity holding the power.
        `kaya:block` | The block broken by the player.
        `kaya:tool_item` | The item used by the player for breaking a block.

    === "Chest"

        Parameter | Description
        ----------|------------
        `kaya:actor_entity` | The entity holding the power.
        `kaya:target_entity` | The player that opened a chest block.
        `kaya:block` | The chest block opened by the player.

    === "Entity"

        Parameter | Description
        ----------|------------
        `kaya:actor_entity` | The entity holding the power
        `kaya:target_entity` | The entity that died.
        `kaya:block` | The block at the position of the entity that died.

    === "Fishing"

        Parameter | Description
        ----------|------------
        `kaya:actor_entity` | The entity holding the power.
        `kaya:target_entity` | The fishing bobber of the entity holding the power.
        `kaya:block` | The block at the position of the fishing bobber.
        `kaya:tool_item` | The rod item used for fishing.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`replacements` | [Replacement Map](#replacement_map) | | Determines which loot tables to replace with other loot tables.
`priority` | [Integer][integer] | `0` | Determines the order of which powers of this type will be iterated.


??? question "About priorities"

    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be executed first before those that have lower priority values.

[](){ #replacement_map }

???+ info "Replacement Map"

    The `replacements` field has the following format:

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `<key>` | [String][string] | | Determines the loot table to replace `<key>` with.


    !!! note

        `<key>` refers to a string formatted as a regular expression, where it will find loot tables where its ID matches the expression. See [Wikipedia: Regular expression](https://en.wikipedia.org/wiki/Regular_expression) for more information and [RegExr](https://regexr.com/) to test regular expressions online.


### Example

=== "Power JSON"

    ```json
    {
        "type": "kaya:replace_loot_table",
        "replacements": {
            "([a-z0-9\\-_]+):blocks/([a-z0-9\\-_/]+)": "example:blocks/$1/$2"
        }
    }
    ```

=== "Loot table JSON (`example:blocks/minecraft/diamond_ore`)"

    ```json
    {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1.0,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:diamond_block"
                    }
                ]
            }
        ]
    }
    ```

This example will replace loot tables of any blocks with loot tables created with the naming scheme: `example:blocks/<namespace>/<path>`. In the provided loot table example, it will replace the diamonds dropped by diamond ores with a diamond block.


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
