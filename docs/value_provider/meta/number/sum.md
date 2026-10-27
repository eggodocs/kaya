#   Sum

Adds all the number values and uses the sum as the provided number value.


Type ID: `kaya:sum`


!!! note
    
    This number meta type can only provide the same kind of value of the field where it was used. *(e.g: if the field is a float provider, the number provider to specify should be a float provider or if the field is an int provider, the number provider to specify should be an int provider)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`values` | [Array][array] of Number Providers | | The numbers to get the sum of.


### Example

```json
{
    "type": "kaya:sum",
    "values": [
        {
            "type": "kaya:equipped_enchantment_level",
            "enchantment": "minecraft:fortune",
            "slot_group": "any",
            "entity": "this"
        },
        1
    ]
}
```

This example is an int provider that will provide the highest level of the `minecraft:fortune` enchantment of the equipped items from the entity provided by the `kaya:this_entity` context parameter + $1$. 

$(Value = EnchantmentLevel + 1)$


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
