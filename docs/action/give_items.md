#   Give Items

Gives item stacks to an entity.


Type ID: `kaya:give_items`


???+ info

    This type provides the following context parameters to the `give_action` field:

    Parameter | Description
    ----------|------------
    `kaya:given_slot` | The slot for the given item stack.
    `kaya:given_item` | The item stack given to the entity.


??? note "Logic for giving items"

    If an indexed item has a specified slot, and the item stack couldn't be placed into the slot, it will be inserted into any available slots in the entity's inventory. If the item stack still couldn't be inserted into the entity's inventory, it will be dropped.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`give_action` | [Action][action] | *optional* | If specified, this action will be executed for every item given to the entity.
`stacks` | [Array][array] of [Indexed Stacks][indexed_stack] | | The item stacks to give to the entity.
`entity` | [Entity Provider][entity_provider] | | The entity to give the item stacks to.


### Example

```json
{
    "type": "kaya:give_items",
    "stacks": [
        {
            "slot": "hotbar.0",
            "id": "minecraft:wooden_sword"
        },
        {
            "slot": "hotbar.1",
            "id": "minecraft:wooden_pickaxe"
        },
        {
            "id": "minecraft:shield"
        }
    ],
    "entity": "this"
}
```

This example will give the following items to the entity provided by the `kaya:this_entity` context parameter:

- A wooden sword placed into the entity's first hotbar slot.
- A wooden pickaxe placed into the entity's second hotbar slot.
- A shield.


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
