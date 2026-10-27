#   Spawn Particles

Spawns particles at a position.


Type ID: `kaya:spawn_particles`


???+ info

    This type provides the following context parameters to its `view_condition` field when spawning the particles:

    Parameter | Description
    ----------|------------
    `kaya:viewer_entity` | The player that would see the spawned particle.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`particle` | [Particle Effect][particle_effect] | | The particle to spawn.
`view_condition` | [Condition][condition] | *optional* | If specified, only players that fulfill this condition will see the spawned particle.
`position` | [Vec3 Provider][vec3_provider] | | The position where the particle will be spawned. 
`spread` | [Vec3 Provider][vec3_provider] | `[0.5, 0.5, 0.5]` | Determines the vector used for inflating the area of where the particles will be spawned.
`speed` | [Float Provider][float_provider] | `0.0` | Determines the speed of the spawned particles.
`count` | [Int Provider][int_provider] | `1` | Determines the number of particles to spawn.
`force` | [Boolean Provider][boolean_provider] | `false` | Determines whether to allow particles to be displayed within 512.0 blocks.


### Example

```json
{
    "type": "kaya:spawn_particles",
    "particle": "minecraft:portal",
    "position": {
        "type": "kaya:block/position",
        "block": "broken_block"
    },
    "count": 8
}
```

This example will spawn 8 `minecraft:portal` particles at the position of the block provided by the `kaya:broken_block` context parameter.


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
