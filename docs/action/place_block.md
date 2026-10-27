#   Place Block

Places a block at a position.


Type ID: `kaya:place_block`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position of where the block would be placed.
`block` | [Block State Argument](https://minecraft.wiki/w/Argument_types#block_state) | | The block to place.
`mode` | [Mode](#mode) | `"default"` | Determines how the block is placed.
`offset_direction` | [Direction Provider][direction_provider] | *optional* | If specified and if `mode` is `"default"`, the position will be offset by this direction if the block couldn't be placed at the position.


[](){ #mode }

???+ info "Mode"

    A [string][string] that determines how a block is placed at a position.


    ### Values

    Value | Description
    ------|------------
    `destroy` | Before the new block is placed, the old block drops both itself and its contents, and the appropriate block breaking noise/particles are played/emitted. 
    `keep` | Places the block only if the position is not occupied by another block.
    `replace` | Replace the old block with the new block; no items are dropped nor noise/particles are played/emitted.
    `default` | Places the block at the position. If the position is occupied by another block, attempts to offset the position by a specific direction.
    `strict` | Places the block as-is without triggering block and shape updates.


### Example

```json
{
    "type": "kaya:place_block",
    "block": "minecraft:cobweb",
    "position": {
        "type": "kaya:entity/position",
        "entity": "projectile"
    },
    "offset_direction": {
        "type": "kaya:context",
        "parameter": "landed_on_side"
    }
}
```

This example will attempt to place a cobweb block at the position of the entity provided by the `kaya:projectile_entity` context parameter.

If the block couldn't be placed, it will attempt to place the cobweb at the side of the block offset by the direction provided by the `kaya:landed_on_side` context parameter.


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
