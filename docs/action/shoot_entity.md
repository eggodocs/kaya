#   Shoot Entity

Summons an entity and applies the specified velocity to it, as if the entity is a thrown projectile.


Type ID: `neo-apoli:shoot_entity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity_type` | [Identifier]({{ mc.identifier }}) | | The ID of the entity to summon.
`tag` | [NBT Provider][nbt_provider] | *optional* | If specified, this NBT will be applied to the entity after it was summoned. 
`position` | [Vec3 Provider][vec3_provider] | | The position of where the entity will be summoned.
`direction` | [Vec3 Provider][vec3_provider] | | The direction of the velocity that will be applied to the summoned entity.
`velocity` | [Float Provider][float_provider] | `1.0` | The velocity to apply to the summoned entity.
`inaccuracy` | [Float Provider][float_provider] | `1.0` | The factor used for randomizing the direction of the velocity.
`count` | [Int Provider][int_provider] | `1` | The amount of entities to summon and apply velocity to.
`shooter` | [Entity Provider][entity_provider] | *optional* | If specified and if the summoned entity is a projectile, this entity will be set as the owner of the projectile.


### Example

```json
{
    "type": "neo-apoli:shoot_entity",
    "entity_type": "minecraft:small_fireball",
    "position": {
        "type": "neo-apoli:entity/position",
        "entity": "this",
        "anchor": "eyes"
    },
    "direction": {
        "type": "neo-apoli:entity/view",
        "enttiy": "this"
    }
}
```

This example will shoot out a small fireball relative at the eyes and towards the direction of where the entity provided by the `neo-apoli:this_entity` context parameter is looking.


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
