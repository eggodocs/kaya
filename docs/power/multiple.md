#   Multiple

Allows for defining powers in a single file.


Type ID: `neo-apoli:multiple`


!!! note

    Sub-powers can be referenced by using the `@` character. (e.g: `namespace:path/to/power@sub_power`)


### Format

Any fields except `type`, `name`, `description`, `hidden`, `fabric:load_conditions`, or fields that starts with `$` will be considered as a "sub-power."


!!! warning

    This power type does **not** support the `active_condition` field.


### Example

```json
{
    "type": "neo-apoli:multiple",
    "cooldown": {
        "type": "neo-apoli:cooldown",
        "hud_element": {
            "type": "neo-apoli:resource_bar"
        },
        "cooldown": 200
    },
    "trigger": {
        "type": "neo-apoli:callback/damage/dealt",
        "on_hit_action": {
            "type": "neo-apoli:trigger_power_cooldown",
            "power": "*:*@cooldown",
            "entity": "this"
        }
    },
    "epic_damage": {
        "type": "neo-apoli:modify/damage/dealt",
        "modifiers": [
            {
                "type": "neo-apoli:multiply_multiplicative",
                "phase": "total",
                "amount": 0.5
            }
        ],
        "active_condition": {
            "type": "neo-apoli:compare",
            "comparison": {
                "type": "neo-apoli:float",
                "comparator": "==",
                "first": {
                    "type": "neo-apoli:power/cooldown/progress",
                    "power": "*:*@cooldown",
                    "entity": "this"
                },
                "second": 1.0
            }
        }
    }
}
```

This example defines three sub-powers: `cooldown` which uses the `neo-apoli:cooldown` power type, `trigger` which uses the `neo-apoli:callback/damage/dealt` power type to trigger the `cooldown` sub-power when damage is dealt, and `epic_damage` which uses the `modify/damage/dealt` power type to deal 50% more damage when the cooldown of `cooldown` is not in progress. 


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
