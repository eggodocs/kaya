#   Modify Damage Dealt

Modifies the damage dealt by the entity holding the power to another entity.


Type ID: `kaya:modify/damage/dealt`


???+ info

    This type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `kaya:actor_entity` | The attacker entity (the entity holding the power.)
    `kaya:target_entity` | The entity that was attacked.
    `kaya:dealt_damage/source` | The damage source dealt to the attacked entity.
    `kaya:dealt_damage/amount` | The amount of damage dealt to the attacked entity.
    `kaya:damaging_entity` | The projectile used for the attack (or the attacker if no projectiles are used.)
    `kaya:direct_damaging_entity` | The owner of the projectile used for the attack (or the attacker if no projectiles are used.)


### Format

Field | Type | Default | Description
------|------|---------|------------
`modifiers` | [Array][array] of [Modifiers][modifier] | | The modifiers to apply to the damage dealt by the entity holding the power.
`on_modify_action` | [Action][action] | *optional* | If specified, this action will be executed when the dealt damage is modified.


### Example

```json
{
    "type": "kaya:modify/damage/dealt",
    "modifiers": [
        {
            "type": "kaya:multiply_multiplicative",
            "phase": "total",
            "amount": -0.5
        }
    ]
}
```

This example essentially halves the damage dealt by the entity holding the power.


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
