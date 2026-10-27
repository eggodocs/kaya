#   Blocks Intersecting Box

Provides the count of blocks which fulfills a condition intersecting with a box.


Type ID: `kaya:blocks_intersecting_box`


???+ info

    This type provides the following context parameters when checking the blocks intersecting with the box:

    Parameter | Description
    ----------|------------
    `kaya:block_intersecting_block` | The block intersecting with the box.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check on the blocks colliding with the box.
`box` | [Box Provider][box_provider] | | The box to use to check for blocks.


### Example

```json
{
    "type": "kaya:blocks_intersecting_box",
    "condition": {
        "type": "kaya:check_block_type",
        "key": "minecraft:grass_block",
        "block": "block_intersecting_box"
    },
    "box": {
        "type": "kaya:inflate",
        "box": {
            "type": "kaya:entity/bounds",
            "entity": "this"
        },
        "vector": [
            1.0,
            1.0,
            1.0
        ]
    }
}
```

This example provides the count of grass blocks intersecting with the bounding box *(inflated by 1 block)* of an entity *(provided by the `kaya:this_entity` context parameter.)*


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
