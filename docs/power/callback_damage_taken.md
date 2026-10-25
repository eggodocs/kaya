#   Callback Damage Taken

Invokes an action upon the entity holding the power taking damage.


Type ID: `neo-apoli:callback/damage/taken`


???+ info
    
    This type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `neo-apoli:taken_damage/source` | The damage source taken by the entity holding the power.
    `neo-apoli:taken_damage/amount` | The damage amount taken by the entity holding the power.
    `neo-apoli:actor_entity` | The attacker entity (the entity holding the power.)
    `neo-apoli:target_entity` | The entity that was attacked.
    `neo-apoli:damaging_entity` | The projectile used for the attack (or the attacker if no projectiles are used.)
    `neo-apoli:direct_damaging_entity` | The owner of the projectile used for the attack (or the attacker if no projectiles are used.)


### Format

Field | Type | Default | Description 
------|------|:-------:|------------
`on_hit_action` | [Action][action] | | The action to invoke when damage is taken.
`priority` | [Integer][integer] | `0` | Determines the order of which powers of this type will be iterated.


??? question "About priorities"
    
    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be executed first before those that have lower priority values.


### Example

```json
{
	"type": "neo-apoli:callback/damage/taken",
	"on_hit_action": {
        "type": "neo-apoli:conditional",
        "condition": {
            "type": "neo-apoli:parameter_exists",
            "parameter": {
                "type": "neo-apoli:entity",
                "name": "actor"
            }
        },
        "on_true": {
            "type": "neo-apoli:set_entity_on_fire",
            "ticks": 200,
            "entity": "actor"
        }
	},
    "active_condition": {
        "type": "neo-apoli:check_damage_type",
        "key": "minecraft:magic",
        "damage_source": "taken_damage/source"
    }
}
```

This example will set the attacker (if it exists) on fire for 10 seconds if the received damage type is `minecraft:magic`.


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
