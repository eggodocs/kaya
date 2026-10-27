#   Multiple

Allows for defining powers in a single file.


Type ID: `kaya:multiple`


???+ tip

    Sub-powers can be referenced by using the `@` character. (e.g: `namespace:path/to/power@sub_power`)


### Format

*Any fields (except `type`, `name`, `description`, `hidden`, `fabric:load_conditions`, or fields that starts with `$`) will be considered as a "sub-power."*


!!! warning

    This type does **not** support the `active_condition` field.


### Example

```json
{
    "type": "kaya:multiple",
    "cooldown": {
        "type": "kaya:cooldown",
        "hud_element": {
            "type": "kaya:resource_bar"
        },
        "cooldown": 200
    },
    "trigger": {
        "type": "kaya:callback/damage/dealt",
        "on_hit_action": {
            "type": "kaya:trigger_power_cooldown",
            "power": "*:*@cooldown",
            "entity": "this"
        }
    },
    "epic_damage": {
        "type": "kaya:modify/damage/dealt",
        "modifiers": [
            {
                "type": "kaya:multiply_multiplicative",
                "phase": "total",
                "amount": 0.5
            }
        ],
        "active_condition": {
            "type": "kaya:compare",
            "comparison": {
                "type": "kaya:float",
                "comparator": "==",
                "first": {
                    "type": "kaya:power/cooldown/progress",
                    "power": "*:*@cooldown",
                    "entity": "this"
                },
                "second": 1.0
            }
        }
    }
}
```

This example defines three sub-powers: `cooldown` which uses the `kaya:cooldown` power type, `trigger` which uses the `kaya:callback/damage/dealt` power type to trigger the `cooldown` sub-power when damage is dealt, and `epic_damage` which uses the `modify/damage/dealt` power type to deal 50% more damage when the cooldown of `cooldown` is not in progress. 


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
