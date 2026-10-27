#   Callback Damage Dealt

Invokes an action upon the entity holding the power dealing damage to another entity.


Type ID: `kaya:callback/damage/dealt`


???+ info
    
    This type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `kaya:dealt_damage/source` | The damage source dealt by the entity holding the power.
    `kaya:dealt_damage/amount` | The damage amount dealt by the entity holding the power.
    `kaya:actor_entity` | The attacker entity (the entity holding the power.)
    `kaya:target_entity` | The entity that was attacked.
    `kaya:damaging_entity` | The projectile used for the attack (or the attacker if no projectiles are used.)
    `kaya:direct_damaging_entity` | The owner of the projectile used for the attack (or the attacker if no projectiles are used.)


### Format

Field | Type | Default | Description 
------|------|:-------:|------------
`on_hit_action` | [Action][action] | | The action to invoke when damage is dealt to an entity.
`priority` | [Integer][integer] | `0` | Determines the order of which powers of this type will be iterated.


??? question "About priorities"
    
    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be executed first before those that have lower priority values.


### Example

```json
{
	"type": "kaya:callback/damage/dealt",
	"on_hit_action": {
		"type": "kaya:execute_command",
		"source": {
			"type": "kaya:entity",
			"entity": "this"
		},
		"command": {
			"type": "kaya:join",
			"strings": [
				"tp @s",
				{
					"type": "kaya:entity/uuid",
					"entity": "target"
				}
			],
			"separator": " "
		}
	}
}
```

This example teleports the entity that was attacked to the entity holding the power.


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
