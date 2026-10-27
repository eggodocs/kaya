#   Modify Item Wearable

Modifies whether the entity holding the power can equip and item in the specified equipment slots.


Type ID: `kaya:modify/item/wearable`


???+ info

    This type provides the following context parameters when an item is about to be equipped into an equipment slot:

    Parameter | Description
    ----------|------------
    `kaya:worn_item` | The item that will be put into an equipment slot.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`slots` | [Slots Map](#slots_map) | | Determines which items to allow in which equipment slots.


!!! warning

    This type does **not** support the `active_condition` field.


[](){ #slots_map }

???+ info "Slots Map"

    An object that contains key-value pairs where the keys are names of equipment slots and its values are [conditions][condition].


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `offhand` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the offhand equipment slot.
    `feet` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the feet equipment slot.
    `legs` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the legs equipment slot.
    `chest` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the chest equipment slot.
    `head` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the head equipment slot.
    `body` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the body equipment slot.
    `saddle` | [Condition][condition] | *optional* | If specified, items which fulfill this condition can be equipped in the saddle equipment slot.


### Example

```json
{
    "type": "kaya:modify/item/wearable",
    "head": {
        "type": "kaya:any_of",
        "conditions": [
            {
                "type": "kaya:item_matches_ingredient",
                "ingredient": "#minecraft:head_armor",
                "item": "worn_item"
            },
            {
                "type": "kaya:item_matches_ingredient",
                "ingredient": "#c:glass_blocks",
                "item": "worn_item"
            }
        ]
    }
}
```

This example allows any item included in either the `#minecraft:head_armor` or `#c:glass_blocks` item tags to be equipped to the head equipment slot.


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
