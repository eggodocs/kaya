#   Adjacent Blocks

Provides the count of blocks adjacent to a block at a specific position that fulfill a condition.


Type ID: `neo-apoli:adjacent_blocks`


???+ info

    This type provides the following context parameters when checking the adjacent blocks:

    Parameter | Description
    ----------|------------
    `neo-apoli:adjacent_block` | The block adjacent to the block at a position.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check on the adjacent blocks.
`position` | [Vec3 Provider][vec3_provider] | | The position of a block to check the blocks adjacent to it.


### Example

```json
{
    "type": "neo-apoli:adjacent_blocks",
    "condition": {
        "type": "neo-apoli:check_block_type",
        "key": "minecraft:dirt",
        "block": "adjacent_block"
    },
    "position": {
        "type": "neo-apoli:block/position",
        "block": "used_block"
    }
}
```

This example counts how many blocks adjacent to a block *(provided by the `neo-apoli:used_block` context parameter)* is a Dirt block.


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
</table>b
