#   Damage Item

Deals damage to an item.


Type ID: `kaya:damage_item`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`amount` | [Int Provider][int_provider] | `1` | The amount of damage to deal.
`slot` | [Slot Provider][slot_provider] | | The slot of the item to damage.
`ignore_enchantments` | [Boolean Provider][boolean_provider] | `false` | Determines whether enchantments *(that can process changes in an item's durability)* are ignored.
`item_holder` | [Entity Provider][entity_provider] | *optional* | If specified, this player will be used as the holder of the item.


??? info

    The `item_holder` is mostly used for the following scenarios when damaging an item:
    
    - If the player is present and has infinite materials (e.g: in creative mode), the item will not be damaged.
    - if the player is present, the `minecraft:item_durability_changed` advancement criterion trigger is invoked.


### Example

```json
{
    "type": "kaya:damage_item",
    "amount": 4,
    "slot": "used_item_slot",
    "item_holder": "this"
}
```

This example will deal 4 damage to the item provided by the `kaya:used_item_slot` context parameter.


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
