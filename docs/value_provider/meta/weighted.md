#   Weighted

Picks an entry at random and provides its value.


Type ID: `kaya:weighted`


!!! note

    This meta type can only provide the same kind of value of the field where it was used. (e.g: if the field is a boolean provider, the value providers to specify must be a boolean provider, etc.)


!!! note

    The chance of an entry being picked is determined by dividing the weight of the entry to the sum of all the entries' weights.<br>$(Chance = Weight_e \div (Weight_1 + Weight_2 + ... + Weight_n))$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entries` | [Array][array] of [Weighted Entries](#weighted_entry) | | The entries to pick a random entry from.


[](){ #weighted_entry }

???+ info "Weighted Entry"

    An object that contains a [value provider][value_provider] and its weight.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `value` | [Value Provider][value_provider] | | The value to provide.
    `weight` | [Integer][integer] | | The weight of the entry. The value must be either 0 or higher.


### Example

```json
{
    "type": "kaya:weighted",
    "entries": [
        {
            "value": {
                "type": "kaya:item/attribute",
                "attribute": "minecraft:armor",
                "item": "used_item"
            },
            "weight": 5
        },
        {
            "value": {
                "type": "kaya:entity/attribute",
                "attribute": "minecraft:armor",
                "entity": "this"
            },
            "weight": 5
        },
        {
            "value": {
                "type": "kaya:entity/fluid_height",
                "fluid_tag": "#minecraft:water",
                "entity": "this"
            },
            "weight": 1
        }
    ]
}
```

This example is a float provider that has three entries to pick from:

- an entry that has 45% chance $(5 \div 11 = 0.45...)$ of providing the value of the `minecraft:armor` attribute from the item stack provided by the `kaya:used_item` context parameter.
- an entry that has a 45% chance $(5 \div 11 = 0.45...)$ of providing the value of the `minecraft:armor` attribute from the entity provided by the `kaya:this_entity` context parameter.
- an entry that has a 9% chance $(1 \div 11 = 0.09...)$ of providing the height of the water fluid from the entity provided by the `kaya:this_entity` context parameter.


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

