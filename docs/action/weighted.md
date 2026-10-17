#   Weighted

Picks an entry at random and executes its action.


Type ID: `neo-apoli:weighted`


!!! note

    The chance of an entry being picked is determined by dividing the weight of the entry to the sum of all the entries' weights.<br>$(Chance = Weight_e \div (Weight_1 + Weight_2 + ... + Weight_n))$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entries` | [Array][array] of [Weighted Entries](#action_weighted_entry) | | The entries to pick a random entry from.


[](){ #action_weighted_entry }

???+ info "Weighted Entry"

    An object that contains an action and its weight.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `action` | [Action][action] | | The action to execute.
    `weight` | [Integer][integer] | | The weight of the entry. The value must be either 0 or higher.


### Example

```json
{
    "type": "neo-apoli:weighted",
    "entries": [
        {
            "action": {
                "type": "neo-apoli:set_entity_on_fire",
                "ticks": 200,
                "entity": "this"
            },
            "weight": 5
        },
        {
            "action": {
                "type": "neo-apoli:apply_effects",
                "effects": [
                    {
                        "id": "minecraft:poison",
                        "duration": 200
                    }
                ],
                "entity": "this"
            },
            "weight": 3
        },
        {
            "action": {
                "type": "neo-apoli:apply_effects",
                "effects": [
                    {
                        "id": "minecraft:regeneration",
                        "duration": 200
                    }
                ],
                "entity": "this"
            },
            "weight": 1
        }
    ]
}
```

This example has three entries to pick from: an entry that has a 55% chance $(5 \div 9 = 0.55...)$ of setting the entity from the `neo-apoli:this_entity` context parameter on fire for 5 seconds, an entry that has a 33% chance $(3 \div 9 = 0.33...)$ of applying a Poison I (00:10) status effect, and an entry that has an 11% chance $(1 \div 9 = 0.11...)$ of applying Regeneration I (00:10) status effect.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
