#   Callback Projectile Land

Invokes an action when a projectile hits a block or an entity.


Type ID: `kaya:callback/projectile/land`


???+ info

    This type provides the following context parameters depending on the scenario:

    === "An entity was hit"

        Parameter | Description
        ----------|------------
        `kaya:projectile_entity` | The projectile entity itself.
        `kaya:actor_entity` | The owner of the projectile or nothing if the projectile doesn't have an owner.
        `kaya:target_entity` | The entity that was hit by the projectile.

    === "A block was hit"

        Parameter | Description
        ----------|------------
        `kaya:landed_on_block` | The block that was hit by the projectile.
        `kaya:landed_on_side` | The side of the block the projectile hit.
        `kaya:projectile_entity` | The projectile entity itself.
        `kaya:actor_entity` | The owner of the projectile or nothing if the projectile doesn't have an owner.


### Format

Field | Type | Default | Description 
------|------|:-------:|-------------
`action` | [Action][action] | | The action to invoke when the entity's projectile hits a block or an entity.


### Example

```json
{
	"type": "kaya:callback/projectile/land",
	"action": {
		"type": "kaya:place_block",
		"block": "minecraft:slime_block",
		"position": {
			"type": "kaya:entity/position",
			"entity": "projectile"
		},
		"offset_direction": {
			"type": "kaya:context",
			"parameter": "landed_on_side"
		}
	}
}
```

This example will place a Slime block at the position of the projectile or at the side of the block/entity when a projectile hits a block/entity.


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
