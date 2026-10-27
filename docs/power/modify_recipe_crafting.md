#   Modify Recipe Crafting

Modifies a recipe and executes an action upon the recipe being modified.


Type ID: `kaya:modify/recipe/crafting`


???+ info

    This type provides the following context parameters when modifying the result of a crafting recipe or taking the result item stack of a crafted recipe:

    === "From the inventory"

        Parameter | Description
        ----------|------------
        `kaya:crafted_item` | The result item stack of the crafted recipe.
        `kaya:crafted_item_slot` | The slot of the result item stack.

    === "From a crafting block"

        Parameter | Description
        ----------|------------
        `kaya:crafting_block` | The block used for crafting the item. (e.g: crafting table)
        `kaya:crafted_item` | The result item stack of the crafted recipe.
        `kaya:crafted_item_slot` | The slot of the result item stack.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`recipe` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, only crafting recipes with this ID will have its result item modified or execute the specified actions.
`replacement` | [Item Stack][item_stack] | *optional* | If specified, the result item stack of the crafted recipe will be replaced with this item stack.
`on_craft_action` | [Action][action] | *optional* | If specified, this action will be executed upon crafting an item.
`on_take_action` | [Action][action] | *optional* | If specified, this action will be executed upon **before** the crafted item is taken from its slot.
`priority` | [Integer][integer] | `0` | Determines the order of which powers of this type will be iterated.

??? question "About priorities"

    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be checked and executed first before those that have lower priority values.


### Example

```json
{
    "type": "kaya:modify/recipe/crafting",
    "on_take_action": {
        "type": "kaya:conditional",
        "condition": {
            "type": "kaya:parameter_exists",
            "parameter": {
                "type": "kaya:block",
                "name": "crafting_block"
            }
        },
        "on_true": [
            {
                "type": "kaya:execute_command",
                "source": {
                    "type": "kaya:entity",
                    "entity": "this"
                },
                "command": "tellraw @s {\"text\": \"The used crafting block has been turned into planks!\", \"color\": \"gray\", \"italic\": true}"
            },
            {
                "type": "kaya:place_block",
                "position": {
                    "type": "kaya:block/position",
                    "block": "crafting_block"
                },
                "block": "minecraft:oak_planks",
                "mode": "replace"
            }
        ]
    },
    "active_condition": {
        "type": "kaya:item_matches_ingredient",
        "ingredient": "minecraft:wooden_sword",
        "item": "crafted_item"
    }
}
```

This example replaces the used crafting block into an Oak Planks when the crafted item is taken from the result slot of the said crafting block.


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
