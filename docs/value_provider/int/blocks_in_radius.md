#   Blocks in Radius

Provides the count of blocks which fulfills a condition within an area with a shape and radius.


Type ID: `neo-apoli:blocks_in_radius`


???+ info

    This type provides the following context parameters when checking the blocks within the radius of the area:

    Parameter | Description
    ----------|------------
    `neo-apoli:block_in_radius` | The block within the radius of the area.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check on the block within the area.
`position` | [Vec3 Provider][vec3_provider] | | The position of the area.
`shape` | [Shape][shape] | | The shape of the area.
`radius` | [Int Provider][int_provider] | | The radius of the area.


### Example

```json
{
    "type": "neo-apoli:blocks_in_radius",
    "condition": {
        "type": "neo-apoli:is_block_in_tag",
        "block_tag": "#minecraft:impermeable",
        "block": "block_in_radius"
    },
    "position": {
        "type": "neo-apoli:block/position",
        "block": "broken_block"
    },
    "shape": "cube",
    "radius": 8
}
```

This example provides the count of blocks that are included in the `#minecraft:impermeable` block tag within an 8 blocks cubical radius relative to a block *(provided by the `neo-apoli:broken_block` context parameter.)*


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
