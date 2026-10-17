#   Modify Item Use

Modifies the interaction of an item.


Type ID: `neo-apoli:modify/item/use`


!!! note "Context info"

    This power type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `neo-apoli:used_item_slot` | The slot of the item used by the player.
    `neo-apoli:used_item` | The item used by the player.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`on_use_action` | [Action][action] | | The action to execute when the player interacts with an item.
`result` | [Interaction Result][interaction_result] | `success` | Determines the result of the player's interaction with an item.
`hands` | [Array][array] of [Hands][hand] | `["main_hand", "off_hand"]` | Determines whether to trigger instances of this type when the player interacts with an item with the specified hands.
`trigger_type` | String | | Determines when instances of this type should be triggered.
`priority` | [Integer][integer] | `0` | Determines the order of which instances of this type is checked and executed.


??? question "About priorities"

    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be checked and executed first before those that have lower priority values.

??? note "Trigger types"

    Each item has specific "triggers" that indicates when a player is interacting with an item. The "triggers" are as follows:

    Value | Description
    ------|------------
    `instant` | The player interacted with an item that doesn't have a use duration but may have effects that are instantly triggered (e.g: thrown an ender pearl, a splash potion, or any throwable items.)
    `start` | The player started interacting with an item that has a use duration.
    `stop` | The player stopped interacting with an item that has a use duration.
    `finish` | The player finished interacting with an item that has a use duration (e.g: finished consuming a consumable item, or finished charging a bow.)
    `during` | The player is using an item with a use duration every tick (e.g: charging a bow.)


### Example

```json
{
    "type": "neo-apoli:modify/item/use",
    "on_use_action": {
        "type": "neo-apoli:apply_effects",
        "effects": [
            {
                "id": "minecraft:regeneration",
                "duration": 200,
                "amplifier": 1,
                "show_icon": true
            }
        ],
        "entity": "this"
    },
    "trigger_type": "finish",
    "active_condition": {
        "type": "neo-apoli:item_matches_predicate",
        "predicate": "*[minecraft:food]",
        "item": "used_item"
    }
}
```

This example will give the player Regeneration II (00:05) after it consumes any item that has the `minecraft:food` item component.


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
