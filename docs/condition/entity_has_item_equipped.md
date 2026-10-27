#   Entity Has Item Equipped

Checks if an entity has an item equipped to a specific slot.


Type ID: `kaya:entity_has_item_equipped`


???+ info

    This type will provide the following context parameters to its `equipped_condition` when checking the items on the specified slot:

    Parameters | Description
    -----------|------------
    `kaya:equipped_item` | The item stack equipped on the slot.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`equipped_condition` | [Condition][condition] | *optional* | If specified, this condition will be checked on the item from the specified slot.
`slot` | [Equipment Slot Group][equipment_slot_group] | | The slot to check the items for.
`entity` | [Entity Provider][entity_provider] | | The entity to get the items from.


### Example

```json
{
    "type": "kaya:entity_has_item_equipped",
    "equipped_condition": {
        "type": "kaya:item_matches_predicate",
        "predicate": "*[minecraft:food]",
        "item": "equipped_item"
    },
    "slot": "hand",
    "entity": "this"
}
```

This example will check if items that has the `minecraft:food` item component is in any of the hands of the entity provided by the `kaya:this_entity` context parameter.


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
