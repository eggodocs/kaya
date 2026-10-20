#   Emit Game Event

Emits a game event at a position.


Type ID: `neo-apoli:emit_game_event`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`game_event` | [Identifier]({{ mc.game_event_identifier }}) | | The ID of the game event to emit.
`position` | [Vec3 Provider][vec3_provider] | | The position where to emit the game event.
`entity_source` | [Entity Provider][entity_provider] | *optional* | If specified, this entity will be considered as the entity that emitted the game event.
`block_source` | [Block Provider][block_provider] | *optional* | If specified, this block will be considered as the block that emitted the game event.


### Example

```json
{
    "type": "neo-apoli:emit_game_event",
    "game_event": "minecraft:projectile_land",
    "position": {
        "type": "neo-apoli:block/position",
        "block": "used_block"
    },
    "entity_source": "this",
    "block_source": "used_block"
}
```

This example will emit a `minecraft:projectile_land` game event *(which has a frequency of $2$)* at the position of the block provided by the `neo-apoli:used_block` context parameter, making the same block and the entity provided by the `neo-apoli:this_entity` context parameter as the block and entity *(respectively)* that emitted the game event.


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
