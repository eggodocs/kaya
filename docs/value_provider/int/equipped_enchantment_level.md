#   Equipped Enchantment Level

Provides the level of an enchantment from items equipped by an entity.


Type ID: `neo-apoli:equipped_enchantment_level`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`enchantment` | [Identifier]({{ mc.enchantment_identifier }}) | | The ID of the enchantment.
`slot_group` | [Equipment Slot Group][equipment_slot_group] | `"any"` | The group of equipment slots to check.
`calculation` | [Calculation](#calculation) | `"max"` | Determines how the level of the enchantment from equipped items is calculated.
`entity` | [Entity Provider][entity_provider] | | The entity get the equipped items from.


[](){ #calculation }

???+ info "Calculation"

    A [string][string] that determines how the level of an enchantment from multiple items is calculated.


    ### Values

    Value | Description
    ------|------------
    `sum` | Provides the sum of all the levels of the enchantment from multiple items.
    `max` | Provides the highest level of the enchantment from multiple items.


### Example

```json
{
    "type": "neo-apoli:equipped_enchantment_level",
    "enchantment": "minecraft:protection",
    "entity": "this"
}
```

This example provides the highest level of the `minecraft:protection` enchantment from all the items equipped by the entity provided by the `neo-apoli:this_entity` context parameter.


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
