#   Explode

Emits an explosion at a position.


Type ID: `neo-apoli:explode`


???+ info

    This type provides the following context parameters to certain fields:

    === "`destructible_condition`"

        Parameter | Description
        ----------|------------
        `neo-apoli:exploded_block` | The block affected by the explosion.


    === "`damageable_condition`"

        Parameter | Description
        ----------|------------
        `neo-apoli:emitter_entity` | The entity that emitted the explosion, or none if the `emitter` field is not present.
        `neo-apoli:exploded_entity` | The entity affected by the explosion.

    
    === "`knockback_multiplier`"

        Parameter | Description
        ----------|------------
        `neo-apoli:emitter_entity` | The entity that emitted the explosion, or none if the `emitter` field is not present.
        `neo-apoli:exploded_entity` | The entity affected by the explosion.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`damageable_condition` | [Condition][condition] | *optional* | If specified, determines which entities can be damaged.
`destructible_condition` | [Condition][condition] | *optional* | If specified, determines which blocks can be destroyed.
`sound` | [Sound Event]({{ mc.sound_event }}) | `"minecraft:entity.generic.explode"` | The sound to play for the explosion.
`small_particle` | [Particle Effect][particle_effect] | `"minecraft:explosion"` | The particle to emit if the explosion is small.
`large_particle` | [Particle Effect][particle_effect] | `"minecraft:explosion_emitter"` | The particle to emit if the explosion is large.
`block_interaction` | [Block Interaction][block_interaction] | | Determines how the explosion will interact with the affected blocks.
`power` | [Float Provider][float_provider] | | Determines the power/radius of the explosion.
`knockback_multiplier` | [Float Provider][float_provider] | `1.0` | Determines the knockback multiplier received by the affected entities. 
`create_fire` | [Boolean Provider][boolean_provider] | `true` | Determines whether fire should be placed within the affected area of the explosion.
`position` | [Vec3 Provider][vec3_provider] | | The position of the explosion.
`emitter` | [Entity Provider][entity_provider] | *optional* | If specified, this entity will be considered the one that emitted the explosion.


??? info "Explosion sizes"

    An explosion is considered small if its `power` is $\lt 2.0$ or if its `block_interaction` is not `"keep"`.


### Example

```json
{
    "type": "neo-apoli:explode",
    "damageable_condition": {
        "type": "neo-apoli:is_entity_of_type",
        "entity_type": "minecraft:creeper",
        "entity": "exploded_entity"
    },
    "block_interaction": "keep",
    "power": 16.0,
    "position": {
        "type": "neo-apoli:block/position",
        "block": "broken_block"
    },
    "emitter": "this"
}
```

This example will emit an explosion with a power/radius of $16.0$ which only damages creepers at the position of the block provided by the `neo-apoli:broken_block` context parameter, with the entity provided by the `neo-apoli:this_entity` context parameter being the entity that emitted the explosion.


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
